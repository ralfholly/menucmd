README
======

This little Python3 CLI tool displays a menu that allows the user to selectively execute a command on a given file list.

Entering this command

```
menucmd.py rm -f -- /tmp/file1 /tmp/file2 /tmp/file3
```

Creates the following menu
```
   1   /tmp/file1
   2   /tmp/file2
   3   /tmp/file3

rm -f ?
```

Entering `2` will execute `rm -f /tmp/file2` and re-display the menu with an additional asterisk, which indicates that the first item has been processed:

```
   1   /tmp/file1
   2 * /tmp/file2
   3   /tmp/file3

rm -f ?
```

The marker(s) can be cleared by entering `0`; CTRL-C aborts the menu.

