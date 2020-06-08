import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Waypoint } from './waypoint';

const apiEndpoint = "http://localhost:8000/app/api/minor-waypoint-history";
const pollingInterval = 5000;

export function Dashboard() {
  const [minorWaypointHistory, setMinorWaypointHistory] = useState([]);
  useEffect(() => {
    async function fetchData() {
      await getMinorWaypointHistory();
    }
    fetchData();
  }, []);

  async function getMinorWaypointHistory() {
    try {
      const response = await axios.get(apiEndpoint);
      setMinorWaypointHistory(response.data);
      console.log(response);
    } catch (error) {
      console.error(error);
    }
    setTimeout(getMinorWaypointHistory, pollingInterval)
  }

  return (
    <div>
      <ul>
        {minorWaypointHistory.map(entry =>
          <Waypoint waypointData={entry}></Waypoint>
        )}
      </ul>
    </div>
  );
}