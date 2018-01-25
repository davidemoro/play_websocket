from copy import deepcopy
import logging
from websocket import create_connection
from pytest_play.providers import BaseProvider


class WebSocketProvider(BaseProvider):
    """ WebSocket provider """

    def __init__(self, engine):
        super(WebSocketProvider, self).__init__(engine)
        self.logger = logging.getLogger()

    def _set_connection(self, options):
        """ Set connection and register teardown """
        url = options.pop('url')
        if not hasattr(self.engine, 'play_websocket'):
            self.engine.play_websocket = {}
        if url not in self.engine.play_websocket:
            ws = create_connection(url, **options)
            self.engine.play_websocket[url] = ws
            self.engine.register_teardown_callback(ws.close)

    def _get_connection(self, url):
        """ Get connection """
        return self.engine.play_websocket[url]

    def command_connect(self, command, **kwargs):
        """ Setup a websocket connection """
        cmd = deepcopy(command)
        self._set_connection(cmd['options'])

    def command_send(self, command, **kwargs):
        """ Send a message """
        ws = self._get_connection(command['url'])
        ws.send(command['payload'])

    def command_recv(self, command, **kwargs):
        """ Receive """
        ws = self._get_connection(command['url'])
        results = ws.recv()

        try:
            self._make_variable(command, results=results)
            self._make_assertion(command, results=results)
        except Exception as e:
            self.logger.exception(
                'Exception for command %r',
                command,
                e)
            raise e

    def _make_assertion(self, command, **kwargs):
        """ Make an assertion based on python
            expression against kwargs
        """
        assertion = command.get('assertion', None)
        if assertion:
            self.engine.execute_command(
                {'provider': 'python',
                 'type': 'assert',
                 'expression': assertion
                 },
                **kwargs,
            )

    def _make_variable(self, command, **kwargs):
        """ Make a variable based on python
            expression against kwargs
        """
        expression = command.get('variable_expression', None)
        if expression:
            self.engine.execute_command(
                {'provider': 'python',
                 'type': 'store_variable',
                 'name': command['variable'],
                 'expression': expression
                 },
                **kwargs,
            )
