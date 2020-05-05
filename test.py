import unittest
import start

class TestFactorial(unittest.TestCase):

    def test_c_to_tb(self):
        source_unit = 'c'
        source_val = 11.1
        convert_to = 'tb'
        answer = 222.2
       
        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, 177.2)

# for i in [0, 255.37, 273.15, 373.15, 473.15]:
#         for unit in start.MULTIPLIERS_FROM_STD.values():
#             print("%.2f K is %.2f %s" % (i, unit.from_kelvins(i), unit.name))
#         print()


if __name__ == '__main__':
    unittest.main()
