#!/usr/bin/env python
import os
import sys
from contrib.image_import import image_import

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RealDelicious.settings')
    if sys.argv[1] == 'import':
        try:
            image_import(sys.argv[2])
        except IndexError as exc:
            raise IndexError(
                "Image folder path import failed "
            ) from exc
    else:
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)
