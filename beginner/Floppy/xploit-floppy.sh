
# After using binwalk, a tool that tries to see if the file passed in is actually another type of file, I found out that foo.ico is actually a zip file, so let's extract it. And we see that the flag is in driver.txt.
cp foo.ico foo.zip
unzip -q foo.zip

echo `grep -o "CTF{.*}" driver.txt`

