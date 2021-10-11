# Calling API Calls for User
import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CODEDIGGER_TOKEN')
URL = os.getenv('CODEDIGGER_API_URL')
AUTH_HEADER = { 'Authorization': 'Bearer {}'.format(TOKEN) }

def bot_verify(username, discord_tag): 
    url = URL + "/bot/verify"
    data = {
        'username': username,
        'discord_tag': discord_tag
    }
    response = requests.put(url= url, headers=AUTH_HEADER, json=data)
    return response