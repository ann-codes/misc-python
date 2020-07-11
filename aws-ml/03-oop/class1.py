class Cat: 
    def __init__(self, name, age, hair_length, dispositon):
        self.name = name
        self.age = age
        self.hair_length = hair_length
        self.dispositon = dispositon
    def has_birthday(self):
        self.age += 1
    def get_groomed(self, new_hair_style):
        self.hair_length = new_hair_style


kitty = Cat("Zues", 10, "long", "grouchy")

print(kitty.name)
print(kitty.age)
print(kitty.hair_length)
print(kitty.dispositon)

kitty.has_birthday()

print(kitty.age)

kitty.get_groomed("curly")

print(kitty.hair_length)

kitty2 = Cat("Bob", 1, "purple", "lazy")
kitty3 = Cat("Punchy", 12, "short", "lazy")

cats = []

cats.append(kitty)
cats.append(kitty2)
cats.append(kitty3)

print("Printing Names ===>")
for i in range(len(cats)):
    print(cats[i].name)
