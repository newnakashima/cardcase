import sys,os
sys.path.append(os.pardir)
sys.path.append(os.getcwd())
from sample import SampleClass
import unittest

class SampleClassTest(unittest.TestCase):
    def test_sum(self):
        s = SampleClass()
        self.assertEqual(s.sum(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
