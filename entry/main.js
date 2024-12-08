const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');

let mainWindow;

  // Make sure the path is correct
const preloadPath = path.join(__dirname, 'pl.js');
console.log("Preload script path:", preloadPath);  // This will print the absolute path to preload.js


app.on('ready', () => {
  mainWindow = new BrowserWindow({
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
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});


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

// Handle close
ipcMain.on('close-window', () => {
  const window = BrowserWindow.getFocusedWindow();
  if (window) window.close();
});