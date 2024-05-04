#!/usr/bin/env bash
# Install nginx on your web-01

sudo apt-get -y update
sudo apt-get -y install nginx
sudo sh -c 'echo "Hello World!" > /var/www/html/index.nginx-debian.html'

# Create these folders if not exists
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file and append a simple content to it
sudo touch /data/web_static/releases/test/index.html
sudo echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | tee /data/web_static/releases/test/index.html

# Create a symbolic link, If already exists, delete and recreate it again.
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set the ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx Configuration file
hbnb_static="        location /hbnb_static {
                alias /data/web_static/current/;
}"
sudo sed -i '54r /dev/stdin'  /etc/nginx/sites-enabled/default <<< "$hbnb_static"

sudo service nginx restart
