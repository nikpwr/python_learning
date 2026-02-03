import flet as ft
import datetime
from hsl import getNextBusses

def main(page:ft.Page):

    def refresh(e)->None:
        print("Updating Page")
        page.update()

    timenow = datetime.datetime
    busses = getNextBusses()

    page.title = "Bus 30"
    page.bgcolor = "#ca4000"
    border_radius=ft.BorderRadius.all(20)
    page.window.width = 300
    page.window.height = 300
    
    # TO get the update working, need create ft.text and use page.update (update the variable with the new API Data

    page.add(ft.Text(f"Bus 30",size=30,color=ft.Colors.WHITE))
    
    for nextBus in busses:

        page.add(ft.Text(f"At the time of: {nextBus}",color=ft.Colors.WHITE))
    
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