import PySimpleGUI as Sg
from pytube import YouTube
from pytube import Playlist
import os

Sg.theme('DarkRed1')


class TelaPython:
    def __init__(self):
        # Layout 
        layout = [
            [Sg.Text('URL Playlist:', size=(7, 00)), Sg.Input(key='url')],
            [Sg.Text('Diretório: '), Sg.Input(key='diretorio')],
            [Sg.Button('Fazer o Download')],
            [Sg.Output(size=(60, 10))]
        ]
        # Janela
        self.janela = Sg.Window("Baixar playlists de músicas").layout(layout)

        # Extrair os dados da tela
        self.button, self.values = self.janela.Read()

    def iniciar(self):

        url = self.values['url']
        diretorio = self.values['diretorio']

        p = Playlist(url)

        for link in p.video_urls[:len([url for url in p.video_urls])]:
            yt = YouTube(str(link))

            # extraindo o audio
            video = yt.streams.filter(only_audio=True).first()

            # baixando o arquivo
            out_file = video.download(output_path=diretorio)

            # salvando o arquivo
            base, ext = os.path.splitext(out_file)

            if os.path.isfile(out_file):
                new_file = base + '_1' + '.mp3'
                os.rename(out_file, new_file)
            else:
                new_file = base + '.mp3'
                os.rename(out_file, new_file)

                # Informa sucesso no download
                print(yt.title + " Foi baixado com sucesso.")


tela = TelaPython()
tela.iniciar()
