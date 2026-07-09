#!/usr/bin/env python3
"""WebSocket server demonstrating unicast communication.

Listens on localhost:8765, tracks all connected clients in a
shared set, and replies to each incoming message only to the
client that sent it (never to the other connected clients).
"""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Handle a single client connection.

    Adds the client to the shared set of connected clients,
    echoes each received message back to that same client only
    (prefixed with "U:"), and removes the client from the set
    once the connection ends.
    """
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send("U:{}".format(message))
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


async def main():
    """Start the WebSocket server and run it forever."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())