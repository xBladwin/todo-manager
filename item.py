import manager
import datetime

class item(object):

    def timestamp():
        list_todos = open("todos.txt", "a+")
        return list_todos.write(str(datetime.datetime.now())), list_todos.write(' ')
        list_todos.close()

    def is_finished():
        list_todos = open("todos.txt", "a+")
        print(list_todos.write("Not Finished: "))
        list_todos.close()
