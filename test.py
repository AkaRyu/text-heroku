import rpc
import time

print("Demo for python-discord-rpc")
client_id = '526492863455035392' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    activity = {
            "state": "Entrain de s'entrainer",
            "details": "Sur les RPC python-discord .",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Petit text",
                "small_image": "th",
                "large_text": "Text plus gros",
                "large_image": "th"
            }
        }
    rpc_obj.set_activity(activity)
time.sleep(30)
