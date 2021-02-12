from pytube import YouTube
from os import system, path
import PySimpleGUI as psg
import platform


class Window:
    """
    Esta classe não serve para outros projetos!
    """

    def __init__(self, title: str, layout: list):
        self.title = title
        self.layout = layout

    def start(self):
        if platform.system() != "Linux":
            psg.Popup(
                "ESTE PROGRAMA FOI FEITO PARA A PLATAFORMA LINUX!, AGUARDE ATÉ UMA PRÓXIMA ATUALIZAÇÃO!", title="ERRO")
            quit()

        self.window = psg.Window(self.title, self.layout, size=(600, 400))

        while True:
            event, values = self.window.read()

            if event == psg.WIN_CLOSED:
                psg.Popup(
                    "Codado e pensado por ViniciusDEV,\nGITHUB: https://github.com/viniciusgustavoRdA,\nAté mais!", title="OBRIGADO")
                break

            if values["Nome"] != "" and values["URL"] != "" and values["Pasta"] != "" and values["Browse"] != "":
                try:
                    player = YouTube(values['URL'])

                    player_config = player.streams.get_highest_resolution()

                    psg.Popup("Baixando o arquivo!", title="BAIXANDO")

                    player_config.download(
                        values['Pasta'], filename=values["Nome"])

                    psg.Popup("Arquivo baixado com sucesso!", title="BAIXADO")

                    psg.Popup("Convertendo arquivo para MP3!",
                              title="CONVERTENDO")

                    system(
                        f"ffmpeg -i '{values['Pasta']}'/'{values['Nome']}.mp4' '{values['Pasta']}'/'{values['Nome']}.mp3'")

                    psg.Popup("Arquivo convertido para MP3!",
                              title="CONVERTIDO")

                    psg.Popup("Limpando arquivos desnecessários!",
                              title="LIMPANDO")

                    system(f"rm -r '{values['Pasta']}'/'{values['Nome']}.mp4'")

                    psg.Popup(
                        f"Sucesso!, seu arquivo está pronto!, na pasta: '{values['Pasta']}'/'{values['Nome']}.mp3'", title="SUCESSO")

                except Exception as error:
                    print(error)
            else:
                psg.Popup("ESPAÇOS NÃO PODEM FICAR VAZIOS")


if __name__ == "__main__":
    layout = [
        [psg.Text("URL:", size=(20, 1)), psg.Input(size=(47, 1), key="URL")],
        [psg.Text("Nome (sem extensão):", size=(20, 1)),
         psg.Input(size=(47, 1), key="Nome")],
        [psg.Text("Pasta:", size=(20, 1)), psg.Input(
            size=(47, 1), key="Pasta"), psg.FolderBrowse()],
        [psg.Button("Download", key="Download")]
    ]

    w1 = Window("YOUTUBE DOWNLOADER", layout)
    w1.start()

# BY ViniciusDEV
