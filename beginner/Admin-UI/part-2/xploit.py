# After going through the main program's binary, I was able to find the secondary login and the program is comparing a password from a flag file.
flag = "84 93 81 BC 93 B0 A8 98  97 A6 B4 94 B0 A8 B5 83 BD 98 85 A2 B3 B3 A2 B5  98 B3 AF F3 A9 98 F6 98 AC F8 BA 2F 62 69 6E 2F  73 68 00 3E 20 00 71 75"

# Remove empty space
flag = bytearray(flag.replace(" ", "").decode('hex'))

# 
output = ""
for ch in flag:
    output += chr(ch ^ 0xC7)

print(output)
# CTF{Two_PasSworDz_Better_th4n_1_k?}
