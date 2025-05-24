import flet as ft


def main(page: ft.Page):
    page.update()
    page.appbar=appbar
    page.add(mainwindow)  
      


navigationbar = ft.Container(
        ft.Column(
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
    ),
    bgcolor=ft.Colors.WHITE30
) 

workspace = ft.Container(
    bgcolor=ft.Colors.BROWN_300,
    expand=True
)

mainwindow = ft.Row(
    controls=[
        navigationbar,
        workspace
    ],
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