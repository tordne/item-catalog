# project/server/api/views.py

from flask import Blueprint, jsonify

from project.server import pg_session
from project.server.models import Category, Item

''' Configuration '''


api_blueprint = Blueprint('api', __name__, url_prefix="/api/v1")


''' Public Routes '''


@api_blueprint.route('/categories')
def listCategoriesJSON():
    '''
    Return a JSON with all the categories

    .. :quickref: API: Get a JSON with all categories

    :return: Return a JSON list of categories.
    '''
    # Retrieve all the categories from the database
    categories = pg_session.query(Category).order_by(Category.name.asc())

    return jsonify(categories=[i.serialize for i in categories])


@api_blueprint.route('/<string:category>')
def listItemsJSON(category):
    '''
    Return a JSON with all the items in the given category

    .. :quickref: API: Get a JSON with all the items under category provided

    :param str category: The selected category
    :return: Retrun a JSON list of items.
    '''
    # Retrieve the last 5 added items from the database
    items = pg_session.query(Item).filter(
        Item.category.has(name=category)).order_by(Item.name.asc())

    return jsonify({'Category': category, 'items': [i.serialize for i in items]})

