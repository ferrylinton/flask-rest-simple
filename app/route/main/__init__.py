from flask import Blueprint, jsonify

main  = Blueprint("main", __name__)

from . import routes