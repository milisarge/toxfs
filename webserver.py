# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from islem import *
from bot import *
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

toxbot = tox_factory(ProfileHelper.open_profile("tox_save.tox"))
sonek=str(toxbot.self_get_address())[0:2]

@app.route('/')
def indeks(): 
    
    arkadaslar=""
    for num in toxbot.self_get_friend_list():
		print toxbot.friend_get_status_message(num)
		arkadaslar+="<tr><td><a href=/toxsys?fno="+str(num)+">"+str(num)+"</td><td>"+toxbot.friend_get_name(num)+"</td><td>"+str(toxbot.friend_get_status_message(num))+"</td><td>"+str(toxbot.friend_get_public_key(num))+"</td></tr>"
    
    return '''<html>
	<h2>Tox Yönetim Sayfası</h2>
	<table border=1>
	<tr><td>no</td><td>isim</td><td>publickey</td></tr>
	<tr><td>-1</td><td>'''+toxbot.self_get_name()+'''</td><td>'''+toxbot.self_get_status_message()+'''</td><td>'''+toxbot.self_get_address()+'''</td></tr>
	'''+arkadaslar+'''
	</tr>
	<a href="/toxfs">toxfs</a> 
	</html>'''

@app.route('/toxfs', methods = ['GET','POST'])
def toxfs():
	
	# localhost:2061
	#if request.method == 'GET':
	islem=Islem()
	islem.fno = request.args.get('fno')
	islem.tip = request.args.get('tip')
	islem.mesaj = request.args.get('mesaj')
	print "islem icerik:"
	islem.icerik()
	islem.dosyala("gelen_komutlar"+sonek)
	return "komut icra edildi."
	#else:
		#return '''<html>
		#paremetreyle gönderin</html>'''
	
@app.route('/toxsys', methods = ['GET','POST'])
def toxsys():
	print "sonek",sonek
	# localhost:2061
	#if request.method == 'GET':
	islem=Islem()
	islem.fno = request.args.get('fno')
	islem.tip = "komut"
	islem.mesaj = ""
	islem.komut = "dosyalar"
	print "islem icerik:"
	islem.icerik()
	islem.dosyala("gelen_komutlar"+sonek)
	return "komut icra edildi."
	#else:
		#return '''<html>
		#paremetreyle gönderin</html>'''
	
if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=2061)

