import logging
logger = logging.getLogger(__name__)
from pyrogram import enums
from pyrogram.errors import *
from MrSyDClone.database.clone_bot_userdb import JoinReqs



syd_db = None  
REQUEST_TO_JOIN_MODE = True
AUTH_CHANNEL = None 

async def setup_join_db(bot_id, auth_channel):
    global syd_db, AUTH_CHANNEL
    syd_db = JoinReqs(bot_id, auth_channel)
    AUTH_CHANNEL = auth_channel

async def syd_subscribed(bot, query):
    global AUTH_CHANNEL
    if syd_db is None or AUTH_CHANNEL is None:
        me = await bot.get_me()
        cd = await db.get_bot(me.id)
        AUTH_CHANNEL = cd["fsub"]
        await setup_join_db(bot_id=me.id, auth_channel=AUTH_CHANNEL)
        
    if REQUEST_TO_JOIN_MODE and syd_db.isActive():
        try:
            user = await syd_db.get_user(query.from_user.id)
            if user and user["user_id"] == query.from_user.id:
                return True
            else:
                try:
                    user_data = await bot.get_chat_member(AUTH_CHANNEL, query.from_user.id)
                except UserNotParticipant:
                    pass
                except Exception as e:
                    logger.exception(e)
                else:
                    if user_data.status != enums.ChatMemberStatus.BANNED:
                        return True
        except Exception as e:
            logger.exception(e)
            return False
    else:
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


