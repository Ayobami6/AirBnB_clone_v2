#!/usr/bin/env bash
# configure web server for error 404 and add custom header

# if nginx exist don't install
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

sudo sh -c "echo 'Hello World!' > /data/web_static/releases/test/index.html"
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/

sudo touch /var/www/html/404.html
sudo sh -c "echo \"Ceci n'est pas une page\" > /var/www/html/404.html"
SERVER_CONFIG="server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;
	add_header X-Served-By $HOSTNAME;

	location / {
		try_files \$uri \$uri/ =404;
	}
	if (\$request_filename ~ redirect_me){
			rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	}
	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}
	error_page 404 /404.html;
	location = /404.html{
		internal;
	}
}"
sudo sh -c "echo '$SERVER_CONFIG' > /etc/nginx/sites-enabled/default"
sudo service nginx restart
