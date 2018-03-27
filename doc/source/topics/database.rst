Databases
=========

User
----
.. csv-table:: User
	:header: "name", "type", "options"
	:widths: 15 10 30

	"id", "Integer", "Primary Key"
	"name", "String(250)", "nullable=False"
	"email", "String(250)", "nullable=False"
	"password_hash", "String(64)"


Category
---------
+---------+-------------+-----------------------+
| name    | type        | options               |
+=========+=============+=======================+
| id      | Integer     | Primary Key           |
+---------+-------------+-----------------------+
| name    | String(250) | nullable=False        |
+---------+-------------+-----------------------+
| user_id | Integer     | ForeignKey('user.id') |
+---------+-------------+-----------------------+


Item
----
+-------------+-------------+---------------------------+
| name        | type        | options                   |
+=============+=============+===========================+
| id          | Integer     | Primary Key               |
+-------------+-------------+---------------------------+
| name        | String(250) | nullable=False            |
+-------------+-------------+---------------------------+
| description | String(250) |                           |
+-------------+-------------+---------------------------+
| user_id     | Integer     | ForeignKey('user.id')     |
+-------------+-------------+---------------------------+
| category_id | Integer     | ForeignKey('category.id') |
+-------------+-------------+---------------------------+

Authentication
--------------

.. csv-table:: Authentication
    :header: "name", "type", "options"
    :widths: 15 10 30

    "id", "Integer", "Primary key"
    "email", "String(100)", "nullable=False"
