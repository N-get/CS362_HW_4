#Ethan Ng
import unittest
class list_test(unittest.TestCase):
    def test1(self):
        self.assertIsNot(0, 0, 'Number of list items is 0!') #Checks to see if the number of list items is 0.
    def test2(self):
        list_test = []
        self.assertTrue(list_test, 'List is empty!')   #checks if the list is emtpy or not.
    def test3(self):
        self.assertNotIn( " ", "5 4", 'Entry is more than one number!')  #Checks if there's a space in the numbers, if it is, it cannot be used as a list variable.
    def test4(self):
        list_a = [5.4, 5.2, 7.2]
        number_of_elements = len(list_a)
        total = float(0)
        count = int(0)
        self.assertTrue(list_a, 'List is emtpy!')
        self.assertIsNot(number_of_elements, 0, 'Number of list items is 0!')
        while count < number_of_elements:
            self.assertIsInstance(list_a[count], float, 'Entry is not of the correct type!')
            total = list_a[count] + total
            count = count + 1
        print(total/number_of_elements)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(list_test('test4'))
    suite.addTest(list_test('test1')) 
    suite.addTest(list_test('test2'))
    suite.addTest(list_test('test3')) 
    unittest.TextTestRunner().run(suite)
