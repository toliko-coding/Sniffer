const dgram = require("dgram");

const socket = dgram.createSocket("udp4");

socket.on("error", (err) => {
  console.error(`UDP error: ${err.stack}`);
});

socket.on("message", (msg, rinfo) => {
  console.log("Recieved UDP message");
});

socket.bind(12321, "localhost");

// Buffer.from("test", 0, 100);
socket.send(
  "abcdfgdfrgtdfgfdgdfgfdgfdgfdgd",
  12321,
  "localhost",
  (err, bytes) => {
    // console.log(bytes);
  }
);
socket.send(Buffer.from("abcdfgdfrgtdfgfdgdfgfdgfdgfdgd"), 12321, "localhost");
socket.send(Buffer.from("abcD"), 12321, "localhost");
