import unittest

from translator import english_to_french, french_to_english


class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Programmer'), 'Programmeur')
        self.assertIsNone(english_to_french(None))


class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Programmeur'), 'Programmer')
        self.assertIsNone(french_to_english(None))


unittest.main()
