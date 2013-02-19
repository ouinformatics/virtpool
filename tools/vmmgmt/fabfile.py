from fabric.api import * 
env.use_ssh_config = True
env.warn_only = True
from vmmgmt import *
from hostmgmt import *

def set_hosts(hostfile):
    env.hosts = open(hostfile, 'r').readlines()
