README
======

## Summary
This little Python3 CLI tool displays a menu that allows the user to selectively execute a command on a given file list.

## Usage
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

Entering `2` will execute `rm -f /tmp/file2` and re-display the menu with an additional asterisk, which indicates that the second item has been processed:

```
   1   /tmp/file1
   2 * /tmp/file2
   3   /tmp/file3

rm -f ?
```

The marker(s) can be cleared by entering `0`; Pressing CTRL-C or CTRL-D aborts the menu.

## My Most Important Use-Case
I mainly use this tool to review my changes in my local Git repository. I have a little wrapper script called `gitreview` that allows me to conveniently diff my modifications:

```
~> cat ~/bin/gitreview
#!/bin/bash
menucmd.py git difftool -y "$@" -- $(git status --porcelain | cut -c 4-)

# Show changes with `meld` diff tool:
~> gitreview -t meld
```
The asterisk helps me keep track of which changes I still need to review.
