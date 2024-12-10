import React from "react";

type RowProps = {
  row: string[]; // Define the type of the row prop
  key: number;
};

type para = {
  type: string;
}

type ant_para = {
  type: string;
  colony_id: string;
}

export default function Row({ row, key }: RowProps) {

  const colors: Record<string, string> = {
    LC1: '#44b9e4',
    LC2: '#6eff9c',
    LC3: '#ff6464',
    LC4: '#ffdd55',
    LC5: '#c041ff',
    LC6: '#6c23ff',
    LC7: '#ffb972',
    LC8: '#e4da6f',
    LC9: '#ff6c6c',
    LC10: '#598eff',
  }

  const Resource = ({type}:para ) =>{

    if (type === "")
      return (<span className="material-symbols-outlined" style={{color: '#12a34c',}}>forest
              </span>);

    else if (type === "1")
            return (<span className="material-symbols-outlined" style={{color: '#73b4ea',}}>water_drop
              </span>);

    else if (type === "2")
      return (<span className="material-symbols-outlined" style={{color: '#ea7373',}}>egg_alt
              </span>);

    else
      return (<span className="material-symbols-outlined" style={{color: '#fff262',}}>warning
              </span>);


  }

  // Ants
  const Ant = ({type, colony_id}:ant_para ) =>{
    if (type === "1")
      return (<span className="material-symbols-outlined" style={{color: colors[colony_id] ,}}>bug_report
              </span>);

    else if (type === "2")
            return (<span className="material-symbols-outlined" style={{color: colors[colony_id],}}>emoji_nature
              </span>);

    else if (type === "3")
      return (<span className="material-symbols-outlined" style={{color: colors[colony_id],}}>pest_control
              </span>);

    else
      return (<span className="material-symbols-outlined" style={{color: colors[colony_id],}}>bug_report
              </span>);


  }

  return (
    <div style={{ display: "flex", flexDirection: "row" , flex:1, marginBottom: 1}}>
     {row.map((cell, index) => {
        let data = cell.split(',');
        if (cell === ',,,,,') {return (
          <div
            key={index}
            style={{
                display: 'flex',
                background:'#120d13',
                textAlign: "center",                        justifyContent:'center',
                        alignItems:'center',
                width: 25,
                height: 35,
                margin: 0.5,
                flex: 1,
            }}
          >
          </div>
        );
        }

        else if (data[3].length > 0 && data[2]==='') {
            // if resource
            return (
                <div
                    key={index}
                    style={{
                        display: 'flex',
                        background: '#120d13',
                        textAlign: "center",                        justifyContent:'center',
                        alignItems:'center',
                        width: 25,
                        height: 35,
                        margin: 1,
                        flex: 1,
                    }}
                >
                  <Resource type={data[5]}/>
                </div>

            );
        }


        else if (data[0].length > 0 && data[1].length > 0 && data[2].length ===0 && data[3].length === 0 && data[4].length === 0 && data[5].length === 0) {
            // if pheromone
            return (
                <div
                    key={index}
                    style={{
                        display: 'flex',
                        background: 'rgba(14,44,33,0.36)',
                        textAlign: "center",
                        width: 25,                        justifyContent:'center',
                        alignItems:'center',
                        height: 35,
                        margin: 1,
                        flex: 1,
                    }}
                >

                </div>

            );
        }

        else if (data[2] !== "") {
          // if ant
          return (<div
              key={index}
              style={{
                display: 'flex',
                background: 'rgba(23,76,56,0.31)',
                textAlign: "center",
                width: 25,                        justifyContent:'center',
                        alignItems:'center',
                height: 35,
                margin: 1,
                flex: 1,
              }}
          >
            <Ant type={data[4]} colony_id={data[1]}/>
          </div>)
        }

           else if (data[1].length > 0 && data[0].length === 0 && data[2] === "") {
            // if colony
            return (
                <div
                    key={index}
                    style={{
                        display: 'flex',
                        background: '#120d13',
                        textAlign: "center",
                        width: 25,
                        height: 35,
                        margin: 1,                        justifyContent:'center',
                        alignItems:'center',

                        flex: 1,
                    }}
                >
                    <span className="material-symbols-outlined" style={{color: '#eee',}}>fort</span>
                </div>

            );
        }


     })}

    </div>
  );
}