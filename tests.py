import unittest
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
