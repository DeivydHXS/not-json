class Literal():
    def __init__(self, value):
        self.value = value

class Identifier():
    def __init__(self, name):
        self.name = name

class Assign():
    def __init__(self, name, value):
        self.name = name
        self.value = value