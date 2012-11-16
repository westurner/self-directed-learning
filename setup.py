from setuptools import setup, find_packages
import sys, os

version = '0.2'

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


setup(name='techw',
      version=version,
      description="techw",
      long_description="""\
TODO""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='TODO',
      author='Wes Turner <wes@wrd.nu>',
      author_email='TODO',
      url='TODO',
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
