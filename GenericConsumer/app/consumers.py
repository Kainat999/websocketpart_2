# Topic - Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer



from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep  # for receive meassages in slow speed
import asyncio # use for asyncwebsocketconsumer in sleep method


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


class MyWebsocketConsumer(WebsocketConsumer):


    def connect(self):
        print('Websocket is connected....')
        self.accept() 

    def receive(self, text_data=None, bytes_data=None):
        print('Message is received from client now ....', text_data)
        for i in range(20):
            self.send(text_data=str(i)) # To send Data to client..
            sleep(1)
        
        self.close()           
        self.close(code=4123)  

    def disconnect(self, close_code):
        print('Websocket is Disconnected....', close_code)         

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        print('Websocket is connected....')
        await self.accept() 

    async def receive(self, text_data=None, bytes_data=None):
        print('Message is received from client now ....', text_data)

        for i in range(20):
            await self.send(text_data=str(i)) # To send Data to client..
            await asyncio.sleep(1)    # To send Data to Client 
        

    async def disconnect(self, close_code):
        print('Websocket is Disconnected....', close_code)  