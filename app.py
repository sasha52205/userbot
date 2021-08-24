import asyncio

from pyrogram import Client, filters

import random
import asyncio
send_to = -1001455318582
send_from =-1001594473201
# send_from = "me"
#
app = Client(
    "my_account",
    api_id=7276093,
    api_hash='960368167d494ca3b1d469f15164e7cc'
)


@app.on_message(filters.chat(send_from))
async def my_handler(client, message):
    chat = message.chat.username
    message_id = message.message_id
    message_text = message.text.lower()
    try:
        await app.send_message(chat_id=send_to, text=f'{message_text}')
        await asyncio.sleep(3)
        print ('[+]')
    except:
        await app.send_message(chat_id=send_to, text=f'flood err')
@app.on_message(filters.command("dialog", prefixes="."))
async def dialog_list(client, message):
     dialogs = await app.get_dialogs()
     print(dialogs)
#     if chat
#     d_list = []
#     for dialog in dialogs:
#         d_list.append("@"+str(dialog.chat.username))
#     print(d_list)



####цитаты бендера
#@app.on_message(filters.private)
#async def my_handler(client, message):
#    await message.reply_text("Готов к работе!")








if __name__ == '__main__':
    app.run()






