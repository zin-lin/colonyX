import React from "react";
import {Link} from "react-router-dom";
import {useAuthDispatch} from "../../redux/hook";
import {toHome, toShop, resetAllVs, toAbout} from "../../redux/authState";


export default function Nav () {
    const dispatch = useAuthDispatch();
    return (
        <nav>
            <div>
                <p  style={{fontSize:24, marginLeft:40, fontWeight:'bold'}}>{'['}Annex<span className='red' style={{color:"#fb6b6b"}}>ColonyX</span>{']'}</p>
            </div>
            <div className='hider' style={{right:10, position:'absolute', display:'flex', height:'100%', alignItems:'center'}}>
                <Link onClick={()=> dispatch(toHome())} to='/'><p style={{fontSize:16, margin:12 }}>Ho<span style={{color:"#fb6b6b"}}>me</span></p></Link>
                <Link onClick={()=> dispatch(toAbout())} to='/about'><p style={{fontSize:16, margin:12 }}>Abo<span style={{color:"#fb6b6b"}}>ut</span></p></Link>
                <Link onClick={()=> dispatch(resetAllVs())} to='/start'><p style={{fontSize:16, margin:12 }}><span className="material-symbols-outlined">
                search
                </span></p></Link>
                <Link onClick={()=> dispatch(toShop())} to='/game'><p style={{fontSize:16, margin:12 }}><span className="material-symbols-outlined red">
                pest_control
                </span></p></Link>
            </div>
            <div className = "hider-reverse" style={{marginTop:'6px', right:0, position:'absolute' }}>
                <Link onClick={()=> dispatch(resetAllVs())} to='/cases'><p style={{fontSize:16, margin:12 }}><span className="material-symbols-outlined">
                    search
                    </span></p>
                </Link>
            </div>
        </nav>
    );
}