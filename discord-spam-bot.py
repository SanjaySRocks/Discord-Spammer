import requests
import time

print("Hi this bot is created by Sanjay Singh (github.com/sanjaysrocks)")

cmd = input("Enter Command to spam: ")
token = input("Enter your discord token: ")
channel = input("Enter Channel ID: ")
n = input("How many times ?: ")
delay = input("Enter delay in seconds: ")

payload = {
    'content' : cmds
}

header = {
    'authorization': token  
}

for i in range(0,int(n)):
    r = requests.post("https://discord.com/api/v8/channels/"+channel+"/messages", data=payload, headers=header)
    time.sleep(int(delay))