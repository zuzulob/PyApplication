import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello Prasad I am in Github Actions")

if __name__ == "__main__":
    unittest.main()
