import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_ota_rahaa_toimii_oikein(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), False)
    
    def test_lataa_rahaa_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, (10+100))
    
    def test_saldo_ei_muutu_jollei_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_saldo_muuttuu_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1)
        self.assertEqual(self.maksukortti.saldo, 9)
    
    def test_ota_rahaa_palauttaa_true_kun_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(3), True)