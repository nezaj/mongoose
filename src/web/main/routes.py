"""
Logic for dashboard related routes
"""
from flask import render_template

from data.db import db
from data.models import User
from . import main

@main.route('/', methods=['GET'])
def index():
    users = db.session.query(User).all()
    return render_template('/main/index.tmpl', users=users)
