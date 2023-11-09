from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/wsct/', consumers.TestWebsocketConsumer.as_asgi()),
    path('ws/awsct/', consumers.TestAsyncWebsocketConsumer.as_asgi()),


    # Real time Example path
    path('ws/wscte/<str:groupname>/', consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/awscte/<str:groupname>/', consumers.MyAsyncWebsocketConsumer.as_asgi()),
]
