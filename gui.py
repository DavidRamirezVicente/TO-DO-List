# Importamos los módulos necesarios
import functions
import PySimpleGUI as sg
import time

# Configuración del tema de la interfaz gráfica
sg.theme("DarkBlue5")

# Definimos los elementos de la interfaz gráfica
label = sg.Text("Type in a to-do")  # Etiqueta para indicar que se debe ingresar una tarea
input_box = sg.InputText(tooltip = "Enter todo", key="todo")  # Cuadro de entrada de texto para agregar una nueva tarea
add_button = sg.Button("Add")  # Botón para agregar una nueva tarea
list_box = sg.Listbox(values = functions.get_todos(), key='todos', enable_events=True, size=[45, 10])  # Lista para mostrar las tareas pendientes
edit_button = sg.Button("Edit")  # Botón para editar una tarea seleccionada
complete_button = sg.Button("Complete")  # Botón para marcar una tarea como completada
exit_button = sg.Button("Exit")  # Botón para salir de la aplicación

# Creamos la ventana principal con todos los elementos de la interfaz gráfica
window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    # Esperamos a que ocurra un evento en la ventana
    event, values = window.read()

    # Imprimimos el evento y los valores obtenidos
    print(event)
    print(values)

    # Utilizamos un patrón "match" para manejar diferentes eventos que ocurran en la ventana
    match event:
        case "Add":  # Si se hace clic en el botón "Add"
            # Obtenemos las tareas actuales, agregamos la nueva tarea ingresada al cuadro de texto
            # y actualizamos la lista y el archivo que guarda las tareas.
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo + "\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":  # Si se hace clic en el botón "Edit"
            try:
                # Obtenemos la tarea seleccionada en la lista y la nueva tarea ingresada al cuadro de texto
                # Luego, actualizamos la tarea en la lista y en el archivo que guarda las tareas.
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup(print("Please select an item first"), font=("Helvetica", 20))

        case "Complete":  # Si se hace clic en el botón "Complete"
            try:
                # Obtenemos la tarea seleccionada en la lista
                todo_to_complete = values['todos'][0]

                todos = functions.get_todos()

                # Verificamos si la tarea está en la lista antes de intentar eliminarla
                if todo_to_complete in todos:
                    todos.remove(todo_to_complete)
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Exit":  # Si se hace clic en el botón "Exit"
            break  # Salimos del bucle while y cerramos la ventana

        case 'todos':  # Si se selecciona un elemento de la lista 'todos'
            window['todo'].update(value=values['todos'][0])  # Actualizamos el cuadro de texto con la tarea seleccionada

        case sg.WIN_CLOSED:  # Si se cierra la ventana
            break  # Salimos del bucle while y cerramos la ventana

# Cerramos la ventana cuando el bucle while termina
window.close()