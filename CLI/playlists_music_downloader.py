"""
Aplicação com o objetivo de fazer o download de playlists do youtube em formato de aúdio mp3.
"""

# importando as dependências
from pytube import (
    Playlist,
    YouTube
)
from pytube.exceptions import RegexMatchError
import os

# url da playlist e verificando validade
p = Playlist(input('Entre com o link da playlist \n>> '))

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

    # separando as urls
    for url in p.video_urls[:len([url2 for url2 in p.video_urls])]:
        try:
            yt = YouTube(str(url))
        except RegexMatchError:
            print(f'O link de um dos vídeos da playlist "{p.title}" é inválido.')
        else:
            # separando só o áudio
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=diretorio)

            # salvando o arquivo
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            # Apresentando mensagem de êxito
            print(yt.title + " Foi baixado com sucesso! \n")
