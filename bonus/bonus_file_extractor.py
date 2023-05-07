import PySimpleGUI as sg
from zip_extractor import *

sg.theme("LightBlue2")
archive_label = sg.Text("Select archive")
archive_input = sg.Input(tooltip="Select archive")
archive_button = sg.FileBrowse("Choose", key="archive")

destination_label = sg.Text("Select destination")
destination_input = sg.Input(tooltip="Select destination")
destination_button = sg.FolderBrowse("Choose", key="destination")

extract_button = sg.Button("Extract", key="extract")
output_label = sg.Text(key="output", text_color="red")

window = sg.Window("Archive Extractor", layout=[[archive_label, archive_input, archive_button],
                                       [destination_label, destination_input, destination_button],
                                       [extract_button, output_label]], font=("Helvetica", 20))


while True:
    event, values = window.read()
    try:
        filepath = values['archive']
    except TypeError:
        exit()
    destination = values['destination']
    extract_archive(filepath, destination)
    window["output"].update(value="Extraction completed!")
    if event == sg.WIN_CLOSED:
        break
window.close()
