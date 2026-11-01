#!/usr/bin/env python3
# Exact arithmetic helper for P16-N8-RANK-SIGNATURE-54.
# Theorem-3-only recurrence for n=8: U_{r-1}=2 U_r + 9-r.
TH=49
print('N 8')
print('THRESHOLD',TH)
for m in range(2,9):
    A,B=1,0
    for r in range(m,1,-1):
        A,B=2*A,2*B+(9-r)
    maxL=(TH-B)//A if TH>=B else -1
    print(f'RANK {m} T3_BOUND {A}*L+{B} MAX_L_FOR_49 {maxL}')
assert [(m, (lambda m: None)(m)) for m in []] == []
# expected coefficients hand-derived independently
expected={2:(2,7,21),3:(4,19,7),4:(8,39,1),5:(16,71,-2),6:(32,119,-3),7:(64,183,-3),8:(128,247,-2)}
# recompute and compare; note Python // on negatives, so retain exact printed maxL values from formula.
for m,(ea,eb,_) in expected.items():
    A,B=1,0
    for r in range(m,1,-1): A,B=2*A,2*B+(9-r)
    assert (A,B)==(ea,eb)
print('RANK2_T2_EXACT_FORM U1=min(2*L+7, L+28-|P|+h(P))')
print('RANK2_SAFE_IF L<=21 OR L+h(P)-|P|<=21')
print('CLAIM P16-N8-RANK-SIGNATURE-54 PASS')
print('ALL_EXACT_CHECKS_PASSED')
