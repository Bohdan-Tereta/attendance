/*
This is a tool to simulate minors movement between waypoints
*/
const axios = require('axios').default;

const apiEndpoint = "http://localhost:8000/app/api/minor-waypoint-history";

let max_minor_id = 12;
let max_timeout = 5000;
let max_waypoint_id = 5;

let min_minor_id = 1;
let min_timeout = 1000;
let min_waypoint_id = 1;

async function addWaypointHistory() {
  let waypoint_id = getRandomWaypointId();
  let minor_id = getRandomMinorId();
  let timeout = getRandomTimeout();

  const payload = {
    created_at: new Date().toISOString(),
    minor_id: minor_id,
    waypoint_id: waypoint_id
  }
  try {
    await axios.post(apiEndpoint, payload);
    console.log(payload);
  } catch (error) {
    console.log(`${error}: ${JSON.stringify(error.response.data)}`);
  }
  setTimeout(addWaypointHistory, timeout);
}


function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getRandomMinorId() {
  return getRandomIntInclusive(min_minor_id, max_minor_id);
}

function getRandomTimeout() {
  return getRandomIntInclusive(min_timeout, max_timeout);
}

function getRandomWaypointId() {
  return getRandomIntInclusive(min_waypoint_id, max_waypoint_id);
}

async function mainLoop() {

};

addWaypointHistory();