from distutils.core import setup
from Cython.Build import cythonize
import numpy


setup(name='text',
      ext_modules=cythonize("text.pyx", language="c++"),
      include_dirs=[numpy.get_include()]
      )
