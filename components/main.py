import flet as ft


def main(page: ft.Page):
    page.update()
    page.add(navigationbar, workspace, appbar)  
      

navigationbar = ft.Column(
    controls=[
        ft.ElevatedButton(
            text="notes",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
        ),
        ft.ElevatedButton(
            text="calendar",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
        ),
        ft.ElevatedButton(
            text="settings",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
        )
    ]
)

workspace = ft.Row(
        controls=[ft.Container(
        content=ft.Text("workspace"),
        bgcolor=ft.Colors.AMBER_100,
        expand=True,
        padding=20 
    )],
    expand=True
)

appbar = ft.AppBar(
    title=ft.Row(
        controls=[
            ft.IconButton(ft.Icons.SEARCH)    
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    bgcolor=ft.Colors.GREY_100,
    actions=[
        ft.IconButton(ft.Icons.SETTINGS)
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