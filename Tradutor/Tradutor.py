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
        window = psg.Window(title=self.title, layout=self.layout,
                            element_justification="center", size=(300, 350))

        while True:
            event, values = window.read()

            if event == psg.WIN_CLOSED:
                break

            try:
                translator = googletrans.Translator()

                pop_up_layout = [
                    [psg.Multiline(translator.translate(values[2], src=idiomas[values[0]],
                                                        dest=idiomas[values[1]]).text, disabled=True, size=(40, 20))]
                ]

                self.pop_up("TRADUÇÃO CONCLUÍDA!", pop_up_layout)
            except TypeError:
                psg.popup_ok(
                    "POR FAVOR, NÃO DEIXE O CAMPO DE TEXTO EM BRANCO!", title="AVISO!")

            except KeyError:
                psg.popup_ok(
                    "POR FAVOR, DIGITE LÍNGUAS VÁLIDAS!", title="ERRO!")

            except:
                psg.popup_ok("ERRO!, TENTE NOVAMENTE!", title="ERRO!")

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

    layout = [
        [psg.Text("Língua do texto....:", size=(14, 1)),
         psg.Input(size=(20, 1))],

        [psg.Text("Língua do tradutor: ", size=(14, 1)),
         psg.Input(size=(20, 1))],

        [psg.Text("Digite abaixo o texto à ser traduzido!",
                  background_color="green")],

        [psg.Multiline(size=(40, 14))],

        [psg.Button("TRADUZIR")]
    ]

    win1 = Window("Tradutor", layout)
    win1.start()
