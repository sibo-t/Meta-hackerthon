import unittest
import rollercoaster

class MyTestCase(unittest.TestCase):

    def test_reading_txt_n_convert_to_int_list(self):
        scary_values = rollercoaster.convert_txt_input_to_int_list("rollercoasters_medium_sample_input.txt")
        self.assertEqual([1,2,1,3], scary_values)

    def test_reading_txt_n_convert_to_int_list_2(self):
        scary_values = rollercoaster.convert_txt_input_to_int_list("rollercoasters_medium_sample_input2.txt")
        self.assertEqual([1,2,1,2], scary_values)

##########################################################

    def test_comparing_first_two_nums(self):
        list_of_fun_rides = rollercoaster.compare_first_two_nums([1,2,1,3])
        self.assertEqual([20,20], list_of_fun_rides)       

    def test_comparing_first_two_nums2(self):
        list_of_fun_rides = rollercoaster.compare_first_two_nums([1,2,1,3])
        self.assertEqual([20,20], list_of_fun_rides)  

    def test_comparing_first_two_nums3(self):
        list_of_fun_rides = rollercoaster.compare_first_two_nums([3,2,1,3])
        self.assertEqual([10,10,20], list_of_fun_rides)


if __name__ == "__main__":
    unittest.main()