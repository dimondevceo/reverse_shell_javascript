import asyncio
import websockets

async def handle_connection(websocket):
    print(f"[+] New client connected: {websocket.remote_address}")
    await websocket.send("Hello, client!")

    while not websocket.closed:
        try:
            await send_message(websocket)
        except websockets.exceptions.ConnectionClosed:
            print(f"[-] Connection closed by client: {websocket.remote_address}")
            break

    print(f"[-] Client disconnected: {websocket.remote_address}")

async def send_message(websocket):
    while True:
        response = await websocket.recv()
        print(response)
        message = input(f"{websocket.remote_address[0]}~# ")
        await websocket.send(message)

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765) as websocket:
        print("[+] WebSocket server started on ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("[!] Shutting down server and exiting...")
