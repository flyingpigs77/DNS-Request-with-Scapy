from scapy.all import *

sr1(IP(dst="1.1.1.1")/ICMP())

# sr1(IP(dst="1.1.1.1")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="www.thepacketgeek.com")),verbose=0)