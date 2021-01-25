import unittest

#list comprehension
def convert(number):
    result = "".join(["Pling" * (number % 3 == 0) +
                    "Plang" * (number % 5 == 0) +
                    "Plong" * (number % 7== 0)])

    return (result if result else str(number))


# def convert(number):
#     result = ""
#     if number % 3 == 0:
#         result += "Pling"
#     if number % 5 == 0:
#         result += "Plang"
#     if number % 7 == 0:
#         result += "Plong"
    
#     return result if result else str(number)


class TestRainDrops(unittest.TestCase):


    def test_1_returns_1(self):
        self.assertEqual(convert(1),"1")


    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling")
    
    
    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang")


    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong")


    def test_the_sound_for_6_is_pling_as_it_has_a_factor_3(self):
        self.assertEqual(convert(6), "Pling")


    def test_2_to_power_3_is_8(self):
        self.assertEqual(convert(2**3), "8")


    def test_the_sound_for_9_is_pling_as_it_has_a_factor_3(self):
        self.assertEqual(convert(9), "Pling")

    
    def test_the_sound_for_10_is_plang_as_it_has_a_factor_5(self):
        self.assertEqual(convert(10), "Plang")

    
    def test_the_sound_for_14_is_plong_as_it_has_a_factor_of_7(self):
        self.assertEqual(convert(14), "Plong")

    
    def test_the_sound_for_15_is_pling_plang_as_it_has_factors_3_and_5(self):
        self.assertEqual(convert(15), "PlingPlang")

    
    def test_the_sound_for_21_is_pling_plong_as_it_has_factors_3_and_7(self):
        self.assertEqual(convert(21), "PlingPlong")

    
    def test_the_sound_for_25_is_plang_as_it_has_a_factor_5(self):
        self.assertEqual(convert(25), "Plang")

    
    def test_the_sound_for_27_is_pling_as_it_has_a_factor_3(self):
        self.assertEqual(convert(27), "Pling")

    
    def test_the_sound_for_35_is_plang_plong_as_it_has_factors_5_and_7(self):
        self.assertEqual(convert(35), "PlangPlong")

    
    def test_the_sound_for_49_is_plong_as_it_has_a_factor_7(self):
        self.assertEqual(convert(49), "Plong")

    
    def test_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52")

    
    def test_the_sound_for_105_is_pling_plang_plong_as_it_has_factors_3_5_and_7(self):
        self.assertEqual(convert(105), "PlingPlangPlong")

    
    def test_the_sound_for_3125_is_plang_as_it_has_a_factor_5(self):
        self.assertEqual(convert(3125), "Plang")


if __name__ == '__main__':
    unittest.main()
    