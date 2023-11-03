from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/Stest/', consumers.TestSyncConsumer.as_asgi()),
    path('ws/Atest/', consumers.TestAsyncConsumer.as_asgi())

]