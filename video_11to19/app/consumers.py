from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync



class TestSyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket Connected now ...', event)
        # get defult channels layer fron a project
        print("Channels Layer...", self.channel_layer)
        # get defult channels name fron a project
        print("Channels Name...", self.channel_name)
        # syncConsumer cant work like async so we can import async_tosync method for this.
        # add channel to a new or existing group.....
        async_to_sync(self.channel_layer.group_add)(
            'Friends',    #friends is a group name
            self.channel_name
            )
        self.send({
            'type': 'websocket.accept'
        })


    def websocket_receive(self, event):
        print('Message receive from clint...', event['text'])
        print('Type of Message receive from clint...', type(event['text']))
        async_to_sync(self.channel_layer.group_send)('Friends', {
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
        # get defult channels layer fron a project
        print("Channels Layer...", self.channel_layer)
        # get defult channels name fron a project
        print("Channels Name...", self.channel_name)

        #discard a group
        async_to_sync(self.channel_layer.group_discard)(
            'Friends', 
            self.channel_name
            )
        raise StopConsumer        



class TestAsyncConsumer(AsyncConsumer):
  async  def websocket_connect(self, event):
        print('websocket Connected now ...', event)
        # get defult channels layer fron a project
        print("Channels Layer...", self.channel_layer)
        # get defult channels name fron a project
        print("Channels Name...", self.channel_name)
        # syncConsumer cant work like async so we can import async_tosync method for this.
        # add channel to a new or existing group.....
        await self.channel_layer.group_add(
            'Friends',    #friends is a group name
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
        # get defult channels layer fron a project
        print("Channels Layer...", self.channel_layer)
        # get defult channels name fron a project
        print("Channels Name...", self.channel_name)

        #discard a group
        await self.channel_layer.group_discard(
            'Friends', 
            self.channel_name
            )
        raise StopConsumer        
    