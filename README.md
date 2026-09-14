# Packet Sniffer

Coursework for a Cyber Risk Assessment course: a UDP client and server on localhost, a separate script that sniffs their traffic with Scapy, and a simulated lost packet that gets resent.

## What it does

- `server.py` listens on UDP `localhost:12321`. It prints each payload and the client's address, and answers every datagram with `Hello UDP Client`.
- `client.py` splits the message `Hello UDP Server` into words and computes an XOR value `e` across them. Each word is sent as a pickled `(data, e, d)` tuple, with `d = 3`, three seconds apart.
- The client holds back the last word on purpose to simulate a lost packet. After the server has buffered two packets it replies `Resend packet`, and the client sends the missing word.
- `sniffer.py` is the adversary. It isn't part of the connection. It uses Scapy's `sniff()` with the filter `port 12321`, captures the first two matching packets, and prints every layer of each one with `packet.show()`.

## Tech stack

- Python 3
- Scapy 2.4.5 (packet capture)
- `socket` (UDP), `pickle` (packet payloads)

## Project structure

| File | Purpose |
| --- | --- |
| `server.py` | UDP server: logs and replies to datagrams, buffers data packets, asks for a resend |
| `client.py` | UDP client: sends the message word by word with the XOR value, answers the resend request |
| `sniffer.py` | Adversary: captures and prints packets on port 12321 with Scapy |
| `requirements.txt` | Pins `scapy==2.4.5` (the file is UTF-16 encoded) |
| `Sniffer.pdf` | The assignment brief |

## Running it

Prerequisites:

- Python 3.9 or newer. `server.py` uses the built-in `tuple[...]` type annotation.
- Scapy: `pip install scapy==2.4.5`
- Packet-capture privileges for the sniffer: root on Linux/macOS, Administrator with Npcap on Windows.

Open three terminals in the repository folder and start the scripts in this order:

```sh
sudo python3 sniffer.py   # adversary, waits for traffic on port 12321
python3 server.py         # UDP server
python3 client.py         # UDP client
```

Notes on behavior:

- `sniffer.py` doesn't choose an interface, so Scapy uses its default one. Depending on the OS, you may need to point it at the loopback interface to see localhost traffic.
- `sniffer.py` exits after two packets because of `count=2`.
- The server socket has a 5-second timeout. Once the client finishes and traffic stops, `server.py` exits with a timeout error.

## Notes

- Team coursework from July 2022, built with yuval1121, who made most of the commits in this repository.
- The brief (`Sniffer.pdf`) asks for more than the committed code does:
  - It asks for an explicit sequence number in each packet. The payload tuple here has none.
  - For Task 2, it asks the server to rebuild a missing packet from the XOR of the received packets. This code computes and sends the XOR value but never uses it to rebuild anything. The server asks the client to resend the missing packet instead.
  - Task 3 (client, server, and adversary as separate bridged VMs) isn't in the code. Everything runs on localhost.
- The brief recommends Python 2.7. The code is written for Python 3.
- The commit history shows a Flask setup, a Node.js client/server, and a Docker Compose setup being tried and removed before the final three Python scripts.

Part of my portfolio: https://tk-coding.com/cybersecurity/toolkit/sniffer
