import flet as ft
import datetime
from ticker import retrieveGoldPrice

def main(page:ft.Page):

    def refresh(e)->None:
        print("Updating Page")
        page.update()

    timenow = datetime.datetime
    priceinfo = retrieveGoldPrice()
    page.title = "Gold Price"
    page.bgcolor = "black"
    
    page.window.width = 300
    page.window.height = 300
    page.add(ft.Text(f"Price {priceinfo['price']}",color=ft.Colors.WHITE))
    page.add(ft.Text(f"At the time of: {priceinfo['date']}",color=ft.Colors.WHITE))
    page.add(ft.Text(f"Source is {priceinfo['source']}",color=ft.Colors.WHITE))
    cont = ft.Container(
        content = ft.Button("Refresh",on_click=refresh),
        alignment = ft.Alignment.CENTER
    )
    page.add(cont)

ft.run(main)



# voidaan ajaa python tiedosto.py
# tai flet run tiedosto.py
# uv run flet run tiedosto.py

# winget install --id=astral-sh.uv  -e