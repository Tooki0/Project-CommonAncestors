from model import Person, find_common_ancestors, is_related
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