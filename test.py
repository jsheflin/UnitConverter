import unittest
import start

class TestFactorial(unittest.TestCase):


    def test_all_temp(self):
        temp = start.MULTIPLIERS_TO_STD['temp'].keys()
        source_val = 111.1
        answer = 232
        for tunit in temp:
            for to_temp in temp:
                if (to_temp != tunit):
                    print ('Convert From ' + tunit +' to ' + to_temp  )
        
       
    def test_all_volume(self):
        volume = start.MULTIPLIERS_TO_STD['volume'].keys()
        source_val = 111.1
        answer = 0.064
        for tunit in volume:
            for to_volume in volume:
                if (to_volume != tunit):
                    print ('Convert From ' +  tunit +' to ' + to_volume )

    def test_c_to_tb_incorrect(self):
        print(self._testMethodName)
        source_unit = 'c'
        source_val = 11.1
        convert_to = 'tb'
        answer = 222.2
       
        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, answer)

    def test_c_to_tb_correct(self):
        print(self._testMethodName)
        source_unit = 'c'
        source_val = 11.1
        convert_to = 'tb'
        answer = 177.6

        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, answer)

    def test_c_to_g_incorrect(self):
        print(self._testMethodName)
        source_unit = 'c'
        source_val = 11.1
        convert_to = 'g'
        answer = 222.2
       
        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, 177.6)

    def test_c_to_g_correct(self):
        print(self._testMethodName)
        source_unit = 'c'
        source_val = 11.1
        convert_to = 'g'
        answer = .7

        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, answer)

    def test_c_to_l_incorrect(self):
        print(self._testMethodName)
        source_unit = 'c'
        source_val = 1
        convert_to = 'l'
        answer = 0.236
       
        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, 177.6)

    def test_c_to_l_correct(self):
        print(self._testMethodName)
        source_unit = 'c'
        source_val = 11.1
        convert_to = 'l'
        answer = 2.6

        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, answer)
    
    def test_c_to_cf_incorrect(self):
        print(self._testMethodName)
        source_unit = 'c'
        source_val = 11.1
        convert_to = 'cf'
        answer = 12.6
       
        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, answer)

    def test_c_to_cf_correct(self):
        print(self._testMethodName)
        source_unit = 'c'
        source_val = 1
        convert_to = 'cf'
        answer = 0.0

        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, answer)
    
    def test_c_to_ci_incorrect(self):
        print(self._testMethodName)
        source_unit = 'c'
        source_val = 11.1
        convert_to = 'ci'
        answer = 222.2
       
        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, answer)

    def test_c_to_ci_correct(self):
        print(self._testMethodName)
        source_unit = 'c'
        source_val = 11.1
        convert_to = 'ci'
        answer = 160.2

        res = start.convert(source_unit, source_val, convert_to,answer)
        self.assertEqual(res, answer)


if __name__ == '__main__':
    unittest.main()
