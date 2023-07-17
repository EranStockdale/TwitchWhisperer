from twitchwhisperer import Whisperer
import os, asyncio
from dotenv import load_dotenv
load_dotenv()

whisperer = Whisperer(os.getenv('TWITCH_USERNAME'), os.getenv('TWITCH_ACCESS_TOKEN'))
asyncio.run(whisperer.run())