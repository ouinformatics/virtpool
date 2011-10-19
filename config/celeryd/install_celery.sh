# Installing celery worker
sudo /usr/bin/easy_install-2.6 pip
sudo /usr/bin/pip install -U Celery pymongo psycopg
wget http://github.com/ouinformatics/  -O /etc/init.d/celeryd
sudo chmod +x /etc/init.d/celeryd
sudo /sbin/chkconfig --add /etc/init.d/celeryd
sudo mkdir /opt/celeryq
# Download queue's worker code
