import PySimpleGUI as sg
from zip_creator import make_archive


label_files = sg.Text("Select files to compress:")
label_folder = sg.Text("Select destination folder:")
input_box_files = sg.InputText(tooltip="Enter filename")
input_box_folder = sg.InputText(tooltip="Enter destination folder")
file_button = sg.FilesBrowse("Choose", key="files")
folder_button = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Compress")
output_label = sg.Text(key="output")

window = sg.Window("File zipper", layout=[[label_files, input_box_files, file_button],
                                          [label_folder, input_box_folder, folder_button],
                                          [compress_button, output_label]])

while True:
    event, values = window.read()
    try:
        filepaths = values['files'].split(";")
    except TypeError:
        exit()
    folder = values['folder']
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")
    if event == sg.WIN_CLOSED:
        break



window.close()

