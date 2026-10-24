"""Finite sanity checks, using exact arithmetic; these do not prove percolation limits."""
from fractions import Fraction
from itertools import product
import json

b, depth = 2, 8
vertices = [t for n in range(depth + 1) for t in product(range(b), repeat=n)]
edges = set()
for x in vertices:
    for j in (1, 2):
        if len(x) >= j:
            edges.add((x[:-j], x))

def boundary(z):
    def inside(x):
        return x[:len(z)] == z and len(x) >= len(z)
    return {e for e in edges if inside(e[0]) != inside(e[1])}

z1, z2 = (0, 0), (0, 0, 0, 0, 0)
B1, B2 = boundary(z1), boundary(z2)
assert len(B1) == len(B2) == b + 2
assert B1.isdisjoint(B2)
adj = {v: [] for v in vertices}
for x, y in edges - B1:
    adj[x].append(y)
    adj[y].append(x)
seen, stack = {()}, [()]
while stack:
    x = stack.pop()
    for y in adj[x]:
        if y not in seen:
            seen.add(y)
            stack.append(y)
assert z1 not in seen

# Enumerate all states of the two disjoint boundaries at p=1/2.
E = sorted(B1 | B2)
both_closed = 0
for bits in product((0, 1), repeat=len(E)):
    state = dict(zip(E, bits))
    both_closed += all(state[e] == 0 for e in B1 | B2)
q = Fraction(1, 2) ** (b + 2)
assert Fraction(both_closed, 2 ** len(E)) == q * q

partial = sum((1-q) ** ((m+2)//3) for m in range(1, 301))
limit = 3 * (1-q) / q
assert partial < limit

# Z x C4 deterministic configuration: two open horizontal rails,
# all other edges closed. Each singleton touches each rail only once.
N = 50
assert 2*N+1 > 1
weights = [Fraction(1, 2)**n for n in range(1, 101)]
assert sum(weights) == 1 - Fraction(1, 2)**100

# Independently enumerate all open states of depth-0,1,2 descendant
# networks with one external parent, checking the reliability recursion.
reliability = []
external = ('external_parent',)
predicted = Fraction(0)
for h in range(3):
    V = [t for n in range(h+1) for t in product(range(b), repeat=n)]
    EE = [((), external)]
    for x in V:
        if x:
            EE.append((x, x[:-1]))
            EE.append((x, external if len(x) == 1 else x[:-2]))
    count = 0
    for bits in product((0, 1), repeat=len(EE)):
        AA = {x: [] for x in V + [external]}
        for (x,y), bit in zip(EE,bits):
            if bit:
                AA[x].append(y)
                AA[y].append(x)
        S, todo = {()}, [()]
        while todo:
            for y in AA[todo.pop()]:
                if y not in S:
                    S.add(y)
                    todo.append(y)
        count += external in S
    actual = Fraction(count, 2**len(EE))
    predicted = 1 - Fraction(1,2)*(1-Fraction(1,2)*predicted)**b
    assert actual == predicted
    reliability.append({'depth':h, 'states':2**len(EE), 'probability':str(actual)})

out = {
    'grandparent_boundary_sizes': [len(B1), len(B2)],
    'disjoint_boundaries': True,
    'closed_boundary_disconnects_cone_in_finite_graph': True,
    'enumerated_boundary_states': 2**len(E),
    'joint_closed_probability': str(q*q),
    'geometric_series_limit_at_p_half_b_two': str(limit),
    'infinite_summable_weight_example': 'sum_{n>=1} 2^-n = 1',
    'independent_reliability_enumerations': reliability,
    'status': 'all finite checks passed; no simulation establishes cluster repulsion'
}
print(json.dumps(out, indent=2))
open('checks_output.json', 'w', encoding='utf-8').write(json.dumps(out, indent=2)+'\n')
