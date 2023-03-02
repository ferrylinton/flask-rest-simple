from flask import Blueprint, jsonify

user  = Blueprint("user", __name__)

from . import routes