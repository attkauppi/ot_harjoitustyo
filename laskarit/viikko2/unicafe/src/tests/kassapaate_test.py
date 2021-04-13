import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.alkusaldo = 100000
    
    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_kassapaate_luotu_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassapaate_luotu_edullisten_lukumaara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kassapaate_luotu_maukkaat_lukumaara_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_kateisosto_kassassa(self):
        rahaa_kassassa_lopuksi = self.kassapaate.kassassa_rahaa + 240
        self.kassapaate.syo_edullisesti_kateisella(240)
        print(self.kassapaate.kassassa_rahaa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa_kassassa_lopuksi)
    
    def test_edullisen_kateisosto_yli_240(self):
        kassassa_rahaa = self.kassapaate.kassassa_rahaa + 240
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, kassassa_rahaa)
    
    def test_edullisen_kateisosto_rahat_takaisin_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        takaisin = self.kassapaate.syo_edullisesti_kateisella(250)
        print("Takaisin: ", takaisin)
        self.assertEqual(takaisin, 10)
    
    def test_edullisen_kateisosto_raha_ei_riita(self):
        kassassa_rahaa = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, kassassa_rahaa)
    
    def test_edullisen_kateisosto_lisaa_edullisia(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukkaan_kateisosto_lisaa_kassaa(self):
        rahaa = self.kassapaate.kassassa_rahaa + 400
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, rahaa)
    
    def test_maukkaan_kateisosto_lisaa_maukkaita(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaan_kateisosto_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(240)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaan_kateisosto_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(vaihtoraha, 10)
    
    def test_edullisen_korttiosto_veloitetaan_oikein(self):
        kortti = Maksukortti(240)
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
    
    def test_edullisen_korttiosto_kasvattaa_myytyja(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    
    def test_edullisen_korttiostoa_ei_hyvaksyta_kun_rahaton(self):
        kortti = Maksukortti(210)
        hyvaksyi = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(hyvaksyi, False)
    
    def test_maukkaan_korttiosto_veloitetaan_oikein(self):
        kortti = Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.alkusaldo)
    
    def test_maukkaan_korttiosto_kasvattaa_myytyja_maukkaita(self):
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_korttiosto_hylataan_kun_rahaton(self):
        kortti = Maksukortti(390)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.alkusaldo)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_rahan_lataus_lisaa_saldoa(self):
        kortti = Maksukortti(0)
        lisattava_summa = 10
        self.kassapaate.lataa_rahaa_kortille(kortti, lisattava_summa)
        self.assertEqual(self.kassapaate.kassassa_rahaa-10, self.alkusaldo)
        self.assertEqual(kortti.saldo, lisattava_summa)
    
    def test_rahan_lataus_ei_onnistu_negatiivisella(self):
        kortti = Maksukortti(0)
        lisattava_summa = -10
        self.kassapaate.lataa_rahaa_kortille(kortti, lisattava_summa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.alkusaldo)
        self.assertEqual(kortti.saldo, 0)


        
    
