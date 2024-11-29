import React, {FormEvent} from "react";
import { useNavigate} from "react-router-dom";
import axios from "axios";

export default function AddCase () {

    const navigate = useNavigate();
    const declare_emergency = (e: FormEvent)=>{
        e.preventDefault();
        let pname = (document.getElementById('name') as HTMLInputElement).value;
        let address = (document.getElementById('address') as HTMLInputElement).value;
        let des = (document.getElementById('des') as HTMLInputElement).value;
        let postcode = (document.getElementById('postcode') as HTMLInputElement).value;
        let nature = (document.getElementById('type') as HTMLSelectElement).value;
        let dob = (document.getElementById('dob-d') as HTMLInputElement).value + '/' + (document.getElementById('dob-m') as HTMLInputElement).value
        + '/' + (document.getElementById('dob-y') as HTMLInputElement).value;

        alert("Declaring fraud emergency in the UK is a serious crime and will have you arrested")

        let case_new = {
            'pname' : pname,
            'address' : address,
            'des' : des,
            'postcode' : postcode,
            'nature' : nature,
            'dob':dob
        }

        const form:FormData = new FormData();
        form.append('pname', pname);
        form.append('address', address);
        form.append('des', des);
        form.append('postcode', postcode);
        form.append('nature', nature);
        form.append('dob', dob);

        console.log(case_new);
        axios.post('http://localhost:8000/api/add-case', form, {withCredentials:true}).then(response => {
            let id = response.data.id;
            navigate(`/track/${id}`);
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
                        background: 'rgb(250,250,250,1.0)',
                        height: '80%',
                        padding: 20,
                        width: '80%',
                        maxHeight: 405,
                        maxWidth: 700,
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
                                        add
                                    </span>
                                </button>
                            </div>

                            <form onSubmit={(e) => {
                                declare_emergency(e);
                            }}>
                                <div style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    marginLeft: 0,
                                    justifyContent: 'center'
                                }}>
                                    <span style={{color: '#777', fontSize: 19, marginRight: 10}}
                                          className="material-symbols-outlined">
                                         person
                                    </span><p style={{color: '#777', fontSize: 14}}>Patient Name</p>
                                </div>
                                <input placeholder='John Doe' className='noner' id="name"/>
                                <br/>

                                <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                                        <span style={{color: '#777', fontSize: 19, marginRight: 10}}
                                              className="material-symbols-outlined">
                                             alarm
                                        </span> <p style={{color: '#777', fontSize: 14}}>Patient DOB</p>
                                </div>
                                <div style={{
                                    display: 'flex',
                                    justifyContent: 'center',
                                    marginLeft: 40,
                                    marginRight: 40, alignItems: 'center'
                                }}>
                                    <input placeholder='DD' className='noner' id="dob-d"/><p>/</p>
                                    <input placeholder='MM' className='noner' id="dob-m"/><p>/</p>
                                    <input placeholder='YY' className='noner' id="dob-y"/>

                                </div>
                                <br/>

                                <div style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    marginLeft: 0,
                                    justifyContent: 'center'
                                }}>
                                        <span style={{color: '#777', fontSize: 19, marginRight: 10}}
                                              className="material-symbols-outlined">
                                             pin_drop
                                        </span> <p style={{color: '#777', fontSize: 14}}>Incident Address</p>
                                </div>
                                <input placeholder='888 Denvers Avenue, Mistone County' className='noner' id="address"/>
                                <br/>

                                <div style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    marginLeft: 0,
                                    justifyContent: 'center'
                                }}>
                                        <span style={{color: '#777', fontSize: 19, marginRight: 10}}
                                              className="material-symbols-outlined">
                                             postcode
                                        </span> <p style={{color: '#777', fontSize: 14}}>Incident Postcode</p>
                                </div>
                                <input placeholder='EH116AR' className='noner' id="postcode"/>
                                <br/>

                                <div style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    marginLeft: 0,
                                    justifyContent: 'center'
                                }}>
                                        <span style={{color: '#777', fontSize: 19, marginRight: 10}}
                                              className="material-symbols-outlined">
                                             description
                                        </span> <p style={{color: '#777', fontSize: 14}}>Incident Description</p>
                                </div>
                                <input placeholder='white female, broken leg' className='noner' id="des"/>
                                <br/>


                                <div style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    marginLeft: 0,
                                    justifyContent: 'center'
                                }}>
                                        <span style={{color: '#777', fontSize: 19, marginRight: 10}}
                                              className="material-symbols-outlined">
                                             category
                                        </span> <p style={{color: '#777', fontSize: 14}}>Incident Nature</p>
                                </div>
                                <select className='noner' id="type">
                                    <option>medical</option>
                                    <option>fire</option>
                                    <option>crime</option>
                                </select>
                                <br/>

                                <button className='redx shRed' type="submit" style={{
                                    margin: 20,
                                    width: 170,
                                    paddingTop: 8,
                                    paddingBottom: 8
                                }}>Declare Emergency
                                </button>
                            </form>
                        </div>
                    </div>

                </div>
            </div>
        </div>

    );

}