import React, {useRef} from "react";
import {Link, useNavigate} from "react-router-dom";

export default function About (){

    return (<div className='page'>
        <link rel="stylesheet"
              href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"/>

        <div style={{
            zIndex: 9,
            height: 'auto',
            background: 'rgba(34,18,18,0.16)',
            marginTop: -2,
            margin:40,
            borderRadius: 23,
            position: 'relative',
            boxShadow: "4px 4px 16px 7px rgba(130,130,130,0.16) ",
        }} className='glassed'>
            <div className='glassed' style={{padding: 30, borderRadius: 23}}>
                <div style={{
                    flex: 2,
                    display: 'flex',
                    height: 'auto',
                    width: 'auto',
                    justifyContent: "center",
                    flexWrap: 'wrap',
                    order: 2,
                    flexDirection: 'row'
                }}>
                    <div style={{
                        borderRadius: 12,
                        background: '#e2ffe1',
                        height: '100%',
                        padding: '20px',
                        margin: '20px',
                        boxShadow: "4px 4px 16px 10px rgba(110,110,110,0.09) "
                    }} className='wrap-text-white shGreen'>
                        <div style={{display: 'flex'}}>
                            <div className='circle' style={{background: 'grey'}}></div>
                            <div className='circle bluex' style={{width: 60, height: 13}}></div>
                            <span className="material-symbols-outlined grayx">
                                        map
                                    </span>
                        </div>
                        <p style={{color: '#555'}}>"Seamless map access in applications helps locate medical
                            services quickly, optimizing routes for emergency responders and ensuring timely assistance,
                            ultimately enhancing healthcare accessibility and response efficiency during emergencies.
                            "</p>
                        <button className='redx shRed'>With Love</button>
                    </div>

                    <div style={{
                        borderRadius: 12,
                        background: '#e1f7ff',
                        height: '100%',
                        padding: '20px',
                        margin: '20px',
                        boxShadow: "4px 4px 16px 10px rgba(110,110,110,0.09) "
                    }} className='wrap-text-white shGreen'>
                        <div style={{display: 'flex'}}>
                            <div className='circle' style={{background: 'grey'}}></div>
                            <div className='circle bluex' style={{width: 60, height: 13}}></div>
                            <span className="material-symbols-outlined grayx">
                                        map
                                    </span>
                        </div>
                        <p style={{color: '#555'}}>"Seamless map access in applications helps locate medical
                            services quickly, optimizing routes for emergency responders and ensuring timely assistance,
                            ultimately enhancing healthcare accessibility and response efficiency during emergencies.
                            "</p>
                        <button className='redx shRed'>Annex App</button>
                    </div>

                    <div style={{
                        borderRadius: 12,
                        background: '#ffffe1',
                        height: '100%',
                        padding: '20px',
                        margin: '20px',
                        boxShadow: "4px 4px 16px 10px rgba(110,110,110,0.09) "
                        }} className='wrap-text-white shGreen'>
                        <div style={{display: 'flex'}}>
                            <div className='circle' style={{background: 'grey'}}></div>
                            <div className='circle bluex' style={{width: 60, height: 13}}></div>
                            <span className="material-symbols-outlined grayx">
                                        map
                                    </span>
                        </div>
                        <p style={{color: '#555'}}>"Seamless map access in applications helps locate medical
                            services quickly, optimizing routes for emergency responders and ensuring timely assistance,
                            ultimately enhancing healthcare accessibility and response efficiency during emergencies.
                            "</p>
                        <button className='redx shRed'>My work</button>
                    </div>
                </div>
            </div>
        </div>

        </div>
    );
}