import unittest
from api_status_ckecker import check_status

class TestApiStatusChecker(unittest.TestCase):

    def test_check_status(self):
        status = check_status('https://jsonplaceholder.typicode.com/posts')
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()
