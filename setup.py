from setuptools import setup

setup(name='jupyter_MyNodejs_kernel',
      version='0.0.1',
      description='Minimalistic Nodejs kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyNodejs-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyNodejs-kernel/tarball/0.0.1',
      packages=['jupyter_MyNodejs_kernel'],
      scripts=['jupyter_MyNodejs_kernel/install_MyNodejs_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'nodejs','js'],
      include_package_data=True
      )
