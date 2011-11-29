# Installing celery worker
# Should convert this script to a fabric script
sudo apt-get install python-virtualenv python-psycopg2 python-pymongo
sudo wget --no-check-certificate http://github.com/ouinformatics/virtpool/raw/master/config/celeryd/celeryd  -O /etc/init.d/celeryd
sudo chmod +x /etc/init.d/celeryd
sudo /sbin/chkconfig --add /etc/init.d/celeryd
sudo mkdir /opt/celeryq
cd /opt/celeryq
sudo ./virtpy/bin/pip install Celery simplejson sqlalchemy

# Download queue's worker code
