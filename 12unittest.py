import unittest

def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
    def test_add_negative(self):
        self.assertEqual(add(-1, -2), -3)
    def test_add_float(self):
        self.assertEqual(add(1.5, 2.5), 4.0)
    def test_add_string(self):
        self.assertEqual(add('hello', 'world'), 'helloworld')
    def test_add_list(self):
        self.assertEqual(add([1, 2], [3, 4]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()

