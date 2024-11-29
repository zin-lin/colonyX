import React, {useEffect, useState} from "react";
import {useNavigate, useParams} from "react-router-dom";
import axios, {all} from "axios";
import { io, Socket } from 'socket.io-client';

interface DATA {
    cid : string ;

}

export default function Track() {
    const {cid} = useParams();
    const [start, setStart] = useState(true);
    const [name, setName] = useState("");
    const [status, setStatus] = useState(0);
    const [hos, setHos] = useState("");
    const [am, setAm] = useState("");
    const [nhs, setNhs] = useState("");
    const [dob, setDob] = useState("");
    const [address, setAddress] = useState("");
    const [medical, setMedical] = useState("");
    const [injury, setInjury] = useState("");
    const [gender, setGender] = useState("");
    const [age, setAge] = useState("");
    const [time, setTime] = useState("");
    const [action, setAction] = useState("");
    const [allergies, setAllergies] = useState("");
    const navigate = useNavigate();

    const handleName = (event: React.ChangeEvent<HTMLInputElement>) => {
        setName(event.target.value);
    };

    const handleAddress = (event: React.ChangeEvent<HTMLInputElement>) => {
        setAddress(event.target.value);
    };

    const handleAllergies = (event: React.ChangeEvent<HTMLInputElement>) => {
        setAllergies(event.target.value);
    };

    const handleMedical = (event: React.ChangeEvent<HTMLInputElement>) => {
        setMedical(event.target.value);
    };

    const handleGender = (event: React.ChangeEvent<HTMLInputElement>) => {
        setGender(event.target.value);
    };

    useEffect(()=>{

        let id = cid!.toString();

        axios.get(`http://localhost:8080/get/${cid}`).then((res) => res.data).then(
            pat =>{
                setNhs(pat['nhs']);
                setHos(pat['hospital_code']);
                setAction(pat['action_taken']);
                if (start){
                setName(pat['name']);
                setAddress(pat['address']);
                setAllergies(pat['allergies']);
                setGender(pat['gender']);
                setMedical(pat['medical']);
                }
                setStart(false);
                setAge(pat['age']);
                setDob(pat['dob']);
                setInjury(pat['injury']);
                setTime(pat['time']);
            }
        ).catch(e => console.log(e));
    }, [name, address, allergies, gender, medical]);

    return (

        <div className="page">
            <link rel="stylesheet"
                  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"/>
            <div style={{padding: 30, borderRadius: 23}}>
                <div style={{
                    flex: 2,
                    display: 'flex',
                    width: 'auto',
                    justifyContent: "center",
                    alignItems: 'center',
                    alignContent: 'center',
                    flexWrap: 'wrap',
                    order: 2,
                    flexDirection: 'row'
                }}>



                </div>
            </div>


            <div style={{
                background: 'rgba(31,43,50,0.39)',
                height: '80%',
                margin:'auto',
                width: '80%',
                maxHeight: 800,
                maxWidth: 1050,
                minWidth: 300,
                minHeight: 250,
                borderRadius: 30,
                overflow: 'auto'
            }} >

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
                                        person
                                    </span>
                        </button>
                    </div>

                    <form onSubmit={(e) => {
                        let namet = (document.getElementById('name') as HTMLInputElement).value;
                        let addresst = (document.getElementById('address') as HTMLInputElement).value;
                        let allergiest = (document.getElementById('allergies') as HTMLInputElement).value;
                        let gendert = (document.getElementById('gender') as HTMLInputElement).value;
                        let medicalt = (document.getElementById('medical') as HTMLInputElement).value;
                        const data: FormData = new FormData();
                        data.append('nhs', nhs);
                        data.append('action_taken', action);
                        data.append('dob', dob);
                        data.append('name', namet);
                        data.append('medical', medicalt);
                        data.append('address', addresst);
                        data.append('allergies', allergiest);
                        data.append('gender', gendert);
                        data.append('injury', injury);
                        data.append('timestamp', time);
                        data.append('age', age);
                        data.append('hospital_code', hos);


                        axios.post(`http://localhost:8080/update/${nhs}`, data, {
                            headers: {
                                'Content-Type': 'multipart/form-data',
                            },
                        }).then(
                            res=>{
                                alert('updated')
                            }
                        ).catch(error => {
                            alert(error)
                        })

                    }}>

                        <div style={{display: 'flex', alignItems: 'center', marginLeft: 26}}>
                                    <span style={{color: '#aaa', fontSize: 19, marginRight: 10}}
                                          className="material-symbols-outlined">
                                         task
                                    </span><p style={{color: '#aaa', fontSize: 14}}>Name</p>
                        </div>
                        <input placeholder='@Name' className='noner' id="name" value={name} style={{color:'#eee'}} onChange={handleName}/>
                        <br/>

                        <div style={{display: 'flex', alignItems: 'center', marginLeft: 26}}>
                                    <span style={{color: '#aaa', fontSize: 19, marginRight: 10}}
                                          className="material-symbols-outlined">
                                         task
                                    </span><p style={{color: '#aaa', fontSize: 14}}>Address</p>
                        </div>
                        <input placeholder='@Address' className='noner' id="address" value={address} style={{color:'#eee'}} onChange={handleName}/>
                        <br/>

                        <div style={{display: 'flex', alignItems: 'center', marginLeft: 26}}>
                                    <span style={{color: '#aaa', fontSize: 19, marginRight: 10}}
                                          className="material-symbols-outlined">
                                         task
                                    </span><p style={{color: '#aaa', fontSize: 14}}>Allergies</p>
                        </div>
                        <input placeholder='@Allergies' className='noner' id="allergies" value={allergies} style={{color:'#eee'}} onChange={handleAllergies}/>
                        <br/>

                        <div style={{display: 'flex', alignItems: 'center', marginLeft: 26}}>
                                    <span style={{color: '#aaa', fontSize: 19, marginRight: 10}}
                                          className="material-symbols-outlined">
                                         task
                                    </span><p style={{color: '#aaa', fontSize: 14}}>Gender</p>
                        </div>
                        <input placeholder='@Gender' className='noner' id="gender" value={gender} style={{color:'#eee'}} onChange={handleGender}/>
                        <br/>

                        <div style={{display: 'flex', alignItems: 'center', marginLeft: 26}}>
                                    <span style={{color: '#aaa', fontSize: 19, marginRight: 10}}
                                          className="material-symbols-outlined">
                                         task
                                    </span><p style={{color: '#aaa', fontSize: 14}}>Medical</p>
                        </div>
                        <input placeholder='@Medical' className='noner' id="medical" value={medical} style={{color:'#eee'}}  onChange={handleMedical}/>
                        <br/>


                        <button className='redx shRed' type="submit" style={{
                            margin: 20,
                            width: 170,
                            paddingTop: 8,
                            paddingBottom: 8
                        }}>Update Record
                        </button>
                    </form>
                </div>

            </div>

        </div>
    );
}