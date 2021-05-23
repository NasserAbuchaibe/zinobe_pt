import unittest

import pep8
from pandas.core.frame import DataFrame

from aux_function.data_countries import data_countries
from aux_function.get_region import get_region
from aux_function.to_data_frame import to_data_frame


class Test_app(unittest.TestCase):

    def test_get_region(self):
        region_list = get_region()

        self.assertEqual(type(region_list), list)
        self.assertTrue(region_list != [])

    def test_data_countries(self):
        countrie_dict = data_countries('Africa')

        self.assertEqual(type(countrie_dict), dict)
        self.assertTrue(countrie_dict != {})

    def test_to_data_frame(self):
        region_list = get_region()
        data_countries_list = [data_countries(
            region) for region in region_list]
        df, df_times = to_data_frame(data_countries_list)

        self.assertEqual(type(df), DataFrame)
        self.assertEqual(type(df_times), DataFrame)
        self.assertTrue(len(df) != 0)
        self.assertTrue(len(df_times) != 0)
