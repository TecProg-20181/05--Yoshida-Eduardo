import unittest
from diskspace import bytes_to_readable, subprocess_check_output, show_space_list
import subprocess


class TestDiskSpace(unittest.TestCase):

    def setUp(self):
        pass

    def test_bytes_to_readable(self):
        self.assertEquals('1.00Kb', bytes_to_readable(2))

    def test_subprocess_check_output(self):
        command = 'du'
        diskspace_output = subprocess_check_output(command)
        subprocess_output = subprocess.check_output(command)
        self.assertEquals(diskspace_output, subprocess_output)

    def test_show_space_list(self):
        self.assertIsNone(show_space_list())


if __name__ == '__main__':
    unittest.main()
