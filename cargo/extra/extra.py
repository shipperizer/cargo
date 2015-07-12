#!/usr/bin/env python

import requests

from urllib.parse import urljoin
from flask.views import MethodView
from flask import render_template, jsonify, request


class ExtraAPI(MethodView):

    methods = ['GET']

    def __init__(self, docker_api=None):
        self.DOCKER_API = docker_api

    def get(self):
        json = request.args.get('json')
        version = self.version()
        info = self.info()
        if json not in ['True', 'true']:
            return render_template('extra.html', version=version, info=info)
        return jsonify(version=version, info=info)

    def version(self):
        return requests.get(urljoin(self.DOCKER_API, 'version')).json()

    def info(self):
        return requests.get(urljoin(self.DOCKER_API, 'info')).json()
