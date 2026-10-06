from model import find_common_ancestor, is_related

class FamilyController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def show_person(self, person):
        self.view.show(person)

    def check_pair(self, a, b):
        names = [p.name for p in find_common_ancestor(a, b)]
        self.view.model(f"{a.name} og {b.name}: fælles aner = {names}, "
                        f"i familie = {is_related(a,b)}")

    def show_tree(self):
        self.view.draw_tree(self.model.people)

