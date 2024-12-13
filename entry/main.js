const { app, dialog , BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { exec } = require('child_process');

let mainWindow;

  // Make sure the path is correct for preloader
const preloadPath = path.join(__dirname, 'pl.js');
console.log("Preload script path:", preloadPath);

// on ready execute this.
app.on('ready', async () => {
    // docker build
    try {
        await dockerUp();
    } catch (error) {
        console.error(error);
        //app.quit()
    }
    finally {
        // build browser window for electron app
        app_build()
    }


});


// docker up and run all images using docker-compose
const dockerUp = async () =>{
    return new Promise((resolve, reject) => {

          const composeFilePath = '../docker-compose.yaml'; // Adjust the path to your file
          const command = `docker-compose -f ${composeFilePath} up -d`;
          console.log('Starting Docker containers...');
          // use exec in cmd
          exec(command, (error, stdout, stderr) => {
            if (error) {
              console.error(`Error starting Docker Compose: ${error.message}`);
              //app.quit(); // Quit the app if Docker fails to start
              reject(error);
            }
            else if (stderr) {
              console.warn(`Docker Compose stderr: ${stderr}`);
              reject(stderr)
            }
            else{
                console.log(`Docker Compose stdout: ${stdout}`);
                resolve(stdout);
            }
          });
            });
        }

// build browser window
const app_build = () =>{
    mainWindow = new BrowserWindow({
    title: 'ColonyX',
    width: 1300,
    height: 600,
    minHeight:800,
    minWidth: 1300,
    icon: path.join(__dirname, 'lg.png'),
    frame: false, // Disable the default title bar
    webPreferences: {
      preload: preloadPath, // Use the preload script
      nodeIntegration: true, // Ensure node integration is off for security
      contextIsolation: false, // Ensure context isolation is enabled for security
    },
  });

  mainWindow.loadFile('index.html');

  mainWindow.on('closed', () => {
    mainWindow = null;

    // Stop Docker containers when the app closes
        const composeFilePath = path.resolve(__dirname, '../docker-compose.yaml');
    exec(`docker-compose -f ${composeFilePath} down --remove-orphans`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error stopping Docker Compose: ${error.message}`);
      }
    });
  });

}

app.on('before-quit', ()=>{
    // Stop Docker containers when the app closes
    const composeFilePath = path.resolve(__dirname, '../docker-compose.yaml');

    exec(`docker-compose -f ${composeFilePath} down --remove-orphans`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error stopping Docker Compose: ${error.message}`);
      }
    });

})

app.on('window-all-closed', () => {
// Stop Docker containers when the app closes

    const composeFilePath = '../docker-compose.yaml'; // Update to your actual file path
    exec(`docker-compose -f ${composeFilePath} down --remove-orphans`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error stopping Docker Compose: ${error.message}`);
      }else{
          console.log(`Docker Compose Down`);
      }
    });
    console.log('all done')
    quit();
});

const quit = ()=>{
    if (process.platform !== 'darwin') {
    app.quit();
  }
}


// Handle minimize
ipcMain.on('minimise-window', () => {
  console.log('minimize window');
  const window = BrowserWindow.getFocusedWindow();
  if (window) window.minimize();
});

// Handle maximize/restore
ipcMain.on('maximise-window', () => {
  const window = BrowserWindow.getFocusedWindow();
  if (window) {
    if (window.isMaximized()) {
      window.unmaximize();
    } else {
      window.maximize();
    }
  }
});

// Stop Docker
const stopDockers = async ()=>{
    const composeFilePath = path.resolve(__dirname, '../docker-compose.yaml');
    return new Promise((resolve, reject) => {
        exec(`docker-compose -f ${composeFilePath} down`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error stopping Docker Compose: ${error.message}`);
                reject(error); // Reject the promise on error
            } else {
                console.log('Docker Compose stopped:', stdout);
                resolve(stdout); // Resolve the promise on success
            }
        });
    });
}


// Handle close
ipcMain.on('close-window', async () => {

  try {
         const options = {
            type: 'info',
            buttons: ['OK'],
            title: 'Closing ColonyX',
            message: 'Docker containers have been stopped successfully. Closing ColonyX...',
        };

        // Stop Docker containers when the app closes
        await stopDockers();
        await dialog.showMessageBox(BrowserWindow.getFocusedWindow(), options);

        console.log('Docker containers stopped successfully.');
    } catch (err) {
        console.error('Failed to stop Docker containers:', err);
    } finally {
        // Kill browser window
        close();
    }
});

const close = ()=>{
    const window = BrowserWindow.getFocusedWindow();
    if (window) window.close();
}