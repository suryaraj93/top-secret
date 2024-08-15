# websocket/asgi.py

import os

from django.core.asgi import get_asgi_application
import myapp.router
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')

print("here")
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles traditional HTTP requests
    "websocket": AuthMiddlewareStack(  # Handles WebSocket connections
        URLRouter(
            myapp.router.websocket_urlpatterns
        )
    ),
})
