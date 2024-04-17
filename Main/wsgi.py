import os
import sys

sys.path.append('/home/ubuntu/django/EarthTracker')
sys.path.append('/home/ubuntu/django/EarthTracker/Main')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Main.settings')
application = get_wsgi_application()