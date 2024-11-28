from pwn import *

def main():
    # Connect to server
    conn = remote("challenge", 5555)

    conn.revuntil(b"==>")
    # Send payload
    conn.sendline(b"wooimaboutto_makeanamefor_myselfhere63")

    # Receive all
    response = conn.recvall()

    # Convert response to ASCII
    response = response.decode()
    # responseß
    # Write flag to file
    with open("./flag", "w") as w:
        w.write(flag)

if __name__ == "__main__":
    main()