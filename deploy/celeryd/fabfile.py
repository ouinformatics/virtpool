from fabric.api import *
from fabric.contrib.files import exists, append, comment
from fabric.colors import red
import os 


def static():
    env.os = 'redhat'
    env.settings = 'static'
    env.path = '/opt/celeryq'
    env.virtpy = '/opt/celeryq/virtpy'
    env.log = '/var/log/celeryd/celery.log'
    env.hosts = ['static.cybercommons.org']

def earth():
    env.os = 'redhat'
    env.settings = 'earth'
    env.path = '/opt/celeryq'
    env.virtpy = '/opt/celeryq/virtpy'
    env.log = '/var/log/celeryd/celery.log'
    env.hosts = ['earth.rccc.ou.edu']

def condor():
    env.os = 'ubuntu'
    env.settings = 'condor'
    env.path = '/opt/celeryq'
    env.virtpy = '/opt/celeryq/virtpy'
    env.log = '/var/log/celeryd/celery.log'
    env.hosts = ['condor_vm.cybercommons.org']
    
def gis():
    env.os = 'redhat'
    env.settings = 'gis'
    env.path = '/opt/celeryq'
    env.virtpy = '/opt/celeryq/virtpy'
    env.log = '/var/log/celeryd/celery.log'
    env.hosts = ['129.15.41.74']

def setup():
    sudo('/usr/sbin/useradd celeryd')
    sudo('mkdir /var/log/celeryd')
    sudo('chown -R celeryd /var/log/celeryd')
    sudo('mkdir /opt/celeryq')
    sudo('chown -R celeryd /opt/celeryq')
    sudo('virtualenv --no-site-packages /opt/celeryq/virtpy', user=celeryd
    sudo('/opt/celeryq/virtpy/bin/pip install celery pymongo sqlalchemy geojson', user=celeryd)

def bounce():
    if env.os == 'redhat':
        sudo('/etc/init.d/celeryd restart')
    elif env.os == 'ubuntu':
        sudo('restart celeryd')

def virtualenv(command):
    """ 
    Wrapper to activate and run virtual environment
    """
    with cd(env.virtpy):
        with prefix('source %(virtpy)s/bin/activate' % env):
            sudo(command)

def update():
    virtualenv('pip install --upgrade https://github.com/ouinformatics/cybercomq/zipball/master')
    bounce()


        

