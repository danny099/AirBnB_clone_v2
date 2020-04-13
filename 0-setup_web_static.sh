#!/usr/bin/env bash
# task 0
# install ngix
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
# directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
# web page
echo "Test!" | sudo tee /data/web_static/releases/test/index.html
# link files
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# give privs
sudo chown -hR ubuntu:ubuntu /data/
# default
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://www.linkedin.com/in/danny-alejandro-martinez-rivera-72b470192/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

sudo service nginx start
