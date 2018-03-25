pyfunstream
===========

This module provide a simple mechanism to chain functions, only using
the operator overloading and a pair of classes


Features
========

- Functional programming with the pipe | operator.
- The stream stores the returned value by the last function.
- Partials.

Example of use
==============

```
    import funstream

    def sum2(a):
        return a + 2

    def mul3(a):
        return a*3

    fns = funstream.Stream()

    2 | fns[sum2] | fns[mul3] | fns[print]

    # The stream keeps the last value returned by the last function call

    fns = funstream.Stream() # Throw away the old stream

    2 | fns[lambda n: n*3]
    fns | fns[lambda n: n + 2]
    # fns.last_value == 8 

```

License
=======

MIT
