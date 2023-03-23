import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")

    def test_rahan_ottaminen_toimii_kun_tarpeeksi_rahaa(self):
        totuus = self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
        self.assertEqual(totuus, True)

    def test_rahan_ottaminen_toimii_kun_ei_tarpeeksi_rahaa(self):
        totuus = self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(totuus, False)

    # def test_rahan_ottaminen_palauttaa_oikean_totuusarvon(self):
    #     self.maksukortti.ota_rahaa(1100)
    #     self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
