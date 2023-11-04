# configuring server using puppet

file_line { 'disable password authentication':
	path	=> '/etc/ssh/ssh_config',
	line	=> 'PasswordAuthentication no',
	replace	=> true
}

file_line { 'Change Identity File':
	path	=> '/etc/ssh/ssh_config',
	line	=> 'IdentityFille ~/.ssh/school',
	replace	=> true
}