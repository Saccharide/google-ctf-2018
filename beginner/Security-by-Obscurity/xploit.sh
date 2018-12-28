#!/bin/sh

unzip -o -qq original.ZIP

while [ ! -f "/password" ]
do
    file=$(ls -t | grep -iv "ZIP$" | grep -v "sh$" | grep -v "txt$")
    echo "-----> [FILE MATACHED] = $file"
    newfile="$file.zip"
    echo "-----> [FILE UNZIPING] = $newfile"
    mv $file $newfile
    7z e $newfile || exit 1 
    rm $newfile
    echo "-----> [NEW FILE DIRECTORY] = "
    ls
done


