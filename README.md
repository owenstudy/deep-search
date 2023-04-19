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

一个简单的Docker+Gunicorn+Flask示例
https://blog.csdn.net/cong_da_da/article/details/82746926?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-82746926-blog-117197014.235%5Ev29%5Epc_relevant_default_base3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-82746926-blog-117197014.235%5Ev29%5Epc_relevant_default_base3&utm_relevant_index=2

gunicorn -c config.py app:app 