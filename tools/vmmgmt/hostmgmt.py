from fabric.api import *
from fabric.colors import *
from fabric.contrib.files import *

def lastlog():
    ll = run('lastlog | grep -v "Never logged in"')
    print(blue(ll))

def uptime():
    uptime = run("uptime", quiet=True)
    print(blue(uptime))

def ssh_config():
    passwords = sudo('grep "^PasswordAuthentication" /etc/ssh/sshd_config', quiet=True)
    if passwords == "PasswordAuthentication yes":
        print(red("Password authentication allowed"))
    else:
        print(green("Password authentication is not allowed"))

    rootlogin = sudo('grep "^PermitRootLogin" /etc/ssh/sshd_config', quiet=True)
    if rootlogin == "PermitRootLogin yes":
        print(red("Root login allowed"))
    else:
        print(green("Root logins not allowed over ssh"))

def saltify():
    if not exists('/etc/yum.repos.d/epel.repo'): 
        sudo('rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm')
    sudo('yum install salt-minion -y ')
    append('/etc/hosts', '129.15.41.46  salt', use_sudo=True)
    sudo('service salt-minion start')


def show_iptables():
    iptables = sudo('cat /etc/sysconfig/iptables', quiet=True)
    print(blue(iptables))

def ssh_keys():
    ''' Audit SSH Keys '''
    keys = run('sudo find /home/ -regex "^.*authorized_keys.*"', quiet=True)
    print(blue(keys))

def adduser(user,group=None):
    if group:
        sudo("useradd -G %s %s" %(group, user))
    else:
        sudo("useradd %s" % user)

def deluser(user):
    if len(run("grep %s /etc/passwd" % user)) > 0:
        test = prompt("Are you sure? (y/n)")
        if test == 'y':
            sudo("/usr/sbin/userdel -rf %s" % user)
    else:
        print("User does not exist on this host")

def passwd(user):
    sudo("passwd %s" % user)
