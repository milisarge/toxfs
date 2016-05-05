# -*- coding: utf-8 -*-
from bootstrap import node_generator
from bot import *
from callbacks import init_callbacks
import time
import sys
import thread
import socket
import os


class FileBot(object):

	def __init__(self, path):
		super(FileBot, self).__init__()
		self.tox = None
		self.stop = False
		self.profile = None
		self.path = path
		print 'milis_toxfs sitemi'


	
	
	def main(self):
		self.tox = tox_factory(ProfileHelper.open_profile(self.path))
		print self.tox.self_get_address()
		init_callbacks(self.tox)
		sonek=str(self.tox.self_get_address())[0:2]
		com_file="gelen_komutlar"+sonek
		# bootstrap
		for data in node_generator():
			self.tox.bootstrap(*data)
		settings = Settings()
		self.profile = Bot(self.tox)
		self.tox.self_set_name("Toxfs_Agent-0.1"+sonek)
		self.tox.self_set_status_message("Tox File Sharing Agent")
		for num in self.tox.self_get_friend_list():
			print num,self.tox.friend_get_name(self.tox.self_get_friend_list()[num])
		print 'Iterate'
		try:
			while not self.stop:
				self.tox.iterate()
				time.sleep(self.tox.iteration_interval() / 1000.0)
				if os.path.exists(com_file) and '##' in open(com_file,"r").read():
					print com_file,"isleniyor..."
					data=open(com_file,"r").read()
					datalar=data.split('##')
					arkadasno=datalar[0]
					islemtip=datalar[1]
					param=datalar[2]
					param2=datalar[3]
					print "gelen ",islemtip,":",arkadasno,islemtip,param,param2
					if self.tox.friend_get_connection_status(int(arkadasno)):
						if islemtip=="mesaj":
							self.tox.friend_send_message(int(arkadasno),0,param)
							print arkadasno,self.tox.friend_get_name(int(arkadasno)),"arkadasa metin mesaji gonderildi."
						if islemtip=="komut":
							self.tox.friend_send_message(int(arkadasno),0,param2)
							print arkadasno,self.tox.friend_get_name(int(arkadasno)),"arkadasa komut mesaji gonderildi."
					print com_file,"siliniyor."
					os.remove(com_file)
					print com_file,"tamamlandi."
                
		except KeyboardInterrupt:
			settings.save()
			data = self.tox.get_savedata()
			ProfileHelper.save_profile(data)
			del self.tox
		print "test"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
        bot = FileBot(path)
        bot.main()
    else:
        raise IOError('Path to save file not found')

