from bootstrap import node_generator
from bot import *
from callbacks import init_callbacks
import time
import sys
import thread
import socket
import os


def elcibey( threadName, delay):
	print 'elci'
	TCP_IP = '127.0.0.1'
	TCP_PORT = 5005
	BUFFER_SIZE = 20  # Normally 1024, but we want fast response
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT))
	s.listen(1)
	time.sleep(delay)
	print 'Connection address:', addr
	conn.close()
	threadName.exit()
		  

class FileBot(object):

    def __init__(self, path):
        super(FileBot, self).__init__()
        self.tox = None
        self.stop = False
        self.profile = None
        self.path = path
        print 'FileBot v0.1.1'

	
	
    def main(self):
        self.tox = tox_factory(ProfileHelper.open_profile(self.path))
        print self.tox.self_get_address()
        init_callbacks(self.tox)
        # bootstrap
        for data in node_generator():
            self.tox.bootstrap(*data)
        settings = Settings()
        self.profile = Bot(self.tox)
        print 'Iterate'
        try:
            while not self.stop:
                self.tox.iterate()
                time.sleep(self.tox.iteration_interval() / 1000.0)
                if self.tox.friend_get_connection_status(0) and os.path.exists("0.txt"):
                    print "mesaj icrae"
                    oku=open("0.txt","r").read()
                    self.tox.friend_send_message(0, 0,oku)
                    os.remove("0.txt")  
                
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

