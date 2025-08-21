import flet as ft


def notes_switch(name: str):
        if name == "notesroutine":
            notespage.controls.append(notesroutine)
            notespage.update()
        elif name == "notesimportant":
            notespage.controls.append(notesimportant)
            notespage.update()

menubar = ft.Row(
    alignment=ft.MainAxisAlignment.CENTER,
    controls=[
        ft.ElevatedButton(
            text="Рутинные",
        bgcolor=ft.Colors.WHITE,
        on_click=lambda e: notes_switch("notesroutine")
        ),
        ft.ElevatedButton(
            text="Важные",
        bgcolor=ft.Colors.WHITE,
        on_click=lambda e: notes_switch("notesimportant")
        )
    ]
)

notesimportant = ft.Container(
    content=ft.ElevatedButton(
            text="addimportant",
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
    )
)

notesroutine = ft.Container(
    content=ft.ElevatedButton(
            text="addroutine",
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
    )
)

notespage = ft.Column(
    controls=[
        menubar,
        notesroutine
    ]
)

def notes_add():
    pass

def notes_delete():
    pass

def notes_sort():
    pass

