import unittest
class firstname_lastname(unittest.TestCase):
    def test1(self):
        self.assertNotEqual("Firstname", "Firstname", 'Entries are equal!') #Checks to see if the entries are equal, if so, the input is incorrect.
    def test2(self):
        self.assertIsInstance(5.4, str, 'Entry is not of the correct type!')   #checks the data type of the first entry, if not a string, you cannot create a full name.
        self.assertIsInstance(5.6, str, 'Entry is not of the correct type!')
    def test3(self):
        self.assertNotIn( " ", "Firstname Lastname", 'Entry is more than one word!')  #Checks if there's a space in the first name, if there is, it cannot be a part of the first or last name.
    def test4(self):
        Firstname = str(input("Input your first name!"))
        Lastname = str(input("Input your last name!"))
        self.assertNotEqual(Firstname, Lastname, 'Entries are the same!')
        self.assertIsInstance(Firstname, str, 'Entry is not of the correct type!')  
        self.assertIsInstance(Lastname, str, 'Entry is not of the correct type!')
        self.assertNotIn(" ", Firstname, 'Entry is more than one word!')
        self.assertNotIn(" ", Lastname, 'Entry is more than one word!')
        print(Firstname, " ", Lastname)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(firstname_lastname('test4'))
    suite.addTest(firstname_lastname('test1')) 
    suite.addTest(firstname_lastname('test2'))
    suite.addTest(firstname_lastname('test3')) 
    unittest.TextTestRunner().run(suite)
