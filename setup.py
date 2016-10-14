#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
"""
打包的用的setup必须引入，
"""

VERSION = '0.1.8'

setup(name='uclime',
      version=VERSION,
      description="A UCloud Command Line tool base on UCloud api",
      long_description='you can use this tool call the api from Command line',
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python ucloud api sdk uhost ufile ucli command line',
      author='hsiun',
      author_email='growdane@gmail.com',
      url='https://github.com/hsiun/ucli',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'requests',
      ],
      entry_points={
        'console_scripts':[
          'uclime = ucli.UCliMain:main'
        ]
      },
)