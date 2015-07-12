#!/usr/bin/env python

import os
import requests
from urllib.parse import urljoin
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.migrate import MigrateCommand
from flask.ext.script import Manager

from cargo.db.db import init_database
from cargo.extra.extra import ExtraAPI

# TODO see below the next TODO
# configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///cargo.db'
DEBUG = True
SECRET_KEY = '5h1pp3r143r'
USERNAME = 'admin'
PASSWORD = 'default'

DOCKER_HOST = 'http://127.0.0.1'
DOCKER_PORT = '4567'
DOCKER_API = ':'.join([DOCKER_HOST, DOCKER_PORT])

# application
app = Flask(__name__)
# TODO spin off the config on another file
app.config.from_object(__name__)
init_database(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


def register_api(view, kwargs, endpoint, url, defaults=None):
    view_func = view.as_view(endpoint, **kwargs)
    app.add_url_rule(url, view_func=view_func, defaults=defaults)

register_api(ExtraAPI, {'docker_api': DOCKER_API}, 'extra', '/extra')


if __name__ == "__main__":
    manager.run()
