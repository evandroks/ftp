#!/usr/bin/pthon

import ftplib
import sys

print "Username:- thunderpy --- Password:- mitr@2017"

data = []

USERNAME = raw_input("Enter username: ")
PASSWORD = raw_input("Enter password: ")

ftp = ftplib.FTP("182.73.79.108")
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

