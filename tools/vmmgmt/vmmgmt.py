from fabric.api import *
def node01():
    env.hosts=['root@node01.cybercommons.org']
def node02():
    env.hosts=['root@node02.cybercommons.org']
def node03():
    env.hosts=['root@node03.cybercommons.org']
def node04():
    env.hosts=['root@node04.cybercommons.org']

def mklv(vmname=None, size=None, pool=None):
    ''' Make an LV '''
    if vmname:
        sudo( 'lvcreate -n %(vmname)s -L %(size)s %(pool)s' % locals() )
    else:
        print("Couldn't create logical volume, no vmname given")

def mkguestlv(vmname=None, size="10G", pool="vol_guests"):
    ''' Make an LV with defaults appropriate for guests '''
    mklv(**locals())

def mkdatalv(vmname=None, size='100G', pool="vol_data"):
    ''' Make an LV with defaults appropriate for data drives '''
    mklv(**locals())

def rmlv(vmname=None, pool='vol_guests'):
    if vmname:
        sudo('lvremove /dev/%(pool)s/%(vmname)s' % locals())
    else:
        print("Without vmname, can't remove lv")

def virtinstall(vmname=None, ram="1024", vcpus="1", net0="bridge0", net1="bridge1", os="centos", kickstart="ks=http://129.15.41.46/ks/ks64.cfg"): 
    if os == 'centos':
        if locals()['vmname']:
            sudo('virt-install --accelerate --name %(vmname)s --vnc --ram %(ram)s --os-type=linux --os-variant=rhel6 --bridge=%(net0)s --bridge=%(net1)s --disk /dev/vol_guests/%(vmname)s --vcpus=%(vcpus)s --keymap="en-us" --location=http://129.15.41.46/centos6_install/ --extra-args "ks=http://129.15.41.46/ks/ks64.cfg"' % locals())
    if os == 'ubuntu':
        if locals()['vmname']:
            sudo('virt-install --accelerate --name %(vmname)s --ram %(ram)s --vnc --os-type=linux --os-variant=ubuntumaverick --location=http://static.cybercommons.org/jduckles/mini.iso --keymap="en-us" --vcpus=%(vcpus)s --bridge=%(net)s --disk /dev/vol_guests/%(vmname)s' % locals() )

def newvm(vmname=None, vcpus="1", ram="1024", guest_disk='10G', data_disk=None, os="centos" ):
    ''' Make a new vm '''
    mkguestlv(vmname, size=guest_disk)
    if data_disk:
        mkdatalv(vmname, size=data_disk)
    virtinstall(vmname, ram=ram, vcpus=vcpus, os=os)
    raise NotImplementedError

def clusterize(vmname):
    ''' Cluster the vm '''
    sudo( 'ccs -f /etc/cluster/cluster.conf --sync --activate --addvm %s migrate="live" path="/etc/libvirt/qemu" recovery="relocate"' % (vmname) )

def declusterize(vmname):
    ''' Declusterize vm '''
    sudo( "ccs -f /etc/cluster/cluster.conf --rmvm %s --sync --activate" % (vmname) )

def lsvms(vmname=None):
    ''' Get list/status of clustered vms optionally returns status of specific vm '''
    if vmname:
        sudo('clustat -s vm:%(vmname)s' % locals())
    else:
        sudo('clustat')

def vmconfig(vmname=None):
    ''' View config of specific vm '''
    if vmname:
        sudo('cat /etc/libvirt/qemu/%(vmname)s.xml' % locals())

def update_packages():
    sudo('yum update')

def bounce(service="httpd"):
    sudo('/etc/init.d/%(service)s restart' % locals() )

@hosts('node01.cybercommons.org')
def lsvm():
    """ List all clusterized VMs """
    sudo('clustat')

@hosts('node01.cybercommons.org')
def bouncevm(service):
    """ Restart a clusterized VM """
    sudo('clusvcadm -s %s;clusvcadm -e %s' % (service, service))

@hosts('node01.cybercommons.org')
def stopvm(service):
    sudo('clusvcadm -s %s' % service)

def installmongos():
    """ Install mongos on a redhat/centos guest """
    sudo('yum install mongodb-server')
    sudo('wget "https://raw.github.com/ouinformatics/virtpool/master/mongo/mongos" -O /etc/init.d/mongos')
    sudo('chmod +x /etc/init.d/mongos')
    sudo('/usr/sbin/adduser mongod')
    sudo('chown mongod /var/log/mongodb')
    sudo('chkconfig mongos on')
    sudo('service mongos start')
