Project Specification -- Item Catalog
=====================================

API Endpoints
--------------
The project implements a JSON endpoint that serves the same information as displayed in the HTML endpoints for an arbitrary item in the catalog.

CRUD: Read
----------
Website reads category and item information from a database.

CRUD: Create
------------
Website includes a form allowing users to add new items and correctly processes submitted forms.

CRUD: Update
------------
Website does include a form to edit/update a current record in the database table and correctly processes submitted forms.

CRUD: Delete
------------
Website does include a function to delete a current record.

Authentication & Authorization
------------------------------

* Create, delete and update operations do consider authorization status prior to execution.
* Page implements a third-party authentication & authorization service (like Google Accounts or Mozilla Persona) instead of implementing its own authentication & authorization spec.
* Make sure there is a 'Login' and 'Logout' button/link in the project. The aesthetics of this button/link is up to the discretion of the student.