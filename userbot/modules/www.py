# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import time
import redis
import random

from datetime import datetime

from speedtest import Speedtest
from userbot import DEVS, CMD_HANDLER as cmd
from userbot import ALIVE_NAME, CMD_HELP, StartTime
from userbot.events import register
from userbot.utils import rzydx_cmd

absen = [
    "**Hadir Woii Gw Hadir** 😎",
    "**Hadir Dongs** 😎",
    "**Hadir Ayangnya Aku** 😉",
    "**Hadir Tod** 😁",
    "**Hadir Kak Ikky ** 😉",
    "**Hadir Kontol**😎 ",
    "**Hadir Sayang** 😉",
]

uy = [
    "**Apa Dev** 😎 ",
    "**Apaan Bang Gw Mo Daring 😭**",
    "**Uuyy Bang** 😉",
    "**Hadir Cuy** 😁",
    "**Yoi Dev** 😎",
    "**Apaan bang** 😎",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=DEVS, pattern=r"^.absen$")
async def _(rzydx):
    await rzydx.reply(random.choice(absen))


@register(incoming=True, from_users=DEVS, pattern=r"^.rzydx$")
async def _(asadekontol):
    await asadekontol.reply(random.choice(uy))


@rzydx_cmd(pattern="rping")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit(".                       /¯ )")
    await pong.edit(".                       /¯ )\n                      /¯  /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f" ➥ `%sms` \n"
                    f"➥ {ALIVE_NAME} \n" % (duration))


@rzydx_cmd(pattern="sping")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**╭━━━━━━━━━━━━━━━━━╮** \n"
                    f"**          ⚡ 𝐍 𝐄 𝐓 𝐖 𝐎 𝐑 𝐊 ⚡** \n"
                    f"**   ▰▱▰▱▰▱▰▱▰▱▰▱** \n"
                    f"**        ❉ ꜱɪɢɴᴀʟ  :** `%sms` \n"
                    f"**        ❉ ᴏᴡɴᴇʀ   :** {ALIVE_NAME}\n"
                    f"**╰━━━━━━━━━━━━━━━━━╯** \n" % (duration))


@rzydx_cmd(pattern="lping")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("❤️‍🔥FLICKS❤️‍🔥")
    await pong.edit("F❤️‍🔥ICKS")
    await pong.edit("FL❤️‍🔥CKS")
    await pong.edit("FLI❤️‍🔥KS")
    await pong.edit("FLIC❤️‍🔥S")
    await pong.edit("FLICKS❤️‍🔥")
    await pong.edit("⚡USERBOT⚡")
    await pong.edit("😈")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⚡{ALIVE_NAME} Bᴏᴛ⚡​**\n"
                    f"➤ __Signal__    __:__ "
                    f"`%sms` \n"
                    f"➤ __Uptime__ __:__ "
                    f"`{uptime}` \n" % (duration))


@rzydx_cmd(pattern="xping")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Please wait.__")
    await pong.edit("__Please wait..__")
    await pong.edit("__Please wait...__")
    await pong.edit("__Please wait.__")
    await pong.edit("__Please wait..__")
    await pong.edit("__Please wait...__")
    await pong.edit("__Please wait.__")
    await pong.edit("__Please wait..__")
    await pong.edit("__Please wait...__")
    await pong.edit("🔥")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**▹  Sɪɢɴᴀʟ   :** "
                    f"`%sms` \n"
                    f"**▹  Uᴘᴛɪᴍᴇ  :** "
                    f"`{uptime}` \n"
                    f"**▹  Oᴡɴᴇʀ   :** {ALIVE_NAME} \n" % (duration))


@rzydx_cmd(pattern="ping")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("࿘")
    await pong.edit("࿘࿘")
    await pong.edit("࿘࿘࿘")
    await pong.edit("࿘࿘࿘࿘")
    await pong.edit("**Pong !!**")
    await pong.edit("😎")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**PONG!!** \n"
                    f"**Speed !!** "
                    f"`%sms` \n"
                    f"**Uptime** - "
                    f"`{uptime}` \n" % (duration))


@rzydx_cmd(pattern="tes")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("🚶..................🐢")
    await pong.edit("🚶................🐢")
    await pong.edit("🚶..............🐢")
    await pong.edit("🚶............🐢")
    await pong.edit("🚶..........🐢")
    await pong.edit("🚶........🐢")
    await pong.edit("🚶......🐢")
    await pong.edit("🚶....🐢")
    await pong.edit("🚶..🐢")
    await pong.edit("🚶🐢")
    await pong.edit("🐢🚶")
    await pong.edit("🐢..🚶")
    await pong.edit("🐢....🚶")
    await pong.edit("🐢......🚶")
    await pong.edit("🐢........🚶")
    await pong.edit("🐢..........🚶")
    await pong.edit("🐢............🚶")
    await pong.edit("🐢..............🚶")
    await pong.edit("**PONGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**FLICKS-USERBOT**\n :` %s`ms\n**Bot Uptime** : `{uptime}`🕛" % (duration))


@rzydx_cmd(pattern="speed")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...⚡`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "✧ **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Signal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "✧ **BOT:**Flicks-Userbot")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@rzydx_cmd(pattern="pong")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong...........🚒`")
    await pong.edit("`Pong..........🚒.`")
    await pong.edit("`Pong.........🚒..`")
    await pong.edit("`Pong........🚒...`")
    await pong.edit("`Pong.......🚒....`")
    await pong.edit("`Pong......🚒.....`")
    await pong.edit("`Pong.....🚒......`")
    await pong.edit("`Pong....🚒.......`")
    await pong.edit("`Pong...🚒........`")
    await pong.edit("`Pong..🚒.........`")
    await pong.edit("`Pong.🚒..........`")
    await pong.edit("`Pong🚒...........`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("**Test Ping!**\n`%sms`" % (duration))


CMD_HELP.update(
    {
        "ping": f"**• Plugin Ping •**\
        \n\n  •  **Perintah :** `{cmd}ping` | `{cmd}lping` | `{cmd}xping` | `{cmd}sping` | `{cmd}fping`\
        \n  •  **Function :** Untuk Menunjukkan Ping Bot Anda\
        \n\n  •  **Perintah :*** `{cmd}speed`\
        \n  •  **Function :** Untuk Menunjukkan Kecepatan Jaringan Anda\
        \n\n  •  **Perintah :** `{cmd}pong` | `{cmd}test`\
        \n  •  **Function :** Sama Seperti Perintah Ping\
    "
    }
)
