from os import getenv


API_ID = int(getenv("API_ID", "21103068"))
API_HASH = getenv("API_HASH", "633ab5bfab52d8763ffc6da7a9b2294a")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6268938019").split()))
MONGO_DB = getenv("MONGO_DB", "")

CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", ""))


