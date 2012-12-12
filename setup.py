from setuptools import setup, find_packages
import sys, os

version = '0.0.5'

install_requires = [
    'PasteDeploy',
    'networkx',
]

docs_extras = [
    'docutils',
    'pygments',
    'Sphinx',
    'Sphinx-PyPi-upload',
    'sphinxfeed',
    'changelog',
    'sphinxcontrib-mercurial',
    'sphinx-git',
    'sphinxcontrib-bitbucket',
    'sphinxcontrib-issuetracker',
    'sphinxcontrib-cheeseshop',
    'sphinxcontrib-bibtex',
    'sphinxcontrib-paverutils',
    'github-tools[template]',
]

def read_file(_path):
    return open(_path).read()

def read_readme():
    import os
    _path = os.path.join(os.path.abspath(__file__).dirname(), 'README.rst')
    return open(_path).read()

setup(name='techw',
      version=version,
      description="Technical Report: Self Directed Learning With Online Resources",
      long_description=read_readme(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='online learning, self directed learning, ',
      author='Wes Turner',
      url='http://self-directed-learning.rtfd.org',
      license='Creative Commons',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=install_requires,
      extras_require={
        "docs": docs_extras,
      },
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      rst_shift = techw.rst_shift:main
      rst_outline = techw.rst_slideoutline:main
      [paste.app_factory]
      main = techw.wsgiapp:make_app
      """,
)
