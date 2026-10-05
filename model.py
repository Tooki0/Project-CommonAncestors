class Person():
    def __init__(self, name, mother=None, father=None):
        self.name = name 
        self.mother = mother
        self.father = father

    def __str__(self):
        mother=self.mother.name if self.mother else "Unknown"
        father=self.father.name if self.father else "Unknown"
        return f"Name: {self.name}, Mother: {mother}, Father: {father}"
    
    def get_parents(self):
        return [p for p in (self.mother, self.father) if p]

    def ancenstors(self):
        result = set()
        for parent in person.parent():
            result.add(parent)
            return result 

        
