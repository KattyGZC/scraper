import unittest
import processor

class Scraping(unittest.TestCase):
    def test_start_scraping(self):
        self.assertTrue(True, processor.start_scraping('dataset', 'economia y finanzas', 'csv', 'donaciones'))

if __name__ == '__main__':
    unittest.main()