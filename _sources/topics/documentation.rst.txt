Documentation
=============

Keeping in mind that I would work on larger projects, I wanted to document the full project.

Over the last several weeks and months I have found different packages and modules.
It quickly became apparent to try and automate the documentation of the project.

The main package usded is Sphinx.

Sphinx
------
Sphinx is perfect to write documentation, after learning the initial syntax it is easy to extract Pdfs and html from the documents writte.

Extra Packages
--------------
To automate the creating of the documents, extra packages were used:

    * sphinx.ext.githubpages: This extension creates .nojekyll file on generated HTML directory to publish the document on GitHub Pages.
    * sphinx.ext.graphviz: This extension allows you to embed Graphviz graphs in your documents.
    * sphinx.ext.autodoc: This extension can import the modules you are documenting, and pull in documentation from docstrings in a semi-automatic way.
    * sphinxcontrib.httpdomain: provides a Sphinx domain for describing HTTP APIs.
    * sphinxcontrib.autohttp.flask: It generates RESTful HTTP API reference documentation from a Flask application’s routing table.
    * sphinxcontrib.autohttp.flaskqref: This generates a quick API reference table for the route documentation produced by sphinxcontrib.autohttp.flask
    * sphinxcontrib.plantuml: Sphinx "plantuml" extension
    * sphinxcontrib.sadisp: Rendering PlantUML diagrams or GraphViz directed graphs generated from SqlALchemy models.

Most of the automation works fine, if the correct syntax is used.

With Flask Routing There have been several issues, when multiple methods are used on a route. Then the full description given will be added to all the methods.

sphinxcontrib.autohttp.flask does not provide a sulution out of the box and this issue has been raised before and Kelly Davis gave a monkey path which can be found `HERE <https://bitbucket.org/birkenfeld/sphinx-contrib/issues/146/httpdomain-flask-route-hello-methods-get>`_
