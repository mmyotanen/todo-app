import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
# exit_button =

window = sg.Window("My to-do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()