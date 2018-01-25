import logging
from websocket import create_connection
from pytest_play.providers import BaseProvider


class WebSocketProvider(BaseProvider):
    """ WebSocket provider """

    def __init__(self, engine):
        super(WebSocketProvider, self).__init__(engine)
        self.logger = logging.getLogger()

    def _set_connection(self, url):
        """ Set connection and register teardown """
        if not hasattr(self.engine, 'play_websocket'):
            self.engine.play_websocket = {}
        if url not in self.engine.play_websocket:
            ws = create_connection(url)
            self.engine.play_websocket[url] = ws
            self.engine.register_teardown_callback(ws.close)

    def _get_connection(self, url):
        """ Get connection """
        return self.engine.play_websocket[url]

    def command_connect(self, command, **kwargs):
        """ Setup a websocket connection """
        self._set_connection(command['url'])

    def command_send(self, command, **kwargs):
        """ Send a message """
        pass

    def command_recv(self, command, **kwargs):
        """ Receive """
        pass
