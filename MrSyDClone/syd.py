import logging
logger = logging.getLogger(__name__)
from pyrogram import enums
from pyrogram.errors import *
from MrSyDClone.database.clone_bot_userdb import JoinReqs
from database.users_chats_db import db


syd_db = None  
REQUEST_TO_JOIN_MODE = True
AUTH_CHANNEL = None 

async def is_req_subscribed(bot, query):
    if await db.find_join_req(query.from_user.id):
        return True
    try:
        user = await bot.get_chat_member(AUTH_CHANNEL, query.from_user.id)
    except UserNotParticipant:
        pass
    except Exception as e:
        logger.exception(e)
    else:
        if user.status != enums.ChatMemberStatus.BANNED:
            return True

    return False
