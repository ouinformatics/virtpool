$apache_home = '/scratch/www/html'

package { 'mapserver6':
	ensure => present,
}

package { 'mod-fcgid':
         ensure => present,
}


file { "${apache_home}/cgi-bin/mapserv":
        source => '/usr/libexec/mapserv',
        ensure => file,
        mode => 755,
}

file { '/scratch/www/html/cgi-bin/mapserv.fcgi':
        source => '/usr/libexec/mapserv',
        ensure => file,
        mode => 755,
}



