from setuptools import setup

setup(name='pg_scofflaw',
      version='0.1a1',
      description='Custom authentication proxy for PostgreSQL',
      url='https://github.com/parksandwildlife/pg_scofflaw',
      license='BSD',
      author='Scott Percival',
      author_email='scott.percival@dpaw.wa.gov.au',
      install_requires=['gevent>=1.1rc1', 'docopt'],
      scripts=['pg_scofflaw'])
