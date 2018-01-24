# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.box_version = "1801.01"

  config.vm.network "private_network", type: "dhcp"

  config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"
  #config.vm.network "forwarded_port", guest: 8000, host: 8000
  #config.vm.network "forwarded_port", guest: 8080, host: 8080
  #config.vm.network "forwarded_port", guest: 5000, host: 5000

  # Synchronise the vagrant folder with NFS
  config.vm.synced_folder ".", "/vagrant", type: "nfs", nfs_udp: false

  # Work around disconnected virtual network cable.
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
  end

  # Copy over server configuration files
  config.vm.provision "file", source: "./server-config/install_tex.sh", destination: "~/install_tex.sh"
  config.vm.provision "file", source: "./server-config/latex.sh", destination: "~/latex.sh"
  config.vm.provision "file", source: "./server-config/prompt.sh", destination: "~/prompt.sh"
  config.vm.provision "file", source: "./server-config/flask.sh", destination: "~/flask.sh"

  config.vm.provision "shell", inline: <<-SHELL
  # Start by making sure your system is up-to-date:
	yum -y update
	yum -y install epel-release
  yum -y install https://centos7.iuscommunity.org/ius-release.rpm

  # Set Global Environmental variables
  mv -v /home/vagrant/latex.sh /etc/profile.d/latex.sh
  mv -v /home/vagrant/prompt.sh /etc/profile.d/prompt.sh
  mv -v /home/vagrant/flask.sh /etc/profile.d/flask.sh

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

	# Python 3.6:
	yum -y install python36u python36u-pip python36u-devel

  su postgres -c 'createuser -dRS vagrant'
  su vagrant -c 'createdb'
  su vagrant -c 'createdb catalog'

  # Install Redis server
  yum -y install redis jemalloc

  # Install texlive for sphinx - pdflatex
  yum install perl-Digest-MD5
  cd /home/vagrant
  . /home/vagrant/install_tex.sh

  # Remove Virtual Enviroment if it exists
  if [ -d /vagrant/env ]; then
    echo "Removing Virtual Environment"
    rm -rf /vagrant/env
  fi

  # Install new Virtual Environment
  python3.6 -m venv env

  vagrantTip="[35m[1mThe shared directory is located at /vagrant\\nTo access your shared files: cd /vagrant[m"
  echo -e $vagrantTip > /etc/motd


  echo "Done installing your virtual machine!"
  SHELL
end
