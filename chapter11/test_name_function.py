import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """#Tests for name_function in different perspective"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' works?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis', 'joplin')

unittest.main()

