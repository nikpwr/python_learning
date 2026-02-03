import flet as ft

def main(page:ft.Page):
    page.title = "Hello world Flet App"
    page.window.width = 200
    page.window.height = 100
    page.add(ft.Text("Hello World, kahville!"))

ft.run(main)

#Hot reload: uv run flet run tiedosto.py