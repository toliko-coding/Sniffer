const dgram = require("dgram");

const socket = dgram.createSocket("udp4");

socket.on("error", (err) => {
  console.error(`UDP error: ${err.stack}`);
});

socket.on("message", (msg, rinfo) => {
  console.log("Recieved UDP message");
});

socket.bind(12321, "localhost");
