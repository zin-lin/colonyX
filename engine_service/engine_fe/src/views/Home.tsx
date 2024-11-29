import React, {useEffect, useRef, useState} from "react";
import {Link, useNavigate} from "react-router-dom";
import promo from '../assets/ad.png';
import Login from "./Login";
import axios from "axios";
export default function Home (){

    const reader = new FileReader();
    //reader.readAsText('../.anx');
    const [data, setData] = useState('');

    const [authed, setAuthed] = useState(false);
    const [id, setId]  = useState("");

    useEffect(() => {

        let data:FormData = new FormData();
        data.append('app_id', 'ambulance_service-234234234sadnnbqweh2u3');

        axios.post('/api/authed', data).then(
            res => {
                console.log(res.data);
                if (res.data['id'] !== ''){
                    setAuthed(true);
                    setId(res.data['id']);
                }
            }
        ).catch(e => e)

    })

    const navigate = useNavigate();

    return (
        <div className='page'>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
            <div style={{padding: 50}}>


                <div style={{padding: 60}}>
                    { !authed?
                        (<button className='redx shRed' style={{width: '360px'}} onClick={() => {
                            navigate('/alogin');
                        }}>
                            <p>{'@hospital> ./login'}</p>
                        </button>) :

                  (  <button className='redx shRed' style={{width: '360px'}} onClick={() => {
                        navigate('/cases');
                    }}>
                        <p>{'@hospital> ./check [database] '} {id}</p>
                    </button>)
                }
                </div>

                <div style={{
                    zIndex: 9,
                    height: 'auto',
                    marginTop: -2,
                    borderRadius: 23,
                    position: 'relative',
                }} className='glassed'>
                    <div className='glassed' style={{padding:30, borderRadius:23}}>
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
                                height: '100%',
                                borderColor:'rgba(244,117,117,0.53)',
                                padding: '20px',
                                margin: '20px',
                                boxShadow: "4px 4px 16px 10px rgba(110,110,110,0.09) "
                            }} className='wrap-text-white shGreen dcs'>
                                <div style={{display: 'flex'}}>
                                    <div className='circle' style={{background: 'white'}}></div>
                                    <div className='circle bluex' style={{width: 60, height: 13}}></div>
                                    <span className="material-symbols-outlined grayx">
                                        map
                                    </span>
                                </div>
                                <p style={{color: 'rgba(244,117,117,0.53)'}}>"Seamless map access in applications helps locate medical
                                    services quickly, optimizing routes for emergency responders and ensuring timely assistance, ultimately enhancing healthcare accessibility and response efficiency during emergencies.
                                    "</p>
                                <button className='redx shRed'>Loate Now</button>
                            </div>
                                <div style={{
                                    borderRadius: 12,
                                    height: '100%',
                                    borderColor:'rgba(220,160,98,0.66)',
                                    padding: '20px',
                                    margin: '20px',
                                    boxShadow: "4px 4px 16px 10px rgba(110,110,110,0.09) "
                                }} className='wrap-text-white dcs'>
                                    <div style={{display: 'flex'}}>
                                        <div className='circle' style={{background: 'rgba(220,160,98,0.66)'}}></div>
                                        <div className='circle'
                                             style={{background: 'orange', width: 60, height: 12}}></div>
                                        <span className="material-symbols-outlined grayx">
                                            call
                                        </span>
                                    </div>
                                    <p style={{color: 'rgba(220,160,98,0.66)'}}>" Ambulances provide rapid transportation and immediate
                                        medical care, bridging the gap between emergency scenes and hospitals, Ambulance Services in the Uk are now ensuring prompt treatment that can significantly improve patient survival and outcomes.

                                    "</p>
                                <button className='orangex shOrange'>Save Lives</button>
                            </div>
                            <div style={{
                                borderRadius: 12,
                                height: '100%',
                                padding: '20px',
                                margin: '20px',
                                boxShadow: "4px 4px 16px 10px rgba(130,130,130,0.15) ",
                                borderColor:'rgba(255,74,252,0.67)'
                            }} className='wrap-text-white dcs'>
                                <div style={{display: 'flex'}}>
                                    <div className='circle' style={{background: 'rgba(255,74,252,0.67)'}}></div>
                                    <div className='circle redx' style={{width: 60, height: 13}}></div>
                                    <span className="material-symbols-outlined grayx">
                                        ambulance
                                    </span>
                                </div>
                                <p style={{color: 'rgba(255,74,252,0.67)'}}>" NHS ambulance services ensure equal access to emergency
                                    care, supporting public health and well-being in the United Kingdom by providing free, life-saving services, reinforcing the NHS’s commitment to accessible healthcare for all."</p>
                                <button className='shPurple purplex'>Ambulance Services</button>
                            </div>
                            <div style={{
                                borderRadius: 12,
                                height: '100%',
                                padding: '20px',
                                margin: '20px',
                                boxShadow: "4px 4px 16px 10px rgba(110,110,110,0.09) ",
                                borderColor:'rgba(93,232,153,0.6)'
                            }} className='wrap-text-white dcs'>
                                <div style={{display: 'flex'}}>
                                    <div className='circle' style={{background: 'rgba(93,232,153,0.6)'}}></div>
                                    <div className='circle purplex' style={{width: 60, height: 13}}></div>
                                    <span className="material-symbols-outlined grayx" >
                                        church
                                    </span>
                                </div>
                                <p style={{color: 'rgba(93,232,153,0.6)'}}>"Effective emergency response and medical aid services across
                                    Scotland reduce critical delays, providing timely care that saves lives, improves patient outcomes, avoid and prevent disasters,and strengthens overall public health and safety."</p>
                                <button className='shGreen greenx'>Save Scotland</button>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </div>);
}