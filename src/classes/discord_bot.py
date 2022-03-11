import time

from discord import VoiceClient, FFmpegPCMAudio, VoiceChannel
from discord.ext import commands


class MyDiscordBot(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)

    async def on_ready(self) -> None:
        print("Connected!!!")

    async def on_shutdown(self) -> None:
        print("Disconnected!!!")
