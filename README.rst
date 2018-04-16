==============
play websocket
==============


.. image:: https://img.shields.io/pypi/v/play_websocket.svg
        :target: https://pypi.python.org/pypi/play_websocket

.. image:: https://travis-ci.org/davidemoro/play_websocket.svg?branch=develop
       :target: https://travis-ci.org/davidemoro/play_websocket

.. image:: https://readthedocs.org/projects/play-websocket/badge/?version=latest
        :target: https://play-websocket.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/davidemoro/play_websocket/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/davidemoro/play_websocket


pytest-play support for websockets

More info and examples on:

* pytest-play_, documentation
* cookiecutter-qa_, see ``pytest-play`` in action with a working example if you want to start hacking


Features
--------

This project defines new pytest-play_ commands.

Connect
=======

::

    {'type': 'connect',
     'provider': 'play_websocket',
     'options': {
         'url': 'ws://echo.websocket.org/',
         'timeout': 2
         }
    }

Send
====

::

    {'type': 'send',
     'provider': 'play_websocket',
     'url': 'ws://echo.websocket.org/',
     'payload': 'Hello!'}


Receive
=======

::

    {'type': 'recv',
     'provider': 'play_websocket',
     'url': 'ws://echo.websocket.org/',
     'variable': 'data',
     'variable_expression': 'response.upper()',
     'assertion': 'data == "HELLO!"',
     'timeout': 10}


Receive until
=============

If you want to filter the data returned by the websocked
until you get what you expect::

    {'provider': 'python',
     'type': 'wait_until',
     'expression': 'variables['data'] == "HELLO!"',
     'timeout': 60,
     'poll': 0,
     'sub_commands': [
         {
          'type': 'recv',
          'provider': 'play_websocket',
          'url': 'ws://echo.websocket.org/',
          'variable': 'data',
          'variable_expression': 'response.upper()',
          'timeout': 60}
         }]
    }

Twitter
-------

``pytest-play`` tweets happens here:

* `@davidemoro`_

Credits
-------

This package was created with Cookiecutter_ and the cookiecutter-play-plugin_ (based on `audreyr/cookiecutter-pypackage`_ project template).

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`cookiecutter-play-plugin`: https://github.com/davidemoro/cookiecutter-play-plugin
.. _pytest-play: https://github.com/davidemoro/pytest-play
.. _cookiecutter-qa: https://github.com/davidemoro/cookiecutter-qa
.. _`@davidemoro`: https://twitter.com/davidemoro
