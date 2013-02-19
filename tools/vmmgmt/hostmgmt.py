from fabric.api import *
from fabric.colors import *
def lastlog():
    run("lastlog")

def uptime():
    run("uptime")

def ssh_config():
    sudo('grep "^PasswordAuthentication" /etc/ssh/sshd_config', quiet=True)
    rootlogin = sudo('grep "^PermitRootLogin" /etc/ssh/sshd_config', quiet=True)
    if rootlogin == "PermitRootLogin yes":
        print(red("Root login allowed"))
    else:
        print(green("Root logins not allowed over ssh"))

def show_iptables():
    sudo('cat /etc/sysconfig/iptables')

def ssh_keys():
    ''' Audit SSH Keys '''
    run('sudo find /home/ -regex "^.*authorized_keys.*"', quiet=True)

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
