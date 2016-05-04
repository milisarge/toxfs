# -*- coding: utf-8 -*-
from pprint import pprint

class Islem:
	def __init__(self):
		
		self.fno=""
		self.tip=""
		self.mesaj=""
		self.komut=""
		
	def icerik(self):
		pprint (vars(self))
	def paketle(self):
		paket=""
		paket+=self.fno
		paket+="@"
		paket+=self.tip
		paket+="@"
		paket+=self.mesaj
		paket+="@"
		paket+=self.komut
		return paket
	def dosyala(self,dosya):
		sonuc=open(dosya,"w").write(self.paketle())
		return sonuc
