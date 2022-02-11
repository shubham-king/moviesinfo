# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from pyrogram import Client

bot_token = os.environ["BOT_TOKEN", "5188870295:AAEoDvJv3R8z8Nw0KsZXVqr9j2R5HIpu33M"]
api_id = int(os.environ["God", "8916614"])
api_hash = os.environ["API", "562fab1bd859199bb7d4a896d75fdbb4"]

plugins = dict(
    root="plugins"
)

Bot = Client(
    "Movie-Info-Bot-V2",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins
)

Bot.run()
