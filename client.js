const dgram = require("dgram");
const s = dgram.createSocket("udp4");

s.send;

setInterval(() => {
  s.send(Buffer.from("this is a test"), 12321, "localhost");
}, 3000);
