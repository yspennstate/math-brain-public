#!/usr/bin/env python3
"""
PROB20-19 descending fresh-leaf Givens theorem self-check.

This artifact is SELF-CHECK ONLY.  The theorem is proved analytically in the
corresponding report.  The Sobol screen is exploratory numerical evidence and
is NOT a proof, certificate, counterexample, or frozen-metric update.
"""
import itertools
import time
from fractions import Fraction

import numpy as np
import sympy as sp
from scipy.stats import qmc, norm

print("SELF_CHECK_ONLY=TRUE")

# 1. Exact Gaussian-regression identity for the first overlapping Givens pair.
l1, l2, a = sp.symbols("l1 l2 a", positive=True, real=True)
c, s = sp.cos(a), sp.sin(a)
varA = l1*c**2 + l2*s**2
varB = l1*s**2 + l2*c**2
covAB = (l2-l1)*s*c
reg_residual = sp.trigsimp(varB - covAB**2/varA - l1*l2/varA)
assert sp.simplify(reg_residual) == 0
print("CONDITIONAL_VARIANCE_IDENTITY=PASS")

# 2. Exact derivative identity for the folded shifted-anisotropic angular kernel.
phi, kappa, eta = sp.symbols("phi kappa eta", positive=True, real=True)
cc, ss, q = sp.cos(phi), sp.sin(phi), sp.cos(2*phi)
K = (2*sp.exp(kappa*q)*sp.cosh(eta*cc)
     + 2*sp.exp(-kappa*q)*sp.cosh(eta*ss))
rhs = (
    2*kappa*sp.sin(2*phi)
    *(sp.exp(-kappa*q)*sp.cosh(eta*ss)
      - sp.exp(kappa*q)*sp.cosh(eta*cc))
    + eta
    *(sp.exp(-kappa*q)*cc*sp.sinh(eta*ss)
      - sp.exp(kappa*q)*ss*sp.sinh(eta*cc))
)
assert sp.simplify(sp.diff(K, phi)/2 - rhs) == 0
print("FOLDED_KERNEL_DERIVATIVE_IDENTITY=PASS")

# 3. Exact rational checks of the harmonic residual formula.
pyth = [(3,4,5), (5,12,13), (7,24,25), (8,15,17), (20,21,29)]
lams = [(1,2), (2,9), (5,17), (7,11)]
exact_cases = 0
for L1,L2 in lams:
    for aa,bb,hh in pyth:
        for sign in (+1,-1):
            C = Fraction(aa,hh)
            S = Fraction(sign*bb,hh)
            assert C*C + S*S == 1
            den = Fraction(L1)*C*C + Fraction(L2)*S*S
            residual = Fraction(L1*L2,1)/den
            assert residual >= min(L1,L2)
            assert residual <= max(L1,L2)
            exact_cases += 1
print(f"EXACT_HARMONIC_CASES={exact_cases}")
print("EXACT_HARMONIC_BOUNDS=PASS")

# 4. Counterexample-first screen OUTSIDE the theorem's residual-variance safe region.
#    This is deliberately numerical and only nominates candidates for later
#    rigorous certification.
def top2sq4(X):
    sq = X*X
    part = np.partition(sq, 2, axis=1)
    return (part[:,2] + part[:,3]).mean()

bases = [
    (1,2,4,8),
    (1,2,3,5),
    (1,3,4,10),
    (1,4,5,9),
    (2,3,7,11),
]
angles = []
for aa,bb,hh in pyth:
    for sign in (+1,-1):
        angles.append((aa/hh, sign*bb/hh, (aa,sign*bb,hh)))

sampler = qmc.Sobol(d=4, scramble=True, seed=20260916)
U = sampler.random_base2(16)
Z = norm.ppf(U)

best_excess = -np.inf
best_record = None
candidate_count = 0
positive_count = 0
t0 = time.time()

for base in bases:
    for lam_tuple in set(itertools.permutations(base)):
        lam = np.array(lam_tuple, dtype=float)
        X0 = Z*np.sqrt(lam)
        fkl = top2sq4(X0)
        tr = lam.sum()

        for c1,s1,rat1 in angles:
            residual = lam[0]*lam[1]/(
                lam[0]*c1*c1 + lam[1]*s1*s1
            )
            # Only screen the complementary region not covered by Theorem 5.1.
            if residual >= lam[2] - 1e-14:
                continue

            A = c1*X0[:,0] + s1*X0[:,1]
            B = -s1*X0[:,0] + c1*X0[:,1]

            for c2,s2,rat2 in angles:
                C = c2*B + s2*X0[:,2]
                D = -s2*B + c2*X0[:,2]
                sq = np.column_stack(
                    [A*A, C*C, D*D, X0[:,3]*X0[:,3]]
                )
                part = np.partition(sq, 2, axis=1)
                frot = (part[:,2] + part[:,3]).mean()
                excess = (frot-fkl)/tr
                candidate_count += 1
                if excess > 0:
                    positive_count += 1
                if excess > best_excess:
                    best_excess = excess
                    best_record = (
                        tuple(map(int,lam)),
                        rat1, rat2,
                        float(residual),
                        float(fkl), float(frot),
                    )

elapsed = time.time()-t0
print("NUMERICAL_SCREEN_CERTIFICATE=FALSE")
print("SOBOL_SAMPLES=65536")
print(f"CONDITION_VIOLATING_CANDIDATES={candidate_count}")
print(f"SAMPLED_POSITIVE_COUNT={positive_count}")
print(f"BEST_SAMPLED_NORMALIZED_EXCESS={best_excess:.16g}")
print(f"BEST_SPECTRUM={best_record[0]}")
print(f"BEST_FIRST_GIVENS_C_S={best_record[1]}")
print(f"BEST_SECOND_GIVENS_C_S={best_record[2]}")
print(f"BEST_RESIDUAL_VARIANCE={best_record[3]:.16g}")
print(f"BEST_F_KL_SAMPLE={best_record[4]:.16g}")
print(f"BEST_F_ROT_SAMPLE={best_record[5]:.16g}")
print(f"SCREEN_SECONDS={elapsed:.3f}")
assert candidate_count == 6760
assert positive_count == 0
print("SCREEN_INTERNAL_ASSERTIONS=PASS")
print("THEOREM_STATUS=ANALYTIC_PROOF_IN_REPORT_NOT_NUMERICAL")
