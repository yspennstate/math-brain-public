from itertools import product

# Exact local state machine for the r=infinity ZGB/catalyst rules.
# States: 0 vacant, 1 CO, 2 O. Graph: a-b-c with three exterior leaves
# x,y,z attached to c. All unlisted neighbors of a,b are frozen vacant.

NBR = {
    'a': ['b'],
    'b': ['a', 'c'],
    'c': ['b', 'x', 'y', 'z'],
    'x': ['c'], 'y': ['c'], 'z': ['c'],
}


def stable(s):
    for u, vs in NBR.items():
        for v in vs:
            if {s[u], s[v]} == {1, 2}:
                return False
    return True


def co(s, v, order):
    s = dict(s)
    if s[v] != 0:
        return s
    opp = [u for u in order[v] if s.get(u) == 2]
    if opp:
        # Arrival reacts with the selected O neighbor; both disappear, so
        # the arrival site remains vacant.
        s[opp[0]] = 0
        s[v] = 0
    else:
        s[v] = 1
    assert stable(s)
    return s


def o2(s, u, v, order):
    s = dict(s)
    if s[u] != 0 or s[v] != 0:
        return s
    # Attach O at each endpoint, then immediately resolve any CO reaction.
    # On the square lattice the two endpoints have no common off-edge
    # nearest neighbor. The deterministic ordering below is one realization
    # of the source's uniform random tie-breaking; the certificate conditions
    # on the corresponding auxiliary marks.
    for w in (u, v):
        if s[w] != 0:
            continue
        s[w] = 2
        opp = [z for z in order[w] if s.get(z) == 1]
        if opp:
            s[opp[0]] = 0
            s[w] = 0
    assert stable(s)
    return s


WORD = [
    ('C', 'c'), ('C', 'c'),
    ('O', 'b', 'c'),
    ('O', 'a', 'b'),
    ('C', 'b'),
    ('O', 'b', 'c'),
    ('C', 'c'), ('C', 'c'),
    ('O', 'a', 'b'),
    ('C', 'a'),
    ('C', 'b'),
]


def run_word(init, target):
    nuis = [w for w in ('x', 'y', 'z') if w != target]
    # The enumeration used for a uniform tie-break may be fixed separately
    # for each prescribed adsorption occurrence without changing its law.
    # Requiring an auxiliary U<1/4 selects the first available neighbor,
    # since there are at most four choices.
    order = {
        'a': ['b'], 'b': ['a', 'c'],
        'c': [target] + nuis + ['b'],
        'x': ['c'], 'y': ['c'], 'z': ['c'],
    }
    s = dict(init)
    assert stable(s)
    for ev in WORD:
        if ev[0] == 'C':
            s = co(s, ev[1], order)
        else:
            s = o2(s, ev[1], ev[2], order)
    return s


# 1. One target clearing works for every exterior assignment.
for target in ('x', 'y', 'z'):
    checked = 0
    for vals in product((0, 1, 2), repeat=3):
        s = {'a': 0, 'b': 0, 'c': 0,
             'x': vals[0], 'y': vals[1], 'z': vals[2]}
        if not stable(s):
            continue
        out = run_word(s, target)
        checked += 1
        assert out['a'] == out['b'] == out['c'] == 0
        assert out[target] == 0
    assert checked == 27


# 2. Clear all three exterior neighbors sequentially; each 11-word restores
# the helpers to vacancy, so the next invocation has the same hypothesis.
for vals in product((0, 1, 2), repeat=3):
    s = {'a': 0, 'b': 0, 'c': 0,
         'x': vals[0], 'y': vals[1], 'z': vals[2]}
    for target in ('x', 'y', 'z'):
        s = run_word(s, target)
    assert all(s[w] == 0 for w in ('a', 'b', 'c', 'x', 'y', 'z'))


# 3. Geometry and dependency moat for displacement D=15.
# The active gadget lies in x=-7..D+2, y=-1..1. We protect a two-layer
# rectangular moat so outside adsorption/reaction events cannot alter any
# neighbor used by the gadget.
D = 15
sync_events_per_target = len(WORD)
step_events = 3 * sync_events_per_target
write_events = 3
m = D * step_events + write_events
assert sync_events_per_target == 11
assert step_events == 33
assert m == 498

# Required seed sites relative to base r=(0,0).
seed = {
    (-7, 0): 2, (-6, 0): 2,
    (-5, 0): 0, (-4, 0): 0,
    (-3, 0): 1, (-2, 0): 1,
    (-1, 0): 0, (0, 0): 0, (1, 0): 0, (2, 0): 0,
    (0, 1): 0, (0, -1): 0, (1, 1): 0, (1, -1): 0,
}
child = {(x + D, y): v for (x, y), v in seed.items()}
assert set(seed).isdisjoint(child)

P0 = {(x, y) for x in range(-9, D + 5) for y in range(-3, 4)}
assert min(x for x, y in P0) == -9
assert max(x for x, y in P0) == 19
assert len(P0) == 29 * 7 == 203


def edge(u, v):
    return tuple(sorted((u, v)))


DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def incident_edges(P):
    E = set()
    for x, y in P:
        for dx, dy in DIRS:
            E.add(edge((x, y), (x + dx, y + dy)))
    return E


E0 = incident_edges(P0)
assert len(E0) == 442
P2 = {(x + 2 * D, y) for x, y in P0}
E2 = incident_edges(P2)
assert P0.isdisjoint(P2)
assert E0.isdisjoint(E2)  # block i and i+2 use disjoint protected clocks


# 4. Certified probability lower-bound arithmetic.
Nv = len(P0)
Ne = len(E0)
# At p=1/2: site clocks have rate 1/2 and O2-edge clocks rate 1/4.
# Total protected adsorption rate = 203/2 + 442/4 = 212 exactly.
assert 2 * Nv + Ne == 848  # four times Lambda
assert 848 == 4 * 212

# Split T=1 into m equal intervals. In each interval require exactly one
# occurrence of the prescribed desired clock and no other protected mark.
# Every desired rate is at least 1/4. Also require two independent tie
# uniforms <1/4, a conservative factor 1/16 per desired event. Therefore
#   P(good) >= (4m)^(-m) * 16^(-m) * exp(-212).
# Since e<3, exp(-212)>3^(-212), hence
#   b0=(64m)^(-m) 3^(-212).
# With m=498=2*3*83, 64m=2^7*3*83.
assert 64 * m == 31872
pow2 = 7 * m
pow3 = m + 212
pow83 = m
assert pow2 == 3486
assert pow3 == 710
assert pow83 == 498

# Elementary exact justification e<3:
# for n>=2, 1/n! <= 1/2^(n-1), strictly for n>=3, so
# e=2+sum_{n>=2}1/n! < 2+sum_{k>=1}2^-k=3.

print('PASS local synchronizer: 3 targets x 27 exterior assignments')
print('PASS triple synchronizer: all 27 exterior assignments -> all six gadget sites vacant')
print(f'PASS geometry: D={D}, events={m}, protected_sites={Nv}, incident_edges={Ne}')
print('PASS dependency: block i and i+2 have disjoint protected site and incident-edge clock sets')
print('PASS rate: Lambda=212 exactly')
print(f'CERTIFIED b0 = 1 / (2^{pow2} * 3^{pow3} * 83^{pow83}) > 0')
print('ALL_EXACT_CHECKS_PASS')
