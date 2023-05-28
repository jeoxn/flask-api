from flask import request, jsonify
from Controller.BaseController import BaseController


class HomeController(BaseController):
    @staticmethod
    def index(current_user = None):
        return jsonify({'message': 'Hello, World!'})
