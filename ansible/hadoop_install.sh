# Preparing a RHIPE Hadoop Client Node

# Set up cloudera and install Hadoop Client
wget http://archive.cloudera.com/cdh4/one-click-install/redhat/6/x86_64/cloudera-cdh-4-0.x86_64.rpm
sudo rpm -i cloudera-cdh-4-0.x86_64.rpm
sudo yum install -y hadoop-client

# install epel
# Set up EPEL to get protobuf
sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

# Install R
sudo yum install -y R-core R-devel.x86_64

#sudo yum install -y protobuf-devel.x86_64 protobuf-c-devel.x86_64
wget http://protobuf.googlecode.com/files/protobuf-2.4.1.tar.gz
tar -xzf protobuf-2.4.1.tar.gz
cd protobuf-2.4.1
./configure --prefix=/opt/protobuf/
make
sudo make install
cd ..
sudo su -c "echo "/opt/protobuf/lib/" > protobuf.conf"

# Get Java
scp 129.15.40.57:/Users/jduckles/Downloads/jdk-6u35-linux-x64-rpm.bin .
chmod +x jdk-6u35-linux-x64-rpm.bin 
./jdk-6u35-linux-x64-rpm.bin 

# Rstudio (optional)
#wget http://download2.rstudio.org/rstudio-server-0.97.245-x86_64.rpm
#sudo yum install -y --nogpgcheck rstudio-server-0.97.245-x86_64.rpm

# Rhipe
wget https://github.com/downloads/saptarshiguha/RHIPE/Rhipe_0.69.tar.gz
sudo su
export PKG_CONFIG_PATH=/opt/protobuf/lib/pkgconfig/
export LD_LIBRARY_PATH=/opt/protobuf/lib/
export HADOOP=/usr/lib/hadoop/
export HADOOP_BIN=/usr/lib/hadoop/bin
#export HADOOP_CONF_DIR=/home/jduckles/hadoop-conf
export JAVA_HOME=/usr/lib/jvm/jre-1.6.0-openjdk.x86_64
#export JAVA_HOME=/usr/java/jdk1.6.0_32

R CMD INSTALL Rhipe_0.69.tar.gz


## Configuring 
node=4
umount /home
mkdir /home
scp -r root@phadoop1:/home/* /home
lvremove /dev/vg_phadoop${node}/lv_home
lvcreate -n lv_hdfs1 -L 1.75TB vg_phadoop${node}
mke2fs /dev/vg_phadoop${node}/lv_hdfs1

pvcreate /dev/sdb
pvcreate /dev/sdc
pvcreate /dev/sdd
vgcreate vg_hdfs2 /dev/sdb
vgcreate vg_hdfs3 /dev/sdc
vgcreate vg_hdfs4 /dev/sdd
lvcreate -n hdfs2 -l 100%VG vg_hdfs2
lvcreate -n hdfs3 -l 100%VG vg_hdfs3
lvcreate -n hdfs4 -l 100%VG vg_hdfs4
for i in {2..4}; do mke2fs /dev/vg_hdfs${i}/hdfs${i}; done
chown -R hdfs:hdfs /hdfs
