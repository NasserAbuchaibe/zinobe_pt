""" test """
import unittest
from pandas.core.frame import DataFrame

from aux_function.data_countries import data_countries
from aux_function.to_data_frame import to_data_frame
from aux_function.get_region import get_region


class TestApp(unittest.TestCase):
    """ Test """

    def test_get_region(self):
        """ testeando get_region que obtiene las regiones exixtentesS
        """
        region_list = get_region()

        self.assertEqual(type(region_list), list)
        self.assertTrue(region_list != [])

    def test_data_countries(self):
        """testeando data_countries que consulta endpoint
            y filtra la informacion de los paises
        """
        countrie_dict = data_countries('Africa')

        self.assertEqual(type(countrie_dict), dict)
        self.assertTrue(countrie_dict != {})

    def test_to_data_frame(self,):
        """test to_data_frame que genera los data frame
            con los resgistros de los tiempos de ejecucion
            y la informacion de los paises
        """
        region_list = get_region()
        data_countries_list = [data_countries(
            region) for region in region_list]
        data_f, df_times = to_data_frame(data_countries_list)

        self.assertEqual(type(data_f), DataFrame)
        self.assertEqual(type(df_times), DataFrame)
        self.assertTrue(len(data_f) != 0)
        self.assertTrue(len(df_times) != 0)
