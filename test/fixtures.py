#!/usr/bin/env python

import pytest


@pytest.fixture(scope='function')
def foo():
    return 1
