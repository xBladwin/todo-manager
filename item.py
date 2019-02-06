import datetime

class item(object):

    def __init__(self, task):
        self.task = task
        self.timestamp = datetime.datetime.now()
        self.complete = False
