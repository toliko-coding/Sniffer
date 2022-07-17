const dgram = require("dgram");
const s = dgram.createSocket("udp4");

console.log("hello from client");

setInterval(() => {
  s.send(Buffer.from("this is a test"), 12321, "localhost");
}, 3000);
