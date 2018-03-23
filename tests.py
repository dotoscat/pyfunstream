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

    def test2_lambda(self):
        s = funstream.Stream()
        value = 2 | s[lambda n: n + 2] | s[lambda n: n*3]
        self.assertEqual(value, 12, "With lambda no equal to 12!")

    def test3_chain(self):
        s = funstream.Stream()

        value = 2 | s[str] | s[partial(add, '2')]
        self.assertEqual(value, "22", "2 and 2 not 22!")

    def test4_last_value(self):
        s = funstream.Stream()
        1 | s[lambda n: n + 1]
        s | s[lambda n: n + 2]
        value = s.last_value | s[str] 
        self.assertEqual(value, s.last_value, "Last values, str & str, are not equal.")
        self.assertEqual(s.last_value, "4", "Last values is not equal to 4!")
