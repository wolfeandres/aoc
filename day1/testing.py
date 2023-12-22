import unittest
from day1p2 import calibrateValues

class AOCTesting(unittest.TestCase):
    def test_calibration(self):
        self.assertEqual(calibrateValues("testing/test.txt"), 281)
        self.assertEqual(calibrateValues("testing/test1.txt"), 543)
        self.assertEqual(calibrateValues("testing/test2.txt"), 558)
        self.assertEqual(calibrateValues("testing/test3.txt"), 561)
        self.assertEqual(calibrateValues("testing/test4.txt"), 546)
        self.assertEqual(calibrateValues("testing/test5.txt"), 762)
        self.assertEqual(calibrateValues("testing/test6.txt"), 708)
        self.assertEqual(calibrateValues("testing/test7.txt"), 495)
        self.assertEqual(calibrateValues("testing/test8.txt"), 495)
        self.assertEqual(calibrateValues("testing/test9.txt"), 495)
        self.assertEqual(calibrateValues("testing/final.txt"), 124)


if __name__ == '__main__':
    unittest.main(verbosity=2)