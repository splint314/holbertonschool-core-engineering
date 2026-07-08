#!/usr/bin/env python3

"""Minimal WebSocket echo server.

Listens on localhost:8765, accepts multiple client connections,
and echoes back any text message it receives.
"""

import asyncio
import websockets


async def connection_handler(websocket):
    """Handle a single client connection.

    Continuously receives messages from the client and sends
    the exact same message back.
    """
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket server and run it forever."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
