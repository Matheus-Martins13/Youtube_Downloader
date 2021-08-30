"""
Aplicação com o objetivo de fazer o download de vídeos do YouTube em formato mp4.
O download será feito na maior qualidade disponível.
"""

# importando as dependências
from pytube import YouTube
# dependência de tratamento de erros
from pytube.exceptions import RegexMatchError

# recebendo a URL e o diretório

# verificando se o link é válido
try:
    yt = YouTube(input("Digite o link do vídeo que deseja baixar \n>> "))

except RegexMatchError:
    print("\nLink inválido. Experimente copiar o link de um vídeo do YouTube!")

else:
    # salvando o diretório
    diretorio = input("Digte o diretório que deseja salvar o vídeo \n>> ")
    print('--------------')
    # informações do vídeo:
    print('\nTítulo do vídeo: ', yt.title)
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
    ys.download(diretorio)

    print('Baixando...')
    print('Download feito com sucesso!')
