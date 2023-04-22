import unittest
from funtranslations_api.morse_code import *

class TestMorseCode(unittest.TestCase):

    def test_text_to_morsecode(self):
        translate = translate_text_to_morse("Sibonelo says hi")
        self.assertEqual(translate, "... .. -... --- -. . .-.. ---     ... .- -.-- ...     .... .. ")

    def test_morse_code_to_text(self):
        translate = translate_morse_to_text("... .. -... --- -. . .-.. ---     ... .- -.-- ...     .... .. ")
        self.assertEqual(translate,"Sibonelo says hi")



if __name__ == '__main__':
    unittest.main()

