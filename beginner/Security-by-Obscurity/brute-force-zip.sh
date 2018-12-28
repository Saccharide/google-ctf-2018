#!/bin/bash

# Using fcrackzip to brute force a password protected zip file

file=$(ls -t | grep -v "ZIP$" | grep -v "sh$" | grep -v "txt$")

# -b [brute force] -c [character set] a for small alphabet and 1 for numeric value, -l [min leng - max leng] -u use unzip and path of password protected file
password="$(fcrackzip -b -c "a1" -l 1-6 -u $file |  mawk '{print $5}')"
unzip -P $password $file
