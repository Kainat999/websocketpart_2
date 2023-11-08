from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync



class TestSyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket Connected now ...', event)
        print("Channels Layer...", self.channel_layer)
        print("Channels Name...", self.channel_name)
        # get defined chennal name 
        print("Group name ...",self.scope['url_route']['kwargs']['mygroupname'])

        self.group_name = self.scope['url_route']['kwargs']['mygroupname']
        print("group name... ", self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,   #groupName  
            self.channel_name
            )
        self.send({
            'type': 'websocket.accept'
        })


    def websocket_receive(self, event):
        print('Message receive from clint...', event['text'])
        print('Type of Message receive from clint...', type(event['text']))
        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            'type': 'chat.message',
            'message': event['text']
        })

    def chat_message(self, event):
        print('Event..', event)  
        print('Event data...', event['message'])  
        print('Type of Event data...', type(event['message']))  

        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self, event):
        print('websocket DisConnected ...', event) 
        print("Channels Layer...", self.channel_layer)
        print("Channels Name...", self.channel_name)



        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
            )
        raise StopConsumer        



class TestAsyncConsumer(AsyncConsumer):
    async  def websocket_connect(self, event):
            print('websocket Connected now ...', event)
            print("Channels Layer...", self.channel_layer)
            print("Channels Name...", self.channel_name)
            self.group_name = self.scope['url_route']['kwargs']['mygroupname']


            await self.channel_layer.group_add(
                self.group_name,    
                self.channel_name
                )
            self.send({
                'type': 'websocket.accept'
            })


    async def websocket_receive(self, event):
            print('Message receive from clint...', event['text'])
            print('Type of Message receive from clint...', type(event['text']))
            await  self.channel_layer.group_send('Friends', {
                'type': 'chat.message',
                'message': event['text']
            })

    async  def chat_message(self, event):
        print('Event..', event)  
        print('Event data...', event['message'])  
        print('Type of Event data...', type(event['message']))  

        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    async  def websocket_disconnect(self, event):
            print('websocket DisConnected ...', event) 
            print("Channels Layer...", self.channel_layer)
            print("Channels Name...", self.channel_name)



            await self.channel_layer.group_discard(
                self.group_name, 
                self.channel_name
               )
            raise StopConsumer        
    