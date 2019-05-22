from flask import Blueprint
import string
import random

import db_con as db

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def hello():
    # TODO give users the option to shorten a link
    # given link, generate a random string and store it in a database
    # with the link for later lookup
    pass

@bp.route('/new', methods=['POST'])
def new_link():
    #TODO make a new link and store it in the database



    # get url to be shortened from the POST request
    new_url = rand_str(5)

    #TODO db.add(new_url, link)
    pass


#@bp.route('/{}', methods=['GET'])
def shortlink():
    # TODO figure out how to take any string in the url and then look that
    # string up in the database.
    # If it exists, retirect to given pair in database
    # Else, render error page
    
    pass


def rand_str(n: int):
    """Generates a random string of length n"""
    return ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)] for i in range(n)])
