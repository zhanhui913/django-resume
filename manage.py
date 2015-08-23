#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
	#Change the module to use the appropriate settings file for deployments.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
