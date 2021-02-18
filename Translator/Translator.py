import PySimpleGUI as psg
import googletrans


class Window:
    """
    This class is used for create a window!
    The logic of tradutor is in this class!
    """

    def __init__(self, title: str, layout: list, theme: str = "Dark"):
        self.title = title
        self.layout = layout

        psg.theme(theme)

    def start(self):
        psg.Popup(
            "Pessoas testando meus programas é incrível, obrigado!, by ViniciusDEV!", title="OBRIGADO!")

        self.window = psg.Window(title=self.title, layout=self.layout,
                                 element_justification="center", size=(400, 450))

        while True:
            event, values = self.window.read()

            if event == psg.WIN_CLOSED:
                break

            try:
                if values["ComboTexto"] != "" and values["ComboTradutor"] != "" and values["Multiline"] != "" and event == "Traduzir":
                    translator = googletrans.Translator()

                    pop_up_layout = [
                        [psg.Multiline(translator.translate(values["Multiline"], src=idiomas[values["ComboTexto"]],
                                                            dest=idiomas[values["ComboTradutor"]]).text, disabled=True, size=(40, 20))]
                    ]

                    self.pop_up("TRADUÇÃO CONCLUÍDA!", pop_up_layout)

            except TypeError:
                psg.popup_ok(
                    "POR FAVOR, NÃO DEIXE O CAMPO DE TEXTO EM BRANCO!", title="AVISO!")

            except Exception as error:
                psg.Popup(error)

    def pop_up(self, title: str, layout: list):
        pop_up_window = psg.Window(title=title, layout=layout)

        event, values = pop_up_window.read()

        del event, values


if __name__ == "__main__":
    idiomas = {
        "Português": "pt",
        "Inglês": "en",
        "Russo": "ru",
        "Francês": "fr",
        "Japonês": "ja",
        "Espanhol": "es",
        "Chinês Tradicional": "zh-tw",
        "Chinês Simplificado": "zh-cn",
        "Coreano": "ko"
    }

    lista_idiomas = sorted(["Português", "Inglês", "Russo", "Francês", "Japonês",
                            "Espanhol", "Chinês Tradicional", "Chinês Simplificado", "Coreano"])

    layout = [
        [psg.Text("Língua do texto......:", size=(16, 1), font="Liberation 12"),
         psg.Combo(lista_idiomas, enable_events=True, key="ComboTexto")],

        [psg.Text("Língua do tradutor.: ", size=(16, 1), font="Liberation 12"),
         psg.Combo(lista_idiomas, enable_events=True, key="ComboTradutor")],

        [psg.Text("Digite abaixo o texto à ser traduzido!",
                  background_color="darkgreen", font="Liberation 12")],

        [psg.Multiline(
            size=(45, 22), background_color="lightgray", key="Multiline")],

        [psg.Button("TRADUZIR", key="Traduzir")]
    ]

    win1 = Window("Tradutor", layout)
    win1.start()

# By ViniciusDEV
