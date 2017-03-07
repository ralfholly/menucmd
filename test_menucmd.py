from unittest import TestCase

from menucmd import get_command_and_filelist, build_menu

# pylint:disable=C0103

class TestMenuCmd(TestCase):

    def test_setup(self):
        self.assertEqual(3, 1 + 2)

    def test_get_command_and_filelist_typical(self):
        args = "blah.py foo -a -b -- file1 file2".split()
        result = get_command_and_filelist(args)
        self.assertEqual(result[0], "foo -a -b".split())
        self.assertEqual(result[1], "file1 file2".split())

    def test_get_command_and_filelist_no_filelist(self):
        args = "blah.py foo -a -b --".split()
        result = get_command_and_filelist(args)
        self.assertEqual(result[0], "foo -a -b".split())
        self.assertEqual(result[1], [])

    def test_get_command_and_filelist_no_command(self):
        args = "blah.py -- file1 file2".split()
        result = get_command_and_filelist(args)
        self.assertEqual(result[0], [])
        self.assertEqual(result[1], "file1 file2".split())

    def test_get_command_and_filelist_no_separator(self):
        args = "blah.py file1 file2".split()
        result = get_command_and_filelist(args)
        self.assertEqual(None, result)


    def test_build_items_list(self):
        item_input = "one two three".split()
        items = [[item, False] for item in item_input]
        menu = build_menu(items)

        self.assertEqual(len(item_input), len(menu.split("\n")) - 1)

        # No visited item yet.
        self.assertNotRegex(menu, r"\*")

        # Visit second item.
        items[1][1] = True
        menu = build_menu(items)
        menu_items = menu.split("\n")

        # Second item now visited.
        self.assertNotRegex(menu_items[0], r"\*")
        self.assertRegex(menu_items[1], r"\*")
        self.assertNotRegex(menu_items[2], r"\*")

