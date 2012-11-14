from setuptools import setup, find_packages
import sys, os

version = '0.2'

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
      install_requires=[
          # -*- Extra requirements: -*-
          'PasteDeploy',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.app_factory]
      main = techw.wsgiapp:make_app
      """,
      )
