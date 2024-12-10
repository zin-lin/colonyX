import React from "react";

type DataProps = {
  row: string[]; // Define the type of the row prop
  key: number;
};



export default function DataStrip({ row, key }: DataProps) {

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


  return (
      <div>
      <div style={{
          width: '100%', borderRadius: 20, borderWidth: 2, borderColor: colors[row[0]], flex: 1,  display:'flex'
      }}>
          <p style={{color: colors[row[0]], marginLeft: 10, marginRight: 10}}>{row[0]}</p>
          <p style={{color: colors[row[0]], marginLeft: 10, marginRight: 10}}> queen count: {row[1]}</p>
          <p style={{color: colors[row[0]], marginLeft: 10, marginRight: 10}}> scout count: {row[2]}</p>
          <p style={{color: colors[row[0]], marginLeft: 10, marginRight: 10}}> minim count: {row[3]}</p>
          <p style={{color: colors[row[0]], marginLeft: 10, marginRight: 10}}> major count: {row[4]}</p>
          <p style={{color: colors[row[0]], marginLeft: 10, marginRight: 10}}> resource count: {row[5]}</p>

      </div>
      <hr/>
      </div>

  );
}