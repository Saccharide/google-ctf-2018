

cp foo.ico foo.zip
unzip -q foo.zip

echo `grep -o "CTF{.*}" driver.txt`

