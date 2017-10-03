class TodoItem():
    name = ''
    state = 'No done'

    def __init__(self, name):
        self.name = name

    def toggle_done(self):
        self.state = 'Done'

    def __str__(self):
        return self.name + '   ' + self.state
