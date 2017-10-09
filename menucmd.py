#!/usr/bin/env python3

# menucmd -- Provides a user interface that allows the user to selectively
# execute a command on a given file list.

# MIT License
#
# Copyright (c) 2017 Ralf Holly.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import subprocess
import signal


def handle_sigint(signum, sigframe):
    signum = signum
    sigframe = sigframe
    print()
    sys.exit(0)


def build_menu(items):
    pos = 1
    menu = ""

    for item, visited in items:
        visited_mark = "*" if visited else " "
        menu += "%4d %s %s\n" % (pos, visited_mark, item)
        pos += 1

    return menu


def show_menu(items, cmd):
    selection = 0
    items_printed = False

    while True:
        if not items_printed:
            print()
            item_list = build_menu(items)
            print(item_list)
            items_printed = True
        cmd_str = " ".join(cmd)
        print(cmd_str + " ", end="", flush=True)
        try:
            # pylint:disable=W0141
            selection = int(input())

        except ValueError:
            items_printed = False
            continue

        except EOFError:
            assert False
            print()
            break

        if 1 <= selection <= len(items):
            items[selection - 1][1] = True
            call = cmd + [items[selection - 1][0]]
            _ = subprocess.Popen(call)

        elif selection == 0:
            for i in range(0, len(items)):
                items[i][1] = False


def get_command_and_filelist(args):
    result = None

    # Skip first argument (program name).
    args = args[1:]
    for i, arg in enumerate(args):
        if arg == "--":
            result = [args[:i], args[i + 1:]]
            break

    return result


def main(args):
    signal.signal(signal.SIGINT, handle_sigint)

    result = get_command_and_filelist(args)

    if result is None or result[0] is None or result[1] is None:
        print("Usage: %s <cmd> <cmd-arg>... -- <file>..." % (args[0]))
        sys.exit(1)

    items = [[item, False] for item in result[1]]
    cmd = result[0]

    # Do nothing if no files given.
    if len(items) > 0:
        show_menu(items, cmd)


if __name__ == "__main__":
    main(sys.argv)
