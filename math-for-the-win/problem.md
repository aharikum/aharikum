# Reversing Python

- Namespace: picoctf/examples
- ID: reversing-C
- Type: custom
- Category: Reverse Engineering
- Points: 300
- Templatable: yes
- MaxUsers: 1

## Description

I don't like math..Can you solve it for me?

## Details
The binary can be downloaded {{url_for("chall", "here")}}.
To get the flag, connect to the program with netcat and give in your key:

`$ nc {{server}} {{port}}`

## Hints

- Do you know about S-box's and how do you reverse them.
- The flag is encrypted and the key is in 3 parts. Find them using 3 math problems
- Okay fine... I'll give you this file I got from my professor: {{url_for("sbox.txt", "sbox.txt")}}

## Solution Overview

The challenge involves viewing the binary in a disassembler. The key is divided into 3 parts. \\ To find key: User needs to solve three different math functions.
 a. First is an sbox  - should give the output - wooimaboutto
 b. quadratic equation with a - should give the output - makeanamefor
 c. some shifting math - should give the output - myselfhere63
 d. Once the key is derived, its connected with _


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

Examining source code to identify functionality

## Tags

- python

## Attributes

- author: LT 'syreal' Jones
- organization: picoCTF
- event: picoCTF Problem Developer Training
