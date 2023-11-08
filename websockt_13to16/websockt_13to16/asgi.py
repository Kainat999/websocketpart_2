"""
ASGI config for websockt_13to16 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import app.routing
from channels.auth import AuthMiddlewareStack  # import AuthMiddlewareStack for Authntication

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websockt_13to16.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(   # add AuthMiddlewareStack
        URLRouter(
            app.routing.websocket_urlpatterns
        )
    )
})
