from model import Person, find_common_ancestor, is_related
import view

#generation 1
ole=Person("Ole", "Male")
inge=Person("Inge", "Female")
hans=Person("Hans", "Male")
grethe=Person("Grethe", "Female")
jens=Person("Jens", "Male")

#generation 2
anne=Person("Anne", mother=inge, father=ole)
peter=Person("Peter", mother=grethe, father=hans)
lise=Person("Lise", mother=grethe, father=hans)

#generation 3
nikolaj=Person("Nikolaj", mother=anne, father=peter)
sofie=Person("Sofie", mother=anne, father=peter)
mads=Person("Mads", mother=lise, father=jens)

family = [ole, inge, hans, grethe, jens, anne, peter, lise, nikolaj, sofie, mads]

view.show(nikolaj)
view.show(hans)

pairs = [(nikolaj, sofie), (nikolaj, mads), (anne, jens)]
for a, b in pairs:
    names = [p.name for p in find_common_ancestor(a, b)]
    view.show(f"{a.name} og {b.name}: fælles aner = {names}, "
              f"i familie = {is_related(a, b)}")
view.draw_tree(family)