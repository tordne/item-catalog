Udacity FSWD Project 4 - Item Catalog
=====================================
Synopsis
--------
The Item Catalog is a project for Udacity Full Stack Web Developer Nano Degree.

A working version of the Catalog can be found on `Heroku <https://cb-udacity-catalog.herokuapp.com/>`_.

The Catalog project consists of the following:

	* A database with a list of categories
	* A database with items belonging to categories
	* An authentication system for user to be access CRUD on items and categories
	* API routes that list categories and items in JSON

With this project the reigns are handed over to the student, and I wanted to make good use of this opportunity.
The project is small, but I've used a directory and file structure for larger projects with the following:

	* `Git Branches <http://nvie.com/posts/a-successful-git-branching-model/>`_: A good branch strategy is important when expanding to teams and make releases of the project.
	* `Flask Blueprints <http://flask.pocoo.org/docs/0.12/blueprints/>`_: seperate all the different sections
	* `Flask CLI <http://flask.pocoo.org/docs/0.12/cli/>`_: Run the site with the flask CL
	* Client / Server: All the files are segregated to Client and Server files
	* config.py: organise all the secret keys and other client_id's
	* `CentOS 7 <https://tordne.github.io/item-catalog/installation/system.html>`_: CentOS is a very stable distribution which I use on my servers, hence I wanted to create my Vagrant Boxes with CentOS 7.


It was the intention of using a large project file structure but still using a minimum of extra packages which solve all the problems. This would give me a need to program my own helper functions and scripts. Example Given:

	* `javascripts <https://github.com/tordne/item-catalog/blob/master/project/client/static/js/close-alerts.js>`_: To close the flash_messages.
	* `Global helper functions <https://github.com/tordne/item-catalog/blob/master/project/server/helpers.py>`_: These are the global helper functions, including @login_required.

I have taken the time to look into other packages to improve my workflow, and used the following:

	* `Sphinx <http://www.sphinx-doc.org/en/master/>`_: Documentation writing
	* `Github Pages <https://tordne.github.io/item-catalog/index.html>`_: Online Documentation which connects with the projects sources
	* `Pencil <https://pencil.evolus.vn/>`_: An open-source GUI prototyping tool



System Installation
-------------------
.. toctree::
	:maxdepth: 3

	installation/system.rst


The Catalog
-----------
.. toctree::
   :maxdepth: 2

   topics/specification
   topics/documentation
   topics/routing
   topics/helpers
   topics/database

TODO
----
.. todolist::
