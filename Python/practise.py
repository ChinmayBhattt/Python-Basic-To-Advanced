class Chk:
    def __init__(self, name, age):
        self.name = name
        self.age = age

c = Chk("np", 23)
print(c.__dict__)
print(help(Chk))