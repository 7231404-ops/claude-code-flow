import asyncio
import aiohttp
import json
from datetime import datetime
from pyrogram import Client

API_ID = 12345
API_HASH = "your_api_hash"
CHAT_ID = 123456789
STATION_NAME = "Astana Radio"
STREAM_URL = "https://api.zeno.fm/mounts/metadata/subscribe/ixpuzfvgywztv"

app = Client("my_session", API_ID, API_HASH)
last_title = None

def log_line(text):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {text}"
    print(line)
    with open("monitor.log", "a", encoding="utf-8") as f:
        f.write(line + "\
")

async def monitor():
    global last_title
    async with aiohttp.ClientSession(headers={"User-Agent": "Mozilla/5.0"}) as session:
        while True:
            try:
                log_line("connecting...")
                timeout = aiohttp.ClientTimeout(total=None, sock_connect=10, sock_read=None)

                async with session.get(STREAM_URL, timeout=timeout) as resp:
                    log_line(f"HTTP: {resp.status}")
                    resp.raise_for_status()

                    async for line_bytes in resp.content:
                        line = line_bytes.decode("utf-8", errors="replace").strip()
                        if not line.startswith("data:"):
                            continue

                        payload = line[5:].strip()
                        try:
                            data = json.loads(payload)
                        except json.JSONDecodeError:
                            continue

                        title = data.get("streamTitle")
                        if title and title != last_title:
                            last_title = title
                            message = f"🎵 {STATION_NAME}\
Сейчас играет:\
{title}"
                            log_line(f"Now playing: {title}")
                            await app.send_message(CHAT_ID, message)

            except Exception as e:
                log_line(f"Error: {e}")

            await asyncio.sleep(10)

async def main():
    async with app:
        await monitor()

if __name__ == "__main__":
    asyncio.run(main())
