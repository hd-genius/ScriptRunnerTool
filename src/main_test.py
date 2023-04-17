import unittest
from unittest import TestCase
from parameterized import parameterized
from src.main import main, UnrecognizedCommandError


class TestFindScriptWithName(TestCase):
    @parameterized.expand([
        ('--not-command'),
        ('--garbage'),
        ('--expected-fail')
    ])
    def test_unrecognized_command(self, command):
        self.assertRaises(UnrecognizedCommandError, main)

    def test_list_scripts(self):
        pass

    def test_print_help(self):
        pass

    def test_run_script(self):
        pass


if __name__ == '__main__':
    unittest.main()
