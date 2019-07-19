#!/usr/bin/pthon

import ftplib
import sys

print "Username:- <USERNAME> --- Password:- <PASSWORD>"

data = []

USERNAME = raw_input("Enter username: ")
PASSWORD = raw_input("Enter password: ")

ftp = ftplib.FTP("<SERVER_NAME>")
ftp.login(USERNAME, PASSWORD)

ftp.dir(data.append)
for line in data:
    print "==>", line

# change dir
ftp.cwd(raw_input("Enter folder name: "))
ftp.dir(data.append)
for line in data:
    print "==>", line


ftp.quit()

