import discord
import youtube_dl
from discord import VoiceChannel, VoiceClient
from discord.ext import commands

from src.classes.discord_bot import MyDiscordBot
from src.cogs.config import FFMPEG_OPTIONS, YD_CONFIG, TEST_URL


class VoiceManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.in_voice_channel = False

    @commands.command(name="join", aliases=['j'])
    async def join(self, ctx: commands.Context) -> None:
        if self.in_voice_channel:
            await ctx.channel.send("I'm already in voice channel")
            return

        voice = ctx.author.voice
        if voice is None:
            await ctx.channel.send("You must be in  voice channel to call me")
            return

        self.in_voice_channel = True
        await voice.channel.connect()

    @commands.command(name="leave", aliases=['l', 'lv'])
    async def leave(self, ctx: commands.Context) -> None:
        if not self.in_voice_channel:
            await ctx.channel.send("I'm not in any voice channel")
            return

        channel: VoiceClient = ctx.voice_client
        if not channel:
            await ctx.channel.send("I'm not in any voice channel")
            return

        self.in_voice_channel = False
        await channel.disconnect()

    @commands.command(aliases=['p', 'queue', 'que'])
    async def play(self, ctx):
        voice_client: VoiceClient = self.bot.voice_clients[0]
        with youtube_dl.YoutubeDL(YD_CONFIG) as ydl:
            song_info = ydl.extract_info(TEST_URL, download=False)
            voice_client.play(discord.FFmpegPCMAudio(song_info["formats"][0]["url"]), after=None)


def setup(bot: MyDiscordBot):
    bot.add_cog(VoiceManager(bot))
