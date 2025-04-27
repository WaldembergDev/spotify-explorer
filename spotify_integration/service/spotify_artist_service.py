from ..models import Token
import requests


def get_id_artist(name_artist, token_spotify):
    url = 'https://api.spotify.com/v1/search'

    headers = {
        'Authorization': f'Bearer {token_spotify}'
    }

    params = {
        'q': name_artist,
        'type': 'artist',
        'limit': 10
    }

    response = requests.get(url, headers=headers, params=params)

    try:
        response.raise_for_status()
        data = response.json()
        if data:
            id_artist = data.get('artists').get('items')[0].get('id')
            return id_artist
        return data
    except requests.HTTPError as e:
        print(f'Erro ao fazer a requisição: {e}')
        return None
    
def get_artist_top_tracks(id_artist, token_spotify):
    url = f'https://api.spotify.com/v1/artists/{id_artist}/top-tracks'

    headers = {
        'Authorization': f'Bearer {token_spotify}'
    }

    response = requests.get(url, headers=headers)

    try:
        response.raise_for_status()
        data = response.json().get('tracks')
        musics = [{'name': music.get('name'), 'url': music.get('external_urls').get('spotify'), 'popularity': music.get('popularity')} for music in data]
        return musics
    except requests.HTTPError as e:
        print(f'Erro ao fazer a requisição: {e}')
        return None