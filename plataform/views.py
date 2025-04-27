from django.shortcuts import render
from spotify_integration.service.spotify_artist_service import get_id_artist, get_artist_top_tracks
from spotify_integration.service.spotify_auth_service import get_token_valid
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        name_artist = request.POST.get('artist')
        # verificando se o usuário preencheu o nome do artista
        if not name_artist:
            pass            
        token_spotify = get_token_valid()
        id_artist = get_id_artist(name_artist, token_spotify)
        musics = get_artist_top_tracks(id_artist, token_spotify)
        # ordenando a lista por ordem de popularidade (do maior para o menor)
        musics_sorted = sorted(musics, key=lambda dict: dict['popularity'], reverse=True)
        return render(request, 'home.html', {'musics': musics_sorted, 'name_artist': name_artist})
        