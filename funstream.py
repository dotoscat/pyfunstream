class _Function:
    """This helps to chain the return values and the functions."""
    def __init__(self, stream, function):
        self.stream = stream
        self.function = function

    def __ror__(self, value):
        result = self.function(value)
        return result

    def __callable__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

class Stream:
    """
    The main class that allows to concatenate functions and its return values.
    """
    def __getattribute__(self, name):
        fun = (getattr(__builtins__, name, None)
               or locals().get(name)
               or globals().get(name))
        if callable(fun):
            return _Function(self, fun)
        raise AttributeError("Function not found.")
