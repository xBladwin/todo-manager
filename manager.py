import item

class manager(object):

    def read():
        listTodos = open("todos.txt", "r")
        print(listTodos.readlines())
        listTodos.close()
        return todo_start()

    def add():
        pass

    def complete():
        pass


def todo_start():
    print("What would you like to do?")
    print("1. View todo's")
    print("2. Add a new todo")
    print("3. Complete a todo")

    entry = input('-> ')

    if entry == '1':
        return manager.read()
    elif entry == '2':
        return manager.add()
    elif entry == '3':
        return manager.complete()
    else:
        print("I dont know that command...")
        return todo_start()
