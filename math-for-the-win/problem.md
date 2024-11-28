# Math for the Win!

- Namespace: picoctf/18739f24
- ID: math-for-the-win
- Type: custom
- Category: Reverse Engineering
- Points: 300
- Templatable: yes
- MaxUsers: 100

## Description

I don't like math..Can you solve it for me?

## Details
The binary can be downloaded {{url_for("chall", "here")}}.
To get the flag, connect to the program with netcat and give in your key:

`$ nc {{server}} {{port}}`

## Hints

- Do you know about S-box's? If so, how do you reverse them?
- You might have to do 3 math problems to get the key
- Okay fine... I'll give you this file I got from my professor: {{url_for("sbox.txt", "sbox.txt")}}
- I heard from "sources" that the second function might be taking in an array of float values!

## Solution Overview

The challenge involves viewing the binary in a disassembler. The key is divided into 3 parts. \\ To find key: User needs to solve three different math functions.
 a. First is an sbox - Reverse the sbox to get the output - wooimaboutto
 b. quadratic equation with an array of target float values. Reversing this should give the output - makeanamefor
 c. some shifting math - should give the output - myselfhere63
 d. Once the key is derived, its connected with _ and you can send it on the server to get the flag



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

Examining C binaries and learning how to reverse them.

## Tags

- C
- Reverse

## Attributes

- author: AK
- organization: picoCTF
- event: picoCTF Problem Developer Training
