import os
import sys
import django
from django.core.management import call_command

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project24.settings')
    django.setup()
    print("Running background database migrations...")
    call_command('migrate', interactive=False)
    print("Starting Django server...")
    call_command('runserver', '127.0.0.1:8000', '--noreload')

if __name__ == '__main__':
    main()