#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_todolist.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    is_testing = 'test' in sys.argv

    # config converage
    if is_testing:
        import coverage
        
        source = ['django_todolist.core',]
        omit = [
            '*/tests/*', '*__init__.py', '*apps.py', '*migrations/*', 
            '*settings*', '*tests/*', '*urls.py', '*wsgi.py'
        ]

        cov = coverage.coverage(source=source, omit=omit)
        cov.set_option('report:show_missing', True)
        cov.erase()
        cov.start()
    
    execute_from_command_line(sys.argv)

    if is_testing:
        cov.stop()
        cov.save()
        cov.html_report(directory='covhtml')
        cov.report()
