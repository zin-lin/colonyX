import React, {useEffect} from "react";
import axios from "axios";
import {useNavigate} from "react-router-dom";

export default function Login() {

    const navigate = useNavigate();

    useEffect(()=>{

        let data:FormData = new FormData();
        data.append('app_id', 'hospital_service-234234234sadnnbqweh2u3');
        axios.post('/api/authed', data).then(
            res => {
                console.log(res.data);
                if (res.data['id'] !== ''){
                    let id = (res.data['id']);
                    navigate('/');
                }
            }
        ).catch(e => e)
    })

    return (
        <div className='page' >
            <link rel="stylesheet"
                  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"/>
            <div style={{
                width: '100%',
                height: '100%',
                display: 'flex',
                flex: 1,
                marginTop: 0 ,
                position: 'relative',
                transition: '0.6s ease',
                opacity: 1,
                justifyContent: 'center',
                alignItems: 'center'
            }} >

                <div style={{display: "flex", justifyContent: "center", height: '100%', alignItems: 'center'}}>
                    <div style={{
                        background: 'rgb(250,250,250,1.0    )',
                        height: '80%',
                        width: '80%',
                        maxHeight: 380,
                        maxWidth: 500,
                        minWidth: 300,
                        minHeight: 350,
                        borderRadius: 30,
                        boxShadow: '4px 4px 16px 10px rgba(110,110,110,0.09)',
                        overflow: 'auto'
                    }} className="shadow-container">
                        <div style={{padding: '20px', textAlign: 'center', justifyContent: 'center'}}>
                            <div style={{display: 'flex'}}>
                                <button className='circle'
                                        style={{background: 'transparent', width: 'auto', height: 'auto', margin: 0}}
                                        onClick={() => {
                                        }}>

                                </button>
                                <button className='circle'
                                        style={{background: 'transparent', width: 'auto', height: 'auto', margin: 0}}
                                        onClick={() => {
                                        }}>
                                    <span className="material-symbols-outlined" style={{color: '#b96a6a'}}>
                                        ambulance
                                    </span>
                                </button>
                            </div>

                            <form onSubmit={(e) => {
                                let hos = (document.getElementById('hos') as HTMLInputElement).value;
                                let pwd = (document.getElementById('password') as HTMLInputElement).value;

                                const data:FormData = new FormData();
                                data.append('hospital', hos);
                                data.append('password', pwd);

                                axios.post('/api/hlogin', data , {
                                    headers: {
                                        'Content-Type': 'multipart/form-data',
                                    },}).then(
                                    response => {
                                        if (response.data['msg'] === "logged in"){
                                            navigate('/cases')
                                        }
                                        else {
                                            alert("error")
                                        }
                                    }
                                ).catch(error => {alert(error)})

                            }}>
                                <div style={{display: 'flex', alignItems: 'center', marginLeft: 26}}>
                                    <span style={{color: '#aaa', fontSize: 19, marginRight: 10}}
                                          className="material-symbols-outlined">
                                         license
                                    </span><p style={{color: '#aaa', fontSize: 14}}>Hospital Code</p>
                                </div>
                                <input placeholder='@hospital code' className='noner' id="hos"/>
                                <br/>
                                <div style={{display: 'flex', alignItems: 'center', marginLeft: 26}}>
                                        <span style={{color: '#aaa', fontSize: 19, marginRight: 10}}
                                              className="material-symbols-outlined">
                                             emergency
                                        </span> <p style={{color: '#aaa', fontSize: 14}}>Password</p>
                                </div>
                                <input placeholder='code' className='noner' type='password' id="password"/>
                                <button className='redx shRed' type="submit" style={{
                                    margin: 20,
                                    width: 170,
                                    paddingTop: 8,
                                    paddingBottom: 8
                                }}>Login As Hospital
                                </button>
                            </form>
                        </div>
                    </div>

                </div>
            </div>
        </div>

    );
}