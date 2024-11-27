#Run this file to generate the PCAP file    


from scapy.all import IP, UDP, DNS, DNSQR, DNSRR, wrpcap
import random
import base64

packets = []

key = "whoop_whoop_thats_the_sound_of_da_police"
def encode_chunk(chunk):
    return base64.b64encode(chunk.encode()).decode()

encoded_key_chunks = [encode_chunk(key[i:i+6]) for i in range(0, len(key), 6)]

real_websites = [
    "www.google.com", "www.facebook.com", "www.amazon.com", "www.nytimes.com",
    "cnn.com", "updates.microsoft.com", "dl.google.com", "api.twitter.com",
    "www.netflix.com", "www.youtube.com", "www.github.com", "login.microsoftonline.com"
]

fake_fragments = [
    encode_chunk("FAKE1"), encode_chunk("NOISE"), encode_chunk("DUMMY1"),
    encode_chunk("FAKE2"), encode_chunk("NOISE2"), encode_chunk("DUMMY2"),
    encode_chunk("FAKE3"), encode_chunk("NOISE3"), encode_chunk("DUMMY3"),
    encode_chunk("FAKE4"), encode_chunk("NOISE4"), encode_chunk("DUMMY4"),
    encode_chunk("FAKE5"), encode_chunk("NOISE5"), encode_chunk("DUMMY5")
]

def add_fake_fragment():
    item = random.randint(0,14)
    record_type = random.choice(["TXT", "CNAME", "PTR"])
    if record_type == "TXT":
        packets.append(
            IP(dst="172.33.44.1")/UDP(dport=53)/DNS(
                id=random.randint(1000, 2000), qr=1, aa=1, qd=DNSQR(qname=f"txt{random.randint(1, 100)}.ctf.aharikum.com", qtype="TXT"),
                an=DNSRR(rrname=f"txt{random.randint(1, 100)}.ctf.aharikum.com", type="TXT", rdata=fake_fragments[item])
            )
        )
    elif record_type == "CNAME":
        packets.append(
            IP(dst="172.33.44.1")/UDP(dport=53)/DNS(
                id=random.randint(1000, 2000), qr=1, aa=1, qd=DNSQR(qname=f"cname{random.randint(1, 100)}.ctf.aharikum.com", qtype="CNAME"),
                an=DNSRR(rrname=f"cname{random.randint(1, 100)}.ctf.aharikum.com", type="CNAME", rdata=f"{fake_fragments[item]}.target.aharikum.com")
            )
        )
    else:
        packets.append(
            IP(dst="172.33.44.1")/UDP(dport=53)/DNS(
                id=random.randint(1000, 2000), qr=1, aa=1, qd=DNSQR(qname=f"1.0.0.127.in-addr.arpa", qtype="PTR"),
                an=DNSRR(rrname="1.0.0.127.in-addr.arpa", type="PTR", rdata=f"{fake_fragments[item]}.ptr.aharikum.com")
            )
        )


def add_random_noise(count=5):
    for _ in range(count):
        record_type = random.choice(["real", "fake"])
        if record_type == "real":
            domain = random.choice(real_websites)
            packets.append(IP(dst="172.33.44.1")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=domain)))
        else:
            add_fake_fragment()

for i, chunk in enumerate(encoded_key_chunks):
    if i % 3 == 0:
        packets.append(IP(dst="172.33.44.1")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=f"{chunk}.sub{i}.ctf.aharikum.com")))
    elif i % 3 == 1:
        packets.append(
            IP(dst="172.33.44.1")/UDP(dport=53)/DNS(
                id=i, qr=1, aa=1, qd=DNSQR(qname=f"txt{i}.ctf.aharikum.com", qtype="TXT"),
                an=DNSRR(rrname=f"txt{i}.ctf.aharikum.com", type="TXT", rdata=chunk)
            )
        )
    else:
        packets.append(
            IP(dst="172.33.44.1")/UDP(dport=53)/DNS(
                id=i, qr=1, aa=1, qd=DNSQR(qname=f"cname{i}.ctf.aharikum.com", qtype="CNAME"),
                an=DNSRR(rrname=f"cname{i}.ctf.aharikum.com", type="CNAME", rdata=f"{chunk}.target.ctf.aharikum.com")
            )
        )
    add_random_noise(random.randint(5, 15))


while len(packets) < 200:
    add_random_noise(1)

output_pcap = "chall.pcap"
wrpcap(output_pcap, packets)

