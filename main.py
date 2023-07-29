import PySimpleGUI as sg

layout = [
    [sg.Input(key='-INPUT-'), sg.Spin(['kg to lbs', 'km to miles'], key='-LIST-'),
     sg.Button('Convert', key='-CONVERT-')],
    [sg.Text('', key='-RESULT-', visible=False)]
]

window = sg.Window("Simple converter", layout)

def ConvertKgToLbs(window):
    try:
        toConvert = int(values['-INPUT-'])
        window['-RESULT-'].update(f'{toConvert} kg = {"{:.2f}".format(toConvert * 2.20462)} lbs')
        window['-RESULT-'].update(visible=True)
    except ValueError:
        print('Value error')
        window['-RESULT-'].update(f'\'{values["-INPUT-"]}\' is not a number')
        window['-RESULT-'].update(visible=True)
    return


def ConvertKmToM(window):
    try:
        toConvert = int(values['-INPUT-'])
        window['-RESULT-'].update(f'{toConvert} km = {"{:.2f}".format(toConvert * 0.6214)} miles')
        window['-RESULT-'].update(visible=True)
    except ValueError:
        print('Value error')
        window['-RESULT-'].update(f'\'{values["-INPUT-"]}\' is not a number')
        window['-RESULT-'].update(visible=True)
    return


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-" and values['-LIST-'] == "kg to lbs":
        ConvertKgToLbs(window)

    if event == "-CONVERT-" and values['-LIST-'] == "km to miles":
        ConvertKmToM(window)

window.close()
