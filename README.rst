==============
play websocket
==============


.. image:: https://img.shields.io/pypi/v/play_websocket.svg
        :target: https://pypi.python.org/pypi/play_websocket

.. image:: https://img.shields.io/travis/tierratelematics/play_websocket.svg
        :target: https://travis-ci.org/tierratelematics/play_websocket

.. image:: https://readthedocs.org/projects/play-websocket/badge/?version=latest
        :target: https://play-websocket.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/tierratelematics/play_websocket/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/tierratelematics/play_websocket


pytest-play support for websockets

More info and examples on:

* pytest-play_, documentation
* cookiecutter-qa_, see ``pytest-play`` in action with a working example if you want to start hacking


Features
--------

This project defines a new pytest-play_ command:

::

    {'type': 'print', 'provider': 'play_websocket'}

You can add more commands adding new methods to the command provider implementation in ``providers.py`` module.

Twitter
-------

``pytest-play`` tweets happens here:

* `@davidemoro`_

Credits
-------

This package was created with Cookiecutter_ and the cookiecutter-play-plugin_ (based on `audreyr/cookiecutter-pypackage`_ project template).

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`cookiecutter-play-plugin`: https://github.com/tierratelematics/cookiecutter-play-plugin
.. _pytest-play: https://github.com/tierratelematics/pytest-play
.. _cookiecutter-qa: https://github.com/tierratelematics/cookiecutter-qa
.. _`@davidemoro`: https://twitter.com/davidemoro
