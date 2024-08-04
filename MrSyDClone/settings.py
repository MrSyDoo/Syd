from pyrogram import Client, filters
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MrSyDClone.database.clone_bot_userdb import clonedb





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
       
