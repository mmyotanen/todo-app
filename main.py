# from functions import *
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.add_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        # new_todos = [item.strip('\n') for item in todos]
        for i, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{i + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()
            new_todo = input("New todo: ") + "\n"
            todos[number - 1] = new_todo
            functions.add_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            completed = int(user_action[9:])
            todos = functions.get_todos()
            index = completed - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            functions.add_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")


print("Bye!")
