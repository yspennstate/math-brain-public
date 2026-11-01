from itertools import product
from fractions import Fraction

M = 4  # m=2w, hence strip half-width w=2
LETTERS = ((0,0),(0,1),(1,0),(1,1))
NAMES = {(0,0):"C",(0,1):"A",(1,0):"B",(1,1):"D"}

def step(state, z):
    x, g = state
    u, v = z
    d = [0]*(M+1)
    for i in range(1, M+1):
        d[i] = (1-g[i-1]) * int(bool(d[i-1] or (x[i-1] == v)))
    xp = x[1:] + (u,)
    gp = tuple(
        [g[i+1] + d[i+2] - d[i+1] for i in range(M-1)]
        + [(1-d[M]) * int(u == v)]
    )
    assert all(q in (0,1) for q in gp)
    return xp, gp

FORMAL = [
    (bits[:M], bits[M:])
    for bits in product((0,1), repeat=2*M)
]

def apply_word(state, word):
    for z in word:
        state = step(state, z)
    return state

def is_synchronizing(word):
    out = apply_word(FORMAL[0], word)
    return all(apply_word(s, word) == out for s in FORMAL), out

# Enumerate the minimal synchronizing language through length M+1=5.
minimal = []
new_by_length = {}
for L in range(1, M+2):
    new = []
    for word in product(LETTERS, repeat=L):
        name = ''.join(NAMES[z] for z in word)
        # A word containing a previously found synchronizing factor is redundant
        # for the first-hit stopping time.
        if any(p in name for p in minimal):
            continue
        ok, _ = is_synchronizing(word)
        if ok:
            new.append(name)
    minimal.extend(new)
    new_by_length[L] = tuple(sorted(new))

assert tuple(len(new_by_length[L]) for L in range(1,6)) == (0,0,0,2,78)
assert len(minimal) == 80
assert set(new_by_length[4]) == {"AAAA","BBBB"}

patterns = frozenset(minimal)

# Build the exact prefix automaton for first occurrence of any reset pattern.
prefixes = {""}
for p in patterns:
    for k in range(1, len(p)):
        prefixes.add(p[:k])
prefixes = tuple(sorted(prefixes, key=lambda s:(len(s),s)))
index = {s:i for i,s in enumerate(prefixes)}

def hit(t):
    return any(t.endswith(p) for p in patterns)

transition = {}
for s in prefixes:
    for ch in "ABCD":
        t = s + ch
        if hit(t):
            transition[(s,ch)] = None
        else:
            transition[(s,ch)] = max(
                (p for p in prefixes if t.endswith(p)),
                key=len
            )

# Solve E_s = 1 + (1/4) sum_{ch: nonabsorbing} E_delta(s,ch)
# in exact rational arithmetic.
n = len(prefixes)
A = [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
b = [Fraction(1) for _ in range(n)]
for i,s in enumerate(prefixes):
    for ch in "ABCD":
        t = transition[(s,ch)]
        if t is not None:
            A[i][index[t]] -= Fraction(1,4)

for col in range(n):
    pivot = next(r for r in range(col,n) if A[r][col] != 0)
    if pivot != col:
        A[col], A[pivot] = A[pivot], A[col]
        b[col], b[pivot] = b[pivot], b[col]
    pv = A[col][col]
    if pv != 1:
        A[col] = [x/pv for x in A[col]]
        b[col] /= pv
    for r in range(n):
        if r == col:
            continue
        fac = A[r][col]
        if fac:
            A[r] = [A[r][c] - fac*A[col][c] for c in range(n)]
            b[r] -= fac*b[col]

E = {s:b[index[s]] for s in prefixes}

# Exact residual verification of every first-step equation.
for s in prefixes:
    rhs = Fraction(1)
    for ch in "ABCD":
        t = transition[(s,ch)]
        if t is not None:
            rhs += Fraction(1,4) * E[t]
    assert E[s] == rhs

E0 = E[""]
previous = Fraction(8*4**M + 10, 21)
assert previous == 98
assert E0 < 23 < previous

print("MODEL=TRUE_IID_BINARY_STRIP_SHARED_COLUMN_BIT")
print("M=", M, "W=", M//2)
print("FORMAL_STATES=", len(FORMAL))
for L in range(1,6):
    print(f"NEW_MINIMAL_SYNC_LENGTH_{L}={len(new_by_length[L])}")
print("TOTAL_MINIMAL_SYNC_PATTERNS=", len(patterns))
print("PREFIX_AUTOMATON_STATES=", len(prefixes))
print("LENGTH4_PATTERNS=", " ".join(new_by_length[4]))
print("LENGTH5_PATTERNS=", " ".join(new_by_length[5]))
print("E_TAU_EXACT=", E0)
print("E_TAU_DECIMAL=", f"{float(E0):.15f}")
print("E_TAU_LT_23=", E0 < 23)
print("PREVIOUS_ONE_DEFECT_CONSTANT=", previous)
print("EXACT_IMPROVEMENT=", previous - E0)
print("IMPROVEMENT_DECIMAL=", f"{float(previous-E0):.15f}")
print("RATIO_NEW_OVER_PREVIOUS=", E0 / previous)
print("ALL_EXACT_CHECKS_PASS")
