"""
✘ Commands Available -

• `{i}speedtest`
    Run a speedtest to check your bot’s internet speed (download, upload, ping).

"""

from telethon import events
from speedtest import Speedtest
from . import *

@ultroid_cmd(pattern="speedtest")
async def speed_test(event):
    await event.edit("Running speed test... ⚡")
    try:
        s = Speedtest()
        s.get_best_server()
        download = s.download()
        upload = s.upload()
        ping = s.results.ping

        await event.edit(
            f"🏓 **SpeedTest Results:**\n\n"
            f"📥 Download: `{download / 1024 / 1024:.2f} Mbps`\n"
            f"📤 Upload: `{upload / 1024 / 1024:.2f} Mbps`\n"
            f"📶 Ping: `{ping:.2f} ms`"
        )
    except Exception as e:
        await event.edit(f"❌ Failed to test speed: `{e}`")
