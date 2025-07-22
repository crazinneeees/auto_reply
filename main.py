from telethon import TelegramClient, events
import asyncio

# 🔐 Твои данные с https://my.telegram.org
api_id = 23397273
api_hash = '89b4af8e761a1853063a68b91d7b1cb0'

# 📂 Название сессионного файла (создастся автоматически)
client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.connect()

    if not await client.is_user_authorized():
        phone = input("📱 Telefon raqamini kiriting: ")
        await client.send_code_request(phone)
        code = input("🔑 Telegramdan kelgan kod: ")
        await client.sign_in(phone, code)

    print("✅ Avtorizatsiya muvaffaqiyatli. Xabar kelishi kutilmoqda...")

    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        if event.is_private:
            sender = await event.get_sender()
            username = getattr(sender, 'username', None) or "no'malum"
            print(f"📩 Xabar keldi @{username}dan: {event.raw_text}")
            await event.reply("Salom hozir javob qaytara olmayman!")

    await client.run_until_disconnected()

asyncio.run(main())
