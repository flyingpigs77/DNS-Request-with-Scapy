from scapy.all import *

sol = sr1(IP(dst="1.1.1.1")/UDP(sport = 53, dport=53)/DNS(qd=DNSQR(qname="twitter.com")))
print(sol[DNS])

# if answer:
#     for packet in answer[0]:
#         received = packet[1]
#         if received.haslayer(DNS):
#             print(received.getlayer(IP).dst)

