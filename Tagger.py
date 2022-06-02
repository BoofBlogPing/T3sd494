import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("Salam Mən DejavuTagBot Group'da User Tag Edmək üçün Yaradıldım...\n\nƏtrafli Məlumat Almaq üçün /help Əmrinə Toxunaraq Məlumat Əldə Edə Bilərsən.",
                    buttons=(
                   
		      [Button.url('➕ Məni Qrupa Sal ➕', 'http://t.me/DejavuTaggerBot?startgroup=a')],
                      [Button.url('Sahib 👨🏻‍💻', 'https://t.me/MUCVE_M')],
                      [Button.url('Qurup 📣', 'https://t.me/DejavuGurup')],
		      [Button.url('Kanal 🛠', 'https://t.me/DejavuSupport')],
                    ),
                    
               

print(">> Bot İşləyir Narahat olma 🚀 Məlumat Almaq üçün @MUCVE_M yazın. <<")
client.run_until_disconnected()
