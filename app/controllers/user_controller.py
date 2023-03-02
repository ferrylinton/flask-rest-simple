import logging
from flask import Blueprint, redirect, request, jsonify, url_for, abort
from markupsafe import escape
from http import HTTPStatus
from app.services import user_service

blueprint  = Blueprint("user", __name__)
LOG = logging.getLogger(__name__)

@blueprint.route('/', methods=['GET','POST'])
def index():
    print("index :: GET")
    LOG.info("index :: GET")

    if(request.method == 'GET'):
        
        page = request.args.get("page", 1, type=int)
        size = request.args.get("size", 10, type=int)
    
        return user_service.find(page, size)
    elif (request.method == 'POST'):
        return user_service.save(request.get_json())

@blueprint.route('/<id>', methods=['GET','PUT', 'DELETE'])
def by_id(id):
    if(request.method == 'GET'):
        return user_service.find_user_by_id(id)

    elif (request.method == 'PUT'):
        body = request.get_json()
        body['id'] = id;
        return user_service.update(body)
    elif (request.method == 'DELETE'):
        return user_service.delete(id)