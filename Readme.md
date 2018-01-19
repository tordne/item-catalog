# Udacity FSWD Project 4 - Item Catalog
## Synopsis
The Item Catalog is a project for Udacity Full Stack Web Developer Nano Degree.
The FSWD course was made around 2014 and several of the packages used throughout the course are not being maintained anymore.
I also did more research and I found several tutorials made in 2017 & 2018, including the Mega tutorial from Miguel Grinberg.
This project is made with the latest versions of software and packages which are maintained at the time of *January 2018*.

Flask provides many packages which are more advanced than the ones used througout the course. But these packages don't show you really how it all works. While using the latest versions I used the most basic packages available, to learn the concepts and underlying structures. 

The Catalog meets several requirements and has several features.
* The Catalog contains Categories
* Items are ordered under these categories.
* There is a read-only side for the Catalog
* There is a login_required side to the Catalog where the user has access to CRUD of the categories and items.
* Google OAuth2.0 is used to authenticate as a user.
* There are also APIs which will return a list of items in JSON

## Prerequisites
This project was written in Linux Centos 7 with Python3.6 and postgreSQL 9.2.23
To run the website you can either run it in a virtual server or in a virtual environment.
#### Vagrant
There is a Vagrant file provided with a basic install of Centos 7, python and PostgreSQL.
Setting up the Server will require at least 2.5GB of free disk space.
> Please note that creating the Vagrant environment will take approximately 10 - 15 mins to complete. As several packages including python 3.6 have to be compiled.

Check if the following packages are installed:
```
vagrant --version
```

#### Virtual Environment
If you are not willing to use or able to use the Vagrant server, you can run the server in a virtual environment. Please check you have the following packages installed with the correct versions.
```
python3 --version
psql --version
```

## How to install
### Linux Instructions
#### Download Project
Open a terminal and download teh full project: `git clone https://github.com/tordne/item-catalog.git`

#### Vagrant
Enter the project folder and startup the new virtual server.
```
cd item-catalog
vagrant up
```
To enter the server and set up the environment enter the following code:
```
vagrant ssh
cd /vagrant
python3.6 -m venv env
source env/bin/activate
pip install -r requirements.txt
export FLASK_APP=catalog.py
```
To configure the environment with all your keys from google OAuth2.0 do the following:
* `cp /vagrant/config-template.py /vagrant/cofig.py` 
* Open config.py and change all the Secret codes and client id's as needed.
* export the last 3 env variables to ensure the config file is read properly
```
export FLASK_CONFIG=/vagrant/config.py
export FLASK_SETTINGS=config.DevelopmentConfig
```

#### Virtual Environment
```
cd item-catalog
python3.6 -m venv env
source env/bin/activate
pip install -r requirements.txt
eport FLASK_APP=catalog.py
```
To configure the environment with all your keys from google OAuth2.0 do the following:
* `cp ~/item-catalog/config-template.py ~/item-catalog/cofig.py` 
* Open config.py and change all the Secret codes and client id's as needed.
* export the last 3 env variables to ensure the config file is read properly
```
export FLASK_CONFIG=~/item-catalog/config.py
export FLASK_SETTINGS=config.DevelopmentConfig
```

#### Last Configurations for Vagrant and Venv 
* Running the flask app by script doesn't activate debug anymore and it needs to be activated by an env variable
```
export FLASK_DEBUG=1
```

## How to run the site
### Linux Instructions
#### Vagrant
Enter your server, navigate to the projects directory, start the venv and run the program:
```
vagrant ssh
cd /vagrant
source env/bin/activate
export FLASK_APP=catalog.py
flask run
```

#### Virtual Environment
Navigate to the projects directory, start the venv and run the program:
```
source env/bin/activate
export FLASK_APP=catalog.py
flask run
```

## Project contents
