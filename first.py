class MyCat:
    def __init__(self,name):
        self.name = name
    
    def show_name(self):
        print(f"My cat's name is {self.name}")
    
x = MyCat("Appa")

print(x)
print(x.name)