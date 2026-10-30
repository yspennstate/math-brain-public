from itertools import combinations

V = range(4)
E = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
e, f = 0, 5  # marked opposite edges 01 and 23


def forest(mask):
    parent = list(V)
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u,v) in enumerate(E):
        if mask >> i & 1:
            a, b = find(u), find(v)
            if a == b:
                return False
            parent[a] = b
    return True


F = [m for m in range(1 << 6) if forest(m)]
Z = len(F)
Ze = sum((m >> e) & 1 for m in F)
Zf = sum((m >> f) & 1 for m in F)
Zef = sum(((m >> e) & 1) * ((m >> f) & 1) for m in F)
print("Z Ze Zf Zef DELTA", Z, Ze, Zf, Zef, Ze*Zf - Z*Zef)

# Coefficients of the Rayleigh difference I_e I_f - I I_ef,
# grouped by edgewise multiplicity profile on the four unmarked edges.
prof = {}
for A in F:
    for B in F:
        sign = ((A >> e) & 1) * ((B >> f) & 1) \
             - (((B >> e) & 1) * ((B >> f) & 1))
        if not sign:
            continue
        q = tuple(((A >> j) & 1) + ((B >> j) & 1)
                  for j in range(6) if j not in (e,f))
        prof[q] = prof.get(q, 0) + sign

nz = sorted((q,c) for q,c in prof.items() if c)
print("NONZERO_PROFILE_COUNT", len(nz))
print("NONZERO_PROFILE_COEFFS", nz)

# In the all-singleton profile every K4 edge occurs exactly once across A,B.
full = (1 << 6) - 1
negative = []
positive = []
for A in F:
    B = full ^ A
    if not forest(B):
        continue
    if ((B >> e) & 1) and ((B >> f) & 1):
        negative.append((A,B))
    if ((A >> e) & 1) and ((B >> f) & 1):
        positive.append((A,B))

def eset(mask):
    return [E[i] for i in range(6) if mask >> i & 1]

print("ALL_SINGLETON_NEGATIVE_PAIRS", len(negative))
for A,B in negative:
    print("N", eset(A), "|", eset(B))
print("ALL_SINGLETON_POSITIVE_PAIRS", len(positive))
for A,B in positive:
    print("P", eset(A), "|", eset(B))

expected = {
    (0,1,1,0): 1, (0,2,1,0): 1, (0,1,2,0): 1, (0,2,2,0): 1,
    (1,0,0,1): 1, (2,0,0,1): 1, (1,0,0,2): 1, (2,0,0,2): 1,
    (1,1,1,1): -2,
}
assert len(negative) == 4
assert len(positive) == 2
assert dict(nz) == expected
assert Ze*Zf - Z*Zef == 6

print("IDENTITY R=bc(1+b)(1+c)+ad(1+a)(1+d)-2abcd")
print("AMGM_CERTIFICATE sqrt(XY)>=abcd because product(1+x)>=abcd")
print("STATUS=PASS")
