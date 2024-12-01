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
