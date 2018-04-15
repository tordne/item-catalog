# project/server/main/views.py

from flask import Blueprint, render_template, session, url_for, \
    redirect, request, flash

from project.server import pg_session
from project.server.models import User, Category, Item
from project.server.helpers import login_required, check_authentication
from functools import wraps

import pdb

''' Configuration '''


main_blueprint = Blueprint('main', __name__,)


''' Public Routes '''


@main_blueprint.route('/')
@main_blueprint.route('/catalog')
def list_categories():
    '''
    List all the categories and last added items

    * items - Retrieve the 5 last added or updated items
    * categories - Retrieve all the categories

    .. http:get:: /catalog

        :return: Render the catalog template

    .. :quickref: Home; List all the categories
    '''
    # Retrieve all the categories from the database
    categories = pg_session.query(Category).order_by(Category.name.asc())

    # Retrieve the last 5 added items from the database
    items = pg_session.query(Item).order_by(Item.date_time.desc()).limit(5)

    return render_template('main/catalog.html',
                           categories=categories,
                           items=items)


@main_blueprint.route('/catalog/<string:category>',
                      methods=['GET'])
def list_items(category):
    '''
    List all the items in the given category

    * items - Retrieve all the ites in the given category
    * categories - Retrieve all the categories

    .. http:get:: /catalog/(string:category)

        :param category: The selected category
        :type category: str
        :return: Render the items template

    .. :quickref: Category; List all the items
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
@main_blueprint.route('/catalog/<string:category>/<string:item>',
                      methods=['GET'])
def info_item(category, item):
    '''
    List the information about the given item

    * items - Retrieve the item at the hand of the name given

    .. http:get:: /catalog/(string:category)/(string:item)

        :param category: The selected category
        :type category: str
        :param item: The selected item
        :type item: str
        :return: Render the description template

    .. :quickref: Item; List the item info
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

    * user - Retrieve the user details from the db with session['id']

    .. http:get:: /catalog/new

        :return: Render the category_new template

    .. http:post:: /catalog/new

        :form name: Category name
        :status 302: and then redirect to :http:get:`/catalog`

    .. :quickref: Category; Create a new category
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
@check_authentication
def category_edit(category):
    '''
    Edit the given category

    * user - Retrieve the user details from the db with session['id']
    * cat_edit - Retrieve the category to be edited from the db.

    .. http:get:: /catalog/(string:category)/edit

        :param category: The selected category
        :type category: str
        :return: Render the category_edit template

    .. http:post:: /catalog/(string:category)/edit

        :param str category: The selected category
        :type category: str
        :form name: Category name
        :status 302: and then redirect to :http:get:`/catalog`

    .. :quickref: Category; Edit the given category
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
@check_authentication
def category_delete(category):
    '''
    Delete the given category

    .. http:get:: /catalog/(string:category)/delete

        :param category: The selected category
        :type category: str
        :return: Render the category_delete template

    .. http:post:: /catalog/(string:category)/delete

        :param category: The selected category
        :type category: str
        :status 302: and then redirect to :http:get:`/catalog`

    .. :quickref: Category; Delete the given category
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

    .. http:get:: /catalog/(string:category)/new

        Initially retrieve a list of categories to display in the select
        options. Identify the user through their google_id.

        :param category: The selected category
        :type category: str
        :return: render template main/item_new

    .. http:post:: /catalog/(string:category)/new

        Retrieve the category id number by the request.form['cat_select']
        Retrieve the user id number through the session['id']
        Create newItem with info form request.form and retrieved cat.id
        and user.id. Redirect to list_items route

        :param category: The selected category
        :type category: str
        :form name: Items name
        :status 302: and then redirect
            to :http:get:`/catalog/(string:category)`

    .. :quickref: Item; Create a new item
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
@check_authentication
def item_edit(category, item):
    '''
    Edit the given item

    .. http:get:: /catalog/(string:category)/(string:item)/edit

        :param category: The selected category
        :type category: str
        :param item: The selected item
        :type item: str
        :return: Render item_edit template

    .. http:post:: /catalog/(string:category)/(string:item)/edit

        :param category: The selected category
        :type category: str
        :param item: The selected item
        :type item: str
        :form name: Item name
        :form description: Item description
        :form category: Item category
        :status 302: and then redirect to \
            :http:get:`/catalog/(string:category)/(string:item)`

    .. :quickref: Item; Edit the given item
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
@main_blueprint.route('/catalog/<string:category>/<string:item>/delete',
                      methods=['GET', 'POST'])
@login_required
@check_authentication
def item_delete(category, item):
    '''
    Delete the given item

    .. http:get:: /catalog/(string:category)/(string:item)/delete

        :param category: The selected category
        :type category: str
        :param item: The selected item
        :type item: str
        :return: Render item_delete template

    .. http:post:: /catalog/(string:category)/(string:item)/delete

        :param category: The selected category
        :type category: str
        :param item: The selected item
        :type item: str
        :status 302: and then redirect to \
            :http:get:`/catalog/(string:category)`


    .. :quickref: Item; Delete the given item
    '''
    if request.method == 'POST':
        item_del = pg_session.query(Item).filter_by(name=item).one()

        pg_session.delete(item_del)
        pg_session.commit()

        flash("Item: {name} is deleted.".format(name=item_del.name), 'success')
        return redirect(url_for('main.list_items', category=category))
    else:
        return render_template(
            'main/item_delete.html',
            category=category,
            item=item)
