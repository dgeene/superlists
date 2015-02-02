"""
A functional test that captures the key points of the user story
"""
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(selft):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Dave visits the app homepage
        self.browser.get('http://localhost:8000')

        # he notices the page title and header mention to-do lists
        self.assertIn('To-Do', self. broswer.title)
        self.fail('Finish the test!')



# he is invited to enter a to-do item right away

# He types "Buy peacock feathers" into a text box

# When he hits enter, the page updates, and now the page lists
# 1: Buy peacock feathers

# There is still a text box inviting him to enter another to do item
# he enters "Use peacock feathers to make a lure"

# The page updates again showing both items

#The site will generate a unique url to come back to the todo list later

# Visiting the url - the todo list is still there

#exit

if __name__ == '__main__':
    unittest.main(warnings='ignore')
