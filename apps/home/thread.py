import threading

class CreateTheads(threading.Thread):

    def __init__(self, target_fun, args=None):
        super().__init__()
        self.target_fun = target_fun
        self.args = args

    def run(self):
        if self.args:
            self.target_fun(args for args in self.args)
        else:
            self.target_fun()

