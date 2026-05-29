import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)   # 原样返回，模拟 GPS 确认

async def main():
    print("WebSocket server started on ws://localhost:8765")
    async with websockets.serve(echo, "localhost", 8765,
                                 max_size=None,
                                 ping_interval=None):
        await asyncio.Future()  # 永远运行

asyncio.run(main())