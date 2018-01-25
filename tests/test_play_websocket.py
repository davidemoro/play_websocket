#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_websocket` package."""

import pytest


@pytest.fixture(scope='session')
def variables():
    return {'skins': {'skin1': {'base_url': 'http://', 'credentials': {}}}}


@pytest.fixture
def websocket_url():
    return 'ws://echo.websocket.org/'


def test_connect(play_json, websocket_url):
    from play_websocket import providers
    provider = providers.WebSocketProvider(play_json)
    assert provider.engine is play_json
    provider.command_connect(
        {'provider': 'play_websocket',
         'type': 'connect',
         'options': {
             'url': websocket_url}})
    assert websocket_url in provider.engine.play_websocket
    websocket = provider.engine.play_websocket[websocket_url]
    assert websocket
    assert websocket.send('hello')
    assert websocket.recv() == 'hello'
    assert len(provider.engine._teardown) == 1
    assert provider.engine._teardown[0] == websocket.close


def test_send(play_json, websocket_url):
    play_json.execute(
        """
        {"steps": [
            {"provider": "play_websocket",
             "type": "connect",
             "options": {"url": "%s", "timeout": 5}},
            {"provider": "play_websocket",
             "type": "send",
             "url": "%s",
             "payload": "ciao"}
        ]}
        """ % (websocket_url, websocket_url,)
    )
    websocket = play_json.play_websocket[websocket_url]
    assert websocket.recv() == 'ciao'


def test_send_recv(play_json, websocket_url):
    play_json.execute(
        """
        {"steps": [
            {"provider": "play_websocket",
             "type": "connect",
             "options": {"url": "%s", "timeout": 5}},
            {"provider": "play_websocket",
             "type": "send",
             "url": "%s",
             "payload": "ciao"},
            {"provider": "play_websocket",
             "type": "recv",
             "url": "%s",
             "variable": "data",
             "variable_expression": "results.upper()",
             "assertion": "variables['data'] == 'CIAO'"}
        ]}
        """ % (websocket_url, websocket_url, websocket_url,)
    )
    assert play_json.variables['data'] == 'CIAO'


def test_send_recv_assertion_error(play_json, websocket_url):
    with pytest.raises(AssertionError):
        play_json.execute(
            """
            {"steps": [
                {"provider": "play_websocket",
                 "type": "connect",
                 "options": {"url": "%s", "timeout": 5}},
                {"provider": "play_websocket",
                 "type": "send",
                 "url": "%s",
                 "payload": "ciao"},
                {"provider": "play_websocket",
                 "type": "recv",
                 "url": "%s",
                 "variable": "data",
                 "variable_expression": "results.upper()",
                 "assertion": "variables['data'] == 'CIaAO'"}
            ]}
            """ % (websocket_url, websocket_url, websocket_url,)
        )
    assert play_json.variables['data'] == 'CIAO'
