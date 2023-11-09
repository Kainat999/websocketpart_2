# Topic - Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer



from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer




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