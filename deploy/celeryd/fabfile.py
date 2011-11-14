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


        

