import config
import unittest
from kyototycoon import KyotoTycoon

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.kt_handle = KyotoTycoon()
        self.kt_handle.open('tiger')

    def test_set(self):
        self.assertTrue(self.kt_handle.clear())
        error = self.kt_handle.error()

        value = {
            "hello": "world"
        }
        ret = self.kt_handle.play_script('echo',value)
        self.assertEqual(ret, value)

if __name__ == '__main__':
    unittest.main()
