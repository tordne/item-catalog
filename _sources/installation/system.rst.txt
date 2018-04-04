System Installation
===================

Host System
-----------
The host system used for this project was CentOS 7 with the following versions of software used.

* CentOS 7 with kernel 4.13.5
* Vagrant 2.0.1
* VirtualBox Version 5.2.6 r120293 (Qt5.6.1)
* NFS 1.3.0
* Firewalld 0.4.4.4

How to Install
--------------
Download the project
^^^^^^^^^^^^^^^^^^^^
Open a terminal and download teh full project:

.. code-block:: bash

  git clone https://github.com/tordne/item-catalog.git

NFS
^^^
Vagrant and CentOS have issues with rsync-auto, and the shared folder doesn't automatically update. For this reason and also increased performace, this Vagrantfile is configured to use NFS.

We just need to make sure that our firewall allows all the NFS ports.

.. code-block:: bash

  firewall-cmd --permanent --add-service=nfs
  firewall-cmd --permanent --add-service=mountd
  firewall-cmd --permanent --add-service=rpc-bind
  firewall-cmd --reload

Vagrant
^^^^^^^
Enter the project folder and install the new virtual server.

.. code-block:: bash

  cd item-catalog
  vagrant up

To enter the server and set up the environment enter the following code:

.. code-block:: bash

  vagrant ssh
  cd /vagrant
  source env/bin/activate
  pip install -r requirements.txt

Flask
^^^^^
To configure the environment with all your keys from google OAuth2.0 do the following:

.. code-block:: bash

  cp /vagrant/config-template.py /vagrant/cofig.py

Open config.py and change all the Secret codes and client id's as needed.