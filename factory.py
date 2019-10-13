class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{{ id: {self.id}, name: {self.name} }}'


class PersonFactory:
    id = 0

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p


pf = PersonFactory()

p1 = pf.create_person('Chris')
p2 = pf.create_person('Sarah')

print(p1)
print(p2)
