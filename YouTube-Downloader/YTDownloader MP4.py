from pytube import YouTube
from os import system, path
import PySimpleGUI as psg
from time import sleep


class Window:
    def __init__(self, title: str, layout: list):
        self.title = title
        self.layout = layout

    def start(self):
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

                    progress_bar = self.window.FindElement("ProgressBar")

                    texto_progress_bar = self.window.FindElement(
                        "TextoProgressBar")

                    texto_progress_bar.Update("Baixando o arquivo!")

                    progress_bar.UpdateBar(50)

                    player_config.download(
                        values['Pasta'], filename=values["Nome"])

                    texto_progress_bar.Update("Arquivo baixado com sucesso!")

                    progress_bar.UpdateBar(100)

                    sleep(3)

                    texto_progress_bar.Update(
                        f"Sucesso!, seu arquivo está pronto!, na pasta: '{values['Pasta']}'/'{values['Nome']}.mp4'")

                    progress_bar.UpdateBar(0)

                    sleep(3)

                    texto_progress_bar.Update("")

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
        [psg.ProgressBar(100, key="ProgressBar",
                         orientation="h", size=(50, 20))],
        [psg.Text("", size=(80, 2), key="TextoProgressBar")],
        [psg.Button("Download", key="Download")]
    ]

    w1 = Window("YOUTUBE DOWNLOADER", layout)
    w1.start()

# By ViniciusDEV
