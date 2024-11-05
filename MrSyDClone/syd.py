import logging
logger = logging.getLogger(__name__)
from pyrogram import Client, enums
from pyrogram.errors import *
from MrSyDClone.database.clone_bot_userdb import clonedb as syd
from database.users_chats_db import db




async def syd_subscribed(bot, query):
    me = await client.get_me()
    cd = await db.get_bot(me.id)
    MR_SYD = cd["fsub"]
    mssydtg = me.id + query.from_user.id
    if await syd.find_join_req(mssydtg):
        return True
    try:
        user = await bot.get_chat_member(MR_SYD, query.from_user.id)
    except UserNotParticipant:
        pass
    except Exception as e:
        logger.exception(e)
    else:
        if user.status != enums.ChatMemberStatus.BANNED:
            return True
 
    return False
