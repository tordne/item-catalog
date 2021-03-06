#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Catalog documentation build configuration file, created by
# sphinx-quickstart on Fri Jan 19 00:32:30 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
print(os.path.abspath('../..'))

# Install mock modules
autodoc_mock_imports = []

autodoc_mock_imports.append('sqlalchemy')


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.autodoc',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.autohttp.flask',
    'sphinxcontrib.autohttp.flaskqref',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.sadisp',
    ]

autodoc_default_flags = ['members']
autosummary_generate = True
autodoc_member_order = 'groupwise'

plantuml = 'java -jar ../../plantuml.jar'.split()
graphviz = 'dot -Tpng -Gsize=10'.split()

sadisplay_default_render = 'graphviz'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Catalog'
copyright = '2018, Christopher Berdahl'
author = 'Christopher Berdahl'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Catalogdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '9pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Catalog.tex', 'Catalog Documentation',
     'Christopher Berdahl', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'catalog', 'Catalog Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Catalog', 'Catalog Documentation',
     author, 'Catalog', 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


import re
import six
from sphinxcontrib.autohttp import common

pattern = re.compile('.. http:(get|GET|put|PUT|post|POST|OPTIONS|options|DELETE|delete):: (.*)')

def http_directive(method, path, content):
    """
    Custom http_directive that will only display parts of the
    content depending on whether the content matches the method
    and path.
    """
    method = method.lower().strip()
    if isinstance(content, six.string_types):
        content = content.splitlines()

    yield ''
    paths = [path] if isinstance(path, six.string_types) else path
    sections = dict()
    path_key = 'any'
    sections[path_key] = []
    for line in content:
        m = pattern.match(line)
        if m:
            section_method = m.group(1)
            path_key = m.group(2).lower()

        if path_key == 'any' or section_method.lower() == method:
            if not path_key in sections:
                sections[path_key] = []
            sections[path_key].append(line)
    for path in paths:
        # Replace angle brackets (flask) with parantheses (sphinx)
        to_match = path.replace('<','(').replace('>',')')

        # Search for path_key that maps to end of path
        # We can't do exact match because path includes
        # url_prefix from blueprint
        matched_path = None
        for path_key in sections:
            if path.endswith(path_key):
                matched_path = path_key
                break

        # If path_key maps to end of path
        if matched_path:
            # Yield first line of section
            yield sections[matched_path][0]
            yield ''

            # Yield common section lines
            for line in sections['any']:
                yield '   ' + line

            # Yield remainder of matched section
            if len(sections[matched_path]) > 1:
                for line in sections[matched_path][1:]:
                    yield line
        else:
            # Default behavior if no matched_path
            yield '.. http:{method}:: {path}'.format(**locals())
            yield ''
            for line in sections['any']:
                yield '   ' + line
    yield ''

# Override default version of http_directive
common.http_directive = http_directive