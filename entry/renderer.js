const {ipcRenderer} = require('electron');
document.getElementById('minimize').addEventListener('click', () => {
  ipcRenderer.send('minimise-window');
});

// Maximize button
document.getElementById('maximize').addEventListener('click', () => {
  ipcRenderer.send('maximise-window');
});

// Close button
document.getElementById('close').addEventListener('click', () => {
  ipcRenderer.send('close-window');
});

const body = document.getElementById('body');

const renderMain = ()=>{

  let start = true
  while (start){
    fetch('http://localhost:15566/check').then(res=>res.json()).then(data=>{
      if (data['msg'] === 'ping'){
        console.log('ready')

        try {
          body.innerHTML = "      <iframe id=\"webview\"\n" +
              "               src=\"http://127.0.0.1:15566/\" style=\" margin:0; outline: none; border: none\"\n" +
              "      ></iframe>\n"
        } catch(err){
          console.error(err)
                    body.innerHTML = "      <iframe id=\"webview\"\n" +
              "               src=\"http://127.0.0.1:15566/\" style=\" margin:0; outline: none; border: none\"\n" +
              "      ></iframe>\n"
          window.location.reload()
        }
      }
      start = false;
    })

  }
}

