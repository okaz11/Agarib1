## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("7592996473:AAFZEPhe06Vj6T_7oNiFXJWQ4fiU803180A", "")
BOT_NAME = getenv("RoleKeeperbot", "Umk")
API_ID = int(getenv("API_ID", "20064681"))
API_HASH = getenv("API_HASH", "6b29eb42b9f21bddd9ebd78c305a7ec8")
OWNER_NAME = getenv("OWNER_NAME", "Mohannad")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Mohannad")
BOT_USERNAME = getenv("BOT_USERNAME", "Mohannad2_Robot")
OWNER_ID = getenv("OWNER_ID", "732370872")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Mohannad2_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "732370872").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-Mohannad/Mohannad-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
