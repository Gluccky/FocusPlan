import flet as ft


def notes_add(e: ft.ControlEvent):
        text = e.control.value.strip()
        if notespagenotes.content == "notesroutine":
            if text:
                notesroutine.controls.append(
                    ft.Container(
                        content=ft.Text(text),
                        bgcolor=ft.Colors.AMBER_100,
                        padding=10,
                        margin=5,
                        border_radius=5
                    )
                )
        elif notespagenotes.content == "notesimportant":
            if text:
                notesimportant.controls.append(
                    ft.Container(
                        content=ft.Text(text),
                        bgcolor=ft.Colors.AMBER_100,
                        padding=10,
                        margin=5,
                        border_radius=5
                    )
                )
            e.control.value = ""
            e.control.update()
            notespagenotes.update()

input_field = ft.TextField(
        hint_text="Введите заметку и нажмите Enter",
        on_submit=notes_add
    )

def notes_switch(name: str):
        if name == "notesroutine":
            notespagenotes.content = notesroutine
            notespage.update()
        elif name == "notesimportant":
            notespagenotes.content = notesimportant
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

notesimportant = ft.Column(
    
)

notesroutine = ft.Column(
  
)



notespagenotes = ft.Container(
     content=notesroutine
)

notespage = ft.Column(
    controls=[
        menubar,
        input_field,
        notespagenotes
    ]
)


def notes_delete():
    pass

def notes_sort():
    pass

