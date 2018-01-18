# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  #config.vm.box_version = "= 201708.22.0"
  config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"

  # Work around disconnected virtual network cable.
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    # Start by making sure your system is up-to-date:
	yum -y update
	yum -y epel-release
	# Compilers and related tools:
	yum groupinstall -y "development tools"
	# Libraries needed during compilation to enable all features of Python:
	yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel

	# Install Postgresql Server
	yum -y install postgresql-server postgresql-contrib
	# Create PostgreSQL database cluster
	postgresql-setup initdb
	# Start & Enable the PostgreSQL service
	systemctl start postgresql
    systemctl enable postgresql


	# Install  the wget tool:
	yum install -y wget

	wget -r --no-parent -A 'epel-release-*.rpm' http://dl.fedoraproject.org/pub/epel/7/x86_64/e/

	# Python 3.6.3:
	wget http://python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
	tar xf Python-3.6.3.tar.xz
	cd Python-3.6.3
	./configure --enable-optimizations --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
	make
	make altinstall
	cd ..

    yum -y install make zip unzip postgresql

    # Install/upgrade pip, setuptools and wheel
    # First get the script:
	wget https://bootstrap.pypa.io/get-pip.py

	# Then execute it using Python 3.6:
	python3.6 get-pip.py

    pip3.6 install flask packaging oauth2client redis passlib flask-httpauth
    pip3.6 install sqlalchemy flask-sqlalchemy psycopg2 bleach requests

    su postgres -c 'createuser -dRS vagrant'
    su vagrant -c 'createdb'
    su vagrant -c 'createdb catalog'

    vagrantTip="[35m[1mThe shared directory is located at /vagrant\\nTo access your shared files: cd /vagrant[m"
    echo -e $vagrantTip > /etc/motd

    yum -y install redis jemalloc

    echo "Done installing your virtual machine!"
  SHELL
end
