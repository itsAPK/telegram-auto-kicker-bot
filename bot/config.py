import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_TOKEN=os.environ.get('TELEGRAM_TOKEN',None)
    TELEGRAM_APP_HASH=os.environ.get('TELEGRAM_APP_HASH',None)
    TELEGRAM_APP_ID=os.environ.get('TELEGRAM_APP_ID',None)
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")