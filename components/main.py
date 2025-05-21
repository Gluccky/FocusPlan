import flet as ft


def main(page: ft.Page):
    t = ft.Text(value="FocusPlan", color="green")
    page.controls.append(t)
    page.update()
    page.add(navigationbar)  
      

navigationbar = ft.Column(
    controls=[
        ft.ElevatedButton(
            text="sds",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
        )
    ]
)



def search_button():
    def search():
        pass

def save_button():
    def safe():
        pass

def exit_button():
    def exit():
        pass

def data_export_button():
    def data_export():
        pass

def data_import_button():
    def data_import():
        pass


ft.app(main)