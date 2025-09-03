import flet as ft

homepage = ft.Container(
    ft.Column(
        controls=[
            ft.Text("Добро пожаловать", size=20)
        ]
    ),
    bgcolor=ft.Colors.BROWN_300,
    expand=True,
    visible=True
)
