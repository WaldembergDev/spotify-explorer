import datetime
from django.shortcuts import render
import requests
from dotenv import load_dotenv
from pathlib import Path
import os
from .models import Token
from datetime import date, datetime
from datetime import timedelta
from django.utils import timezone


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


def save_token():
    data_token = get_token()
    if not data_token:
        return False
    # pegando a hora atual, adicionando a validade do token e subtraindo 10 segundos
    expires_in = timezone.now() + timedelta(seconds = data_token.get('expires_in')) - timedelta(seconds = 10)
    token = Token(
        access_token = data_token.get('access_token'),
        token_type = data_token.get('token_type'),
        expires_in = expires_in
    )
    token.save()
    return token

def get_token_valid():
    last_token = Token.objects.last()

    # verificando se agora é maior do que a validade do último token gerado
    if timezone.now() > last_token.expires_in:
        new_token = save_token()
        return new_token.access_token        
    else:
        return last_token.access_token
