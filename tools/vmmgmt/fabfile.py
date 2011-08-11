from fabric.api import run, sudo, hosts



@hosts('node01.cybercommons.org')
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

def virtinstall(vmname=None, ram="1024", vcpus="1", net="bridge0",os="redhat"):        
    if os == 'redhat':
        if locals()['vmname']:
            sudo('virt-install --accelerate --name %(vmname)s --ram %(ram)s --vnc --os-type=linux --os-variant=rhel6 --bridge=%(net)s --disk /dev/vol_guests/%(vmname)s --vcpus=%(vcpus)s --keymap="en-us" --location=http://129.15.41.46/rhel6_install/ --extra-args "ks=http://129.15.41.46/ks/ks64.cfg"' % locals())

def newvm(vmname=None, vcpus="1", ram="1024", guest_disk='10G', data_disk="100G" ):
    ''' Make a new vm '''
    mkguestlv(vmname)
    mkdatalv(vmname,data_disk)
    virtinstall(vmname)
    raise NotImplementedError

def clusterize():
    ''' Cluster the vm '''
    raise NotImplementedError


def lsvms(vmname=None):
    ''' Get list/status of clustered vms optionally returns status of specific vm '''
    if vmname:
        sudo('clustat -s vm:%(vmname)s' % locals())
    else:
        sudo('clustat')


def update_packages():
    sudo('yum update')

def bounce(service="httpd"):
    sudo('/etc/init.d/%(service)s restart' % locals() )


