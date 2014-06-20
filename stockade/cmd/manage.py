#!/usr/bin/env python
import contextlib
import os
import sys


@contextlib.contextmanager
def change_dir(path):
    old_path = os.getcwd()
    os.chdir(path)

    yield

    os.chdir(old_path)


# TODO(kgriffs): This does not work yet, since the "vault" dir is not
# part of the "stockade" package.
def main():
    my_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(my_dir)

    change_dir(parent_dir)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stockade.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
