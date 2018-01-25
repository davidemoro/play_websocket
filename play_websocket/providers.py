from pytest_play.providers import BaseProvider


class WebSocketProvider(BaseProvider):
    """ WebSocket provider """

    def command_connect(self, command, **kwargs):
        pass

    def command_send(self, command, **kwargs):
        pass

    def command_recv(self, command, **kwargs):
        pass
