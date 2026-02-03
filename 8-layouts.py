import flet as ft

def main(page: ft.Page):
    page.title = "Flet Layouts Demo"
    page.window.width = 250
    page.window.height = 300

    main_layout = ft.Column(
        [
            ft.Text("1) Vertical layout:"),
            ft.ElevatedButton("Top"),
            ft.ElevatedButton("Middle"),
            ft.ElevatedButton("Bottom"),
            ft.Container(height=12),  # Spacer

            ft.Text("2) Horizontal layout:"),
            ft.Row(
                [
                    ft.ElevatedButton("Left"),
                    ft.ElevatedButton("Center"),
                    ft.ElevatedButton("Right"),
                ]
            ),
        ],
    )

    page.add(main_layout)

ft.run(main)

# Controls in this category are often described as container controls that can hold child controls. These controls enable you to arrange widgets on an app's GUI to create a well-organized and functional interface.

# Flet has many container controls. Here are some of them:

# Page: This control is the root of the control hierarchy or tree. It is also listed as an adaptive container control.
# Column: A container control used to arrange child controls in a column.
# Row: A container control used to arrange child controls horizontally in a row.
# Container: A container control that allows you to modify its size (e.g., height) and appearance.
# Stack: A container control where properties like bottom, left, right, and top allow you to place children in specific positions.
# Card: A container control with slightly rounded corners and an elevation shadow.
# By default, Flet stacks widgets vertically using the Column container.

#In this example, we use a Column object as the app's main layout. This layout stacks text labels and buttons vertically, while the inner Row object arranges three buttons horizontally. The Container object with a fixed height acts as a spacer between the vertical and horizontal sections.