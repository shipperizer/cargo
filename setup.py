import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    """
    Extension to setuptools' test command to allow us to run py.test
    using `python setup.py test`.

    Copied from the py.test documentation (see 'Good Integration Practises').
    """
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='cargo',
    version='0.0.99',
    description='Cargo',
    install_requires=[
        'flask>=0.10.0,<1',
        'flask-sqlalchemy>=2.0.0',
        'flask-script>=2.0.5',
        'flask-migrate>=1.4.0',
        'sqlalchemy>=1.0',
        'alembic',
    ],
    tests_require=[
        'pytest-cov',
        'mock',
        'python-coveralls'
    ],
    author='shipperizer',
    author_email='alexcabb@gmail.com',
    url='http://tiffzhang.com/startup/index.html?s=538178832968',
    packages=find_packages(),
    include_package_data=True,
    cmdclass={'test': PyTest}
)
