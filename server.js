const dgram = require("dgram");

const socket = dgram.createSocket("udp4");

socket.on("listening", () => {
  const addr = socket.address;
  console.log(`Listening for UDP packets at ${addr.address}:${addr.port}`);
});

socket.on("error", (err) => {
  console.error(`UDP error: ${err.stack}`);
});

socket.on("message", (msg, rinfo) => {
  console.log("Recieved UDP message");
});
socket.bind(12321, "localhost");

// socket.send(Buffer.from("abc"), 12321, "localhost");
