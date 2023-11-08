from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/Stest/<str:mygroupname>/', consumers.TestSyncConsumer.as_asgi()),
    path('ws/Atest/<str:mygroupname>/', consumers.TestAsyncConsumer.as_asgi())

]