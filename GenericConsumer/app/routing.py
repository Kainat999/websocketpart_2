from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/wsct/', consumers.TestWebsocketConsumer.as_asgi()),
    path('ws/awsct/', consumers.TestAsyncWebsocketConsumer.as_asgi()),


    # Real time Example path
    path('ws/wscte/', consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/awscte/', consumers.MyAsyncWebsocketConsumer.as_asgi()),
]
