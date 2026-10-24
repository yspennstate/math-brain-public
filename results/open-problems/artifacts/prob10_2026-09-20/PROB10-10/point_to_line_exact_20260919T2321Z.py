from functools import lru_cache
from fractions import Fraction as F


def q(level):
    """Exact E[first directed Exp(1) passage time from 0 to x+y=level]."""
    verts = [(x, s - x) for s in range(level) for x in range(s + 1)]
    idx = {v: i for i, v in enumerate(verts)}
    start = 1 << idx[(0, 0)]

    @lru_cache(None)
    def E(mask):
        rates = {}
        absorb = 0
        for i, (x, y) in enumerate(verts):
            if not ((mask >> i) & 1):
                continue
            for w in ((x + 1, y), (x, y + 1)):
                if w[0] + w[1] == level:
                    absorb += 1
                else:
                    j = idx[w]
                    if not ((mask >> j) & 1):
                        rates[j] = rates.get(j, 0) + 1

        total = absorb + sum(rates.values())
        assert total > 0

        # Exponential memorylessness: next boundary edge rings after Exp(total).
        ans = F(1, total)
        for j, r in rates.items():
            ans += F(r, total) * E(mask | (1 << j))
        # Absorbing transitions to x+y=level have zero future cost.
        return ans

    ans = E(start)
    return ans, E.cache_info().currsize


print("PROB10-10 exact oriented point-to-line block certificate")
vals = []
for m in (1, 2, 3):
    qm, states = q(2 * m)
    cm = qm / F(m, 1)
    vals.append(cm)
    print(f"m={m}")
    print(f"q_m={qm}")
    print(f"c_m=q_m/m={cm}")
    print(f"states={states}")

assert vals[1] < vals[0]
assert vals[2] < vals[1]

# R08's old exact fixed-corner full-square m=3 certificate.
old_u3 = F(5675443731448268047, 5807171543040000000)
assert vals[2] < old_u3
print(f"old_R08_U3={old_u3}")
print(f"c3_lt_old_U3={vals[2] < old_u3}")
print("ALL_EXACT_CHECKS_PASS = True")
