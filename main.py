from model import Person, FamilyModel
from view import FamilyView
from controller import FamilyController

model = FamilyModel()
view = FamilyView()
controller = FamilyController(view, model)

#generation 1
ole = model.add(Person("Ole"))
inge = model.add(Person("Inge"))
hans = model.add(Person("Hans"))
grethe = model.add(Person("Grethe"))
jens = model.add(Person("Jens"))

#generation 2
anne = model.add(Person("Anne", mother=inge, father=ole))
peter = model.add(Person("Peter", mother=grethe, father=hans))
lise = model.add(Person("Lise", mother=grethe, father=hans))

#generation 3
nikolaj = model.add(Person("Nikolaj", mother=anne, father=peter))
sofie = model.add(Person("Sofie", mother=anne, father=peter))
mads = model.add(Person("Mads", mother=lise, father=jens))


controller.show_person(nikolaj)
controller.show_person(hans)


for a, b in [(nikolaj, sofie), (nikolaj, mads), (anne, jens)]:
    controller.check_pair(a,b)

controller.show_tree()

    