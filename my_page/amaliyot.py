
class Pen:
    holati=False
    energy=20
    def my_read(self,file):
        print(file.read())
    def chiq(self):
        if self.holati:
            self.holati=False
        else:
            self.holati=True