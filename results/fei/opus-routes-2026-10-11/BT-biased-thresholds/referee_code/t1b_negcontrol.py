"""Real negative arms for t1: the same exact checker, with one deliberate fault each, must FAIL.
 arm A: e_i computed by averaging over the remaining coordinates under the UNIFORM law (wrong measure);
 arm B: e_i computed under mu, but the termwise comparison uses a factor 2 (wrong normalization).
 arm C: the true check (must pass)."""
import random
from fractions import Fraction as Fr
from bfcore import *
import t1_lemma41 as L

def check_variant(T, qs, order, arm):
    n = len(qs)
    Gf = gtrans([Fr(2 * t - 1) for t in T], qs)
    for k, i in enumerate(order):
        U = order[:k]
        R = [c for c in range(n) if c != i and c not in U]
        d = pivotal(T, n, i)
        m = len(U)
        e = []
        for z in range(1 << m):
            base = 0
            for b in range(m):
                if (z >> b) & 1:
                    base |= 1 << U[b]
            acc = Fr(0)
            for r in range(1 << len(R)):
                y = base; pr = Fr(1)
                for b in range(len(R)):
                    qq = Fr(1, 2) if arm == "A" else qs[R[b]]
                    if (r >> b) & 1:
                        y |= 1 << R[b]; pr *= qq
                    else:
                        pr *= 1 - qq
                acc += pr * d[y]
            e.append(acc)
        Ge = gtrans(e, [qs[c] for c in U])
        for Bl in range(1 << m):
            Bg = 0
            for b in range(m):
                if (Bl >> b) & 1:
                    Bg |= 1 << U[b]
            lhs = Gf[Bg | (1 << i)]
            rhs = 2 * Ge[Bl] if arm == "B" else Ge[Bl]
            if lhs != rhs:
                return False
    return True

random.seed(7)
res = {"A": 0, "B": 0, "C": 0}
N = 400
for t in range(N):
    n = 4
    T = [random.randint(0, 1) for _ in range(16)]
    qs = [L.rq() for _ in range(n)]
    order = random.sample(range(n), n)
    for arm in "ABC":
        if not check_variant(T, qs, order, arm):
            res[arm] += 1
print("failures out of", N, ":", res, "(A and B should fail on almost all nonconstant cases, C on none)")
