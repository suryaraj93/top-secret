import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'You are connected!'
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        if not text_data.strip():  # Check if the received data is empty
            return  # Ignore the empty message

        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            # Echo the message back to the client
            self.send(text_data=json.dumps({
                'message': message
            }))
        except json.JSONDecodeError:
            self.send(text_data=json.dumps({
                'error': 'Invalid JSON received'
            }))
