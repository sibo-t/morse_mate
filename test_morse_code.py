import unittest
from funtranslations_api.morse_code import *

class TestMorseCode(unittest.TestCase):

    def test_text_to_morsecode(self):
        translate = eng_to_morse("Sibonelo says hi")
        self.assertEqual(translate, "... .. -... --- -. . .-.. ---     ... .- -.-- ...     .... .. ")


if __name__ == '__main__':
    unittest.main()

