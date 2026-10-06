import matplotlib.pyplot as plt

class FamilyView:
    def show(self, text):
        print(text)

    def generation(self, person):
        parents = person.get_parents()
        if not parents:
            return 0
        return 1 + max(self.generation(p) for p in parents)

    def draw_tree(self, people):
        levels = {}
        for p in people:
            levels.setdefault(self.generation(p), []).append(p)

        pos = {}
        for g, group in levels.items():
            for i, p in enumerate(group):
                pos[p] = ((i + 1) / (len(group) + 1), -g)

        fig, ax = plt.subplots(figsize=(10,6))

        for p in people:
            for parent in p.get_parents():
                ax.plot(*zip(pos[p], pos[parent]), color="gray", zorder = 1)

        for p, (x, y) in pos.items():
            ax.text(x, y, p.name, ha='center', va='center', zorder=2, bbox=dict(boxstyle="round", fc="lightyellow"))

        ax.set_title("Family Tree")
        ax.axis("off")
        plt.show()