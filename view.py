import matplotlib.pyplot as plt

def show(text):
    print(text)

def generation(person):
    parents=person.parents()
    if not parents:
        return 0
    return 1 + max(generation(p) for p in parents)

def draw_tree(people):
    levels = {}
    for p in people:
        levels.setdefault(generation(p), []).append(p)

    pos = {}
    for g, group in levels.items():
        for i, p in enumerate(group):
            pos[p] = ((i + 1) / (len(group) + 1), -g)

    fig, ax = plt.subplots(figsize=(10,6))

    for p in people:
        for parent in p.parents():
            ax.plot(*zip(pos[p], pos[parent]), color="gray", zorder = 1)

    for p, (x, y) in pos.items():
        ax.text(x, y, p.name, ha='center', va='center', zorder=2, bbox=dict(boxstyle="round", fc="lightyellow"))

    ax.set_title("Family Tree")
    ax.axis("off")
    plt.show()