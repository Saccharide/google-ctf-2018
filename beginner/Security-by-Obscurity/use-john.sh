#!/bin/sh

#1) Go to where the directory where the binary folder of john is installed
cd ~/src/john/run

#2) Run zip2john on the password protected zip file
./zip2john PATH_TO_ZIP > hash.txt

#) Run john on that hash
./john hash.txt

