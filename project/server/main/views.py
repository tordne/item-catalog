# project/server/main/views.py

from flask import Blueprint, render_template


''' Configuration '''


main_blueprint = Blueprint('main', __name__,)


''' Public Routes '''


# Route listing all the categories
@main_blueprint.route('/')
@main_blueprint.route('/catalog')
def list_categories():
    return render_template('main/catalog.html')


# Route showing all the items under category
@main_blueprint.route('/catalog/<string:category>')
def list_items(category):
    return render_template('main/items.html', category=category)


# Route showing information about the item
@main_blueprint.route('/catalog/<string:category>/<string:item>')
def info_item(category, item):
    return render_template(
        'main/description.html',
        category=category,
        item=item)


''' Private Routes '''


# Create a new Category
@main_blueprint.route('/catalog/new')
def category_new():
    return render_template('main/category_new.html')


# Route to edit the category
@main_blueprint.route('/catalog/<string:category>/edit')
def category_edit(category):
    return render_template('main/category_edit.html', category=category)


# Route to delete the category
@main_blueprint.route('/catalog/<string:category>/delete')
def category_delete(category):
    return render_template('main/category_delete.html', category=category)


# Create a new item
@main_blueprint.route('/catalog/<string:category>/new')
def item_new(category):
    return "Create a new item"


# Route to edit the item
@main_blueprint.route('/catalog/<string:category>/<string:item>/edit')
def item_edit(category, item):
    return "Edit the item"


# Route to delete the item
@main_blueprint.route('/catalog/<string:category>/<string:item>/delete')
def item_delete(category, item):
    return render_template(
    	'main/item_delete.html',
    	category=category,
    	item=item)
