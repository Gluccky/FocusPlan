import flet as ft


def notes_add(e: ft.ControlEvent):
        text = e.control.value.strip()
        if text:
            notespagenotes.controls.append(
                ft.Container(
                    content=ft.Text(text),
                    bgcolor=ft.Colors.AMBER_100,
                    padding=10,
                    margin=5,
                    border_radius=5
                )
            )
            e.control.value = ""
            notespagenotes.update()

def notes_switch(name: str):
        if name == "notesroutine":
            notesbuttons.content = notesroutine
            notespage.update()
        elif name == "notesimportant":
            notesbuttons.content = notesimportant
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
        on_click=lambda e: (notespagenotes.controls.append(ft.TextField(on_submit=notes_add())), notespage.update()),
        text="addroutine",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
    )
)

notesbuttons = ft.Container(
     
)

notespagenotes = ft.Column(
     expand=True
     
)

notespage = ft.Column(
    controls=[
        menubar,
        notesbuttons,
        notespagenotes
    ]
)


def notes_delete():
    pass

def notes_sort():
    pass

