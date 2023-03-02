from flask import Flask, redirect, request, jsonify, url_for, abort
from http import HTTPStatus
from mysql.connector import Error

class BaseRepository(object):

    def __init__(self, db):
        self.db = db

    def find_by_id(self, id):
        try:
            connection = self.db.get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM m_user WHERE id=%s", (id,))

           
            row = cursor.fetchone()

            if row:
                response = jsonify(row)
                response.status_code = 200
            else:
                response = jsonify({"msg": "not found"})
                response.status_code = 404
            
            return response
        except Error as sqle:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(sqle))
        except Exception as e:
            abort(HTTPStatus.BAD_REQUEST, description=str(e))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def find(self, page, size):

        result = {
            "data": [],
            "total" : 0,
            "page": page,
            "size": size
        }

        try:
            connection = self.db.get_connection()

            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM m_user ORDER BY id limit %s offset %s', (size, (page-1)))
            result['data'] = cursor.fetchall()

            cursor.execute('SELECT count(id) as total FROM m_user')
            result['total'] = cursor.fetchone()['total']

            response = jsonify(result)
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

    def save(self, data):
        try:
            connection = self.db.get_connection()
            connection.autocommit = False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("INSERT INTO m_user (id, name) VALUES(%(id)s, %(name)s)", data)
            connection.commit()

            cursor.execute("SELECT * FROM m_user WHERE id=%s", (data['id'],))
            row = cursor.fetchone()
            response = jsonify(row)
            response.status_code = 200

            return response
        except Error as sqle:
            connection.rollback()
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(sqle))
        except Exception as e:
            connection.rollback()
            abort(HTTPStatus.BAD_REQUEST, description=str(e))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def update(self, data):
        try:
            connection = self.db.get_connection()
            connection.autocommit = False

            cursor = connection.cursor(dictionary=True)
            cursor.execute("update m_user set name=%(name)s where id=%(id)s", data)
            connection.commit()

            cursor.execute("SELECT * FROM m_user WHERE id=%s", (data['id'],))
            row = cursor.fetchone()
            response = jsonify(row)
            response.status_code = 200

            return response
        except Error as sqle:
            connection.rollback()
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(sqle))
        except Exception as e:
            connection.rollback()
            abort(HTTPStatus.BAD_REQUEST, description=str(e))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete(self, id):
        try:
            connection = self.db.get_connection()
            connection.autocommit = False

            cursor = connection.cursor()
            cursor.execute("DELETE FROM m_user WHERE id=%s", (id,))
            connection.commit()

            response = jsonify({'message' : f'data with id={id} is deleted'})
            response.status_code = 200

            return response
        except Error as sqle:
            connection.rollback()
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(sqle))
        except Exception as e:
            connection.rollback()
            abort(HTTPStatus.BAD_REQUEST, description=str(e))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()