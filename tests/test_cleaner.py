import os
import sys
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from html_cleaner.cleaner import clean_tags


class TestCleaner(unittest.TestCase):
    def test_clean_tags_returns_none_if_none_is_passed(self):
        input_text = None
        result = clean_tags(input_text)
        self.assertIsNone(result)

    def test_clean_tags_returns_empty_string_if_empty_string_is_passed(self):
        input_text = ''
        result = clean_tags(input_text)
        self.assertEqual(result, input_text)

    def test_clean_tags_returns_input_text_if_text_without_tags_is_passed(
        self):
        input_text = 'This is a text without HTML tags.'
        result = clean_tags(input_text)
        self.assertEqual(result, input_text)

    def test_clean_tags_returns_input_text_without_tags_if_text_with_tags_is_passed(
        self):
        input_text = '<a>This is a text</a><br></br> <b>with</b> HTML tags.'
        expected_result = 'This is a text with HTML tags.'
        result = clean_tags(input_text)
        self.assertEqual(result, expected_result)

    def test_clean_tags_returns_input_text_without_tags_without_removing_math_signs(
        self):
        input_text = '<b>This is a math expression</b>: a^2 + b^2 < c^2'
        expected_result = 'This is a math expression: a^2 + b^2 < c^2'
        result = clean_tags(input_text)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
