import flet as ft


def main(page: ft.Page):
    page.title = "Flet Dialog Demo"
    page.window.width = 300
    page.window.height = 300
    page.window.title_bar_buttons_hidden=True # toimii vain macissa
    page.window.title_bar_hidden=True # piilotetaan minimize/maximize/close -napit

    async def handle_yes_click(e: ft.Event [ft.Button]):
        await page.window.destroy()
        
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmation"),
        content=ft.Text("Do you want to exit?"),
        actions=[
            ft.Button(content="Yes", on_click=handle_yes_click),
            ft.TextButton("No", on_click=lambda e: page.pop_dialog()),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.add(
        ft.ElevatedButton(
            "Exit",
            on_click=lambda e: page.show_dialog(dlg_modal),
        ),
    )

ft.app(target=main)