# Math-For-The-Win Challenge

## Introduction
This is a reverse engineering challenge. The user is given a x86-64 
compiled binarywhich they can view using any disassembler. Obtain 
the key by solving 3 different functions that perform some mathematical 
operation. Once the key has been determined,the player can check if it 
is accurate. On a successful key input, the server will provide the player 
their flag.
The executable is compiled with no optimisation and has a PTRACE_TRACEME 
check to prevent running breakpoints. 

## Walkthrough

The challenge is primarily written in C and is designed to be analysed
using a disassembler. The code logic is esentially as follows:
- Dynamically generates a fixed key in three parts
   - get_key_part_1 : Solve to get the string "wooimaboutto" 
      - This function will have ou reverse an sbox. The sbox was generated using 
      a random seed.The ASCII number of each letter in the actual key string part
      has been used to index the sbox and the resulting element from sbox is part
      of the transformed input array for this function. Essentially getting the 
      sbox and a simple reverse based on the transformed input should let the 
      player get part 1 of the key
   - get_key_part_2 : Solve to get the string "makeanamefor"
      - This function takes in a target input array of float values. Each value 
      is the value of a quadratic equation where a = 1, b = -3 and c = 1. For 
      the equation y = ax^2 + bx +c, plug in the input values of a, b, c and y 
      as each value from float array, the player should be able to get the asciis
      of key part 2.
   - get_key_part3: Solve to get the string "myselfhere63"
      - This is a very simple function that shifts each value in the taret array
       with this logic : output[i] = (target_shifted_values[i] - i) % 26 + 'a'; 
       Solving this for each value in the array should get the player part3.
- Once the key parts are recovered, they are joined together with _ as a delimiter. 
This key is then hashed using SHA256. 
- The player can now enter their key and check if the hash matches. With a 
confirmation,the player can connect to the server to input the key and get
their flag.

# To play
All you need to do to run the challenge is to copy the "math-for-the-win"
directory into your local challenges/ dir inside cmgr. 
Run the following commands
- ```cmgr update```
- ```cmgr playtest picoctf/examples/math-for-the-win```

# Conclusion
This was a fun little challenge. I hated doing all the math to create the
challenge myself. Hoping people playing this will not curse me!