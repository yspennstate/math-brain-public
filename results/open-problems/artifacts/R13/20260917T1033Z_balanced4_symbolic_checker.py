from fractions import Fraction as F
from functools import lru_cache
from itertools import product

SIGNS = [(1,) + x for x in product((-1, 1), repeat=3)]

# Positive diagonal weights lambda_j=a_j/16, sum a_j=16.
WEIGHTS = []
for a in range(1, 14):
    for b in range(1, 15-a):
        for c in range(1, 16-a-b):
            d = 16-a-b-c
            if d >= 1:
                WEIGHTS.append((a,b,c,d))
assert len(WEIGHTS) == 455

def set_partitions(n):
    out, blocks = [], []
    def rec(i):
        if i == n:
            out.append(tuple(tuple(b) for b in blocks))
            return
        for b in blocks:
            b.append(i); rec(i+1); b.pop()
        blocks.append([i]); rec(i+1); blocks.pop()
    rec(0)
    return out

PARTITIONS = set_partitions(8)
assert len(PARTITIONS) == 4140

def orientation_options(block):
    k = len(block)
    for tail in product((-1,1), repeat=k-1):
        sig = (1,) + tail
        yield tuple(sig[j]*(block[j]+1) for j in range(k))

def oriented_vectors(key):
    out = []
    for z in key:
        sg = 1 if z > 0 else -1
        s = SIGNS[abs(z)-1]
        out.append(tuple(sg*x for x in s))
    return out

@lru_cache(None)
def block_lb(key, a):
    # Exact lower bound L_B(lambda) from all nonempty subset sums.
    vecs = oriented_vectors(key)
    k = len(vecs)
    best = F(0)
    for mask in range(1, 1 << k):
        q = mask.bit_count()
        v = [0,0,0,0]
        for i,t in enumerate(vecs):
            if (mask >> i) & 1:
                for j in range(4):
                    v[j] += t[j]
        if v == [0,0,0,0]:
            return None  # block constraints infeasible
        den = 16 * sum(F(v[j]*v[j], a[j]) for j in range(4))
        val = F(q*q, 1) / den
        if val > best:
            best = val
    return best

def check_residue(r):
    # Symbolic balanced budgets:
    # C_j(q)=q+1 for j<r and q otherwise, q>=1;
    # T(q)=3(4q+r)/4.
    #
    # For lambda_j=a_j/16 and s=sum_{j<r}lambda_j,
    # R_q=(q+s)/(3q+3r/4) lies between R_1 and 1/3.
    # So it suffices to certify L >= max(R_1,1/3).
    C1 = tuple(2 if j < r else 1 for j in range(4))
    T1 = F(3*(4+r), 4)
    count = 0
    min_margin = None
    worst = None

    for part in PARTITIONS:
        opts = [tuple(orientation_options(b)) for b in part]
        for keys in product(*opts):
            count += 1
            ok = False
            best_margin = None
            best_a = None
            for a in WEIGHTS:
                total = F(0)
                infeasible = False
                for key in keys:
                    lb = block_lb(key, a)
                    if lb is None:
                        infeasible = True
                        break
                    total += lb
                if infeasible:
                    ok = True
                    best_margin = None
                    best_a = a
                    break

                rhs_q1 = F(sum(a[j]*C1[j] for j in range(4)), 16) / T1
                target = max(F(1,3), rhs_q1)
                margin = total - target
                if best_margin is None or margin > best_margin:
                    best_margin, best_a = margin, a
                if margin >= 0:
                    ok = True
                    break

            if not ok:
                print("FAIL residue", r, "count", count, "part", part,
                      "keys", keys, "best_margin", best_margin, "a", best_a)
                raise SystemExit(1)

            if best_margin is not None and (min_margin is None or best_margin < min_margin):
                min_margin = best_margin
                worst = (part, keys, best_a)

    print("PASS residue", r, "configs", count,
          "min_chosen_margin", min_margin, "witness", worst)
    return count

counts = [check_residue(r) for r in range(4)]
assert counts == [75905]*4

# Exact envelope comparisons against the immediately preceding R13 envelope.
def old_F2(n):
    from math import ceil
    return min(
        F(3)*ceil(n/4),
        F(4)*ceil(n/5),
        F(9,2)*ceil(n/6),
        F(21,4)*ceil(n/7),
        F(6)*ceil(n/8),
        F(27,4)*ceil(n/9),
    )

old_small = {4:F(3), 5:F(4), 6:F(9,2), 7:F(21,4), 8:F(6), 9:F(27,4)}
strict = []
equal = []
for n in range(4,75):
    new = F(3*n,4)
    if n <= 9:
        old = old_small[n]
    elif n <= 72:
        old = old_F2(n)
    elif n == 73:
        old = F(55)
    else:
        old = F(56)
    if new < old:
        strict.append(n)
    elif new == old:
        equal.append(n)
    else:
        raise AssertionError((n,new,old))

# n=75: new squared bound 225/4 beats 18*pi using pi>223/71.
assert F(225,4) < 18*F(223,71)
strict.append(75)

# At n=76 the finite 3n/4 bound loses to the universal constant:
# 18*pi < 57 using pi<22/7.
assert 18*F(22,7) < F(57)

print("STRICT_IMPROVEMENTS", len(strict), strict)
print("EQUAL_RETAINED", len(equal), equal)
print("CROSSOVER: finite 3n/4 wins through n=75; universal 18*pi wins from n=76")
print("ALL_EXACT_CHECKS_PASS")
