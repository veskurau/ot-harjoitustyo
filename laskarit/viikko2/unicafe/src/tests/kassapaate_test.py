import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luodun_kassapaatteen_rahamaara_ja_lounasmäärä_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_toimii_kun_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(vaihtoraha, 500-240)

    def test_syo_maukkaasti_kateisella_toimii_kun_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(vaihtoraha, 500-400)

    def test_syo_edullisesti_maukkaasti_kateisella_toimii_kun_maksu_ei_riittava(self):
        vaihtoraha_edullinen = self.kassapaate.syo_edullisesti_kateisella(100)
        vaihtoraha_maukas = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual((self.kassapaate.edulliset, self.kassapaate.maukkaat), (0,0))
        self.assertEqual((vaihtoraha_edullinen, vaihtoraha_maukas), (100,100))

    def test_syo_edullisesti_kortilla_toimii_kun_rahaa_riittavasti(self):
        kortti = Maksukortti(1000)
        totuusarvo = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(kortti.saldo, 1000-240)
        self.assertEqual(totuusarvo, True)

    def test_syo_maukkaasti_kortilla_toimii_kun_rahaa_riittavasti(self):
        kortti = Maksukortti(1000)
        totuusarvo = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(kortti.saldo, 1000-400)
        self.assertEqual(totuusarvo, True) 

    def test_syo_edullisesti_maukkaasti_kortilla_toimii_kun_rahaa_ei_riittavasti(self):
        kortti = Maksukortti(100)
        totuusarvo1 = self.kassapaate.syo_edullisesti_kortilla(kortti)
        totuusarvo2 = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual((self.kassapaate.edulliset,self.kassapaate.maukkaat), (0,0))
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual((totuusarvo1, totuusarvo2), (False, False))

    def test_lataa_rahaa_kortille_toimii(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+500)

    def test_lataa_rahaa_kortille_toimii_kun_annetaan_negatiivinen_summa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -500)
        self.assertEqual(kortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
