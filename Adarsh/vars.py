import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '25065882'))
    API_HASH = str(getenv('API_HASH', '7711af532d45686e38c6b360161e2483'))
    PICS = (environ.get('PICS','https://graph.org/file/5607e02882ec4aebf95a2.jpg')).split()
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6732590282:AAHGuZFg79T5R97UaRRmV19z3oaVZUR-qcY'))
    name = str(getenv('name', 'File_Stream_FcBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001920843740'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6302537270").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'myd_boy'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL', True))
    if HAS_SSL:
        URL = "https://file-stream-bot-7jli.onrender.com/".format(FQDN)
    else:
        URL = "https://file-stream-bot-7jli.onrender.com/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://jarramahesh24:VLAsRFbaFT8WFbJn@cluster0.gleasay.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'FILMCLAN'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))
