import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mwsolutions.settings')

# Create the WSGI application callable
application = get_wsgi_application()
