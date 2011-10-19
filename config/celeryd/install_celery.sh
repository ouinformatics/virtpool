# Installing celery worker
# Should convert this script to a fabric script
sudo /usr/bin/easy_install-2.6 pip
sudo /usr/bin/pip install -U Celery pymongo psycopg
sudo wget --no-check-certificate http://github.com/ouinformatics/virtpool/raw/master/config/celeryd/celeryd  -O /etc/init.d/celeryd
sudo chmod +x /etc/init.d/celeryd
sudo /sbin/chkconfig --add /etc/init.d/celeryd
sudo mkdir /opt/celeryq
# Download queue's worker code
