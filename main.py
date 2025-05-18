import flet as ft
 
 
def main(page: ft.Page):
 
    page.title = "Flet Trello clone"
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_200
    app = TrelloApp(page)
    page.add(app)
    page.update()
 
class TrelloApp:
    def __init__(self, page: ft.Page):
        self.page = page 
        self.appbar_items = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(text="Settings")
        ]


            
ft.app(main)