const dgram = require("dgram");

const server = dgram.createSocket("udp4");

server.on("error", (err) => {
  console.error(`UDP error: ${err.stack}`);
});

server.on("message", (msg, rinfo) => {
  console.log("Recieved UDP message");
});

server.bind(12321, "localhost", () => {
  server.setSendBufferSize(100);
});
