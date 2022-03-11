import time
from pprint import pprint

from discord.ext import commands
from discord import VoiceChannel, FFmpegPCMAudio, VoiceClient, AudioSource
from cogs import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import youtube_dl as yd

from src.classes.discord_bot import MyDiscordBot

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.spotify_ID,
                                                           client_secret=config.spotify_secret))

bot = MyDiscordBot(command_prefix=config.prefix)
bot.load_extension('cogs.voice_manager')

bot.run(config.token)