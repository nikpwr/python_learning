# uv init
# uv add flet[all]

import flet as ft

def main(page:ft.Page):
    page.title = "Hello world Flet App"
    page.window.width = 300
    page.window.height = 300
    page.add(ft.Text("Hello World, Kahville!"))

ft.run(main)
# voidaan ajaa python tiedosto.py
# tai flet run tiedosto.py
# uv run flet run tiedosto.py

# winget install --id=astral-sh.uv  -e