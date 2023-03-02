from flask import Flask, redirect, request, jsonify, url_for, abort
from http import HTTPStatus
from mysql.connector import Error
from app import connection_pool
from . import main

@main.get("/")
def index():
    try:
        connection = connection_pool.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM m_user")

        users = []
        for row in cursor.fetchall():
            print(row);
            users.append({"id": row['id'], "name": row['name']})

        response = jsonify(users)
        response.status_code = 200
        return response
    except Error as sqle:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(sqle))
    except Exception as e:
        abort(HTTPStatus.BAD_REQUEST, description=str(e))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


@main.get("/insert")
def insert():
    try:
        connection = connection_pool.get_connection()

        mySql_insert_query = """INSERT INTO m_user (id, name) 
                            VALUES 
                            (3, '333333') """

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        response = jsonify({"message" : "ok"})
        response.status_code = 200
        return response

    except Error as sqle:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(sqle))
    except Exception as e:
        abort(HTTPStatus.BAD_REQUEST, description=str(e))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@main.get('/about')
def about_page():
    return "<h1 style='color:blue'>About</h1>"

def get_response_msg(data, status_code):
    message = {
        'status': status_code,
        'data': data if data else 'No records found'
    }
    response_msg = jsonify(message)
    response_msg.status_code = status_code
    return response_msg