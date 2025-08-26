import socket
import struct

# Create raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
    packet, addr = s.recvfrom(65535)

    # Extract IP header (first 20 bytes)
    ip_header = packet[:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    iph_length = ihl * 4

    ttl = iph[5]
    protocol = iph[6]
    src_ip = socket.inet_ntoa(iph[8])
    dst_ip = socket.inet_ntoa(iph[9])

    print(f"\n📡 IP Packet: {src_ip} → {dst_ip} | Protocol: {protocol} | TTL: {ttl}")

    # Extract TCP header (next 20 bytes after IP header)
    tcp_header = packet[iph_length:iph_length+20]
    tcph = struct.unpack('!HHLLBBHHH', tcp_header)

    src_port = tcph[0]
    dst_port = tcph[1]
    sequence = tcph[2]
    ack = tcph[3]
    doff_reserved = tcph[4]
    tcph_length = doff_reserved >> 4

    print(f"🔗 TCP Segment: {src_ip}:{src_port} → {dst_ip}:{dst_port} | Seq={sequence} Ack={ack}")
