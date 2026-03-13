import json
from websockets.sync.client import connect

headers = {"Authorization": "Bearer secret"}

ws = connect("ws://localhost:8000/v1/realtime")
server_first_message = json.loads(await ws.recv())
print("First Server Message:")
print(server_first_message)
