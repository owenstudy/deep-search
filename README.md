# deep-search

gunicorn -b localhost:8080 -w 3 app:app

package install:
-gevent,gunicorn

gunicorn -c config.py app:app 