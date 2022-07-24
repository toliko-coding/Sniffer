from scapy.all import *

conf.L3socket = L3RawSocket


def packet_callback(packet):
    print(packet.show())


def main():
    print("hello from sniffer")
    sniff(prn=packet_callback, count=2, filter="port 12321", iface="lo")


if __name__ == "__main__":
    main()
