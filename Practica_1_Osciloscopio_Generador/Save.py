class save:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def open(self):
        f = open(self.name, 'w')
        for i in str(len(self.data)):
            f.write(str(self.data))

        f.close()
