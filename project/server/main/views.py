# project/server/main/views.py

from flask import Blueprint, render_template, session, url_for, \
    redirect, request, flash

from project.server import pg_session
from project.server.models import User, Category, Item
from project.server.helpers import login_required

import pdb

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
    '''
    # Retrieve all the categories from the database
    categories = pg_session.query(Category).order_by(Category.name.asc())

    # Retrieve the last 5 added items from the database
    items = pg_session.query(Item).order_by(Item.date_time.desc()).limit(5)

    return render_template('main/catalog.html',
                           categories=categories,
                           items=items)


@main_blueprint.route('/catalog/<string:category>')
def list_items(category):
    '''
    List all the items in the given category

    .. :quickref: Category; List all the items

    :param str category: The selected category
    :return: Render the items template
    '''
    # Retrieve all the categories from the database
    categories = pg_session.query(Category).order_by(Category.name.asc())

    # Retrieve the last 5 added items from the database
    items = pg_session.query(Item).filter(
        Item.category.has(name=category)).order_by(Item.name.asc())

    return render_template('main/items.html',
                           category=category,
                           categories=categories,
                           items=items)


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

    # Retrieve all the information about the item concerned
    items = pg_session.query(Item).filter_by(name=item).one()

    return render_template(
        'main/description.html',
        items=items)


''' Private Routes '''


@main_blueprint.route('/catalog/new', methods=['GET', 'POST'])
@login_required
def category_new():
    '''
    Create a new category.

    Query the database and get user.id with the google_id provided by session

    Create a new category with a name provided by request.form and the user.id

    .. :quickref: Category; Create a new category

    :return: Render the category_new template
    '''
    # Retrieve the user.id at the hand of the google_id from the database
    user = pg_session.query(User).filter_by(google_id=session['id']).one()

    if request.method == 'POST':
        newCategory = Category(
            name=request.form['category'],
            user_id=user.id)
        pg_session.add(newCategory)
        pg_session.commit()
        flash("New Category: {name} created.".format(
            name=newCategory.name), 'success')
        return redirect(url_for('main.list_categories'))
    else:
        return render_template('main/category_new.html')


@main_blueprint.route('/catalog/<string:category>/edit',
                      methods=['GET', 'POST'])
@login_required
def category_edit(category):
    '''
    Edit the given category

    .. :quickref: Category; Edit the given category

    :param str category: The selected category
    :return: Render the category_edit template
    '''
    user = pg_session.query(User).filter_by(google_id=session['id']).one()
    cat_edit = pg_session.query(Category).filter_by(name=category).one()

    if request.method == 'POST':
        if request.form['category']:
            cat_edit.name = request.form['category']
            cat_edit.user_id = user.id
            pg_session.add(cat_edit)
            pg_session.commit()
            flash("Category: {name} is edited.".format(
                name=cat_edit.name), 'success')
        return redirect(url_for('main.list_categories'))
    else:
        return render_template('main/category_edit.html', category=category)


@main_blueprint.route('/catalog/<string:category>/delete',
                      methods=['GET', 'POST'])
@login_required
def category_delete(category):
    '''
    Delete the given category

    .. :quickref: Category; Delete the given category

    :param str category: The selected category
    :return: Render the category_delete template
    '''
    cat_del = pg_session.query(Category).filter_by(name=category).one()

    if request.method == 'POST':
        pg_session.delete(cat_del)
        pg_session.commit()
        flash("Category: {name} is deleted.".format(
            name=cat_del.name), 'success')
        return redirect(url_for('main.list_categories'))
    else:
        return render_template('main/category_delete.html', category=category)


@main_blueprint.route('/catalog/<string:category>/new',
                      methods=['GET', 'POST'])
@login_required
def item_new(category):
    '''
    Create a new item

    method['GET']:

    * Initially retrieve a list of categories to display in the select options.
    * Identify the user through their google_id.

    method['POST']:

    * Retrieve the category id number by the request.form['cat_select']
    * Retrieve the user id number through the session['id']
    * Create newItem with info form request.form and retrieved cat.id and user.id
    * Redirect to list_items route

    .. :quickref: Item; Create a new item

    :param str category: The selected category
    :return: Render the item_new template
    '''
    # Retrieve a list of categories to display in the form
    categories = pg_session.query(Category).order_by(Category.name.asc())

    if request.method == 'POST':
        cat = pg_session.query(Category).filter_by(
            name=request.form['cat_select']).one()

        # Retrieve the user.id with the session['google_id']
        user = pg_session.query(User).filter_by(google_id=session['id']).one()

        newItem = Item(
            name=request.form['name'],
            description=request.form['description'],
            category_id=cat.id,
            user_id=user.id
        )
        pg_session.add(newItem)
        pg_session.commit()
        flash("New Item: {name} created.".format(
            name=newItem.name), 'success')
        return redirect(url_for('main.list_items', category=category))
    else:
        return render_template('main/item_new.html',
                               category=category,
                               categories=categories)


@main_blueprint.route('/catalog/<string:category>/<string:item>/edit',
                      methods=['GET', 'POST'])
@login_required
def item_edit(category, item):
    '''
    Edit the given item

    .. :quickref: Item; Edit the given item

    :param str category: The selected category
    :param str item: The selected item
    :return: Render the item_edit template
    '''
    # Retrieve a list of categories to display in the form
    categories = pg_session.query(Category).order_by(Category.name.asc())
    editItem = pg_session.query(Item).filter_by(name=item).one()

    if request.method == 'POST':
        # Retrieve the category_id with the request.form['cat_select']
        cat = pg_session.query(Category).filter_by(
            name=request.form['cat_select']).one()

        # Retrieve the user.id with the session['google_id']
        user = pg_session.query(User).filter_by(google_id=session['id']).one()

        editItem.name = request.form['name']
        editItem.description = request.form['description']
        editItem.category_id = cat.id
        editItem.user_id = user.id

        pg_session.add(editItem)
        pg_session.commit()

        flash("Item: {name} is edited.".format(
            name=editItem.name), 'success')
        return redirect(url_for('main.info_item',
                                category=cat.name,
                                item=editItem.name))
    else:
        return render_template('main/item_edit.html',
                               category=category,
                               categories=categories,
                               editItem=editItem)


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
