# -*- coding: utf-8 -*-

import requests, base64, os, ctypes

code = None

print("Ürün anahtarı kontrol ediliyor...")

while True:
	try:
		url = "https://drive.google.com/u/0/uc?id=1iyizwZIisahbDf4BVV5nGU13DjurEz5M&export=download"
	
		r = requests.get(url=url)
	
		if r.status_code == 200 and r.text[0:95] == "I1NNUyBUb29sIGJ5IFdpcGVyCiNnaXRodWI6IGh0dHBzOi8vZ2l0aHViLmNvbS93aXBlcmRldgojZGM6IFdpcGVyIzA1NjU":
			code = r.text
			break
		else:
			ctypes.windll.user32.MessageBoxW(0, "Ürün anahtarınız geçersiz!", "SMS Tool", 0)
			try:
				os.remove("main.py")
			except:
				pass
			os.system("client.py")
	except:
		ctypes.windll.user32.MessageBoxW(0, "Bilinmeyen bir problem oluştu.", "SMS Tool", 0)
		try:
			os.remove("main.py")
		except:
			pass
		os.system("client.py")

exec(base64.b64decode(code))