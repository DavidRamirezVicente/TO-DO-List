todos = []

while True:
    user_action = input("Type add, show, edit,exit or complete: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('./venv/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('./venv/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('./venv/todos.txt', 'r') as file:
                todos = file.readlines()
            '''
            for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
            
            new_todos =[item.strip('\n') for item in todos]
            '''
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit:"))
            number = number - 1
            with open('./venv/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a todo: ")
            todos[number] = new_todo + '\n'

            with open('./venv/todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to edit:"))
            with open('./venv/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            with open('./venv/todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."

            print(message)

        case 'exit':

            break
print("Bye!")
