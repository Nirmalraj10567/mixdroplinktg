#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


import aiohttp
import os, time
from hurry.filesize import size
from bot.plugins.display.time import  time_data
from pyrogram.errors import FloodWait
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )



async def fileIO(file, client, bot, s_time):
    file_size = size(os.path.getsize(file))
    file_name = file.split('/')[-1]
    try:
        await client.edit_message_text(
        chat_id=bot.from_user.id,
        message_id=bot.message.message_id,
        text="Uploadig to File.IO"
        )
        async with aiohttp.ClientSession() as session:
            files = {
            'file': open(file, 'rb')
            }
            response = await session.post('https://file.io/', data=files)
            link = await response.json()
            dl_b = link['link']
            await client.edit_message_text(
            chat_id=bot.from_user.id,
            message_id=bot.message.message_id,
            text=f"Uploaded...100% in {time_data(s_time)}"
            )
            await client.send_message(
            chat_id=bot.from_user.id,
            text=(
                f"File Name: <code>{file_name}</code>"
                f"\nFile Size: <code>{file_size}</code>"
                ),
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "🔗 DOWNLOAD URL",
                        url=f"{dl_b}"
                        )
                ],
                [
                    InlineKeyboardButton(
                        "Subscribe 🤪🤪🤪",
                        url = "https://youtu.be/Tr8FXHyZeTA"
                    )
                ]])
            )
    except FloodWait as error:
        print(time.sleep(error.x))
