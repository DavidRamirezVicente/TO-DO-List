# Importamos los módulos necesarios
import streamlit as st
import functions

# Inicializamos la variable 'todos' obteniendo la lista de tareas desde functions.get_todos()
todos = functions.get_todos()

# Definimos una función para agregar una nueva tarea a la lista de tareas
def add_todo():
    global todos
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

# Configuramos la apariencia de la interfaz gráfica de Streamlit
st.title("My Todo App")  # Título de la aplicación
st.subheader("This is my Todo app.")  # Subtítulo de la aplicación
st.write("This app is to increase your productivity")  # Mensaje descriptivo

# Iteramos sobre las tareas para mostrarlas en la interfaz gráfica
for index, todo in enumerate(todos):
    # Creamos un checkbox para cada tarea
    checkbox = st.checkbox(todo, key=todo)

    # Si el checkbox se marca (es decir, la tarea se completa)
    if checkbox:
        # Eliminamos la tarea completada de la lista de tareas y actualizamos el archivo que guarda las tareas.
        todos.pop(index)
        functions.write_todos(todos)

        # Eliminamos la información de sesión relacionada con esta tarea
        del st.session_state[todo]

# Creamos un cuadro de entrada de texto para agregar una nueva tarea
st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

