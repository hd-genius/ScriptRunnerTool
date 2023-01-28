import unittest
from unittest import TestCase
from parameterized import parameterized

class TestFindScriptWithName(TestCase):
    @parameterized.expand([
        ('--not-command'),
        ('--garbage'),
        ('--expected-fail')
    ])
    def test_unrecognized_command_throws_error(self, command):
        pass

    def test_list_scripts(self):
        pass

    def test_print_help(self):
        pass

    def test_run_script(self):
        pass

if __name__ == '__main__':
    unittest.main()