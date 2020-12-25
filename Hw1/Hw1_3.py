

Person = type('Person', (), {'age': 21})
P = Person()
print(P)
print(Person)
inst = isinstance(P, Person)
print(inst)
print(P.age)

