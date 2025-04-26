from django.shortcuts import render
import requests
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path('.venv/.env'))

# Create your views here.
def get_token():
    # constantes
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    # endpoint
    url = 'https://accounts.spotify.com/api/token'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(url, headers=headers, data=data)

    try:
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as e:
        print(f'Erro ao fazer a requisição: {e}')
        return None

    