class Person():
    def __init__(self, name, mother=None, father=None):
        self.name = name
        self.mother = mother
        self.father = father

    def __str__(self):
        mother = self.mother.name if self.mother else "Unknown"
        father = self.father.name if self.father else "Unknown"
        return f"Name: {self.name}, Mother: {mother}, Father: {father}"

    def get_parents(self):
        return [p for p in (self.mother, self.father) if p]


def ancestors(person):
    result = set()
    for parent in person.get_parents():
        result.add(parent)
        result |= ancestors(parent)
    return result


def find_common_ancestor(a, b):
    return list(ancestors(a) & ancestors(b))


def is_related(a, b):
    return len(find_common_ancestor(a, b)) > 0

class FamilyModel:
    def __init__(self):
        self.people = []

    def add(self, person):
        self.people.append(person)