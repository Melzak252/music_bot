spotify_ID="2917d83fd2964864b5d6766350371938"
spotify_secret="7a28ac4a8ce8460a94da3446eda67f04"
prefix=">>>"
token="OTQ5MDU5MTUzMDM1NDE5Njc4.YiE2Ng.TFky6FTuC-mAqGGLQGVBs8aidy0"
TEST_URL="https://www.youtube.com/watch?v=1aJveSQt91w"
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
YD_CONFIG = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'ytsearch',
    'source_address': '0.0.0.0',
}