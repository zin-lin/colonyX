import React, {useEffect, useRef, useState} from "react";
import {Link, useNavigate} from "react-router-dom";
import axios from "axios";

// default function Home
// author: Zin Lin Htun
export default function Home (){

    const reader = new FileReader();
    //reader.readAsText('../.anx');
    const [data, setData] = useState('');

    const [authed, setAuthed] = useState(false);
    const [id, setId]  = useState("");

    useEffect(() => {

        let data:FormData = new FormData();

        axios.post('http://localhost:15000/', data).then(
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

                        <button className='redx shRed' style={{width: '360px'}} onClick={() => {
                            navigate('/start');
                        }}>
                            <p> <span style={{color:'#511c2f'}}>{'@annex_system>'}</span> new_game <span
                                style={{color:'#e4da6f'}}
                            >--start</span></p>
                        </button>


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
                                    <span className="material-symbols-outlined grayx" style={{color:'#5ebcff'}}>
                                        pest_control
                                    </span>
                                </div>
                                <p style={{color: 'rgba(244,117,117,0.53)'}}>"
                                    Leafcutter ants are remarkable insects known for their intricate social structure and cooperative behaviors.
                                    They cultivate fungus by cutting leaves and using them as a substrate for growing their food source.
                                    This benefits providing a sustainable food supply.
                                    "</p>
                                <button className='redx shRed'>Try Now</button>
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
                                        <span className="material-symbols-outlined" style={{color:'#ffa65e'}}>
                                            emoji_nature
                                        </span>
                                    </div>
                                    <p style={{color: 'rgba(220,160,98,0.66)'}}>"
                                        With Annex: ColonyX you can simulate entire colonies of ants, with different roles, including soldiers, scouts
                                        workers and of course the queen. Each colony needs specific ants to function as a whole adding to
                                        the complexity of the ColonyX system.
                                    "</p>
                                <button className='orangex shOrange'>Try Now</button>
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
                                    <span className="material-symbols-outlined grayx" style={{color:'#ff5e7c'}}>
                                        road
                                    </span>
                                </div>
                                <p style={{color: 'rgba(255,74,252,0.67)'}}>"
                                        With Annex: ColonyX you can simulate entire environments, with different resources, including meat, trees
                                        leafs and of course water. Each colony needs specific resources to feed the queen adding more ants promoting
                                        the realism of the ColonyX system.
                                </p>
                                <button className='shPurple purplex'>Simulate</button>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>);
}