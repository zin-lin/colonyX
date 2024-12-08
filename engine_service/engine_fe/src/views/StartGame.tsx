import React, {FormEvent} from "react";
import {useNavigate} from "react-router-dom";
import axios from "axios";

export default function StartGame () {

    const navigate = useNavigate();
    const start_game = (e: FormEvent)=>{
        e.preventDefault();
        let size = (document.getElementById('size') as HTMLInputElement).value;
        let col_len = (document.getElementById('colonies') as HTMLInputElement).value;

        let case_new = {
            'pname' : size,
            'address' : col_len,
        }

        const form:FormData = new FormData();
        form.append('size', size);
        form.append('col_len', col_len);

        console.log(case_new);
        axios.post('http://localhost:15000/api/create_game', form, {withCredentials:true}).then(response => {
            let id = response.data.id;
            navigate(`/game`);
        }).catch(error => {})
    }

    return (
        <div className='page'>
            <link rel="stylesheet"
                  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"/>
            <div style={{
                width: '100%',
                height: '100%',
                display: 'flex',
                flex: 1,
                marginTop: 0,
                position: 'relative',
                transition: '0.6s ease',
                opacity: 1,
                justifyContent: 'center',
                alignItems: 'center'
            }}>

                <div style={{display: "flex", justifyContent: "center", height: '100%', alignItems: 'center', width:'100%'}}>
                    <div style={{
                        background: 'rgba(55,83,73,0.45)',
                        height: '80%',
                        padding: 20,
                        width: '80%',
                        maxHeight: 405,
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
                                        style={{background: 'transparent', width: 'auto', height: 'auto', margin: 0, justifyContent:'center', alignItems: 'center'}}
                                        onClick={() => {
                                        }}>
                                    <span className="material-symbols-outlined" style={{color: '#ea7373', fontWeight:'bold', fontSize:33}}>
                                        tv
                                    </span>
                                </button>
                            </div>

                            <form onSubmit={(e) => {
                                start_game(e);
                            }}>
                                <div style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    marginLeft: 0,
                                    justifyContent: 'center'
                                }}>
                                    <span style={{color: '#777', fontSize: 19, marginRight: 10}}
                                          className="material-symbols-outlined">
                                         toys_and_games
                                    </span><p style={{color: '#777', fontSize: 14}}>Grid Size</p>
                                </div>

                                <input placeholder='for both x and y, 25' className='noner' id="size" type='number'/>
                                <br/>

                                <div style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    marginLeft: 0,
                                    justifyContent: 'center'
                                }}>
                                        <span style={{color: '#777', fontSize: 19, marginRight: 10}}
                                              className="material-symbols-outlined">
                                             home
                                        </span> <p style={{color: '#777', fontSize: 14}}>Number of Colonies</p>
                                </div>
                                <input placeholder='4 max' className='noner' id="colonies" type='number'/>
                                <br/>
                                <br/>

                                <button className='purplex shPurple' type="submit" style={{
                                    margin: 20,
                                    width: 170,
                                    paddingTop: 8,
                                    alignItems:'center',
                                    alignContent:'center',
                                    paddingBottom: 8,
                                    display:'flex',
                                    justifyContent:'center',
                                    alignSelf:'center',
                                    justifySelf:'center'
                                }}> <p>Create Game</p> <span style={{color: '#fff', fontSize: 19, marginLeft: 10}}
                                              className="material-symbols-outlined">
                                    tactic
                                </span>
                                </button>
                            </form>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    );
}