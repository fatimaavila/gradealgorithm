import unittest
from notas import verificarnota

class TestNotas(unittest.TestCase):
  def test_area(self):
    #Test areas
    self.assertEqual(verificarnota(78), "O")
    self.assertEqual(verificarnota(61), "A")
    self.assertEqual(verificarnota(53), "B")
    self.assertEqual(verificarnota(46), "C")
    self.assertEqual(verificarnota(13), "D")
    self.assertEqual(verificarnota(75.1), "O")
    self.assertEqual(verificarnota(-9), "Inválida")

  def test_types(self):
    self.assertRaises(TypeError, verificarnota, "nota")
    self.assertRaises(TypeError, verificarnota, "2j")

    