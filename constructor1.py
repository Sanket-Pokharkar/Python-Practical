# This is an example of parametrized construtor
print("Hello ")
class car:
    def __init__(self, modelname, year):
        self.modelname=modelname
        self.year=year
    def dispaly(self):
        print(self.modelname,self.year)

c1=car("audi",2010)
c1.dispaly()