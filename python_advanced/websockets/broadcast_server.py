#!/usr/bin/env python3
"""WebSocket server demonstrating broadcast communication.

Listens on localhost:8765, tracks all connected clients in a
shared set, and forwards each incoming message to every
connected client (prefixed with "B:").
"""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Handle a single client connection.

    Adds the client to the shared set of connected clients,
    broadcasts each received message to every connected client
    (prefixed with "B:"), and removes the client from the set
    once the connection ends.
    """
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients.copy():
                await client.send("B:{}".format(message))
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