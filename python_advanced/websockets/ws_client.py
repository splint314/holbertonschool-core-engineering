#!/usr/bin/env python3

"""Minimal WebSocket client.

Connects to the echo server, sends one message, waits for the
response, prints it, and closes the connection.
"""

import asyncio
import websockets


async def client():
    """Send one message to the server and print its response."""
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(client())
