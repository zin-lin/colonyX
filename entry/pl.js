// preload.js
const { contextBridge, ipcRenderer } = require('electron');

console.log("Preload script loaded");
// Expose the ipcRenderer safely to the renderer process
contextBridge.exposeInMainWorld('electron', {
  ipcRenderer: ipcRenderer,
});
