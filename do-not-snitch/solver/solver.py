from scapy.all import rdpcap, DNS
import re
import base64

chunks = []

packets = rdpcap('../chall.pcap')

def get_key():
    fake_chunks = {"FAKE", "DUMMY", "NOISE"}
    for pkt in packets:
        found_noise = 0
        if DNS in pkt:
            dns = pkt[DNS]
            if dns.qr == 0 and dns.opcode == 0 and dns.qdcount > 0:
                qname = dns.qd.qname.decode()
                match = re.match(r'^([A-Za-z0-9+/=]+)\.sub(\d+)\.ctf\.aharikum\.com\.?$', qname)
                if match:
                    chunk = match.group(1)
                    chunk = base64.b64decode(chunk).decode()
                    idx = int(match.group(2))
                    for fragment in fake_chunks:
                        if fragment in chunk:
                            found_noise = 1
                    if not found_noise:
                        chunks.append((idx, chunk))
            elif dns.qr == 1 and dns.opcode == 0 and dns.qdcount > 0:
                qname = dns.qd.qname.decode()
                if dns.ancount > 0:
                    for i in range(dns.ancount):
                        rr = dns.an[i]
                        if rr.type == 16: 
                            match = re.match(r'^txt(\d+)\.ctf\.aharikum\.com\.?$', qname)
                            if match:
                                idx = int(match.group(1))
                                txt_data = ''.join([txt.decode() if isinstance(txt, bytes) else txt for txt in rr.rdata])
                                chunk = txt_data
                                chunk = base64.b64decode(chunk).decode()
                                for fragment in fake_chunks:
                                    if fragment in chunk:
                                        found_noise = 1
                                if not found_noise:
                                    chunks.append((idx, chunk))
                        elif rr.type == 5: 
                            match = re.match(r'^cname(\d+)\.ctf\.aharikum\.com\.?$', qname)
                            if match:
                                idx = int(match.group(1))
                                rdata = rr.rdata.decode() if isinstance(rr.rdata, bytes) else rr.rdata
                                match_chunk = re.match(r'^([A-Za-z0-9+/=]+)\.target\.ctf\.aharikum\.com\.?$', rdata)
                                if match_chunk:
                                    chunk = match_chunk.group(1)
                                    chunk = base64.b64decode(chunk).decode()
                                    for fragment in fake_chunks:
                                        if fragment in chunk:
                                            found_noise = 1
                                    if not found_noise:
                                        chunks.append((idx, chunk))


    chunks.sort(key=lambda x: x[0])

    chunks = [chunk for idx, chunk in chunks]
    key = ''.join(chunks)
    return key


def main():
    # Connect to server
    conn = remote("challenge", 5555)

    conn.revuntil(b"==>")
    key = get_key()
    conn.sendline(key.encode())

    # Receive all
    response = conn.recvall()

    # Convert response to ASCII
    response = response.decode()

    # responseß
    # Write flag to file
    with open("./flag", "w") as w:
        w.write(response.decode("utf-8"))

if __name__ == "__main__":
    main()