import flet as ft
from components.focus_calendar import calendarpage
from components.settings import settingspage
from components.notes import notespage
from components.homepage import homepage


def main(page: ft.Page):
    def show_workspace(name: str):
        if name == "notespage":
            workspace.content = notespage
            page.update()
        elif name == "calendarpage":
            workspace.content = calendarpage
            page.update()
        elif name == "settingspage":
            workspace.content = settingspage
            page.update() 
        elif name == "homepage":
            workspace.content = homepage
            page.update()               

    navigationbar = ft.Container(
            ft.Column(
            controls=[
                ft.ElevatedButton(
                    text="notes",
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
                on_click=lambda e: show_workspace("notespage")
                ),
                ft.ElevatedButton(
                    text="calendar",
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
                on_click=lambda e: show_workspace("calendarpage")
                ),
                ft.ElevatedButton(
                    text="settings",
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
                on_click=lambda e: show_workspace("settingspage")
                )
            ]
        ),
        bgcolor=ft.Colors.WHITE30
    ) 

    workspace = ft.Container(
        content=homepage,
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
        leading=ft.IconButton(
            ft.Icons.HOME,
            on_click=lambda e: show_workspace("homepage")
        ),
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

    page.update()
    page.appbar = appbar
    page.add(mainwindow)  
ft.app(target=main)