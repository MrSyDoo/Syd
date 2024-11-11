 # Don't Remove Credit Tg - @SyD_XyZ
# Ask Doubt on telegram @Syd_XyZ

# Clone Code Credit : YT - @SyD_Xyz / TG - @GetTGLinks / GitHub - @Bot_Cracker 

from info import API_ID, API_HASH, CLONE_MODE, LOG_CHANNEL, SYD_CHANNELS
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, CallbackQuery
from database.users_chats_db import db
from pyrogram.errors import UserNotParticipant
import re, os
from Script import script

async def not_subscribed(_, __, message):
    for channel in SYD_CHANNELS:
        try:
            user = await message._client.get_chat_member(channel, message.from_user.id)
            if user.status in {"kicked", "left"}:
                return True
        except UserNotParticipant:
            return True
    return False


@Client.on_message(filters.command('clone'))
async def clone_menu(client, message):
    if CLONE_MODE == False:
        return 

    if await db.is_clone_exist(message.from_user.id):
        return await message.reply("**Yᴏᴜ ʜᴀᴠᴇ ᴀʟʀᴇᴀᴅʏ ᴄʟᴏɴᴇᴅ ᴀ ʙᴏᴛ ᴅᴇʟᴇᴛᴇ ғɪʀsᴛ ɪᴛ ʙʏ /deleteclone \n\nWᴇ 'ʟʟ ᴛʜɪɴᴋ ᴀʙᴏᴜᴛ ɪᴛ, ᴛᴏ ᴍᴀᴋᴇ ᴍᴏʀᴇ ᴛʜᴀɴ ᴏɴᴇ ʙᴏᴛ, ᴄᴜʀʀᴇɴᴛʟʏ ᴜꜱᴇ ᴀɴᴏᴛʜᴇʀ ᴀᴄᴄᴏᴜɴᴛ. \n\n Fᴏʀ ꜱᴜᴩᴩᴏʀᴛ 🌴; @Bot_Cracker ⚡**")
    else:
        pass

    not_joined_channels = []
    for channel in SYD_CHANNELS:
        try:
            user = await client.get_chat_member(channel, message.from_user.id)
            if user.status in {"kicked", "left"}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)
            
    if not_joined_channels:
        buttons = [
            [
                InlineKeyboardButton(
                    text=f"✧ Jᴏɪɴ {channel.capitalize()} ✧", url=f"https://t.me/{channel}"
                )
            ]
            for channel in not_joined_channels
        ]
        buttons.append(
            [
                InlineKeyboardButton(
                    text="✧ Jᴏɪɴ Back-up ✧", url="https://t.me/+0Zi1FC4ulo8zYzVl"

                )
            ]
        )
        buttons.append(
            [
                InlineKeyboardButton(
                    text="✔ ɪ ᴀᴍ ᴊᴏɪɴᴇᴅ ✔", callback_data="check_subscription"
                )
            ]
        )

        text = "**Sᴏʀʀʏ, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴊᴏɪɴ ɪɴ ᴏᴜʀ ʀᴇqᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟꜱ, ᴩʟᴇᴀꜱᴇ ᴅᴏ ꜱᴏ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ,,... ⚡ .**"
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
        
    techvj = await client.ask(message.chat.id, "<b>1) Sᴇɴᴅ <code>/newbot</code> ᴛᴏ @BotFather\n2) Gɪᴠᴇ ᴀ ɴᴀᴍᴇ ꜰᴏʀ ʏᴏᴜʀ ʙᴏᴛ.\n3) Gɪᴠᴇ ᴀ ᴜɴɪǫᴜᴇ ᴜsᴇʀɴᴀᴍᴇ.\n4) Tʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ.\n5) Fᴏʀᴡᴀʀᴅ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ.\n\n/cancel - ᴄᴀɴᴄᴇʟ ᴛʜɪs ᴘʀᴏᴄᴇss.</b>")
    if techvj.text == '/cancel':
        await techvj.delete()
        return await message.reply('<b>Cᴀɴᴄᴇʟᴇᴅ ᴛʜɪs ᴘʀᴏᴄᴇss 🚫</b>')
    if techvj.forward_from and techvj.forward_from.id == 93372553:
        try:
            bot_token = re.findall(r"\b(\d+:[A-Za-z0-9_-]+)\b", techvj.text)[0]
        except:
            return await message.reply('<b>Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ 😕</b>')
    else:
        return await message.reply('<b>Nᴏᴛ ꜰᴏʀᴡᴀʀᴅᴇᴅ ꜰʀᴏᴍ @BotFather 😑</b>')
    user_id = message.from_user.id
    msg = await message.reply_text('<b><blockqoute>Wᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ ɪ ᴀᴍ ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ,</blockqoute>\n \n<u>⚠️ɴᴏᴛᴇ: ʙʏ ᴄʟᴏɴɪɴɢ ʏᴏᴜ ᴀʀᴇ ᴀᴄᴄᴇᴩᴛɪɴɢ ᴛᴏ ᴏᴜʀ ᴩᴏʟɪᴄɪᴇꜱ!</u></b>')
    try:
        vj = Client(
            f"{bot_token}", API_ID, API_HASH,
            bot_token=bot_token,
            plugins={"root": "MrSyDClone"}
        )
        await vj.start()
        bot = await vj.get_me()
        await db.add_clone_bot(bot.id, user_id, bot_token)
        await msg.edit_text(f"<b>SᴜᴄᴄᴇssғᴜʟʟY Cʟᴏɴᴇᴅ Yᴏᴜʀ Bᴏᴛ: @{bot.username}.\n\nYᴏᴜ ᴄᴀɴ ᴄᴜsᴛᴏᴍɪsᴇ ʏᴏᴜʀ ᴄʟᴏɴᴇ ʙᴏᴛ ʙʏ \n/settings ᴀɴᴅ /edit \nCᴏᴍᴍᴀɴᴅ ɪɴ ʏᴏᴜʀ ᴄʟᴏɴᴇ ʙᴏᴛ</b>\n\n<blockqoute>Nᴇᴠᴇʀ Fᴏʀɢᴇᴛ ᴛᴏ ᴇxᴩᴇʀɪᴇɴᴄᴇ ᴛʜᴇ ꜱᴜᴩᴇʀʙ ꜱᴇʀᴠɪᴄᴇᴇʜ⚡</blockqoute>")
    except BaseException as e:
        await msg.edit_text(f"⚠️ <b>Bᴏᴛ Eʀʀᴏʀ:</b>\n\n<code>{e}</code>\n\n**Tʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ ⚡ ᴏʀ Kɪɴᴅʟʏ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ @SyD_XyZ ᴛᴏ ɢᴇᴛ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ.**")
    await client.send_message(LOG_CHANNEL, script.LOG_BOT.format(message.from_user.id, message.from_user.mention, bot.username))
    

