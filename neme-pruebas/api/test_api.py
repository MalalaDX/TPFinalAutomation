import requests
import unittest
#Punto 4 Trabajo integrador Módulo 3 - QA

class Test_Poke(unittest.TestCase):

    def setUp(self):
        self.url = 'https://pokeapi.co/api/v2/'


    def test_caso1(self):
        r = requests.get(self.url+'berry/1')
        resp = r.json()
        self.assertEqual(resp ['size'], 20)
        self.assertEqual(resp ['soil_dryness'], 15)
        self.assertEqual(resp ['firmness'] ['name'], 'soft')

    def test_caso2(self):
        r = requests.get(self.url+'berry/2')
        resp = r.json()
        self.assertEqual(resp ['firmness'] ['name'], 'super-hard')
        self.assertGreater(resp ['size'], 20)
        self.assertEqual(resp ['soil_dryness'], 15)

    def test_caso3(self):
        r = requests.get(self.url+'pokemon/pikachu/')
        resp = r.json()
        self.assertGreater(resp ['base_experience'], 10)
        self.assertLess(resp ['base_experience'], 1000)
        self.assertEqual(resp ['types'] [0] ['type'] ['name'], 'electric' )

