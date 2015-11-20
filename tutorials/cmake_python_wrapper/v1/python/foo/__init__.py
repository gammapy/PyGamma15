import ctypes
import numpy as np
import os
import sys

__all__ = ['square']

_path = os.path.dirname(__file__)

libname = None
if sys.platform.startswith('linux'):
	libname = 'libfoo.so'
elif sys.platform == 'darwin':
	libname = 'libfoo.dylib'
elif sys.platform.startswith('win'):
	libname = 'foo.dll'
if libname ==None:
	print("Unknow platform", sys.platform) 
	
else:
	lib = ctypes.CDLL(libname)

	lib.square.restype = ctypes.c_int
	lib.square.argtypes = [ctypes.c_int]


	def square(value):
		"""
		Parameters
		----------
		value: int

		Returns
		--------
		value square
		"""
		return lib.square(value)
