
from telethon import Button
from telethon.events import InlineQuery
from telethon.tl.types import InputWebDocument

from userbot import LOGS, tgbot, bot, BOT_USERNAME, SUDO_USERS

user = bot.get_me()
OWNER = user.first_name
OWNER_ID = user.id


MSG = f"""
**Rzydx - UserBot**
➖➖➖➖➖➖➖➖➖➖
**Owner**: [{OWNER}](tg://user?id={OWNER_ID})
**Assistant** : @{BOT_USERNAME}
➖➖➖➖➖➖➖➖➖➖
"""

IN_BTTS = [
    [
        Button.url(
            "Repository",
            url="https://github.com/muhammadhanif71/Itachi-Userbot",
        ),
        Button.url("Channel", url="https://t.me/stufchannel"),
    ]
]


def in_pattern(**kwargs):
    """Assistant's inline decorator."""

    def don(func):
        async def wrapper(event):
            if event.sender_id not in OWNER_ID and SUDO_USERS():
                res = [
                    await event.builder.article(
                        title="Rzydx Userbot",
                        url="https://t.me/stufsupport",
                        description="(c) Itachi Userbot",
                        text=MSG,
                        thumb=InputWebDocument(
                            "https://telegra.ph/file/7d3e2c6d397dfbd88cdb9.jpg.jpg",
                            0,
                            "image/jpeg",
                            [],
                        ),
                        buttons=IN_BTTS,
                    )
                ]
                return await event.answer(
                    res,
                    switch_pm=f"🤖: Assistant of {OWNER}",
                    switch_pm_param="start",
                )
            try:
                await func(event)
            except Exception as er:
                LOGS.exception(er)

        tgbot.add_event_handler(
            wrapper, InlineQuery(
                pattern=pattern, **kwargs))

    return don
