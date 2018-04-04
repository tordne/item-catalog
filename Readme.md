# Udacity FSWD Project 4 - Item Catalog
## Synopsis
The Item Catalog is a project for Udacity Full Stack Web Developer Nano Degree.

The Catalog meets several requirements and has several features.
* The Catalog contains Categories
* Items are ordered under these categories.
* There is a read-only side for the Catalog
* There is a login_required side to the Catalog where the user has access to CRUD of the categories and items.
* Google OAuth2.0 is used to authenticate as a user.
* There are also APIs which will return a list of items in JSON

The main packages used are.
* Flask
* SQLAlchemy
* Sphinx
* Google.Auth
* Google.auth.Oauthlib
* Jinja2

## Prerequisites
This project was written in Linux Centos 7 with Python3.6 and postgreSQL 9.2.23
To run the website you can either run it in a virtual server or in a virtual environment.

## Heroku
I've added the project to heroku, please check it out @ [Heroku Udacity Catalog](https://cb-udacity-catalog.herokuapp.com/catalog)

## Full Documentation
With Sphinx and Github-pages I've created online documentation which can be found @ [Udacity Catalog Project](https://tordne.github.io/item-catalog/)
