FILEPATH = 'todo.txt'
def get_todos(fpath=FILEPATH):
    with open(fpath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def append_todos(todo,fpath=FILEPATH):
    with open(fpath, 'a') as file:
        file.write(todo + "\n")

def write_todos(todos, fpath=FILEPATH):
    with open(fpath, 'w') as file:
        file.writelines(todos)