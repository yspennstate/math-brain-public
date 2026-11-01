"""
PROB20-17 checker for run 2026-09-15T205502Z.

PROVED assertions checked:
  1. Heinz bridge:
       ||U+U*|| >= 2 ||AB||^2,
       U=A^(3/2) B^2 A^(1/2).
  2. Exact rank-one rational certificate C23 < S.
  3. Bhatia-Davis-derived middle-repeat upper relation C23 <= 2 O
     on random PSD quadruples.

UNPROVED diagnostics only:
  - ||U||^2 <= x*y
  - ||U+U*|| <= x+y
  - x+y >= 2p^2
  - x*y >= p^4

Random tests do not replace proofs.
"""
from fractions import Fraction
from collections import Counter, defaultdict
import itertools
import numpy as np


def opnorm(M):
    return np.linalg.svd(M, compute_uv=False)[0]


def psd_power(A, t):
    w, V = np.linalg.eigh(A)
    w = np.maximum(w, 0.0)
    return (V * (w**t)) @ V.conj().T


def random_pd(d, rng, complex_field=False):
    if complex_field:
        X = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
    else:
        X = rng.normal(size=(d,d))
    Q, _ = np.linalg.qr(X)
    vals = np.exp(rng.normal(0.0, 2.0, size=d))
    return Q @ np.diag(vals) @ Q.conj().T


# ---------- exact rational rank-one certificate ----------
u = [
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(20,29), Fraction(21,29)],
    [Fraction(16,21), Fraction(13,21), Fraction(4,21)],
]
scales = [Fraction(312), Fraction(52), Fraction(110), Fraction(5)]


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


g = [[abs(dot(u[i],u[j])) for j in range(4)] for i in range(4)]

assert g[0][1] == 0
assert g[0][2] == 0
assert g[0][3] == Fraction(16,21)
assert g[1][2] == Fraction(20,29)
assert g[1][3] == Fraction(13,21)
assert g[2][3] == Fraction(344,609)


def rank1_word_norm(w):
    z = Fraction(1)
    for i in w:
        z *= scales[i]
    for i,j in zip(w,w[1:]):
        z *= g[i][j]
    return z


S = sum(rank1_word_norm(w) for w in itertools.permutations(range(4)))
classes = defaultdict(Fraction)
for w in itertools.product(range(4), repeat=4):
    cnt = Counter(w)
    if sorted(cnt.values(), reverse=True) == [2,1,1]:
        repeated = next(k for k,v in cnt.items() if v == 2)
        positions = tuple(i+1 for i,z in enumerate(w) if z == repeated)
        classes[positions] += rank1_word_norm(w)

P = sum(
    (scales[i]*scales[j]*g[i][j])**2
    for i in range(4) for j in range(i+1,4)
)

assert S == Fraction(196072448000,17661)
assert classes[(1,2)] == Fraction(2009002729760,41209)
assert classes[(1,3)] == Fraction(718641054372800,225866529)
assert classes[(1,4)] == Fraction(854366656000,370881)
assert classes[(2,3)] == Fraction(1832928073600,370881)
assert classes[(2,4)] == classes[(1,3)]
assert classes[(3,4)] == classes[(1,2)]
assert P == Fraction(905839238000,52983)
assert classes[(2,3)] < S
assert classes[(2,3)] * 4 * P > S*S

print("EXACT CERTIFICATE")
print("S =", S)
print("C23 =", classes[(2,3)])
print("C23/S =", float(classes[(2,3)]/S))
print("P =", P)
print("C23/(S^2/(4P)) =", float(classes[(2,3)]*4*P/(S*S)))

# ---------- random proved/conjectural diagnostics ----------
rng = np.random.default_rng(20260915205502)
min_heinz = float("inf")
max_geom = 0.0
max_sumbridge = 0.0
min_pairsum = float("inf")
min_pairprod = float("inf")

for complex_field in (False, True):
    for d in (2,3,4,6):
        for _ in range(300):
            A = random_pd(d, rng, complex_field)
            B = random_pd(d, rng, complex_field)
            Ah = psd_power(A, 0.5)
            A3h = psd_power(A, 1.5)
            U = A3h @ B @ B @ Ah
            p = opnorm(A @ B)
            x = opnorm(A @ A @ B @ B)
            y = opnorm(A @ B @ A @ B)

            heinz = opnorm(U + U.conj().T) / (2*p*p)
            min_heinz = min(min_heinz, heinz)
            assert heinz >= 1 - 2e-9

            # UNPROVED diagnostics: record but do not assert theorem status.
            max_geom = max(max_geom, opnorm(U)**2/(x*y))
            max_sumbridge = max(max_sumbridge, opnorm(U+U.conj().T)/(x+y))
            min_pairsum = min(min_pairsum, (x+y)/(2*p*p))
            min_pairprod = min(min_pairprod, (x*y)/(p**4))

print("\nRANDOM PAIR DIAGNOSTICS")
print("proved Heinz min ratio =", min_heinz)
print("UNPROVED max ||U||^2/(xy) =", max_geom)
print("UNPROVED max ||U+U*||/(x+y) =", max_sumbridge)
print("UNPROVED min (x+y)/(2p^2) =", min_pairsum)
print("UNPROVED min xy/p^4 =", min_pairprod)

# ---------- random C23 <= 2O check ----------
def word_norm(A, w):
    M = np.eye(A[0].shape[0], dtype=A[0].dtype)
    for i in w:
        M = M @ A[i]
    return opnorm(M)


min_upper_slack = float("inf")
for _ in range(100):
    A = [random_pd(3, rng, False) for _ in range(4)]
    C23 = 0.0
    for Bidx in range(4):
        rest=[i for i in range(4) if i!=Bidx]
        for i,k in itertools.permutations(rest,2):
            C23 += word_norm(A,(i,Bidx,Bidx,k))
    O = sum(word_norm(A,(i,i,j,j)) for i in range(4) for j in range(4) if i!=j)
    ratio = 2*O/C23 if C23>0 else np.inf
    min_upper_slack=min(min_upper_slack,ratio)
    assert C23 <= 2*O + 1e-8*max(1.0,2*O)

print("\nMIDDLE-REPEAT UPPER COUPLING")
print("min 2O/C23 =", min_upper_slack)
print("All proved assertions passed.")
