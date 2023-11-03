import asyncio
from time import sleep
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
import json

# SyncConsumer testing
class TestSyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket is Connected', event)
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print('Message is received....',event['text'])
        for i in range(10):
            self.send({
                'type':'websocket.send',
                'text': json.dumps({"count": i})
            })
            sleep(i)

    def websocket_disconnect(self, event):
        print('Websocket is Disconnect..... ', event)
        raise StopConsumer        


# AsyncConsumer testing

class TestAsyncConsumer(AsyncConsumer):

    def websocket_connect(self, event):
        print('Websocket is Connected', event)
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        print('Message is received....',event['text'])
        for i in range(10):
            self.send({
                'type':'websocket.send',
                'text': json.dumps({"count": i})
            })
            sleep(i)

    def websocket_disconnect(self, event):
        print('Websocket is Disconnect..... ', event)
        raise StopConsumer        
