from pytest_play.providers import BaseProvider


class NewProvider(BaseProvider):
    """ Print provider """

    def command_print(self, command, **kwargs):
        print(command['message'])

    def command_yetAnotherCommand(self, command, **kwargs):
        pass
