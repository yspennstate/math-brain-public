"""Side check for it01_check.py: sizes of the arcs grown in random order, and the arc test done a second way
(a point set is an arc iff no line of the plane, enumerated directly, carries three of its points)."""
import random
import it01_check as C

for e, poly, trials in ((3, 0b1011, 40), (4, 0b10011, 40)):
    F = C.GF2e(e, poly)
    q = F.q
    allpts = [(1, x, y) for x in range(q) for y in range(q)] + [(0, 1, x) for x in range(q)] + [(0, 0, 1)]
    lines = allpts
    rng = random.Random(100 + e)
    sizes = {}
    worst = 0
    for t in range(trials):
        order = allpts[:]
        rng.shuffle(order)
        arc = []
        for pt in order:
            if all(C.det3(F, arc[i], arc[j], pt) for i in range(len(arc)) for j in range(i + 1, len(arc))):
                arc.append(pt)
        sizes[len(arc)] = sizes.get(len(arc), 0) + 1
        for (a, b, c) in lines:
            on = sum(1 for (x, y, z) in arc if (F.mul(a, x) ^ F.mul(b, y) ^ F.mul(c, z)) == 0)
            worst = max(worst, on)
    print("q %d: %d points, sizes of %d grown arcs %s, most points of a grown arc on one line %d" % (q, len(allpts), trials, sorted(sizes.items()), worst))
