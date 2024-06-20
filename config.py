## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("BQGDy8YAgMVuwx-VT53k5IOa-eHl9s-OB8ajlv5dP9Ukm0bxXP5r66zdye-jVV2zJ9XYZ_Pxo14K3Hk7z3BHIjVvaYffbOpHBD-v2ApnM8t366XEsax0sQF1jbOmMWPPFnbLAe_pSOq8TtER3yX05NIr2gExGTquSvXMjx-v6FgGMn5aCbg3ROQtDbRgof92UGx6PWDOvZ9MVtryBlyvH0mP4Ix0X-jFw_QKo92W68qpzXdLHY7LEJJTJxrG0JNIPAfnLi0M7yXHOIS3-uGWh1sMlymoufzRlXRnW7WhFYuhkzjCGSpGUn0_cp25u9xwFCC3DhupMNffPJt1Ev_BbUqDhdLK-AAAAAF7LnaDAA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "7296236206:AAFWegPql0H-NceQtgOLKhM54lzmkJsLbg0")
BOT_NAME = getenv("BOT_NAME", "beast x music")

API_ID = int(getenv("API_ID", "25414598"))
API_HASH = getenv("API_HASH", "aea15d329df8a58537c8da1e53c3e5e0")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://kuldiprathod2003:kuldiprathod2003@cluster0.wxqpikp.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "beast")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ll_Timeisnotwaiting_ll")
ALIVE_NAME = getenv("ALIVE_NAME", "Beast")
BOT_USERNAME = getenv("BOT_USERNAME", "Beast_X_musicbot")
OWNER_ID = getenv("OWNER_ID", "6128266949")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "@Sexzyxi")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Voilet_Chat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Voilet_Chat")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5935765877").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
