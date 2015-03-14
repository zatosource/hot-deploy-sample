
from zato.server.service import Service

class MyService2(Service):
    def handle(self):
        self.response.payload = {'response': 'All good, cheers'}

