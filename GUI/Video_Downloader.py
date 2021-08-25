import PySimpleGUI as Sg
from pytube import YouTube

Sg.theme('Kayak')


class TelaPython:
    def __init__(self):
        # Layout 
        layout = [
            [Sg.Text('URL', size=(6, 00)), Sg.Input(key='url')],
            [Sg.Text('Diretório'), Sg.Input(key='diretorio')],
            [Sg.Button('Baixar')],
            [Sg.Output(size=(60, 10))]
        ]
        # Janela
        self.janela = Sg.Window("Baixar vídeos").layout(layout)
        # Extrair os dados da tela
        self.button, self.values = self.janela.Read()
    
    def iniciar(self):
        url = self.values['url']
        diretorio = self.values['diretorio']

        yt = YouTube(url)
        path = diretorio

        # Informações do Vídeo
        print('Título do vídeo: ', yt.title)

        tamanho = float(yt.length)

        if tamanho < 60.00:
            print('Tamanho do vídeo: ', tamanho, 'segundos')
        else:
            minutos = tamanho / 60.00
            min_form = round(minutos, 2)
            print('Tamanho do vídeo: ', min_form, 'minutos')

        # Escolhendo a melhor resolução
        ys = yt.streams.get_highest_resolution()

        # Baixando
        print('Baixando...')
        ys.download(path)
        print('Download concluído!')


tela = TelaPython()
tela.iniciar()
