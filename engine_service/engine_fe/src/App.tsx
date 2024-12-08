import './App.css';
import {HashRouter as R, Route, Routes} from 'react-router-dom'
import Nav from './components/Navigators/Nav';
import MobileNav from './components/Navigators/MobileNav';
import Home from './views/Home';
import About from './views/About';
import Login from './views/Login';
import Cases from "./views/Cases";
import Game from "./views/Game";
import StartGame from "./views/StartGame";

function App() {
  return (
      // wrap around navigation

      <R>
        <div className="App">
          <Nav/>
          <div className='rom-app'>
            <Routes>
                <Route element={<Home/>} path='/' />
                <Route element={<About/>} path='/about' />
                <Route element={<Login/>} path='/alogin' />
                <Route element={<Cases/>} path='/cases' />
                <Route element={<Game/>} path='/game' />
                <Route element={<StartGame/>} path='/start' />
            </Routes>
          </div>
          <MobileNav/>
        </div>
      </R>
  );
}

export default App;
