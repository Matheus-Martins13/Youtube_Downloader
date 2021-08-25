"""
Aplicação com o objetivo de fazer o download de playlists do youtube em formato de aúdio mp3.
"""

# importando as dependências
from pytube import Playlist
from pytube import YouTube
import os

# url da playlist
p = Playlist(str(input('Entre com o link da playlist \n>> ')))

# checando o diretório
diretorio = str(input("Entre com o diretório para salvar suas músicas: "))

# Procesando as URLs
for url in p.video_urls[:len([url for url in p.video_urls])]:
    yt = YouTube(str(url))

    # extraindo o audio
    video = yt.streams.filter(only_audio=True).first()

    # baixando o arquivo
    out_file = video.download(output_path=diretorio)

    # salvando o arquivo
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # Apresentando mensagem de êxito
    print(yt.title + " Foi baixado com sucesso! \n")

print('Todas as músicas foram baixados com sucesso!')
