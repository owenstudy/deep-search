# deep-search

gunicorn -b localhost:8080 -w 3 app:app

package install:
-gevent,gunicorn

quit gunicorn:
macos:
ps -ef|grep gunicorn

linux:
$ pstree -ap | grep gunicorn  
--restart gunicorn:
kill -HUP xxx

stop:
$ kill -9 31979


gunicorn -c config.py app:app 