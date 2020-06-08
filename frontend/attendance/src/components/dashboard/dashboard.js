import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Waypoint } from '../waypoint/waypoint';

const apiEndpoint = "http://localhost:8000/app/api/minor-waypoint-history";
const pollingInterval = 1000;

function minorWaypointHistoryToWaypointData(minorWaypointHistory) {
  const waypointData = new Map();
  minorWaypointHistory.forEach(entry => {
    if (!waypointData.has(entry.waypoint_id.id)) {
      waypointData.set(
        entry.waypoint_id.id,
        {
          waypoint: entry.waypoint_id,
          minors: [entry.minor_id]
        }
      )
    } else {
      waypointData.get(entry.waypoint_id.id).minors.push(entry.minor_id) ;
    }
  });
  return waypointData;
}

export function Dashboard() {
  const [minorWaypointHistory, setMinorWaypointHistory] = useState(new Map());
  useEffect(() => {
    async function fetchData() {
      async function getMinorWaypointHistory() {
        try {
          const response = await axios.get(apiEndpoint);
          setMinorWaypointHistory(minorWaypointHistoryToWaypointData(response.data));
          console.log(response);
        } catch (error) {
          console.error(error);
        }
        setTimeout(getMinorWaypointHistory, pollingInterval)
      }
      await getMinorWaypointHistory();
    }
    fetchData();
  }, []);

  return (
    <div>
      <ul>
        {Array.from(minorWaypointHistory).map(entry =>
          <Waypoint waypointData={entry}></Waypoint>
        )}
      </ul>
    </div>
  );
}