
# Using linux's pdftotext to convet the PDF file to normal text file to see the content of the email. The black rectangle box is actually just a layer on top of the actual page, so we can still see the underneath password filed.
pdftotext challenge.pdf

# Using grep to find the flag
echo `grep -o "CTF{.*}" challenge.txt`
