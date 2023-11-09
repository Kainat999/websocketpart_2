# Topic - Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer



from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep  # for receive meassages in slow speed
import asyncio # use for asyncwebsocketconsumer in sleep method
from asgiref.sync import async_to_sync
import json
from .models import Chat, Group
from channels.db import database_sync_to_async

class TestWebsocketConsumer(WebsocketConsumer):

# This handler is called when client initially opens a connection and 
# is about to finish the websocker gabdshake.

    def connect(self):
        print('Websocket is connected....')
        self.accept() # To accept the connection
        # self.close()  # To reject the connection

# This handler is called when data received from client

    def receive(self, text_data=None, bytes_data=None):
        print('Message is received from client now ....', text_data)

        self.send(text_data="Message from server to client")    # To send Data to Client 
        # self.send(bytes_data=data)   # To send binary frome to client
        self.close()           # To reject the connection
        self.close(code=4123)  # To add a custom websocket error code 
        
# This handler is called when either connection to the client is 
# lost, either from the client closing the connection, the server 
# closing the connection, or loss of the socket.

    def disconnect(self, close_code):
        print('Websocket is Disconnected....', close_code)  




        # AsyncWebsocketConsumers

class TestAsyncWebsocketConsumer(AsyncWebsocketConsumer):

# This handler is called when client initially opens a connection and 
# is about to finish the websocker gabdshake.

    async def connect(self):
        print('Websocket is connected....')
        await self.accept() # To accept the connection
        # await self.close()  # To reject the connection

# This handler is called when data received from client

    async def receive(self, text_data=None, bytes_data=None):
        print('Message is received from client now ....', text_data)

        await self.send(text_data="Message from server to client")    # To send Data to Client 
        # await self.send(bytes_data=data)   # To send binary frome to client
        # await self.close()           # To reject the connection
        # await self.close(code=4123)  # To add a custom websocket error code 
        
# This handler is called when either connection to the client is 
# lost, either from the client closing the connection, the server 
# closing the connection, or loss of the socket.

    async def disconnect(self, close_code):
        print('Websocket is Disconnected....', close_code)  




# Real-time Data Example
# Real-time Data Example with Front End
# chat app with Dynamic Group Name - 

# class MyWebsocketConsumer(WebsocketConsumer):


#     def connect(self):
#         print('Websocket is connected....')
#         print("Channel layer...", self.channel_layer)
#         print("Channel Name...", self.channel_name)
#         self.group_name = self.scope['url_route']['kwargs']['groupname']
#         print("Group Name..", self.group_name)
#         async_to_sync(self.channel_layer.group_add)(
#             self.group_name,
#             self.channel_name
#         )
#         self.accept() 

#     def receive(self, text_data=None, bytes_data=None):
#         print('Message is received from client now ....', text_data)
#         # for i in range(10):
#         #     self.send(text_data=str(i)) # To send Data to client..
#         #     sleep(1)
        
#         # self.close()           
#         # self.close(code=4123) 
#         data = json.loads(text_data)
#         print("Data..", data)
#         message = data['msg']
#         async_to_sync(self.channel_layer.group_send)(
#             self.group_name,
#             {
#                 'type':'chat.message',
#                 'message': message
#             }
#         )
#     def chat_message(self, event):
#         print("Event...", event)
#         self.send(text_data=json.dumps({
#             'msg':event['message']
#         }))    



#     def disconnect(self, close_code):
#         print('Websocket is Disconnected....', close_code)
#         print("Channel Layer..", self.channel_layer)
#         print("Channel Name...", self.channel_name)
#         async_to_sync(self.channel_layer.group_discard)(
#             self.group_name,
#             self.channel_name
#         )         

# class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):


#     async def connect(self):
#         print('Websocket is connected....')
#         print("Channel layer...", self.channel_layer)
#         print("Channel Name...", self.channel_name)
#         self.group_name = self.scope['url_route']['kwargs']['groupname']
#         print("Group Name..", self.group_name)
#         await self.channel_layer.group_add(
#              self.group_name,
#              self.channel_name
#         )
#         await self.accept() 

#     async def receive(self, text_data=None, bytes_data=None):
#         print('Message is received from client now ....', text_data)
#         # for i in range(10):
#         #     self.send(text_data=str(i)) # To send Data to client..
#         #     sleep(1)
        
#         # self.close()           
#         # self.close(code=4123) 
#         data = json.loads(text_data)
#         print("Data..", data)
#         message = data['msg']
#         await self.channel_layer.group_send(
#             self.group_name,
#             {
#                 'type':'chat.message',
#                 'message': message
#             }
#         )
#     async def chat_message(self, event):
#         print("Event...", event)
#         await self.send(text_data=json.dumps({
#             'msg':event['message']
#         }))    



#     async def disconnect(self, close_code):
#         print('Websocket is Disconnected....', close_code)
#         print("Channel Layer..", self.channel_layer)
#         print("Channel Name...", self.channel_name)
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         ) 

# PART 3 DATABASE

class MyWebsocketConsumer(WebsocketConsumer):


    def connect(self):
        print('Websocket is connected....')
        print("Channel layer...", self.channel_layer)
        print("Channel Name...", self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("Group Name..", self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept() 

    def receive(self, text_data=None, bytes_data=None):
        print('Message is received from client now ....', text_data)
        data = json.loads(text_data)
        print("Data..", data)
        message = data['msg']
        group = Group.objects.get(name= self.group_name)
        if self.scope['user'].is_authenticated:
            chat = Chat(
            content = data['msg'],
            group = group
            )
            chat.save()
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type':'chat.message',
                    'message': message
                }
            )
        else:
            self.send(text_data=json.dumps({
                "msg": "Login is required.."
                }
            ))
    
           
    
    def chat_message(self, event):
        print("Event...", event)
        self.send(text_data=json.dumps({
            'msg':event['message']
        }))    



    def disconnect(self, close_code):
        print('Websocket is Disconnected....', close_code)
        print("Channel Layer..", self.channel_layer)
        print("Channel Name...", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )         

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        print('Websocket is connected....')
        print("Channel layer...", self.channel_layer)
        print("Channel Name...", self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("Group Name..", self.group_name)
        await self.channel_layer.group_add(
             self.group_name,
             self.channel_name
        )
        await self.accept() 

    async def receive(self, text_data=None, bytes_data=None):
        print('Message is received from client now ....', text_data) 
        data = json.loads(text_data)
        print("Data..", data)
        message = data['msg']
        group = await database_sync_to_async(Group.objects.get)(name= self.group_name)
        if self.scope['user'].is_authenticated:
            chat = Chat(
            content = data['msg'],
            group = group
            )
            await database_sync_to_async(chat.save)()
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'chat.message',
                    'message': message
                }
            )
        else:
            await self.send(text_data=json.dumps({
                "msg": "Login is required.."
                }
            ))
    async def chat_message(self, event):
        print("Event...", event)
        await self.send(text_data=json.dumps({
            'msg':event['message']
        }))    



    async def disconnect(self, close_code):
        print('Websocket is Disconnected....', close_code)
        print("Channel Layer..", self.channel_layer)
        print("Channel Name...", self.channel_name)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        ) 