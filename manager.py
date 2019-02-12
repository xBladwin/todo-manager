import item

class Manager(item.item):

    def read():
        list_todos = open("todos.txt", "r")
        print(list_todos.readlines())
        list_todos.close()
        return todo_start()

    def add():
        list_todos = open("todos.txt", "a+")
        new_todo_name = input("What would you like to add? ")
        return(item.item.timestamp(), list_todos.write(new_todo_name), item.item.is_finished(), list_todos.write('\n'))



    def complete():
        pass


def todo_start():
    print("What would you like to do?")
    print("1. View todo's")
    print("2. Add a new todo")
    print("3. Complete a todo")
    print("To exit type quit")

    entry = input('-> ')

    if entry == '1':
        return Manager.read()
    elif entry == '2':
        return Manager.add()
    elif entry == '3':
        return Manager.complete()
    elif entry == 'quit':
        exit(0)
    else:
        print("I dont know that command...")
        return todo_start()
