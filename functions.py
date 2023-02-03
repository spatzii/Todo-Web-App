FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """Return the contents of todos list from
    text file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes to-do item to list in the text file.
    Returns nothing."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


