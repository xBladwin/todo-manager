import items

class manager(object):

    def read(self):

        tasks = open('todo.txt', 'r')

        read_lines = tasks.readlines()

        while read_line != "":
            lines = line.split(" - ")
            # check to see if items are complete or not
        tasks.close()

    def add(self, item):

        tasks = open('todo.txt', 'a')
        task.append(item.task)
        task.append(item.timestamp)
        task.append(item.complete)
        task.close()

    def complete(self):
        pass
