# Do Not Snitch Challenge

## Introduction
DNS is a vital part of the internet, translating human-readable domain 
names into IP addresses. This challenge involves a lot of packet analysis.
The player is given a Packet capture to analyse.However, in this challenge, 
it’s being abused as a smuggling route for secret data. The hidden payload 
is split into chunks, disguised as various DNS records, and spread across 
the traffic in the PCAP file. Some records contain noise to confuse you, 
but the real chunks, when correctly extracted and  reassembled, will reveal 
the secret key.


## Walkthrough
Here is the outline on how to solve this challenge
1. Open the PCAP File:
   Load chall.pcap in Wireshark and check a few packet. 
   Then use a Python library like Scapy. Filter the traffic for DNS packets 
   (dns filter in Wireshark).

2. Identify the Data Chunks:
   Look for unusual domains and subdomains. They might contain base64-encoded strings.
   Pay attention to TXT and CNAME records—they may hide valuable chunks.
   Subdomain names can also contain hidden data.

3. Filter Out the Noise:
   Ignore packets that look like realistic traffic (e.g., queries to google.com or facebook.com).
   Focus on domains ending with ctf.aharikum.com.

4. Reassemble the Key:
   Sort the chunks by their indices (embedded in subdomains or records).
   Decode the chunks using base64 and concatenate them in the correct order.

5. Retrieve the Secret:
   Combine the decoded data to reveal the flag or key.


# Conclusion
This was an exciting challenge to build as this was the first time I generated a 
PCAP file. Had to understand the basis of DNS smuggling and the type of 
records I can use to hide data in plain sight. I'm sure it'll be a bit pain to 
figure out how to eliminate the noise, but once you understand how the packets
are layed out, it won't be hard at all!