#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_websocket` package."""

import pytest


@pytest.fixture(scope='session')
def variables():
    return {'skins': {'skin1': {'base_url': 'http://', 'credentials': {}}}}


def test_provider(play_json):
    from play_websocket import providers
    provider = providers.WebSocketProvider(play_json)
    assert provider.engine is play_json
    provider.command_connect(
        {'provider': 'play_websocket',
         'type': 'connect',
         'message': 'Hello, World!'})
