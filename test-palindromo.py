
import unittest
import main
from main import palindromo

#UNITTEST
class PalindromoUnittest(unittest.TestCase):

    def test_hola(self):
        self.assertEqual(palindromo('hola'),False)

    def test_ana(self):
        self.assertEqual(palindromo('ana'),True)
    
    def test_neuquen(self):
        self.assertEqual(palindromo('neuquen'),True)
    
    def test_reconocer(self):
        self.assertEqual(palindromo('reconocer'),True)

    def test_auto(self):
        self.assertEqual(palindromo('auto'),False)

if __name__=='__main__':
    unittest.main()
