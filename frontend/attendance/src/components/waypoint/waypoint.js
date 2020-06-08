import React, { useState, useEffect } from 'react';
import './waypoint.scss';

function waypointDataToText(waypointData) {
  return `${waypointData.waypoint.description}, children: ${waypointData.minors.length}`;
}

export function Waypoint(props) {
  const [waypointData, setWaypointData] = useState(props.waypointData);
  useEffect(() => {
    setWaypointData({ ...props.waypointData });
  }, [props.waypointData]);

  return (
    <li className="waypoint_block" key={waypointData[0]}>
      {waypointDataToText(waypointData[1])}
      <ul>
        {waypointData[1].minors.map(minor =>
          <li className='minor_block'>
            {`${minor.user_id.first_name} ${minor.user_id.last_name} (${minor.user_id.username})`}
          </li>
        )}
      </ul>
    </li >
  );
}