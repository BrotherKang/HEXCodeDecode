#! python3
# -*- coding: utf-8 -*-

import os
import sys

# 開啟檔案破譯(HEX)檔案
file0 = open("IPs_out.txt", "r")

# 讀取 HEX 字串並開始解譯

for line0 in file0:
    strHEX = str(bytearray.fromhex(line0.strip()[38:int(len(line0.strip()))-1]).decode())
    #print (strHEX)

    pwdFile = open("password.txt","a")
    pwdFile.write(line0.strip() + strHEX + "\n")
    pwdFile.close()

file0.close()
