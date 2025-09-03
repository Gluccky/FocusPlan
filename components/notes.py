import flet as ft


def edit_note(note_text: ft.Text, note_container: ft.Container):
        # заменяем Text на TextField
        text_field = ft.TextField(
            value=note_text.value,
            autofocus=True,
            expand=True,
            on_submit=lambda e: save_edit(e, note_text, text_field, note_container)
        )

        # на время редактирования заменим текст на поле ввода
        note_container.content.controls[0] = text_field
        note_container.update()

def save_edit(e: ft.ControlEvent, note_text: ft.Text, text_field: ft.TextField, note_container: ft.Container):
        new_text = (text_field.value or "").strip()
        if new_text:
            note_text.value = new_text
        # возвращаем обратно Text вместо TextField
        note_container.content.controls[0] = note_text
        note_container.update()


def delete_note(note_container: ft.Container):
    if notespagenotes.content == notesroutine:
        notesroutine.controls.remove(note_container)
        notespagenotes.update()
    elif notespagenotes.content == notesimportant:
        notesimportant.controls.remove(note_container)
        notespagenotes.update()

def notes_add(e: ft.ControlEvent, ):
        text = e.control.value.strip()
        if text:
            note_text = ft.Text(text, expand=True)
            note = ft.Container(
                  content=ft.Row(
                        controls=[
                            note_text,
                            ft.IconButton(
                                icon=ft.Icons.EDIT,
                                icon_color=ft.Colors.BLUE,
                                tooltip="Редактировать",
                                on_click=lambda ev, nt=note_text, nc=None: edit_note(nt, note)
                            ),
                            ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color=ft.Colors.RED,
                            tooltip="Удалить",
                            on_click=lambda ev, note_ref=None: delete_note(note)
                            )
                        ]
                        
                ),
                bgcolor=ft.Colors.WHITE24,
                alignment=ft.alignment.top_left,
                padding=10,
                margin=5,
                border_radius=5
            )
        if notespagenotes.content == notesroutine:
                notesroutine.controls.append(note)
                e.control.value = ""
                notespage.update()
        elif notespagenotes.content == notesimportant:
                notesimportant.controls.append(note)
                e.control.value = ""
                notespage.update()
                e.control.update()

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

notespage = ft.Container(
    ft.Column(
    controls=[
        menubar,
        input_field,
        notespagenotes
    ],
    ),
    bgcolor=ft.Colors.BLUE_100,
)


