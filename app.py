import io
import PySimpleGUI as sg
import os
from photo import resize_image
from PIL import Image
def openApp():
    sg.theme("dark")

    left = [[sg.Text("Choose a file: ")],
            [sg.Text("File: "), sg.InputText(), sg.FileBrowse(key='-IN-')],
            [sg.Button("Select")]]

    right = [sg.Text("Podglad zdjecia"),
             [sg.Image(key="-IMAGE-")]]

    layout = [[sg.Column(left),
              sg.VSeparator(),
              sg.Column(right)]]

    app = sg.Window('Ascii formater', layout, size=(800, 400))

    while True:
        event, value = app.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Select":
            file = value['-IN-']
            if os.path.exists(file):
                image = Image.open(value['-IN-'])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                app["-IMAGE-"].update(data=bio.getvalue())
                resize_image(file)

