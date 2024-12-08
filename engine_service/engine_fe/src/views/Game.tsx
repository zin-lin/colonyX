import React, {useEffect, useState} from "react";
import axios, {all} from "axios";
import Row from "../components/Row";
import {useNavigate} from "react-router-dom";

interface DATA {
    cid : string ;

}

export default function Game() {

    const [grid, setGrid] = useState([[]]);
  const [auto, setAuto] = useState(true);
  let intervalId: NodeJS.Timeout | null = null;
  const navigate = useNavigate();

  const perform_turn = () => {
    intervalId = setInterval(async () => {
      try {
        const response = await fetch(`http://localhost:15000/api/game/`);
        const data = await response.json();
        if (data['env'].length !== 0) {
          setGrid(data['env']);
        } else {
          stopTurn();
        }
      } catch (err) {
        console.error(err);
      }
    }, 200);
  };

  const stopTurn = () => {
    if (intervalId) {
      clearInterval(intervalId);
      intervalId = null;
    }
  };

  useEffect(() => {
    fetch(`http://localhost:15000/api/game`)
      .then((res) => res.json())
      .then((data) => {
        setGrid(data['env']);
        if (auto) {
          perform_turn();
        }
      })
      .catch((e) => console.log(e));

    return () => stopTurn(); // Cleanup interval on unmount
  }, []);

    return (

        <div className="page">
            <link rel="stylesheet"
                  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"/>
            <div style={{padding: 30, borderRadius: 23}}>
                <div style={{

                    flex: 2,
                    display: 'flex',
                    width: '100%',
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
                padding: '20px',
                margin:'auto',

                maxHeight: 1500,
                maxWidth: 1050,
                borderRadius: 30,
                marginBottom: 20,
                overflow: 'auto'
            }} >

                {
                    grid.map((row, index) =>{
                        return (
                            <Row row={row} key={index}/>
                        );
                    })
                }

                <div style={{display:'flex', justifyContent:'center'}}>
                    <button><span className='material-symbols-outlined' style={{color: '#ff5959'}} onClick={()=>{
                        setAuto(false);

                        window.location.reload();
                        navigate(-1);
                    }}>stop</span></button>
                    <button><span className='material-symbols-outlined' style={{color: '#5ebcff'}}>arrow_back</span></button>
                    <button><span className='material-symbols-outlined' style={{color: '#86f4a0'}} onClick={()=>{
                        setAuto(true)
                        perform_turn();
                    }}>play_arrow</span></button>

                </div>

            </div>

        </div>
    );
}