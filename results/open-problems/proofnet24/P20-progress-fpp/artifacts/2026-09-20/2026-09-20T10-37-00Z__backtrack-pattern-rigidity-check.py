from fractions import Fraction
from itertools import product

# Supplementary exact sanity checker for the P20 T10 backtrack/pattern rigidity run.
# This does NOT prove asymptotic FPP strict convexity.  It checks only the finite
# pattern geometry and the deterministic l1-away identities used in the proof.

# Fixed 3x2 pattern box Lambda={0,1,2}x{0,1}.
V = [(x, y) for x in range(3) for y in range(2)]
E = set()
for u in V:
    for v in V:
        if u < v and abs(u[0]-v[0]) + abs(u[1]-v[1]) == 1:
            E.add((u, v))

u = (0, 0)
v = (2, 0)
desired_path = ((0,0),(0,1),(1,1),(2,1),(2,0))
desired = {tuple(sorted((desired_path[i], desired_path[i+1])))
           for i in range(len(desired_path)-1)}
other = E - desired
assert len(E) == 7 and len(desired) == 4 and len(other) == 3

# Enumerate all self-avoiding u-v paths in Lambda.
adj = {z: [] for z in V}
for a, b in E:
    adj[a].append(b)
    adj[b].append(a)
paths = []
def dfs(cur, seen, p):
    if cur == v:
        paths.append(tuple(p))
        return
    for w in adj[cur]:
        if w not in seen:
            dfs(w, seen | {w}, p + [w])
dfs(u, {u}, [u])

# Pattern event: desired detour edges in [1,101/100], all other edges >=10.
lo = Fraction(1, 1)
hi = Fraction(101, 100)
badlo = Fraction(10, 1)

def path_edges(p):
    return [tuple(sorted((p[i], p[i+1]))) for i in range(len(p)-1)]

def lower_cost(p):
    return sum((lo if e in desired else badlo) for e in path_edges(p))

def upper_cost(p):
    # Only called for the desired path.
    return sum((hi if e in desired else Fraction(10**9, 1)) for e in path_edges(p))

assert upper_cost(desired_path) == 4 * hi
for p in paths:
    if p == desired_path:
        continue
    assert any(e in other for e in path_edges(p))
    assert lower_cost(p) >= badlo > upper_cost(desired_path)

# For any target z, either orientation of the length-4 detour has at least one
# l1-away edge, since its endpoints are l1-distance 2 apart.
def l1(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def away_count(p, z):
    return sum(l1(p[i+1], z) == l1(p[i], z) + 1
               for i in range(len(p)-1))

for z in product(range(-10, 13), repeat=2):
    assert away_count(desired_path, z) >= 1
    assert away_count(tuple(reversed(desired_path)), z) >= 1

# Exact identity for any nearest-neighbor path p from s to t:
# away = (length + d(t,z)-d(s,z))/2.
for z in product(range(-4, 7), repeat=2):
    for p in (desired_path, tuple(reversed(desired_path))):
        ell = len(p)-1
        rhs = Fraction(ell + l1(p[-1], z) - l1(p[0], z), 2)
        assert rhs.denominator == 1
        assert away_count(p, z) == rhs

# A fixed physical edge can be one of the four desired pattern edges in at most
# two translations: two top-horizontal positions or two side-vertical positions.
fixed_edges = [((0,0),(1,0)), ((0,0),(0,1))]
for fe in fixed_edges:
    fe = tuple(sorted(fe))
    translations = set()
    for a, b in desired:
        for f0, f1 in (fe, (fe[1], fe[0])):
            dx, dy = f0[0]-a[0], f0[1]-a[1]
            if (b[0]+dx, b[1]+dy) == f1:
                translations.add((dx, dy))
    assert len(translations) <= 2

print('P20 T10 pattern/backtrack rigidity sanity')
print('vertices=', len(V), 'edges=', len(E), 'self_avoiding_u_v_paths=', len(paths))
print('desired_upper_cost=', float(upper_cost(desired_path)))
print('competing_lower_cost_min=', float(min(lower_cost(p) for p in paths if p != desired_path)))
print('away_identity_window=PASS')
print('desired-edge translate multiplicity <= 2: PASS')
print('ALL_EXACT_CHECKS_PASS=True')
