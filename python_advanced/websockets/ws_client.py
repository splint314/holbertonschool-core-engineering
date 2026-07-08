#!/usr/bin/env python3
"""Minimal WebSocket client.

Connects to a WebSocket server, sends one message, waits for the
response, and returns it.
"""
import asyncio
import os
import sys
import websockets


async def connect_and_send(uri, message):
    """Connect to uri, send message, and return the server response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response


if __name__ == "__main__":
    ws_uri = os.environ.get("WS_URI", "ws://localhost:8765")
    message = os.environ.get("WS_MESSAGE", "Hello WebSocket")
    result = asyncio.run(connect_and_send(ws_uri, message))
    sys.stdout.write(result)