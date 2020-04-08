from flask import render_template, flash, redirect, url_for, jsonify, abort, g
from webapp import app, db, auth
from webapp import app
from flask import Response
from flask import request
from werkzeug.urls import url_parse
from webapp.models import User
from flask_login import current_user, login_user, logout_user, login_required

@auth.verify_password
def verify_password(username_token, password):
    #first try to use token for auth
    user = User.verify_auth_token(username_token)
    if not user:
        # try authenticate with username/password
        user = User.query.filter_by(username = username_token).first()
        if not user or not user.check_password(password):
            return False

    g.user = user
    return True

@app.route('/api')
@app.route('/api/index')
def index():
    return jsonify({'version': '1.0'})


@app.route('/api/user/<int:userId>', methods = ['GET'])
@auth.login_required
def getUser(userId):
    user = User.query.filter(User.id == userId).first()
    if user:
        return jsonify({'id': user.id,
                        'name': user.username
                        })
    else:
        return abort(401)




