import ctypes
import numpy as np
import os

__all__ = ['square']

_path = os.path.dirname(__file__)
#lib = np.ctypeslib.load_library('foo')
lib = ctypes.cdll.LoadLibrary("libfoo.so")

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

