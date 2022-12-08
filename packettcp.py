import socket

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
s.bind(("ens3", 0))

ethernet  = b'\xfa\x16\x3e\x6e\x6b\x0b' # MAC Address Destination
ethernet += b'\xfa\x16\x3e\x6b\x6b\x0b' # MAC Address Source
ethernet += b'\x08\x00'                 # Protocol-Type: IPv4

ip_header  = b'\x45\x00\x00\x7d'  # Version, IHL, Type of Service | Total Length
ip_header += b'\x04\xa2\x40\x00'  # Identification | Flags, Fragment Offset
ip_header += b'\x3e\x06\xf4\x0e'  # TTL, Protocol | Header Checksum
ip_header += b'\x0a\x00\x01\x01'  # Source Address
ip_header += b'\x0a\x00\x01\x89'  # Destination Address

tcp_header  = b'\xc3\xea\x80\x4b' # Source Port | Destination Port
tcp_header += b'\xc1\xd9\x8a\xcb' # Sequence Number
tcp_header += b'\x78\xfa\x2e\xfe' # Acknowledgement Number
tcp_header += b'\x80\x18\x0a\x9e' # Data Offset, Reserved, Flags | Window Size
tcp_header += b'\xca\xf7\x00\x00' # Checksum | Urgent Pointer

payload = bytes('kdflaejupoiqhfkadlncalspnehkohivwjnpokrnhofandkljvnhffadfcdeafefafscsdfcsdfaaadfcdfdasfafdsfasdfasdvnhsakldrjfklsdfh;asldkhgklafdsfaefklh;asdklfjslak;fh;aklshfaksljflaj', 'utf-8')
packet = ethernet + ip_header + tcp_header + payload
#s.send(packet)
i=0
while i==0:
	s.send(packet)
