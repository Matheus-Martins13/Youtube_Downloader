"""
Aplicação com o objetivo de fazer o download de playlists de vídeos do YouTube em formato mp4.
O download será feito na maior qualidade disponível.
"""

# importando as dependências
from pytube import (
    YouTube,
    Playlist
)
from pytube.exceptions import RegexMatchError

# url da playlist
p = Playlist(str(input('Entre com o link da playlist \n>> ')))
try:
    verificacao = [url for url in p.video_urls]

except KeyError:
    print('\nOcorreu um erro ao acessar a playlist. Por favor, certifique-se de estar colocando '
          'um link válido de uma playlist do YouTube.')

else:
    # Informações da playlist:
    print(f'Nome: "{p.title}"')
    print(f'Tamanho: {len([url2 for url2 in p.video_urls])} vídeos')

    # recebendo o diretório
    diretorio = input("\nEntre com o diretório para salvar suas músicas \n>> ")

    for url in p.video_urls[:len([url for url in p.video_urls])]:
        try:
            yt = YouTube(str(url))
        except RegexMatchError:
            print(f'O link de um dos vídeos da playlist "{p.title}" é inválido.')
        else:
            # informações do vídeo:
            print('Título do vídeo: ', yt.title)
            tamanho = float(yt.length)

            # convertendo o tamanho:
            if yt.length < 60.00:
                print('Tamanho do vídeo: ', yt.length, 'segundos')
            else:
                minutos = yt.length / 60.00
                min_form = round(minutos, 2)
                print('Duração do vídeo: ', min_form, 'minutos')

            # maior resolução:
            ys = yt.streams.get_highest_resolution()

            # download:
            print('Baixando...')
            ys.download(diretorio)
            print(yt.title, ' - Baixado com sucesso. \n--------')
