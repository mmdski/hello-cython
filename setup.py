from setuptools import setup
from setuptools.command.build_ext import build_ext as _build_ext

try:
    from Cython.Build import cythonize
except ImportError:
     def cythonize(*args, **kwargs):
         from Cython.Build import cythonize
         return cythonize(*args, **kwargs)

setup(name='Hello world app',
      setup_requires=['Cython'],
      ext_modules=cythonize(['hello.pyx']),
      zip_safe=False)
