#!/usr/bin/env python3
"""Independent arithmetic audit of P16-N8-RANK-SIGNATURE-54.

Checks the Theorem-3-only recurrence U_{r-1}=2U_r+9-r for n=8,
expands it from minimal parent rank m, and derives the largest integer L
that forces U_1 <= 49. The p(P,2)=|P| identity is proved in the report from
the Frankl-Pin definition; here we check the resulting r=2 formula.
"""

threshold = 49
rows = []
for m in range(2, 9):
    # Represent U_m = L as affine pair (coef_L, const).
    a, b = 1, 0
    for r in range(m, 1, -1):
        a, b = 2*a, 2*b + 9-r
    maxL = (threshold-b)//a
    if maxL < 0:
        maxL = None
    rows.append((m, a, b, maxL))

expected = [
    (2, 2, 7, 21),
    (3, 4, 19, 7),
    (4, 8, 39, 1),
    (5, 16, 71, None),
    (6, 32, 119, None),
    (7, 64, 183, None),
    (8, 128, 247, None),
]
assert rows == expected

# For r=2, Theorem 2 contributes C(8,2)-p(P,2)+h(P) = 28-|P|+h(P)
# after a rank-two word of length L, while Theorem 3 gives 2L+7.
# Thus U1 <= min(2L+7, L+28-|P|+h(P)).
# Each term is <=49 exactly under the stated sufficient inequalities.
assert 2*21 + 7 == 49
assert 21 + 28 == 49

for m,a,b,maxL in rows:
    print(f"m={m} U1={a}*L+{b} max_L_for_U1_le_49={maxL if maxL is not None else 'none'}")
print("r2_formula=min(2L+7,L+28-|P|+h(P))")
print("sufficient_conditions=L<=21 OR L+h(P)-|P|<=21")
print("AUDIT_ARITHMETIC_PASS")
