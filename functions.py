FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)

# below code will be executed only if the functions,py is run as the main python script
if __name__=="__main__":
    print ("Hello")
    
def add_todo():
    pass         