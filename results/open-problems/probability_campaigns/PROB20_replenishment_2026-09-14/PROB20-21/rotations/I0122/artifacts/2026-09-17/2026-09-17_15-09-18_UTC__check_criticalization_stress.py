from fractions import Fraction
import itertools

V = (0,1,2,3)
# Poset C3 + isolated point 3: 0<1<2.
rels = {(0,1),(1,2),(0,2)}

def is_linear_extension(order):
    pos = {v:i for i,v in enumerate(order)}
    return all(pos[a] < pos[b] for a,b in rels)

exts = [p for p in itertools.permutations(V) if is_linear_extension(p)]
E = len(exts)
assert E == 4

def prob_before(x,y):
    return Fraction(sum(order.index(x) < order.index(y) for order in exts), E)

def mean_rank(x):
    return Fraction(sum(order.index(x)+1 for order in exts), E)

D = {x:{z for z in V if (z,x) in rels} for x in V}
U = {x:{z for z in V if (x,z) in rels} for x in V}

def incomparable(x,y):
    return x != y and (x,y) not in rels and (y,x) not in rels

def critical(x,y):
    return incomparable(x,y) and D[x] <= D[y] and U[y] <= U[x]

mus = {x: mean_rank(x) for x in V}
critical_pairs = [(x,y) for x in V for y in V if critical(x,y)]

# Perfectly balanced noncritical pair (1,3).
assert incomparable(1,3)
assert prob_before(1,3) == Fraction(1,2)
assert mus[3] - mus[1] == 0
assert not critical(1,3)

# One legitimate criticalization step descends x from 1 to predecessor 0.
assert (0,1) in rels and incomparable(0,3)
assert critical(0,3)
assert prob_before(0,3) == Fraction(3,4)
assert mus[3] - mus[0] == Fraction(5,4)

# Symmetric upward critical pair.
assert critical(3,2)
assert prob_before(3,2) == Fraction(3,4)
assert mus[2] - mus[3] == Fraction(5,4)

print("I0122 exact criticalization stress test")
print("poset=C3 + isolated")
print("linear_extensions=", E)
for order in exts:
    print("extension", order)
print("mean_ranks", {x: str(mus[x]) for x in V})
print("balanced_noncritical_pair=(1,3)",
      "p(1<3)=", prob_before(1,3),
      "gap=", mus[3]-mus[1])
print("critical_pairs", critical_pairs)
for x,y in critical_pairs:
    print("critical", (x,y),
          f"p({x}<{y})=", prob_before(x,y),
          "expected_rank_gap=", mus[y]-mus[x])
print("criticalization (1,3)->(0,3):",
      "p 1/2 ->", prob_before(0,3),
      "gap 0 ->", mus[3]-mus[0])
print("ALL_EXACT_CHECKS_PASS")
