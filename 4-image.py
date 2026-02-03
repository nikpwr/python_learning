import flet as ft

def main(page: ft.Page):
    page.title = "Flet Information Displays Demo"
    page.window.width = 340
    page.window.height = 400

    header = ft.Text("Latest image", size=18)

    img = ft.Image(
        src="https://picsum.photos/320/320",
        #width=320,
        #height=400,        
    )
    page.add(
        header,
        img,
    )
ft.run(main)

# https://docs.flet.dev/map/image_source_attribution/?h=image