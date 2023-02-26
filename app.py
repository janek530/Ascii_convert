import io
import PySimpleGUI as sg
import os
from photo import resize_image
from PIL import Image
def openApp():
    sg.theme("dark")

    left = [[sg.Text("Choose a file: ")],
            [sg.Text("File: "), sg.InputText(size=(45,5)), sg.FileBrowse(key='-IN-')],
            [sg.Text("Select background of image:"), sg.Radio("White", "color", key='-WHITE-'), sg.Radio("Black", "color", default=True, key='-BLACK-')],
            [sg.Text("Image Scale: "), sg.Slider(range=(50, 250), default_value=100, orientation='h', key="-SCALE-")],
            [sg.Button("Select"), sg.Button("Convert")]]


    right = [[sg.Text("Podgląd zdjęcia")],
            [sg.Image(key="-IMAGE-")]]

    layout = [[sg.Column(left),
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
        elif event == 'Convert':
            if file:
                if value['-WHITE-']==True:
                    resize_image(file, 'white', value['-SCALE-'])
                elif value['-BLACK-']==True:
                    resize_image(file, 'black', value['-SCALE-'])
            else:
                pass