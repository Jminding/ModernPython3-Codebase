class Pen:

    def __init__(self):
        self.has_ink = True
    
    def write(self, message):
        if self.has_ink:
            print(message)
        else:
            pass

my_pen = Pen()

