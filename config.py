from os import environ
from typing import List

API_ID = int(environ.get("API_ID", "23889992"))
API_HASH = environ.get("API_HASH", "70bf3c9baebf30afff8c32649bf23c3d")
BOT_TOKEN = environ.get("BOT_TOKEN", "8158676731:AAFiU94v1QpsQXz0nsM3FwPjz6PsdZJ1qbY")
OWNER_ID = int(environ.get("OWNER_ID", "1900118264"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002318862336"))
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://HDMoviesEarth:unqOY8gUrmDLNXHd@cluster0.0xjypxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT = int(environ.get('PORT', 8080))
IS_FSUB = bool(environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, environ.get("AUTH_CHANNEL", "-1002288558945 -1001943817170").split())) # Add Multiple channel id
