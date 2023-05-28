from flask import Blueprint
from Controller.BaseController import BaseController
from Controller.HomeController import HomeController
from Controller.AuthController import AuthController


routes = Blueprint('routes', __name__)


@routes.route('/', methods=['GET'])
@BaseController.token_required
def index(current_user):
    return HomeController.index(current_user)


@routes.route('/login', methods=['POST'])
def login():
    return AuthController.login()


@routes.route('/register', methods=['POST'])
def register():
    return AuthController.register()