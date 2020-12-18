import sys
from setuptools import setup


CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of geomap-docs requires Python {}.{}, but you're trying to
install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install geomap-docs
This will install the latest version of geomap-docs which works on your
version of Python.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

setup(
    name='GeomapDocs',
    version='201907',
    author='Samuel Elkind',
    author_email='samuel.elkind@gmail.com',
    packages=['GeomapDocs', 'GeomapDocs.tests'],
    url='http://pypi.org/pypi/GeomapDocs',
    license='LICENSE.md',
    description='The unofficial end-user documentation for the GeoMAP project\n'
                'a continent-scale digital geological dataset of Antarctica',
    long_description=open('README.md').read(),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
                'pytest',
                'geopandas',
                'pandas',
                'mdutils',
                'sphinx',
                'PyYAML',
    ],
)
