# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from islem import *
from bot import *
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

toxbot = tox_factory(ProfileHelper.open_profile("tox_save.tox"))
sonek=str(toxbot.self_get_address())[0:2]
karsi_dosyalar="gelen_cevaplar"+sonek
komut_dosyasi="gelen_komutlar"+sonek

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
	</tr></table>
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
	dosyalar_html=""
	# localhost:2061
	#if request.method == 'GET':
	islem=Islem()
	if 'fno' in request.args and 'dosya' not in request.args:
		islem.fno = request.args.get('fno')
		islem.tip = "komut"
		islem.mesaj = "x"
		islem.komut = "@100@dlist"
		print "islem icerik:"
		islem.icerik()
		islem.dosyala(komut_dosyasi)
		cevap_geldi=False
		while not cevap_geldi:
			time.sleep(0.5)
			if os.path.exists(karsi_dosyalar):
				cevaplar=open(karsi_dosyalar,"r").read()
				cevaplar=cevaplar.split("\n")
				for dosya in cevaplar:
					dosyalar_html+="<tr><td><a href=/toxsys?fno="+str(islem.fno)+"&dosya="+dosya+">"+dosya+"</td><td></tr>"
				os.remove(karsi_dosyalar)
				cevap_geldi=True
				return '''<html>
				<h3>dosyalar</h3>
				<table border=1>
				'''+dosyalar_html+'''
				</tr>
				<a href="/toxfs">toxfs</a> 
				</html>'''
	if 'fno' in request.args and 'dosya' in request.args:
		islem.fno = request.args.get('fno')
		dosya = request.args.get('dosya')
		islem.tip = "komut"
		islem.mesaj = "x"
		islem.komut = "@102@"+dosya
		islem.dosyala(komut_dosyasi)
		cevap_geldi=False
		while not cevap_geldi:
			time.sleep(0.5)
			#md5sum kontrol
			if os.path.exists(karsi_dosyalar):
				cevap=open(karsi_dosyalar,"r").read()
				if cevap =="dosya_inme_tamam":
					cevap_geldi=True
					os.remove(karsi_dosyalar)
					return "dosya geldi statikte"
	else:
		return '''<html>
		paremetreyle gönderin</html>'''
	
if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=2061)

