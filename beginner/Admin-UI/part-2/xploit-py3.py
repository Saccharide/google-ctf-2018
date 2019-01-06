# Python 3 version of the exploit, it's cool to see how python 2 and python 3 differs.
flag = "84 93 81 BC 93 B0 A8 98  97 A6 B4 94 B0 A8 B5 83 BD 98 85 A2 B3 B3 A2 B5  98 B3 AF F3 A9 98 F6 98 AC F8 BA 2F 62 69 6E 2F  73 68 00 3E 20 00 71 75"

flag = bytes.fromhex(flag.replace(" ", ""))

output = ""
for ch in flag:
    output += chr(ch ^ 0xC7)

print(output)
# CTF{Two_PasSworDz_Better_th4n_1_k?}
