import subprocess
import sys
import unittest

class CliTest(unittest.TestCase):
    def test_adds_via_cli(self):
        completed = subprocess.run([sys.executable, 'p6_python_cli.py', '2', '3'],
                                   capture_output=True, text=True, check=True)
        self.assertEqual(completed.stdout.strip(), '5')
    def test_zero(self):
        completed = subprocess.run([sys.executable, 'p6_python_cli.py', '2', '0'],
                                   capture_output=True, text=True, check=True)
        self.assertEqual(completed.stdout.strip(), '2')
