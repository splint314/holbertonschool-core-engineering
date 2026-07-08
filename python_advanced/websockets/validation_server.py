#!/usr/bin/env python3
"""WebSocket server with basic message validation.

Listens on localhost:8765, accepts multiple client connections,
validates each incoming text message, and responds with either
an "OK:" prefixed echo or an "ERR:EMPTY" error for blank messages.
"""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Handle a single client connection.

    Continuously receives messages from the client, validates
    them, and sends back the appropriate response while keeping
    the connection open. Handles clients disconnecting mid-stream.
    """
    try:
        async for message in websocket:
            trimmed = message.strip()
            if trimmed == "":
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send("OK:{}".format(trimmed))
    except ConnectionClosed:
        pass


async def main():
    """Start the WebSocket server and run it forever."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())