@Client.on_message(filters.command('deleteclone'))
async def delete_clone_menu(client, message):
    if await db.is_clone_exist(message.from_user.id):
        await db.delete_clone(message.from_user.id)
        await message.reply("**Sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ʏᴏᴜʀ ᴄʟᴏɴᴇ ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ᴄʀᴇᴀᴛᴇ ᴀɢᴀɪɴ ʙʏ /clone**")
    else:
        await message.reply("**Nᴏ ᴄʟᴏɴᴇ ʙᴏᴛ ғᴏᴜɴᴅ ✖**")

async def restart_bots():
    bots_cursor = await db.get_all_bots()
    bots = await bots_cursor.to_list(None)
    for bot in bots:
        bot_token = bot['bot_token']
        try:
            vj = Client(
                f"{bot_token}", API_ID, API_HASH,
                bot_token=bot_token,
                plugins={"root": "MrSyDClone"},
            )
            await vj.start()
        except Exception as e:
            print(f"Error while restarting bot with token {bot_token}: {e}")
        
# Don't Remove Credit Tg - @SyD_XyZ
# Ask Doubt on telegram @Syd_XyZ



@Client.on_callback_query(filters.regex("check_subscription"))
async def check_subscription(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    not_joined_channels = []

    for channel in SYD_CHANNELS:
        try:
            user = await client.get_chat_member(channel, user_id)
            if user.status in {"kicked", "left"}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)

    if not not_joined_channels:
        await callback_query.message.edit_text(
            "**Tʜᴀɴᴋꜱ 🩵, Yᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ ᴏɴ ᴀʟʟ ᴛʜᴇ ʀᴇqᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟꜱ. \nCʟɪᴄᴋ ᴏɴ 😊 /clone ɴᴏᴡ ᴛᴏ ꜱᴛᴀʀᴛ ᴛʜᴇ ᴩʀᴏᴄᴇꜱꜱ.....⚡**"
        )
    else:
        buttons = [
            [
                InlineKeyboardButton(
                    text=f"✧ Jᴏɪɴ {channel.capitalize()} ✧",
                    url=f"https://t.me/{channel}",
                )
            ]
            for channel in not_joined_channels
        ]
        buttons.append(
            [
                InlineKeyboardButton(
                    text="✧ Jᴏɪɴ Back-up ✧", url="https://t.me/+0Zi1FC4ulo8zYzVl"

                )
            ]
        )

        buttons.append(
            [
                InlineKeyboardButton(
                    text="✔ ɪ ᴀᴍ ᴊᴏɪɴᴇᴅ ✔", callback_data="check_subscription"
                )
            ]
        )

        text = "**Sᴛɪʟʟ 🥲, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴊᴏɪɴ ɪɴ ᴏᴜʀ ᴀʟʟ ʀᴇqᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟꜱ, ᴩʟᴇᴀꜱᴇ ᴅᴏ ꜱᴏ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ,,... ⚡ .**"
        await callback_query.message.edit_text(
            text=text, reply_markup=InlineKeyboardMarkup(buttons)
        )
