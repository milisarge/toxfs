# TOXFS

###File Sharing based Tox Agents with Web Mamagement

need to tox.h to wrapping 
 
flask for web management ( pip install flask )

run tox agent - create a tox profile named tox_save.tox

```
python main.py tox_save.tox
```

run tox agent management web server

```
python webserver.py
```

to connect 

```
https://localhost:2061
```

if you use tox agent also a tox agent should be run on your friend's local. ( tox agents must be friend )

after requirrements put your sharing files to "shared" directory ,you can list and fetch your friends shared files,it will download to "static" directory.
