from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery, Message, InputMediaPhoto
from utils import check_sydtoken, sydfy_user, update_sydfy_status, get_sydfy_status, get_token, check_sydfication, get_shortlink, get_tutorial, get_seconds, VERIFIED
from database.users_chats_db import db

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    data = message.command[1]
    if data.split("-", 1)[0] == "sydclone":
        userid = data.split("-", 2)[1]
        token = data.split("-", 3)[2]
        if str(message.from_user.id) != str(userid):
            return await message.reply_text(
                text="<b>Iɴᴠᴀʟɪᴅ ʟɪɴᴋ ᴏʀ Exᴘɪʀᴇᴅ ʟɪɴᴋ !</b>",
                protect_content=True
            )
        is_valid = await check_sydtoken(client, userid, token)
        if is_valid == True:
            tz = pytz.timezone('Asia/Kolkata')
            mr_syd = await db.get_syd(userid)
            mr_sy = mr_syd["bot_name"]
            await message.reply_text("⚡")
            syd = datetime.now(tz)+timedelta(hours=384)
            btn = [[
                InlineKeyboardButton("Gᴇᴛ Bᴏᴛ", url=f"https://telegram.me/{mr_sy}")
            ]]
            await message.reply_text("🩵")
            await sydfy_user(client, userid, token)
            await message.reply_text(
                text=f"<b>Hᴇʏ {message.from_user.mention}, Yᴏᴜ ᴀʀᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ᴠᴇʀɪғɪᴇᴅ !\n\n<blockquote>Nᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ <u>16ᴅᴀʏꜱ [ {syd} ]</u>, Eɴᴊᴏʏ ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ ⚡</blockquote></b>",
                protect_content=True,
                reply_markup=InlineKeyboardMarkup(btn)
            )
            return
        else:
            return await message.reply_text(
                text="<b>Iɴᴠᴀʟɪᴅ ʟɪɴᴋ ᴏʀ Exᴘɪʀᴇᴅ ʟɪɴᴋ !</b>",
                protect_content=True
            )
