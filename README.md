pyfunstream
===========

This module provide a simple mechanism to chain functions, only using
the operator overloading and a pair of classes

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
```

License
=======

MIT
