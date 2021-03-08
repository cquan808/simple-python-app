import unittest
import unitConverter


class TestMain(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def test_kg_to_lbs(self):
        """
        Test that kg is converted to lbs
        """
        result = unitConverter.kg_to_lbs(145)
        self.assertEqual(result, 65.25)

    def test_lbs_to_kg(self):
        """
        Test that lbs is converted to kg
        """
        result = unitConverter.kg_to_lbs(90)
        self.assertEqual(result, 200.0)