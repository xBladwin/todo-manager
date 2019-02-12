import manager
import datetime

class item(object):

    def timestamp():
        list_todos = open("todos.txt", "a+")
        return list_todos.write(str(datetime.datetime.now())), list_todos.write(' ')
        list_todos.close()
