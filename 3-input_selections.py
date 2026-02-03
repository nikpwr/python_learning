import flet as ft

def main(page: ft.Page):
    page.title = "Flet Input and Selections Demo"
    page.window.width = 360
    page.window.height = 320

    name = ft.TextField(label="Name")
    agree = ft.Checkbox(label="I agree to the terms")
    level = ft.Slider(
        label="Experience level",
        min=0,
        max=10,
        divisions=10,
        value=5,
    )
    color = ft.Dropdown(
        label="Favorite color",
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    framework = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="Flet", label="Flet"),
                ft.Radio(value="Tkinter", label="Tkinter"),
                ft.Radio(value="PyQt6", label="PyQt6"),
                ft.Radio(value="PySide6", label="PySide6"),
            ]
        )
    )
    notifications = ft.Switch(label="Enable notifications", value=True)

    page.add(
        ft.Text("Fill in the form and adjust the options:"),
        name,
        agree,
        level,
        color,
        framework,
        notifications,
    )

ft.run(main)

# TextField: A common single-line or multi-line text entry control.
# Dropdown: A selection control that lets users pick a value from a list of options.
# Checkbox: A control for boolean input, often useful for preferences and agreement toggles.
# Radio: A selection radio button control commonly used inside a RadioGroup to choose a single option from a set.
# Slider: A control for selecting a numeric value along a track.
# Switch: A boolean on/off toggle.