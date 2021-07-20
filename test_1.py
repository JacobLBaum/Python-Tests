import testProgram

import unittest

class testing(unittest.TestCase):
 
    def test_oneWord(self):
        a = testProgram.testProgram('start')
        a.clear()
        a.addWord('Test')
        self.assertEqual(a.longestWord, 'Test', 'Should be Test')
        self.assertEqual(a.lenLongestWord, 4, 'Should be 4')

    def test_multipleWords(self):
        a = testProgram.testProgram('start')
        a.addWord('coding')
        a.addWord('call')
        a.addWord('farther')
        a.addWord('whip')
        self.assertEqual(a.longestWord, 'farther', 'Should be farther')
        self.assertEqual(a.lenLongestWord, 7, 'Should be 7')

    def test_clear(self):
        a = testProgram.testProgram('start')
        a.clear()
        self.assertFalse(a.words)
        self.assertEqual(a.longestWord, '', 'Should be none')
        self.assertEqual(a.lenLongestWord, 0, 'Should be 0')

    def test_addInt(self):
        a = testProgram.testProgram('start')
        with self.assertRaises(TypeError):
            a.addWord(5)

    def test_addInt(self):
        a = testProgram.testProgram('start')
        with self.assertRaises(TypeError):
            a.addWord([1, 2, 3])

    def test_addNone(self):
        a = testProgram.testProgram('start')
        with self.assertRaises(TypeError):
            a.addWord()


if __name__ == '__main__':
    unittest.main()