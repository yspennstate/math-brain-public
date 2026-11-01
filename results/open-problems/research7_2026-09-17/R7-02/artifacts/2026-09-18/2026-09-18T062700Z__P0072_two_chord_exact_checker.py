import itertools
import collections
import sympy as sp

V = ["s", "a", "b", "c", "t"]
E = [
    ("s", "a", "sa"), ("a", "t", "at"),
    ("s", "b", "sb"), ("b", "t", "bt"),
    ("s", "c", "sc"), ("c", "t", "ct"),
    ("a", "b", "ab"), ("b", "c", "bc"),
]

def is_tree(sub):
    if len(sub) != len(V) - 1:
        return False
    parent = {v: v for v in V}
    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    def union(u, v):
        u, v = find(u), find(v)
        if u == v:
            return False
        parent[v] = u
        return True
    for u, v, _ in sub:
        if not union(u, v):
            return False
    return len({find(v) for v in V}) == 1

def path_edges(sub):
    adj = collections.defaultdict(list)
    for u, v, name in sub:
        adj[u].append((v, name))
        adj[v].append((u, name))
    prev = {"s": (None, None)}
    q = collections.deque(["s"])
    while q:
        u = q.popleft()
        if u == "t":
            break
        for v, name in adj[u]:
            if v not in prev:
                prev[v] = (u, name)
                q.append(v)
    ans = set()
    v = "t"
    while v != "s":
        u, name = prev[v]
        ans.add(name)
        v = u
    return ans

la, ra, lb, rb, lc, rc, x, y = sp.symbols(
    "la ra lb rb lc rc x y", positive=True
)
W = {
    "sa": la, "at": ra,
    "sb": lb, "bt": rb,
    "sc": lc, "ct": rc,
    "ab": x, "bc": y,
}

trees = []
for sub in itertools.combinations(E, len(V) - 1):
    if is_tree(sub):
        wt = sp.prod(W[name] for _, _, name in sub)
        trees.append((sub, wt, path_edges(sub)))
assert len(trees) == 45

Z = sp.expand(sum(wt for _, wt, _ in trees))
P = {}
for _, _, name in E:
    P[name] = sp.factor(
        sum(wt for _, wt, path in trees if name in path) / Z
    )

# General terminal-pair ratio identity on the minimal two-chord graph.
Sa = sp.factor(P["sa"] / la + P["at"] / ra)
Sb = sp.factor(P["sb"] / lb + P["bt"] / rb)
Sc = sp.factor(P["sc"] / lc + P["ct"] / rc)
assert sp.simplify(Sa - Sb) == 0
assert sp.simplify(Sb - Sc) == 0

# Balanced terminal pairs.
a, b, c = sp.symbols("a b c", positive=True)
sub_bal = {la: a, ra: a, lb: b, rb: b, lc: c, rc: c}
Zb = sp.factor(Z.subs(sub_bal))
Pb = {k: sp.factor(v.subs(sub_bal)) for k, v in P.items()}
s = a + b + c
B = (
    4*a*b*c + 2*a*b*y + 2*a*c*x + 2*a*c*y
    + a*x*y + 2*b*c*x + b*x*y + c*x*y
)
assert sp.simplify(Zb - s*B) == 0
assert sp.simplify(Pb["sa"] - a/s) == 0
assert sp.simplify(Pb["at"] - a/s) == 0
assert sp.simplify(Pb["sb"] - b/s) == 0
assert sp.simplify(Pb["bt"] - b/s) == 0
assert sp.simplify(Pb["sc"] - c/s) == 0
assert sp.simplify(Pb["ct"] - c/s) == 0
assert sp.simplify(
    Pb["ab"] - 2*a*x*(2*b*c + (b+c)*y)/(s*B)
) == 0
assert sp.simplify(
    Pb["bc"] - 2*c*y*(2*a*b + (a+b)*x)/(s*B)
) == 0

# Normalize s=1 and certify exact negative chord drifts.
cn = 1 - a - b
A = 2*b*cn + (b+cn)*y
K = 2*cn*(a+b) + y
D = 2*a*A + x*K
pab = sp.factor(Pb["ab"].subs(c, cn))
assert sp.simplify(pab - 2*a*x*A/D) == 0
assert sp.simplify((pab - x) + x**2*K/D) == 0

C = 2*a*b + (a+b)*x
L = 2*a*(b+cn) + x
D2 = 2*cn*C + y*L
pbc = sp.factor(Pb["bc"].subs(c, cn))
assert sp.simplify(D - D2) == 0
assert sp.simplify(pbc - 2*cn*y*C/D) == 0
assert sp.simplify((pbc - y) + y**2*L/D) == 0

print("TREE_COUNT=45")
print("GENERAL_TERMINAL_PAIR_RATIO_IDENTITY=PASS")
print("BALANCED_TERMINAL_PROBABILITIES=PASS")
print("TWO_CHORD_DRIFT_FACTORIZATION=PASS")
print("p_ab-x = -x^2*(2*c*(a+b)+y)/D")
print("p_bc-y = -y^2*(2*a*(b+c)+x)/D")
print("ALL_EXACT_CHECKS_PASS")
