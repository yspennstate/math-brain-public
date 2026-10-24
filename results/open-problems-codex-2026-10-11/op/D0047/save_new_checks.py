from pathlib import Path
p=Path('ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write('''
## 17. Additional-attempt verification record

check_new_series.py passed exact symbolic checks of (17) and the leading multiplier (18) for n=3,...,10, retaining arbitrary intervening coefficients. It computed the recursively selected nonlinear sigma series through order 9 and the gap candidate through order 7; the latter is 1-ar+a^2r^4/36-a^2r^6/675+O(r^8). The all-orders proof is Section 15, rather than extrapolation from these finite checks.

check_new_moment.py checked the regularized diffusion inequality on a grid of x, epsilon and c, and numerically integrated the elementary beta integral for c=0.01,0.1,0.5,1,2,10. Those checks are consistent with the written bound, but certify no floating-point error interval. The largest quadrature discrepancy was about 2.1e-7 near a weak endpoint singularity; the exact integral evaluation in Section 13 does not depend on numerical quadrature. External Nystrom determinants at s=0.05,0.2,0.5,1 satisfied the new upper bound. At s=0.05 the determinant gap remainder was about 1.10e-9, the proved upper bound 1.22e-6, and the exponential remainder 3.16e-5, confirming numerically that the exponential candidate fails the new bound. The explicit estimates, not numerical results, prove its exclusion. Matrices were at most 64 by 64, and all checks used negligible memory relative to the 1 GB cap.

Boundary and logical checks: beta=0 is excluded because c must be positive for discounted stopping and p>1; the a=0 sector is excluded from formal uniqueness because the leading multipliers would vanish. The power estimate allows s=0 directly. For beta>=4, p=2 and the bound becomes (s/L)^3/3. No derivative bounds are inferred from Peano asymptotics. No actual PDE solution is inferred from the formal PV recurrence. Route B has not been executed and supplies no proved residual equation.
''')
print('Additional verification record saved.')
