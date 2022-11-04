from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os

DuskyInfo=Client(
    "DuskyInfo",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@DuskyInfo.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f'Heya {message.from_user.mention},\nI'm Dusky User Information Bot Here To Provide Telegram Information!\n\n<u><b>Commands</b></u>:\n/m - To Get Your Information\n/u - To Get User Information (Reply To a Forwarded Message)\n/c - To Get Group/Channel Information (Reply To a Forwarded Message)'
    reply_markup = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Updates', url='https://t.me/DuskysUpdates')
        ]]
    )
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@DuskyInfo.on_message(filters.command('m') & filters.private)
async def start(client, message):
    await message.reply(
        f"""        
<b>First name</b>: {message.from_user.first_name}
<b>Last name</b>: {message.from_user.last_name}
<b>Username</b>: {message.from_user.username}
<b>Telegram id</b>: <code>{message.from_user.id}</code>
<b>Phone number</b>: {message.from_user.phone_number}
<b>Language</b>: {message.from_user.language_code}
<b>Status</b>: {str(message.from_user.status)[11:]}
<b>Data center id</b>: {message.from_user.dc_id}"""
)

@DuskyInfo.on_message(filters.command('u') & filters.private)
async def start(client, message):
    await message.reply(
        f"""
<b>First name</b>: {message.reply_to_message.forward_from.first_name}
<b>Last name</b>: {message.reply_to_message.forward_from.last_name}
<b>Username</b>: {message.reply_to_message.forward_from.username}
<b>Telegram id</b>: <code>{message.reply_to_message.forward_from.id}</code>
<b>Phone number</b>: {message.reply_to_message.forward_from.phone_number}
<b>Language</b>: {message.reply_to_message.forward_from.language_code}
<b>Status</b>: {str(message.reply_to_message.forward_from.status)[11:]}
<b>Data center id</b>: {message.reply_to_message.forward_from.dc_id}"""
)

@DuskyInfo.on_message(filters.command('c'))
async def start(client, message):
    await message.reply(
        f"""
<b>Name</b>: {message.reply_to_message.forward_from_chat.title}
<b>Username</b>: {message.reply_to_message.forward_from_chat.username}
<b>Telegram id</b>: {message.reply_to_message.forward_from_chat.id}
<b>Type</b>: {str(message.reply_to_message.forward_from_chat.type)[9:]}
<b>Data center id</b>: {message.reply_to_message.forward_from_chat.dc_id}
"""
)
 
print("DuskyInfo is alive!")
DuskyInfo.run()