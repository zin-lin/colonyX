import React, {useEffect, useRef, useState} from "react";
import {Link, useNavigate} from "react-router-dom";
import axios from "axios";

export default function Cases () {

    const [cases, setCases] = useState([]);
    const [id, setId] = useState('');
    const navigate = useNavigate();
    useEffect(()=>{
        axios.get('/api/authed').then(res=>res.data).then(data=> {
            if (data['id'] === '')
                navigate('/');
            else {
                setId(data['id']);
                axios.get(`http://localhost:8080/getAll/${data['id']}`).then(res=>res.data
                ).then(data=> {
                    setCases(data)
                    console.log(data)
                })
            }
        })


    }, [])

    return (
        <div className='page'>
            <link rel="stylesheet"
                  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"/>
            <div style={{margin:0, marginBottom:0, justifyContent:'center', width:'100%', justifyItems:'center',
                display:'flex', flexDirection:'column', alignItems:'center'

                
            }}>
                <div style={{
                    borderRadius: 20, margin: '40px', background: 'rgba(31,43,50,0.39)', width: '80%', minHeight: 140,
                  maxWidth: 1100, padding: 30
                }}>
                    <div style={{display:'flex', flex:'auto'}}>
                        <span style={{color:'#56c1b5', marginRight:20}}>{'@database_id> '}</span><span style={{color:'#777'}}>hos_login
                        <span className='orangex' style={{marginLeft:20, padding:7, borderRadius:7}}>{id}</span></span>
                    </div>
                    <hr style={{color:'#444'}}/>
                {
                    cases.map((caseD, index) =>{
                        return (
                           <div style={{width:'100%'}} onClick={()=>{
                                // axios.get(`/api/update/${caseD['id']}`).then(res=>console.log(res.data)).catch(e => console.log(e))
                                navigate(`/track/${caseD['nhs']}`);
                            }}>
                               <div style={{display: 'flex', alignContent: 'center', alignItems: 'center'}}>
                                   <div style={{marginRight: 20,}}>

                                   </div>
                                   <span className="material-symbols-outlined grayx"
                                         style={{color: '#aaa', fontSize: 33, marginRight: 20}}>
                                            person
                                    </span>
                                   <div
                                       style={{display: 'flex'}}> {(caseD!['name']) !== null ? caseD!['name'] : 'John/Jane Doe'}
                                   </div>

                                   <span className="material-symbols-outlined grayx"
                                         style={{color: '#aaa', fontSize: 33, marginRight: 20, marginLeft:20}}>
                                       fingerprint
                                    </span>
                                   <div
                                       style={{display: 'flex'}}> {(caseD!['nhs']) !== null ? caseD!['nhs'] : 'John/Jane Doe'}
                                   </div>

                                   <div style={{padding: 30, left:0}}>
                                       <button className='redx shRed'>  <span
                                           className="material-symbols-outlined grayx"
                                           style={{color: '#fff', fontSize: 18, marginRight: 20, marginLeft: 20}}>
                                       edit
                                    </span></button>
                                   </div>
                               </div>
                               <div>
                                   <hr style={{color: '#666'}}/>
                               </div>

                           </div>
                        );
                    })
                }
                </div>
            </div>
        </div>
    );

}