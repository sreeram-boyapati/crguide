#!/usr/bin/env python
import os
import sys
if __name__ == "__main__":
	try:
		if os.environ['SETTINGS'] == 'Production':
			os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crguide.settings.production")
	except Exception:
		os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crguide.settings.local")

	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)