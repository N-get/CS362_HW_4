#Ethan Ng
import unittest
class Cube(unittest.TestCase):
    def test1(self):
        self.assertTrue("", 'Entry is blank!') #Checks to see if the entry is blank, if no entry, volume cannot be calculated.
    def test2(self):
        self.assertIsInstance("asdf", float, 'Entry is not of the correct type!')   #checks the data type of the first entry, if not a float, you cannot calculate the value of the volume.
    def test3(self):
        self.assertLess(0, -4, 'Entry is a negative!')  #Checks the number against 0, if less, the cube cannot exist.
    def test4(self):
        self.assertLess(0, 5.0, 'Entry is a negative!')
        self.assertIsInstance(5.0, float, 'Entry is not of the correct type!')
        self.assertTrue(5.0, 'Entry is blank!')
        print("Volume for a cube with side length 5: ", 5.0 * 5.0 * 5.0)
        


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Cube('test4'))
    suite.addTest(Cube('test1')) 
    suite.addTest(Cube('test2'))
    suite.addTest(Cube('test3')) 
    unittest.TextTestRunner().run(suite)
