import unittest
import processor

class ProcessData(unittest.TestCase):
    def test_process_data(self):
        self.assertTrue(processor.process_data('donaciones.csv'))

if __name__ == '__main__':
    unittest.main()