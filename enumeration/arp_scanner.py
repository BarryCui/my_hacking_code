from scapy.all import *

interface = "your-NIC-name"
ip_range = "subnet/mask"
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst=ip_range)

ans, unans = srp(packet, timeout=2, iface=interface, inter=0.1)

for send, receive in ans:
    print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))