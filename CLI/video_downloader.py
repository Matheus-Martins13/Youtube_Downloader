"""
Aplicação com o objetivo de fazer o download de vídeos do YouTube em formato mp4.
O download será feito na maior qualidade disponível.
"""

# importando as dependências
from pytube import YouTube

# recebendo a URL e o diretório:
link = input("Digite o link do vídeo que deseja baixar: ")
diretorio = input("Digte o diretório que deseja salvar o vídeo: ")
yt = YouTube(link)

# informações do vídeo:
print('Título do vídeo: ', yt.title)
tamanho = float(yt.length)

if yt.length < 60.00:
    print('Tamanho do vídeo: ', yt.length, 'segundos')
else:
    minutos = yt.length / 60.00
    min_form = round(minutos, 2)
    print('Duração do vídeo: ', min_form, 'minutos')

# escolhendo a melhor resolução:
ys = yt.streams.get_highest_resolution()

# iniciando o download:
print('Baixando...')
ys.download(diretorio)
print('Download feito com sucesso!!')
