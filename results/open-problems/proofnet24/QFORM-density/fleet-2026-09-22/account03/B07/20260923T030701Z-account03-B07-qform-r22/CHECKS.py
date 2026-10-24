from itertools import product
from math import sqrt, e

theta=1/16
Lambda=1.0
kappa=1/(256*sqrt(3))
alpha_gate=(1+sqrt(3)/15)**2/2
assert alpha_gate < 2/3
strict_rank_upper=225/theta
assert strict_rank_upper == 3600
core_row_lower=sqrt(theta/450)*kappa/Lambda

# Deterministic finite sanity grid for the spectral inequality.
checked=0
min_ratio=10**9
for d in range(3,8):
    for raw in product(range(1,6), repeat=d):
        lam=sorted(raw, reverse=True)
        S=sum(lam)
        T=sum(lam[2:])
        if T < theta*S:
            continue
        e2=sum(lam[i]*lam[j] for i in range(d) for j in range(i+1,d))
        e3=sum(lam[i]*lam[j]*lam[k] for i in range(d) for j in range(i+1,d) for k in range(j+1,d))
        assert T*e2 <= 3*e3 + 1e-12
        target=theta**2*S**3/6
        assert e3 + 1e-12 >= target
        min_ratio=min(min_ratio,e3/target)
        checked+=1

paid = 3456*e*Lambda*(6/theta**2)**(1/6)
print(f"alpha_gate={alpha_gate:.15f}")
print(f"kappa={kappa:.15f}")
print(f"theta={theta:.15f}")
print(f"sqrt_theta={sqrt(theta):.15f}")
print(f"strict_selected_core_rank_lt={strict_rank_upper:.0f}")
print(f"physical_core_rowcol_lower_Lambda1={core_row_lower:.15f}")
print(f"paid_constant_Lambda1={paid:.12f}")
print(f"grid_spectra_checked={checked}")
print(f"grid_min_E3_over_bound={min_ratio:.12f}")
print("STATUS=PASS")
