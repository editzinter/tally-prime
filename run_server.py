import os
import sys
import datetime

# PyInstaller with console=False strips sys.stdout. We must redirect it to avoid crashes!
log_dir = os.path.expanduser('~/.tally-prime')
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, 'server.log')

log_file = open(log_path, 'a', encoding='utf-8')
log_file.write(f"\n--- Server Started at {datetime.datetime.now()} ---\n")

if sys.stdout is None:
    sys.stdout = log_file
if sys.stderr is None:
    sys.stderr = log_file

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