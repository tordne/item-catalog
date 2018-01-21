Udacity FSWD Project 4 - Item Catalog
=====================================
Synopsis
--------
The Item Catalog is a project for Udacity Full Stack Web Developer Nano Degree.

The Catalog is a browseable and viewers will be able to see more detailed information when selecting an item.
There will be an authentication system with google login using OAuth2.0.
When users are authenticated, they will be able to use CRUD to modify the content of the catalog.

The lessons prior to this project were made at around 2014.
Since there have been a lot of software udates and many packages are no longer being maintained.

With this project the reigns are handed over to the student, and I wanted to make good use of this opportunity.
The project is small, but I've used a directory and file structure for larger projects with the following:
	* Flask Blueprints: seperate all the different sections
	* Flask scripts: Run the site with the flask CL
	* Client / Server: All the files are segregated to Client and Server files
	* config.py: organise all the secret keys and other client_id's
I have made the time to look into other packages to improve my workflow, and looking at Amazon's Github I've found Sphinx.
This improves the writing of README and other docs, and will organise all the information needed to get the project started.


Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   intro

   topics/specifications
   topics/routing
   topics/databases



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
