from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_page_load_timeout(30)
    

    def tearDown(self):
        self.browser.quite()

    
    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get("http://127.0.0.1:8000/")

        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
