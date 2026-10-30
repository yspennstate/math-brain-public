from fractions import Fraction

# Exact regression 1: generic defect/arity selector.
# If epsilon is the endpoint minority and q_i are m canonical outward
# minority events, exact transport gives sum_i q_i >= 1-2 epsilon.
# Thus max(epsilon,q_i) >= 1/(m+2).
for m in (1, 2, 3):
    c = Fraction(1, m + 2)
    D = 60
    for en in range(D + 1):
        eps = Fraction(en, D)
        small = [Fraction(q, D) for q in range(D + 1) if Fraction(q, D) < c]
        if eps < c:
            max_sum = m * max(small) if small else Fraction(0)
            assert max_sum < 1 - 2 * eps

# Exact regression 2: fleet02/B19 prime comparable-fringe 2-cycle.
covers = [(0,1),(0,5),(1,2),(1,6),(1,10),(2,3),(4,1),(4,5),
          (5,3),(5,6),(6,7),(8,9),(8,0),(9,5),(9,10),(10,3),(10,7)]
n = 11
rel = set(covers)
changed = True
while changed:
    old = len(rel)
    rel |= {(a,c) for a,b in tuple(rel) for bb,c in tuple(rel) if b == bb}
    changed = len(rel) != old
pred = [0] * n
for a,b in rel:
    pred[b] |= 1 << a

exts = []
def enum(mask, seq):
    if len(seq) == n:
        exts.append(tuple(seq))
        return
    for v in range(n):
        if not (mask >> v) & 1 and pred[v] & ~mask == 0:
            enum(mask | (1 << v), seq + [v])
enum(0, [])
assert len(exts) == 515

def counts(x, y, d, u):
    vals = {"eps":0, "alpha":0, "beta":0, "overlap":0}
    for e in exts:
        p = {v:i for i,v in enumerate(e)}
        A = p[y] < p[x]
        L = p[x] < p[d]
        R = p[u] < p[y]
        vals["eps"] += A
        vals["alpha"] += L
        vals["beta"] += R
        vals["overlap"] += L and R
    return vals

A = counts(5,10,1,6)
B = counts(10,6,5,3)
assert A == {"eps":141, "alpha":128, "beta":161, "overlap":56}
assert B == {"eps":161, "alpha":141, "beta":88, "overlap":36}
assert max(A["eps"], A["alpha"], A["beta"]) * 4 >= 515
assert max(B["eps"], B["alpha"], B["beta"]) * 4 >= 515

print("GENERIC_THRESHOLDS", {m: str(Fraction(1,m+2)) for m in (1,2,3)})
print("B19_EXTENSIONS", len(exts))
print("B19_CYCLE_A", A)
print("B19_CYCLE_B", B)
print("B19_MIN_ENDPOINT_MINOR", str(Fraction(min(A["eps"],B["eps"]),515)))
print("POS3_DEFECT_ARITY_SELECTOR_CHECK_PASS")
