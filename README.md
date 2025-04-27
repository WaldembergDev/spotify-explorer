# Django App Spotify 🎵

Um aplicativo Django que integra a API do Spotify, permitindo que os usuários explorem informações sobre músicas de artista. Este projeto foi desenvolvido com foco em aprendizado e demonstração de habilidades em desenvolvimento web com Django.

## 📋 Funcionalidades

- **Autenticação de Usuários**:
  - Registro, login e logout.
  - Atualização de perfil.
- **Integração com a API do Spotify**:
  - Busca de artistas e músicas.
  - Exibição de informações detalhadas.
- **Interface Amigável**:
  - Design responsivo utilizando Bootstrap.
  - Mensagens de feedback para o usuário.
- **Gerenciamento de Playlists**:
  - Criação e personalização de playlists.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2
- **Frontend**: Bootstrap 5
- **Banco de Dados**: SQLite
- **APIs**: Spotify API
- **Outras Bibliotecas**:
  - `django.contrib.messages` para mensagens de feedback.
  - `requests` para integração com a API do Spotify.

## 📂 Estrutura do Projeto

```plaintext
django-app-spotify/
├── accounts/               # Gerenciamento de usuários
│   ├── templates/          # Templates de login, registro e perfil
│   ├── static/             # Arquivos estáticos (CSS, JS, imagens)
│   └── [views.py](http://_vscodecontentref_/0)            # Lógica de autenticação e perfil
├── artist_hits_finder/     # Configurações principais do projeto
├── plataform/              # Funcionalidades da plataforma
│   └── templates/          # Template da página inicial
├── spotify_integration/    # Integração com a API do Spotify
│   └── service/            # Serviços para autenticação e busca de artistas
├── static/                 # Arquivos estáticos globais
├── templates/              # Templates base e parciais
└── [requirements.txt](http://_vscodecontentref_/1)        # Dependências do projeto