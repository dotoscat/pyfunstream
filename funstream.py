# Copyright 2018 Oscat 'dotoscat' Triano

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from functools import partial

class _Function:
    """This helps to chain the return values and the functions."""
    def __init__(self, stream, function):
        self.stream = stream
        self.function = function

    def __ror__(self, value):
        if isinstance(value, Stream):
            value = value.value
        result = self.function(value)
        self.stream.value = result
        return result

    def __callable__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

class Stream:
    """
    The main class that allows to concatenate functions and their return values.
    """
    def __init__(self):
        self.value = None

    @property
    def last_value(self):
        return self.value

    def __getitem__(self, fun):
        if isinstance(fun, tuple):
            if not fun:
                raise RuntimeError("Do not pass an emtpy tuple.")
            function, *arguments = fun
            if not callable(function):
                raise RuntimeError("First element in the tuple must be a callable.")
            fun = partial(function, *arguments)
        if callable(fun):
            return _Function(self, fun)
        raise AttributeError("Function {} not found.", fun.__name__)