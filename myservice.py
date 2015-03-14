
from zato.server.service import Service

class MyService1(Service):
    def handle(self):
        self.response.payload = 'How goes it?'
