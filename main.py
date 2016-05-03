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
		com_file="gelen_komutlar"
		self.tox = tox_factory(ProfileHelper.open_profile(self.path))
		print self.tox.self_get_address()
		init_callbacks(self.tox)
		# bootstrap
		for data in node_generator():
			self.tox.bootstrap(*data)
		settings = Settings()
		self.profile = Bot(self.tox)
		self.tox.self_set_name("Toxfs_Agent-0.1")
		self.tox.self_set_status_message("Tox File Sharing Agent")
		print 'Iterate'
		try:
			while not self.stop:
				self.tox.iterate()
				time.sleep(self.tox.iteration_interval() / 1000.0)
				if os.path.exists(com_file):
					print "mesaj isleniyor"
					data=open(com_file,"r").read()
					datalar=data.split('@')
					arkadasno=datalar[0]
					komut=datalar[1]
					param=datalar[2]
					print arkadasno,komut,param
					if self.tox.friend_get_connection_status(0):
						if komut=="mesaj":
							self.tox.friend_send_message(int(arkadasno),0,param)
						if komut=="dosya":
							#send file olacak
							
							self.profile.send_file("README.md",int(arkadasno) )
					os.remove(com_file)
					print "mesaj islendi"  
                
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

