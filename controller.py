from model import Person, find_common_ancestor, is_related
import view

#generation 1
Ole = Person("Ole")
Inge = Person("Inge")
Hans = Person("Hans")
Grethe = Person("Grethe")
Jens = Person("Jens")

#generation 2
Anne=Person("Anne", mother=Inge, father=Ole)
Peter=Person("Peter", mother=Grethe, father=Hans)
Lise=Person("Lise", mother=Grethe, father=Hans)

#generation 3
Nikolaj=Person("Nikolaj", mother=Anne, father=Peter)
Sofie=Person("Sofie", mother=Anne, father=Peter)
Mads=Person("Mads", mother=Lise, father=Jens)

family = [Ole, Inge, Hans, Grethe, Jens, Anne, Peter, Lise, Nikolaj, Sofie, Mads]

view.show(Nikolaj)
view.show(Hans)

pairs = [(Nikolaj, Sofie), (Nikolaj, Mads), (Anne, Jens)]
for a, b in pairs:
    names = [p.name for p in find_common_ancestor(a, b)]
    view.show(f"{a.name} og {b.name}: fælles aner = {names}, "
              f"i familie = {is_related(a, b)}")
view.draw_tree(family)