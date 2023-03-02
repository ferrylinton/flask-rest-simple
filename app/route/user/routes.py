from flask import Flask, redirect, request, jsonify, url_for, abort
from markupsafe import escape
from http import HTTPStatus
from mysql.connector import Error
from app import connection_pool
from app.dao import user_dao
from . import user

@user.route('/', methods=['GET','POST'])
def index():
    if(request.method == 'GET'):
        page = request.args.get("page", 1, type=int)
        size = request.args.get("size", 10, type=int)
    
        return jsonify({
            "method": "GET",
            "page": page,
            "size": size
        })
    elif (request.method == 'POST'):
        body = request.get_json()
        return jsonify(body)

@user.route('/<id>', methods=['GET','PUT', 'DELETE'])
def by_id(id):
    if(request.method == 'GET'):
        test = user_dao.find_user_by_id('22222222')
        print(test)

        return jsonify({
            "method": "GET",
            "id": escape(id)
        })
    elif (request.method == 'PUT'):
        body = request.get_json()
        return jsonify({
            "method": "PUT"
        })
    elif (request.method == 'DELETE'):
        return jsonify({
            "method": "DELETE"
        })