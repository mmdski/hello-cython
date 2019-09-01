from setuptools import setup, Extension

setup(name='Hello world app',
      setup_requires=['cython'],
      ext_modules=[Extension('hello', sources=['hello.pyx'])],
      zip_safe=False)
