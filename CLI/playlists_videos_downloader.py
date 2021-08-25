"""
Aplicação com o objetivo de fazer o download de playlists de vídeos do YouTube em formato mp4.
O download será feito na maior qualidade disponível.
"""

# importando as dependências
from pytube import Playlist
from pytube import YouTube

# url da playlist
p = Playlist(str(input('Entre com o link da playlist \n>> ')))

# checando o diretório
diretorio = str(input("Entre com o diretório para salvar sua playlist \n>> "))

for url in p.video_urls[:len([url for url in p.video_urls])]:
    yt = YouTube(str(url))

    # informações do vídeo:
    print('Título do vídeo: ', yt.title)
    tamanho = float(yt.length)

    # Convertendo o tamanho:
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
    print(yt.title, 'Baixado com sucesso. \n--------')

print('Todos os vídeos foram baixados com sucesso!')
