import PySimpleGUI as sg


def feet_to_metric(feet, inches):
    metric = float(feet) * 0.3048 + float(inches) * 0.0254
    return metric


sg.theme("black")
feet_label = sg.Text("Enter feet:")
feet_value = sg.Input(key="feet")
inches_label = sg.Text("Enter inches:")
inches_value = sg.Input(key="inches")
convert_button = sg.Button("Convert")
convert_label = sg.Text(key="msg")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor", layout=[[feet_label, feet_value],
                           [inches_label, inches_value],
                           [convert_button, exit_button,  convert_label]])
while True:
    event, values = window.read()
    if event == "Exit":
        break
    elif event == sg.WIN_CLOSED:
        break
    try:
        calculate = feet_to_metric(values['feet'], values['inches'])
        window['msg'].update(f"{calculate} m")
    except TypeError:
        break
    except ValueError:
        sg.Popup("Please provide two numbers", font=("Helvetica", 20))



window.close()