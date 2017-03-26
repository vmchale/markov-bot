from setuptools import setup

setup(name='markovbot',
      version='0.1',
      description='Make a markov chain based twitter bot',
      url='http://github.com/vmchale/markov-bot',
      author='Vanessa McHale',
      author_email='tmchale@wisc.edu',
      license='BSD3',
      packages=['markovbot'],
      scripts=['bin/markovbot'],
      install_requires=[
          'gitpython',
          'markovify',
          'python-twitter',
      ],
      zip_safe=False)
