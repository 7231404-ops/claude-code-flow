from pyrogram import Client
import requests
import asyncio

# Вставь свои данные с my.telegram.org
API_ID = 12345678
API_HASH = "вставь_свой_hash"
CHAT_ID = "вставь_свой_chat_id"

app = Client("veda", api_id=API_ID, api_hash=API_HASH)

async def monitor():
    print("VedaStack Monitor START")
    while True:
        try:
            resp = requests.get("https://api.zeno.fm/mounts/metadata/subscribe/ixpuzfvgywztv").json()
            listeners = resp.get("listeners", 0)
            print(f"Listeners: {listeners}")
            
            if listeners >= 6:
                await app.send_message(CHAT_ID, f"Astana Radio: {listeners} listeners")
            
            await asyncio.sleep(10)
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(10)

if __name__ == "__main__":
    app.run(monitor())
