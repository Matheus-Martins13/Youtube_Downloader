"""
Aplicação com o objetivo de fazer o download de aúdios do youtube em formato mp3.
"""

# Importando as dependências
from pytube import YouTube
import os

#
yt = YouTube(str(input("Entre com o link do vídeo \n>> ")))

# extraindo o áudio
video = yt.streams.filter(only_audio=True).first()

# coletando o diretório
print("Entre com o diretório onde deseja salvar a música.")
destination = str(input(">> ")) or '.'

# iniciando o processo de download
out_file = video.download(output_path=destination)

# salvando o arquivo
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# Apresentando mensagem de êxito
print(f"'{yt.title}'" + " Foi baixado com sucesso!")
