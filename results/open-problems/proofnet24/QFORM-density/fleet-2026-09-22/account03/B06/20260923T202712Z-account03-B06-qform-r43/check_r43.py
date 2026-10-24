from math import sqrt

# Exact constants from REPORT.md.  This checks arithmetic only; the report has the proofs.
rank1_constant = 2 ** (11 / 4)
innovation_threshold = 2 ** -12
rank1_paid = rank1_constant / sqrt(innovation_threshold)

wmax_floor = (61 / 1728) ** (1 / 3)
partner_paid = 12 * ((1 / 4) * (wmax_floor / 64)) ** (-1 / 3)

print(f"rank1_constant={rank1_constant:.15f}")
print(f"rank1_threshold_paid={rank1_paid:.15f}")
print(f"partner_wmax_floor={wmax_floor:.15f}")
print(f"partner_sharpened_paid={partner_paid:.15f}")

assert rank1_paid < 430.539
assert wmax_floor > 0.328
assert partner_paid < 110.481

# Counterexample algebra.  For the reordered bipartite cross block
# C=[[eps,1],[1,1/eps]], det(C)=0 and ||C||_F=eps+1/eps.
for eps in (0.5, 0.25, 0.1, 0.01):
    det_c = eps * (1 / eps) - 1
    frob_sq = eps * eps + 2 + 1 / (eps * eps)
    sigma = eps + 1 / eps
    assert abs(det_c) < 1e-14
    assert abs(frob_sq - sigma * sigma) < 1e-10
    # Density lower bound from the analytic proof at t=eps/200:
    t = eps / 200
    lower = (eps / 2) * __import__('math').log(eps / (2 * t))
    assert lower > 0

print("QFORM_B06_R43_CHECK_PASS")
