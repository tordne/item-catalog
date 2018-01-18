# project/server/main/views.py

from flask import Blueprint


''' Configuration '''


main_blueprint = Blueprint('main', __name__,)


''' Routes '''


@main_blueprint.route('/')
@main_blueprint.route('/catalog')
def catalog():
    return "This is a Catalog"
