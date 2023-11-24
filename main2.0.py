# Importa el módulo 'functions' que contiene funciones personalizadas y el módulo 'time' para trabajar con fechas y horas.
import functions
import time

# Obtiene la fecha y hora actual en un formato legible.
now = time.strftime("%b %d, %Y %H:%M:%S")

# Bucle principal que permite al usuario interactuar con la aplicación de lista de tareas.
while True:
    # Solicita al usuario que ingrese un comando ('add', 'show', 'edit', 'complete', o 'exit').
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # Elimina espacios en blanco al principio y al final de la entrada del usuario.

    # Verifica si el usuario quiere agregar una tarea.
    if user_action.startswith('add'):
        todo = user_action[4:]  # Extrae la descripción de la tarea del comando del usuario.

        # Obtiene la lista de tareas existente desde el módulo 'functions'.
        todos = functions.get_todos()

        # Agrega la nueva tarea a la lista de tareas.
        todos.append(todo + '\n')

        # Escribe la lista actualizada de tareas en el archivo.
        functions.write_todos(todos)

    # Verifica si el usuario quiere mostrar la lista de tareas.
    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # Itera sobre la lista de tareas y muestra cada tarea numerada.
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    # Verifica si el usuario quiere editar una tarea.
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])  # Extrae el número de tarea a editar del comando del usuario.
            number = number - 1

            todos = functions.get_todos()

            # Solicita al usuario la nueva descripción de la tarea.
            new_todo = input("Enter a todo: ")
            todos[number] = new_todo + '\n'

            # Escribe la lista actualizada de tareas en el archivo.
            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    # Verifica si el usuario quiere marcar una tarea como completada.
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])  # Extrae el número de tarea a completar del comando del usuario.

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # Escribe la lista actualizada de tareas en el archivo.
            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."

            print(message)

        except IndexError:
            print("Not a valid index")
            continue

    # Verifica si el usuario quiere salir del programa.
    elif user_action.startswith('exit'):
        break

    # Si el usuario ingresa un comando no válido, muestra un mensaje de error.
    else:
        print("Command not valid")

# Mensaje de despedida cuando el usuario decide salir del programa.
print("Bye!")
