exec { 'install_puppet_lint':
  command => '/usr/bin/gem install puppet-lint -v 2.5.0',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/gem list puppet-lint | grep 2.5.0',
}

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
  require  => Exec['install_puppet_lint'],
}

