import os

token = os.getenv("BOT_TOKEN")

print("TOKEN EXISTS:", token is not None)

if token:
    print("TOKEN LENGTH:", len(token))
else:
    print("TOKEN NOT FOUND")
