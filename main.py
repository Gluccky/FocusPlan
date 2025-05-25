import flet as ft
from components.notes import notespage


def main(page: ft.Page):
    global window_switch
    page.update()
    page.appbar=appbar
    page.add(mainwindow, notespage)  
   
    def window_switch(page):
        mainwindow.controls.append(notespage)
        notespage.visible=True 
        if mainwindow.controls:  
            mainwindow.controls.pop(0)  
        page.update()

navigationbar = ft.Container(
        ft.Column(
        controls=[
            ft.ElevatedButton(
                text="notes",
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            on_click=window_switch()
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
    expand=True,
    visible=True
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


ft.app(target=main)