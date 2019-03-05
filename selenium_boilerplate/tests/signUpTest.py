from tests.baseTest import BaseTest
import unittest


class SignUpTest(BaseTest, unittest.TestCase):

    def setUp(self):
        print("calling super setup...")
        super().setUp()

    def test_a(self):
        print("Running test")


if __name__ == "__main__":
    unittest.main()
