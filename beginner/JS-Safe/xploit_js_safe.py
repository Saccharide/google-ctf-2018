secret = [230,104,96,84,111,24,205,187,205,134,179,94,24,181,37,191,252,103,247,114,198,80,206,223,227,255,122,0,38,250,29,238]
secret_hash = ""

for item in secret:
	# Makes sure that the hex is 4 digit long, because I encounter that there is a 0x0 case, which messed up the final decrypt lookup. 
	# We will need to convert 0x0 to 0x00 to make the whole string 64 character long. (padding the hex to 2 digit)
	padded_string = '0x%02x' % item
	secret_hash  += padded_string[2:]

print secret_hash
# Secret hash = e66860546f18cdbbcd86b35e18b525bffc67f772c650cedfe3ff7a0026fa1dee
# After a reverse look up in google, we found it is Passw0rd!

# The flag is: CTF{Passw0rd!}