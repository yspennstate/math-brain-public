from fractions import Fraction
from collections import defaultdict

# Exact self-check for the restricted d=5 complete-interface serial-bulk theorem.
# A transition (a,b,c) is admitted under the relaxed necessary degree conditions
# 0 <= r_b = 5-a-c <= b-1.  Actual simple-layer realizability adds parity,
# but proving the inequalities on this relaxed superset is stronger.

def admissible(a, b, c):
    return (a + c <= 5) and (a + b + c >= 6)

transitions = [
    (a, b, c)
    for a in range(1, 5)
    for b in range(1, 5)
    for c in range(1, 5)
    if admissible(a, b, c)
]
assert len(transitions) == 30

P = {
    (1, 1): Fraction(3, 4),
    (1, 2): Fraction(1, 4),
    (1, 3): Fraction(1, 12),
    (1, 4): Fraction(3, 4),
}
Q = {
    (1, 1): Fraction(15, 32),
    (2, 1): Fraction(1, 16),
    (3, 1): Fraction(7, 96),
    (4, 1): Fraction(3, 16),
    (4, 2): Fraction(1, 16),
    (4, 3): Fraction(1, 48),
}
ETA = Fraction(15, 32)

def val(table, key):
    return table.get(key, Fraction(0))

base_zero = []
stability_zero = []
for a, b, c in transitions:
    base_slack = (
        val(P, (b, c)) - val(P, (a, b))
        - (Fraction(1, b*c) - Fraction(b, 4))
    )
    assert base_slack >= 0, (a, b, c, base_slack)
    if base_slack == 0:
        base_zero.append((a, b, c))

    stability_slack = (
        val(Q, (b, c)) - val(Q, (a, b))
        - (Fraction(1, b*c) - Fraction(b, 4) + ETA*(b-2))
    )
    assert stability_slack >= 0, (a, b, c, stability_slack)
    if stability_slack == 0:
        stability_zero.append((a, b, c))

# Prove that the only directed cycle in the base zero-slack graph is 11->14->41->11.
nodes = {(a, b) for a, b, c in base_zero} | {(b, c) for a, b, c in base_zero}
adj = defaultdict(set)
radj = defaultdict(set)
for a, b, c in base_zero:
    u, v = (a, b), (b, c)
    adj[u].add(v)
    radj[v].add(u)

def reach(start, graph):
    seen = {start}
    stack = [start]
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen

unused = set(nodes)
sccs = []
while unused:
    u = next(iter(unused))
    comp = reach(u, adj) & reach(u, radj)
    sccs.append(comp)
    unused -= comp

nontrivial = [
    comp for comp in sccs
    if len(comp) > 1 or any(v in adj[v] for v in comp)
]
expected_cycle = {(1, 1), (1, 4), (4, 1)}
assert len(nontrivial) == 1 and nontrivial[0] == expected_cycle
assert adj[(1, 1)] & expected_cycle == {(1, 4)}
assert adj[(1, 4)] & expected_cycle == {(4, 1)}
assert adj[(4, 1)] & expected_cycle == {(1, 1)}

def word_stats(word):
    L = len(word)
    S = sum(word)
    R = sum(Fraction(1, word[i]*word[(i+1) % L]) for i in range(L))
    C = Fraction(S, 1) / R
    density = Fraction(L, S)
    rs = []
    for i, b in enumerate(word):
        a = word[(i-1) % L]
        c = word[(i+1) % L]
        r = 5-a-c
        assert 0 <= r <= b-1
        assert (b*r) % 2 == 0
        rs.append(r)
    return S, R, C, density, rs

S114, R114, C114, D114, r114 = word_stats((1, 1, 4))
assert (S114, R114, C114, D114, r114) == (
    6, Fraction(3, 2), 4, Fraction(1, 2), [0, 0, 3]
)

S1144, R1144, C1144, D1144, r1144 = word_stats((1, 1, 4, 4))
delta = Fraction(1, 2) - D1144
stability_bound = Fraction(4, 1) / (1 - Fraction(15, 4)*delta)
assert (S1144, R1144, C1144, D1144, r1144) == (
    10, Fraction(25, 16), Fraction(32, 5), Fraction(2, 5), [0, 0, 0, 0]
)
assert delta == Fraction(1, 10)
assert stability_bound == C1144

print('admissible_transitions', len(transitions))
print('base_potential_all_transitions PASS')
print('base_zero_transitions', len(base_zero), base_zero)
print('base_zero_cycle_unique_114 PASS')
print('word_114', 'S', S114, 'R', R114, 'C', C114,
      'diam_density', D114, 'r', r114)
print('base_inequality_sharp_114 PASS')
print('stability_potential_all_transitions PASS')
print('stability_zero_transitions', len(stability_zero))
print('word_1144', 'S', S1144, 'R', R1144, 'C', C1144,
      'diam_density', D1144, 'delta', delta, 'r', r1144)
print('sharp_stability_constant_15_over_32 PASS')
print('ALL_EXACT_CHECKS_PASSED')
