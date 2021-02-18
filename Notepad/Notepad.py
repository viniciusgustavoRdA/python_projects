import PySimpleGUI as psg
import os


class Window:
    """
    This class isn't usable to another project!, I've used why is too organized!
    """

    def __init__(self, title, layout):
        self.title = title
        self.layout = layout
        self.file_path = ""
        self.file_name = ""

        self.events = {
            'Save': self.save_file,
            'Open': self.open_file,
            'New': self.new_file,
            'Delete': self.delete_file,
            'To upper': self.content_to_upper,
            'To lower': self.content_to_lower,
            'About': self.about
        }

        psg.theme("Dark")

    def save_file(self):
        # Verifying if the path of file isn't empty, if the path of the file isn't empty:
        if self.file_path not in (None, "", ()):
            with open(self.file_path, "w") as archive:
                # Writing in the file opened, the values putted on Input Field
                archive.writelines(self.values['InputField'])
        else:
            # Getting the name of file to create a new
            self.file_path = psg.popup_get_file(
                "Digite o nome do arquivo", save_as=True, no_window=True, file_types=(("TEXT Files", "*.txt"),))

            # If the path of file isn't empty
            if self.file_path not in (None, "", ()):
                self.file_name = os.path.basename(
                    self.file_path)  # Getting the name of the file

                self.window["FileName"].update(
                    f"File name: {self.file_name}")

    def open_file(self):
        self.file_path = psg.popup_get_file(
            "Procure o arquivo TXT", file_types=(("TEXT Files", "*.txt"),))

        if self.file_path not in (None, "", ()):
            with open(self.file_path, "r") as archive:
                self.window["InputField"].update(archive.read())

            self.file_name = os.path.basename(self.file_path)

            self.window["FileName"].update(f"File name: {self.file_name}")

    def new_file(self):
        self.file_path = psg.popup_get_file(
            "Digite o nome do arquivo", save_as=True, no_window=True, file_types=(("TEXT Files", "*.txt"),))

        if self.file_path not in (None, "", ()):
            self.file_name = os.path.basename(self.file_path)

            self.window["FileName"].update(
                f"File name: {self.file_name}")

            self.window["InputField"].update("")

    def delete_file(self):
        if self.file_path not in (None, "", ()):
            if os.path.exists(self.file_path):
                os.remove(self.file_path)

                self.file_name = ""
                self.file_path = ""

                self.window["FileName"].update("File name:")

                self.window["InputField"].update("")
            else:
                psg.popup(
                    f"O arquivo {self.file_name} não existe ainda!, aperte o botão Save para criar o arquivo!", title="ERRO!")
        else:
            psg.popup(f"Nenhum arquivo aberto!", title="ERRO!")

    def content_to_upper(self):
        self.window['InputField'].update(self.values["InputField"].upper())

    def content_to_lower(self):
        self.window['InputField'].update(self.values["InputField"].lower())

    def about(self):
        psg.popup("Notepad BY ViniciusDEV, thanks for testing!", title="ABOUT")

    def start(self):
        self.window = psg.Window(
            title=self.title, layout=self.layout, size=(600, 500))

        while True:
            event, self.values = self.window.read()

            if event == psg.WIN_CLOSED:
                break

            if event in self.events:
                self.events[event]()


menu_def = [
    ['&File', ['&New', '&Open', '&Save', '&Delete']],
    ['&Edit', ['&To upper', '&To lower']],
    ['&Help', ['&About']]
]


layout = [
    [psg.MenuBar(menu_def, key="MenuBar", background_color="gray",
                 text_color="white", font="Comic 10 bold")],
    [psg.Text("File name: ", key="FileName", size=(30, 1),
              background_color="gray", text_color="white", font="Comic")],
    [psg.Multiline(size=(600, 500), key="InputField",
                   background_color="gray", text_color="white", font="Comic")]
]

win = Window("Notepad", layout)

win.start()

# By ViniciusDEV
