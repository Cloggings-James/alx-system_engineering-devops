exec { 'http header':
  command  => "sudo apt-get update -y; \
               sudo apt-get install nginx -y; \
               sudo sed -i '/server_name _/a add_header X-Served-By $hostname;' /etc/nginx/sites-available/default; \
               sudo service nginx restart",
  provider => shell,
  path     => ['/usr/bin', '/bin'],  # Specify the PATH environment variable
  user     => 'root',                # Specify the user running the commands
  group    => 'root',                # Specify the group for the commands
}

