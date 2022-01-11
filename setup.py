#!/usr/bin/env python
# coding: utf-8
with open("README.md", "r") as f:
	long_description = f.read()
import setuptools
setuptools.setup(name='jupyter_MyNodejs_kernel',
      version='0.0.1',
      description='Minimalistic Nodejs kernel for Jupyter',
    long_description=long_description,
    long_description_content_type="text/markdown",
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      url='https://github.com/nufeng1999/jupyter-MyNodejs-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyNodejs-kernel/releases/tag/0.0.1',
    packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
      scripts=['jupyter_MyNodejs_kernel/install_MyNodejs_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'nodejs','js'],
      include_package_data=True
      )
