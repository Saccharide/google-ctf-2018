# After looking thtough IDA, I see that the program is checking for 0n3_W4rM as the username and zLl1ks_d4m_T0g_I as the password. However, the password was checked from the reverse, so we have to input the password backwards. To flip the password, we can simply do:
password = "zLl1ks_d4m_T0g_I"[::-1]
print(password)

# Then we were able to get the flag CTF{I_g0T_m4d_sk1lLz}
