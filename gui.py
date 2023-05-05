import functions
import PySimpleGUI as sg
import time


sg.theme("LightBlue2")
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[65, 20])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My to-do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=50)
    window["clock"].update(time.strftime("%b %d, %Y %H:%M:%S"))
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.add_todos(todos)
        window['todo'].update("")
        window['todos'].update(values=todos)
    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.add_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Click on a item first to edit", font=("Helvetica", 20))
    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])
    elif event == "Complete":
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.add_todos(todos)
            window['todo'].update("")
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Click on a item first to complete a todo", font=("Helvetica", 20))
    elif event == "Exit":
        break
    elif event == sg.WIN_CLOSED:
        break


window.close()
