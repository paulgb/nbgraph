from setuptools import setup, find_packages

import nbgraph

setup(name='nbgraph',
      version=nbgraph.__version__,
      description='Interactive graph exploration inside of a Jupyter notebook.',
      url='https://github.com/paulgb/nbgraph',
      author='Paul Butler',
      author_email='paulgb@gmail.com',
      packages=find_packages(),
      install_requires=['ipython>=5.0.0'],
)
