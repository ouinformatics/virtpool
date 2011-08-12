$apache_home = '/scratch/www/html'
$data_home = '/scratch/data/'

package { 'httpd':
            ensure => present,
}

package { 'mapserver6':
	ensure => present,
}

package { 'mod_fcgid':
         ensure => present,
}

# Set up cgi-bin with normal CGI
file { "${apache_home}/cgi-bin/mapserv":
        source => '/usr/libexec/mapserv',
        ensure => file,
        mode => 755,
}

# Setup fastCGI as well
file { '/scratch/www/html/cgi-bin/mapserv.fcgi':
        source => '/usr/libexec/mapserv',
        ensure => file,
        mode => 755,
}


# Get mapfiles in place




