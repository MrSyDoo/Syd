from pyrogram import Client, filters
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MrSyDClone.database.clone_bot_userdb import clonedb
from database.users_chats_db import db





@Client.on_message(filters.private & filters.command(['edit']))
async def settings(client, message):
    me = await client.get_me()
    owner = await db.get_bot(me.id)
    if owner["user_id"] != message.from_user.id:
        return
    text="<b>Cʀᴇᴀᴛᴇ Yᴏᴜʀ Oᴡɴ Bᴏᴛ Δɴᴅ Eᴅɪᴛ ɪᴛ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ ᴍᴀʜɴ.....⚡</b>"
    await message.reply_text(
        text=text,
        reply_markup=main_buttons(),
        quote=True
    )
@Client.on_callback_query(filters.regex(r'^settings'))
async def settings_query(bot, query):
  user_id = query.from_user.id
  i, type = query.data.split("#")
  buttons = [[InlineKeyboardButton('🔙 Back', callback_data="settings#main")]]
  
  if type=="main":
     await query.message.edit_text(
       "<b>Change Your Settings As Your Wish</b>",
       reply_markup=main_buttons())

  elif type=="url":
     me = await client.get_me()
     url = await client.ask(message.chat.id, "<b>Now Send Me Your Shortlink Site Domain Or Url Without https://</b>")
     api = await client.ask(message.chat.id, "<b>Now Send Your Api</b>")
     try:
         shortzy = Shortzy(api_key=api.text, base_site=url.text)
         link = 'https://t.me/+-VpGTWWWTldhZWNl'
         await shortzy.convert(link)
     except Exception as e:
         await message.reply(f"**Error In Converting Link**\n\n<code>{e}</code>\n\n**Start The Process Again By - /settings**", reply_markup=InlineKeyboardMarkup(btn))
         return
     data = {
        'url': url.text,
        'api': api.text
     }
     await db.update_bot(me.id, data)
     await message.reply("**Successfully Uᴩᴅᴀᴛᴇᴅ Settings**")

def main_buttons():
  buttons = [[
       InlineKeyboardButton('Sʜᴏʀᴛ-ᴜʀʟ',
                    callback_data=f'settings#url')
       ],[
       InlineKeyboardButton('🕵‍♀ Filters',
                    callback_data=f'settings#filters'),
       InlineKeyboardButton('🏓 Button',
                    callback_data=f'settings#button')
       ],[
       InlineKeyboardButton('⚙️ Extra Settings',
                    callback_data='settings#nextfilters')
       ],[      
       InlineKeyboardButton('🔙 Back', callback_data='settings#syd')
       ]]
  return InlineKeyboardMarkup(buttons)
