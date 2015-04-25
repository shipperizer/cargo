#!/usr/bin/env python

import requests

from urllib.parse import urljoin
from flask.views import MethodView
from flask import render_template, jsonify, request

import cargo

class ExtraAPI(MethodView):

    methods = ['GET']

    def get(self):
        json = request.args.get('json')
        version = self.version()
        info = self.info()
        if not json in ['True', 'true']:
            return render_template('extra.html', version=version, info=info)
        return jsonify(version=version, info=info)

    def version(self):
        return requests.get(urljoin(cargo.DOCKER_API, 'version')).json()

    def info(self):
        return requests.get(urljoin(cargo.DOCKER_API, 'info')).json()
        