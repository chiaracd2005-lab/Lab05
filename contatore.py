import flet as ft

class Contatore(ft.Row):
    def __init__(self, valore_iniziale):
        super().__init__()
        self.valore = valore_iniziale
        self.alignment = ft.MainAxisAlignment.CENTER

        self.txt_valore = ft.TextField(value=str(self.valore),         #campo di testo centrale che mostra il valore corrente
                                       text_align=ft.TextAlign.CENTER,
                                       width=50,
                                       read_only=True)

        self.btn_decrementa = ft.IconButton(icon=ft.Icons.REMOVE,    #pulsante per decrementare
                                            icon_color=ft.Colors.RED,
                                            on_click=self.decrementa)

        self.btn_incrementa = ft.IconButton(icon=ft.Icons.ADD,       #pulsante per incrementare (+)
                                            icon_color=ft.Colors.GREEN,
                                            on_click=self.incrementa)

        self.controls = [self.btn_decrementa, self.txt_valore, self.btn_incrementa]

    def incrementa(self, e):
        self.valore += 1
        self.txt_valore.value = str(self.valore)
        self.txt_valore.update()

    def decrementa(self, e):
        if self.valore > 0:
            self.valore -= 1
            self.txt_valore.value = str(self.valore)
            self.txt_valore.update()

    def get_valore(self):
        return self.valore

    def reset(self, valore):
        self.valore = valore
        self.txt_valore.value = str(self.valore)
        self.txt_valore.update()