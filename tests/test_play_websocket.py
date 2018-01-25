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
         'url': websocket_url})
    assert websocket_url in provider.engine.play_websocket
    websocket = provider.engine.play_websocket[websocket_url]
    assert websocket
    assert websocket.send('hello')
    assert websocket.recv() == 'hello'
    assert len(provider.engine._teardown) == 1
    assert provider.engine._teardown[0] == websocket.close


def test_send(play_json, websocket_url):
    pass
