When I first downloaded and unzipped this attachment, I found out that this is a Linux rev 1.0 ext4 filesystem data (using `file` on the extracted file).
Then I created an empty directory to serve as my mount directory, by using `sudo mount challenge2.ext4 mount_dir`. After doing `ll -ha` to list everything in this filesystem, I found an intresting gz file called ".mediapc_backdoor_password.gz". Intuitively, I extracted the zip file and found the flag using `sudo 7z e .mediapc_backdoor_password.gz`
CTF{I_kn0W_tH15_Fs}
