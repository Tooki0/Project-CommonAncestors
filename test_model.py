import unittest
from model import Person, FamilyModel, find_common_ancestor, is_related


class TestFamily(unittest.TestCase):
    def setUp(self):
        self.ole = Person("Ole")
        self.inge = Person("Inge")
        self.hans = Person("Hans")
        self.grethe = Person("Grethe")
        self.jens = Person("Jens")
        self.anne = Person("Anne", mother=self.inge, father=self.ole)
        self.peter = Person("Peter", mother=self.grethe, father=self.hans)
        self.lise = Person("Lise", mother=self.grethe, father=self.hans)
        self.nikolaj = Person("Nikolaj", mother=self.anne, father=self.peter)
        self.sofie = Person("Sofie", mother=self.anne, father=self.peter)
        self.mads = Person("Mads", mother=self.lise, father=self.jens)

    def test_siblings_are_related(self):
        self.assertTrue(is_related(self.nikolaj, self.sofie))

    def test_siblings_common_ancestors(self):
        common = find_common_ancestor(self.nikolaj, self.sofie)
        self.assertEqual(
            set(common),
            {self.anne, self.peter, self.ole, self.inge, self.hans, self.grethe},
        )

    def test_cousins_share_grandparents(self):
        common = find_common_ancestor(self.nikolaj, self.mads)
        self.assertEqual(set(common), {self.hans, self.grethe})

    def test_cousins_are_related(self):
        self.assertTrue(is_related(self.nikolaj, self.mads))

    def test_unrelated_persons(self):
        self.assertFalse(is_related(self.anne, self.jens))
        self.assertEqual(find_common_ancestor(self.anne, self.jens), [])

    def test_persons_without_parents(self):
        self.assertEqual(find_common_ancestor(self.ole, self.inge), [])

    def test_str(self):
        self.assertEqual(
            str(self.nikolaj),
            "Name: Nikolaj, Mother: Anne, Father: Peter",
        )
        self.assertEqual(
            str(self.hans),
            "Name: Hans, Mother: Unknown, Father: Unknown",
        )

    def test_family_model_add_returns_person(self):
        model = FamilyModel()
        person = model.add(Person("Test"))
        self.assertEqual(person.name, "Test")
        self.assertEqual(len(model.people), 1)


if __name__ == "__main__":
    unittest.main()