import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    # name check
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

# id check

    def test_validate_id_with_empty(self):
        self.assertEqual(False, validate_id(""))

    def test_validate_id_with_13_digit(self):
        self.assertEqual(True, validate_id("1234567890123"))

    def test_validate_id_with_not_13_digit(self):
        self.assertEqual(False, validate_id("12345678901234"))

    def test_validate_id_with_alpha_digit(self):
        self.assertEqual(False, validate_id("12345678901nm"))

    def test_validate_id_with_alpha(self):
        self.assertEqual(False, validate_id("chutimachutim"))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
