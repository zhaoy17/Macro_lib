from macro_lib import assist
import unittest

class Test_assist(unittest.TestCase):

    def testIntroduce(self):
        self.assertTrue(assist.introduct() == "A python library aim to provide computational tools \
            for Macroeconomics Models. Currently, we are still in the \
            planning phase.")