Routing
=======

Public
-------
Categories
^^^^^^^^^^
* / and /catalog -- list all the categories

Items
^^^^^
* /catalog/<str:category> -- list all the items under the category
* /catalog/<str:category>/<str:item> -- list information about the item

Authentication
^^^^^^^^^^^^^^
* /login -- login with google account
* /logout -- disconnect the user account


Private
-------
Categories
^^^^^^^^^^
* /catalog/new -- create a new category
* /catalog/<str:category>/edit -- edit a category
* /catalog/<str:category>/delete -- delete a category
Items
^^^^^
* /catalog/<str:category>/new -- create a new item
* /catalog/<str:category>/<str:item>/edit -- edit an item
* /catalog/<str:category>/<str:item>/delete -- delete an item


API
---
Categories
^^^^^^^^^^
* /api/v1/catalog -- JSON all the categories
* /api/v1/<str:category> -- JSON all the items under the category
* /api/v1/<str:category>/<str:item> -- JSON information about the item