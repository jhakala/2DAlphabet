#!/usr/bin/env python

import setuptools

setuptools.setup(name='TwoDAlphabet',
      version='2.0',
      description='Framework for performing 2D binned-likelihood fits with one background derived from a transfer function.',
      author='Lucas Corcodilos',
      author_email='corcodilos.lucas@gmail.com',
      url='https://github.com/lcorcodilos/2DAlphabet',
      packages=setuptools.find_packages(),
      include_package_data=True,
      # cmdclass={'install': AddToPath},
      install_requires = [
            'pytest'
      ]
     )