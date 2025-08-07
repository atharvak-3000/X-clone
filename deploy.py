#!/usr/bin/env python
"""
Deployment script for X Clone application
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

def deploy():
    """Run deployment tasks"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xclone.production_settings')
    
    try:
        # Collect static files
        print("Collecting static files...")
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
        
        # Run migrations
        print("Running migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        # Create superuser if it doesn't exist
        print("Creating superuser...")
        execute_from_command_line(['manage.py', 'shell', '-c', '''
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
    print("Superuser created: admin/admin123")
else:
    print("Superuser already exists")
'''])
        
        print("Deployment completed successfully!")
        
    except Exception as e:
        print(f"Deployment failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    deploy()
