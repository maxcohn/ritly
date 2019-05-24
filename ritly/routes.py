from flask import Blueprint, request, render_template, redirect
import string
import random

from . import db_con

bp = Blueprint('routes', __name__)
db = db_con.RitlyDB()

#TODO main objectives: make home page, error page
#TODO error proof bad input

@bp.route('/', methods=['GET'])
def home():
    # TODO give users the option to shorten a link
    # given link, generate a random string and store it in a database
    # with the link for later lookup
    return render_template('base.html')

@bp.route('/new', methods=['POST'])
def new_link():
    # get link from json
    data = request.get_json()
    link = data['link']

    # get url to be shortened from the POST request
    new_url = rand_str(5)

    # add the pair to the database
    db.add_link(new_url, link)

    return '200'



@bp.route('/<url>', methods=['GET'])
def shortlink(url):
    # If it exists, retirect to given pair in database
    # Else, render error page

    link = db.lookup(url)

    # if the link was invalid, redirect them to the error page
    if link is None:
        return '500' #TODO redirect to error page (/bad?)
    
    #TODO fix url to always hav proper formatting
    return redirect(f'http://{db.lookup(url)}', code=301) #TODO change this to render template


def rand_str(n: int):
    """Generates a random string of length n"""
    return ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)] for i in range(n)])
