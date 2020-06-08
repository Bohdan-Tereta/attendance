import React, { useState, useEffect } from 'react';

export function Waypoint(props) {
  const [waypointData, setWaypointData] = useState(props.waypointData);
  useEffect(() => {
    setWaypointData({ ...props.waypointData });
  }, [props.waypointData]);

  return (
    <li key={waypointData.id}>
      {JSON.stringify(waypointData)}
    </li>
  );
}