import unittest
from functools import partial
from operator import add
import funstream

def sum2(a):
    return a + 2

def mul3(a):
    return a*3

class Test(unittest.TestCase):
    def test1_sum2(self):
        s = funstream.Stream()
        value = 2 | s[sum2] | s[mul3]
        self.assertEqual(value, 12, "Not equal to 12!")
        print(value)

    def test2_lambda(self):
        s = funstream.Stream()
        value = 2 | s[lambda n: n + 2] | s[lambda n: n*3]
        self.assertEqual(value, 12, "With lambda no equal to 12!")

    def test3_chain(self):
        class File:
            def __init__(self):
                value = 0

            def write(self, value):
                self.value = value
        f = File()
        s = funstream.Stream()

        value = 2 | s[str] | s[f.write] | s[partial(add, '2')]
        self.assertEqual(value, "22", "2 and 2 not 22!")
        self.assertEqual(f.value, "2", "2 is not written by dummy file")
