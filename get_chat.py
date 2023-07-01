from telethon import TelegramClient, events
from config import configure

list = configure.init_ini()
api_id = list[0]
api_hash = list[1]
client = TelegramClient('telegram', api_id, api_hash)

@client.on(events.NewMessage(pattern=r'^get_chat$', outgoing=True))
async def get_chat_id(event):
    await event.message.delete()
    print(f'chat id: {event.message.chat_id}')

with client as cl:
    cl.run_until_disconnected()
