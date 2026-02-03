import flet as ft

def main(page:ft.Page):
    page.title = "Hello world Flet App"
    page.window.width = 300
    page.window.height = 300
    

    page.add(ft.ElevatedButton("ElevatedButton"))
    page.add(ft.FilledButton("FilledButton"))
    page.add(ft.FloatingActionButton(icon=ft.Icons.HELP_CENTER))



ft.run(main)