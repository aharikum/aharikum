# Do Not Snitch!

- Namespace: picoctf/examples
- ID: do-not-snitch
- Type: custom
- Category: Forensics
- Points: 200
- Templatable: yes
- MaxUsers: 100

## Description
Hmm.. Someone’s been sneaking secrets through DNS. I need you help officer!

## Details
The packet information can be downloaded {{url_for("chall.pcap", "here")}}.
To get the flag, connect to the program with netcat and give in your key:

`$ nc {{server}} {{port}}`

## Hints

- Look for patterns in the DNS traffic. Some domains might stand out from the noise?
- The key is smuggled inside DNS packets, hidden across different types of records and is encoded.
- The fragments are ordered. Get them correctly and you can bypass our checks!

## Solution Overview

The challenge involves analysing the PCAP. The key is spread acrross multiple DNS requests as chunks of information as a part of multiple record types. There are also packets with random noise that should be filtered out. The type of records used are Subdomain, TXT, CNAME and PTR. Use scapy to script and decode the information and get the key (solve script is given in the solver directory)
The key comes out to be : whoop_whoop_thats_the_sound_of_da_police

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Examining PCAP and understanding different DNS requests. Learn about DNS smuggling

## Tags

- PacketAnalysis
- DNSsmuggling


## Attributes

- author: AK
- organization: picoCTF
- event: picoCTF Problem Developer Training
