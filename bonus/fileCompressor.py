import PySimpleGUI as sg


label_files = sg.Text("Select files to compress:")
label_folder = sg.Text("Select destination folder:")
input_box_files = sg.InputText(tooltip="Enter filename")
input_box_folder = sg.InputText(tooltip="Enter destination folder")
file_button = sg.FilesBrowse("Choose")
folder_button = sg.FolderBrowse("Choose")
compress_button = sg.Button("Compress")

window = sg.Window("File zipper", layout=[[label_files, input_box_files, file_button],
                                          [label_folder, input_box_folder, folder_button],
                                          [compress_button]])
window.read()
window.close()