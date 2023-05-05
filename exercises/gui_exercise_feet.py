import PySimpleGUI as sg


def feet_to_metric(feet, inches):
    metric = float(feet) * 0.3048 + float(inches) * 0.0254
    return metric


feet_label = sg.Text("Enter feet:")
feet_value = sg.Input(key="feet")
inches_label = sg.Text("Enter inches:")
inches_value = sg.Input(key="inches")
convert_button = sg.Button("Convert")
convert_label = sg.Text(key="msg")

window = sg.Window("Convertor", layout=[[feet_label, feet_value],
                           [inches_label, inches_value],
                           [convert_button, convert_label]])
while True:
    event, values = window.read()
    calculate = feet_to_metric(values['feet'], values['inches'])
    window['msg'].update(f"{calculate} m")


window.close()