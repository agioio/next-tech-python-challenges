import unittest

def hello():
    return "Hello, World!"


class HelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello(),"Hello, World!")


if __name__ == '__main__':
    unittest.main()
    