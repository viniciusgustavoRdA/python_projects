import PySimpleGUI as psg
import datetime as dt


class Window:
    def __init__(self, title: str, theme: str = "Dark"):
        self.title = title

        psg.theme(theme)

    def start(self):
        self.get_time()

        self.layout = [
            [psg.Text(
                f"{self.hour}:{self.minute}:{self.second}", key="clock", size=(27, 1), justification="center", background_color="gray", text_color="black", font="Consolas 32")]
        ]

        window = psg.Window(title=self.title, layout=self.layout)

        while True:
            self.get_time()

            event, values = window.read(timeout=0)

            window.find_element("clock").update(
                f"{self.hour}:{self.minute}:{self.second}")

            if event in (None, "Exit"):
                break

    def get_time(self):
        self.hour = dt.datetime.now().strftime("%H")
        self.minute = dt.datetime.now().strftime("%M")
        self.second = dt.datetime.now().strftime("%S")


w1 = Window("Horário agora")
w1.start()

# By VinciusDEV
