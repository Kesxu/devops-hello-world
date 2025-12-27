import unittest 
class TestApp(unittest.TestCase):
    def test_math(self):
        #A simple test to prove the robot works
        self.assertEqual(1+1,2)
        print("Math works! 1 + 1 = 2")

if __name__ == '__main__':
    unittest.main()
    

    