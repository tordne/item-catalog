# project/server/main/views.py

from flask import Blueprint, render_template


''' Configuration '''


main_blueprint = Blueprint('main', __name__,)


''' Public Routes '''


@main_blueprint.route('/')
@main_blueprint.route('/catalog')
def list_categories():
    '''
    List all the categories and last added items

    .. :quickref: Home; List all the categories

    :return: Render the catalog template

    .. todo:: def list_categories()

        * list all the categories
        * list the 5 latest items with the corresponding category in ()
    '''
    return render_template('main/catalog.html')


@main_blueprint.route('/catalog/<string:category>')
def list_items(category):
    '''
    List all the items in the given category

    .. :quickref: Category; List all the items

    :param str category: The selected category
    :return: Render the items template
    '''
    return render_template('main/items.html', category=category)


# Route showing information about the item
@main_blueprint.route('/catalog/<string:category>/<string:item>')
def info_item(category, item):
    '''
    List the information about the given item

    .. :quickref: Item; List the item info

    :param str category: The selected category
    :param str item: The selected item
    :return: Render the description template
    '''
    return render_template(
        'main/description.html',
        category=category,
        item=item)


''' Private Routes '''


@main_blueprint.route('/catalog/new')
def category_new():
    '''
    Create a new category

    .. :quickref: Category; Create a new category

    :return: Render the category_new template
    '''
    return render_template('main/category_new.html')


@main_blueprint.route('/catalog/<string:category>/edit')
def category_edit(category):
    '''
    Edit the given category

    .. :quickref: Category; Edit the given category

    :param str category: The selected category
    :return: Render the category_edit template
    '''
    return render_template('main/category_edit.html', category=category)


@main_blueprint.route('/catalog/<string:category>/delete')
def category_delete(category):
    '''
    Delete the given category

    .. :quickref: Category; Delete the given category

    :param str category: The selected category
    :return: Render the category_delete template
    '''
    return render_template('main/category_delete.html', category=category)


@main_blueprint.route('/catalog/<string:category>/new')
def item_new(category):
    '''
    Create a new item

    .. :quickref: Item; Create a new item

    :param str category: The selected category
    :return: Render the item_new template
    '''
    return render_template(
        'main/item_new.html',
        category=category)


@main_blueprint.route('/catalog/<string:category>/<string:item>/edit')
def item_edit(category, item):
    '''
    Edit the given item

    .. :quickref: Item; Edit the given item

    :param str category: The selected category
    :param str item: The selected item
    :return: Render the item_edit template
    '''
    return render_template(
        'main/item_edit.html',
        category=category,
        item=item)


# Route to delete the item
@main_blueprint.route('/catalog/<string:category>/<string:item>/delete')
def item_delete(category, item):
    '''
    Delete the given item

    .. :quickref: Item; Delete the given item

    :param str category: The selected category
    :param str item: The selected item
    :return: Render the item_delete template
    '''
    return render_template(
        'main/item_delete.html',
        category=category,
        item=item)
