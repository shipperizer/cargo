#!/usr/bin/env python

import requests
from urllib.parse import urljoin
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

from cargo.extra.extra import ExtraAPI 

# configuration
DATABASE = '/tmp/flasking.db'
DEBUG = True
SECRET_KEY = '5h1pp3r143r'
USERNAME = 'admin'
PASSWORD = 'default'

DOCKER_HOST = 'http://127.0.0.1'
DOCKER_PORT = '4567'
DOCKER_API = ':'.join([DOCKER_HOST, DOCKER_PORT])

# application
app = Flask(__name__)
app.config.from_object(__name__)

def register_api(view, endpoint, url, defaults=None):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, view_func=view_func, defaults=defaults)
    
register_api(ExtraAPI, 'extra', '/extra')
