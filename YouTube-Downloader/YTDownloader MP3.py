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

        self.window = psg.Window(self.title, self.layout, size=(600, 200))

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

                    if not path.exists(f"{values['Pasta']}/{values['Nome']}.mp3"):

                        texto_progress_bar.Update("Baixando o arquivo!")

                        progress_bar.UpdateBar(25)

                        player_config.download(
                            values['Pasta'], filename=values["Nome"])

                        texto_progress_bar.Update(
                            "Convertendo arquivo para MP3!")

                        progress_bar.UpdateBar(50)

                        system(
                            f"ffmpeg -i '{values['Pasta']}'/'{values['Nome']}.mp4' '{values['Pasta']}'/'{values['Nome']}.mp3'")

                        texto_progress_bar.Update(
                            "Limpando arquivos desnecessários!")

                        progress_bar.UpdateBar(100)

                        system(
                            f"rm -r '{values['Pasta']}'/'{values['Nome']}.mp4'")

                        psg.Popup("Arquivo baixado com sucesso!",
                                  title="SUCESSO")

                        texto_progress_bar.Update("")

                        progress_bar.UpdateBar(0)

                    else:
                        psg.Popup(
                            f"Já existe um arquivo com o nome ({values['Nome']}.mp3) na pasta ({values['Pasta']}),\nColoque outro nome!", title="ERRO")

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
                         orientation="h", size=(60, 20))],

        [psg.Text("", size=(40, 1), key="TextoProgressBar")],

        [psg.Button("Download", key="Download", pad=(250, 0))]
    ]

    w1 = Window("YOUTUBE DOWNLOADER", layout)
    w1.start()

# BY ViniciusDEV
