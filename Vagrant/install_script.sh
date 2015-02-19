#!/bin/bash

# install web server dependencies
sudo apt-get update
sudo apt-get -y install python python-dev python-virtualenv nginx python3-dev build-essential python3-tk tk-dev libpng12-dev  supervisor

# install application (source location in $1)
mkdir /home/vagrant/PDomoCla
cp -R $1/PDomoCla/* /home/vagrant/PDomoCla/

# create a virtualenv and install dependencies
virtualenv /home/vagrant/PDomoCla/venv
/home/vagrant/PDomoCla/venv/bin/pip install flask
/home/vagrant/PDomoCla/venv/bin/pip install flask-bootstrap
/home/vagrant/PDomoCla/venv/bin/pip install flask-wtf
/home/vagrant/PDomoCla/venv/bin/pip install flask-sqlalchemy
/home/vagrant/PDomoCla/venv/bin/pip install flask-login
/home/vagrant/PDomoCla/venv/bin/pip install pysftp
/home/vagrant/PDomoCla/venv/bin/easy_install -U distribute

/home/vagrant/PDomoCla/venv/bin/pip install matplotlib
/home/vagrant/PDomoCla/venv/bin/pip install gunicorn








# configure supervisor
sudo cp /vagrant/pdomocla.conf /etc/supervisor/conf.d/
sudo mkdir /var/log/PDomoCla
sudo supervisorctl reread
sudo supervisorctl update

# configure nginx
# sudo mkdir /etc/nginx/sites-available/
sudo cp /vagrant/pdomocla.nginx /etc/nginx/sites-available/PDomoCla
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/PDomoCla /etc/nginx/sites-enabled/
sudo service nginx restart

echo Application deployed to http://192.168.1.99/
