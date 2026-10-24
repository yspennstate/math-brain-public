from itertools import product
from math import log2

# Exact finite sanity-check for the fold/projection lemma used in R03 run57.
# For every coefficient vector v in {-2,-1,0,1,2}^n, 2<=n<=6,
# every split n=r+m, and every nonzero pivot q<r, verify
#   #Z_n(v) = sum_b #Z_r(F_b(v))
# and |projection_r Z_n(v)| <= #Z_n(v).
# This is not the proof of the theorem-sized lemma; the report contains the proof.


def zero_signs(v):
    return [eps for eps in product((-1, 1), repeat=len(v))
            if sum(e*x for e, x in zip(eps, v)) == 0]

checks = 0
for n in range(2, 7):
    for v in product((-2, -1, 0, 1, 2), repeat=n):
        if not any(v):
            continue
        zn = zero_signs(v)
        zn_count = len(zn)
        for r in range(1, n):
            m = n-r
            projected = {eps[:r] for eps in zn}
            for q in range(r):
                if v[q] == 0:
                    continue
                fold_sum = 0
                fold_union = set()
                for b in product((-1, 1), repeat=m):
                    w = list(v[:r])
                    w[q] = v[q] + sum(b[j]*v[r+j] for j in range(m))
                    zw = zero_signs(w)
                    fold_sum += len(zw)
                    fold_union.update(zw)
                assert fold_sum == zn_count
                assert fold_union == projected
                assert len(projected) <= zn_count
                checks += 1

# Exact counterexample to the pointwise first inequality in Blinovsky v7 Eq. (22).
assert len(zero_signs((1, 1, 2))) == 2
assert len(zero_signs((1, -1))) == 2

c = 0.5*log2(1/0.51) - 0.3
print(f"EXHAUSTIVE_CASES={checks}")
print("COEFFICIENT_BOX={-2,-1,0,1,2}; N_RANGE=2..6; ALL_SPLITS_AND_NONZERO_PIVOTS")
print("IDENTITY: #Z_n(v)=sum_b #Z_r(F_b(v)) : PASS")
print("PROJECTION: union_b Z_r(F_b(v))=projection_r Z_n(v) and |projection|<=#Z_n(v) : PASS")
print("BLINOVSKY_EQ22_COUNTEREXAMPLE: rho(1,1,2)=2/8=1/4; rho(1,-1)=2/4=1/2")
print(f"PAPER_SPLIT_C=0.5*log2(1/0.51)-0.3={c:.18f}")
print(f"DENSE_N2_EXPONENT_0.3C={0.3*c:.18f}")
print("SELF-CHECK PASS")
