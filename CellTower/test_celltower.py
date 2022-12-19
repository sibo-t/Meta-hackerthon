import unittest
import celltower

class MyTestCase(unittest.TestCase):

    def test_finding_centres_n_outages(self):
        f = open("data_centers_sample.txt", "r")
        a = f.read()
        f.close()
        data_centre_n_poss_outages = celltower.find_no_centres_n_outage(a)
        self.assertEqual((2,2), data_centre_n_poss_outages)

    def test_finding_more_centres_n_outages(self):
        f = open("data_centers_more_sample.txt", "r")
        a = f.read()
        f.close()
        data_centre_n_poss_outages = celltower.find_no_centres_n_outage(a)
        self.assertEqual((2,3), data_centre_n_poss_outages)

########################################################################################################
#               Retrieve coordinates of data_centre  
#################################################################
    def test_create_list_of_data_centres_sample(self):
        f = open("data_centers_sample.txt", "r")
        a = f.read()
        f.close()
        data_centre_n_poss_outages = celltower.find_no_centres_n_outage(a)
        data_centre_lists = celltower.list_of_data_centres(data_centre_n_poss_outages[0],a)
        self.assertEqual([(1,5),(3,7)], data_centre_lists)

    def test_create_list_of_data_centres_sample_more(self):
        f = open("data_centers_more_sample.txt", "r")
        a = f.read()
        f.close()
        data_centre_n_poss_outages = celltower.find_no_centres_n_outage(a)
        data_centre_lists = celltower.list_of_data_centres(data_centre_n_poss_outages[0],a)
        self.assertEqual([(5,5),(3,7)], data_centre_lists)

    def test_create_list_of_data_centres_sample_more_more(self):
        f = open("data_centers_more_more_sample.txt", "r")
        a = f.read()
        f.close()
        data_centre_n_poss_outages = celltower.find_no_centres_n_outage(a)
        data_centre_lists = celltower.list_of_data_centres(data_centre_n_poss_outages[0],a)
        self.assertEqual([(5,5),(3,7),(4,1)], data_centre_lists)

    ########################################################################
    #              Retrieve outage coordinates 
    ########################################################################
    def test_create_list_of_possible_outages_sample(self):
        f = open("data_centers_sample.txt", "r")
        a = f.read()
        f.close()
        data_centre_n_poss_outages = celltower.find_no_centres_n_outage(a)
        all_poss_outages = celltower.list_of_poss_outages(data_centre_n_poss_outages[1],a)
        self.assertEqual([(2,5,6),(2,3,4)], all_poss_outages)

    def test_create_list_of_possible_outages_sample_more(self):
        f = open("data_centers_more_sample.txt", "r")
        a = f.read()
        f.close()
        data_centre_n_poss_outages = celltower.find_no_centres_n_outage(a)
        all_poss_outages = celltower.list_of_poss_outages(data_centre_n_poss_outages[1],a)
        self.assertEqual([(2,6,3),(2,6,4),(2,2,1)], all_poss_outages)

    def test_create_list_of_possible_outages_sample_more_more(self):
        f = open("data_centers_more_more_sample.txt", "r")
        a = f.read()
        f.close()
        data_centre_n_poss_outages = celltower.find_no_centres_n_outage(a)
        all_poss_outages = celltower.list_of_poss_outages(data_centre_n_poss_outages[1],a)
        self.assertEqual([(2,6,3),(2,6,4),(2,2,1),(1,1,1)], all_poss_outages)

    ################################################################################
    #             Compare all_possible_outages to all_data_centres
    ################################################################################
    def test_compare_an_outage_to_data_centre(self):
        ON_OFF = celltower.compare_centres_t_outages((1,5),(2,5,6))
        self.assertEqual(0, ON_OFF)

    def test_compare_an_outage_to_data_centre_more(self):
        ON_OFF = celltower.compare_centres_t_outages((3,7),(2,5,6))
        self.assertEqual(1, ON_OFF)

    def test_compare_an_outage_to_data_centre_more_more(self):
        ON_OFF = celltower.compare_centres_t_outages((3000,77),(20,5,600))
        self.assertEqual(0, ON_OFF)

    def test_compare_an_outage_to_data_centre_more_more(self):
        ON_OFF = celltower.compare_centres_t_outages((3000,77),(20,5,6000))
        self.assertEqual(1, ON_OFF)

    def test_compare_an_outage_to_data_centre_more_more_more(self):
        ON_OFF = celltower.compare_centres_t_outages((30500,770),(20,50,60000))
        self.assertEqual(1, ON_OFF)

if __name__ == "__main__":
    unittest.main()