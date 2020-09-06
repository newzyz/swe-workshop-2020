import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("วิทวัส"))

    def test_validate_name_with_valid_input_language(self):
        self.assertEqual(True, validate_name("Wittawat"))

    def test_validate_name_with_invalid_input_contain_string_digit(self):
        self.assertEqual(False, validate_name("Wittawat50"))

    def test_validate_name_with_invalid_input_contain_digit(self):
        self.assertEqual(False, validate_name("100054545"))

    def test_validate_name_with_invalid_input_contain_special(self):
        self.assertEqual(False, validate_name("!#@///+-="))

    def test_validate_name_with_invalid_input_contain_string_special(self):
        self.assertEqual(False, validate_name("*#Wittawat"))

    def test_validate_name_with_invalid_input_contain_number_special(self):
        self.assertEqual(False, validate_name("*#5000"))

    def test_validate_name_with_invalid_input_contain_string_number_special(self):
        self.assertEqual(False, validate_name("Wittawat*#5000"))

    def test_validate_name_with_empty(self):
        self.assertEqual(False, validate_name(""))

    def test_validate_name_with_space(self):
        self.assertEqual(False, validate_name("chu tima"))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
