# account02/B17 — finite-compound-Poisson fragment no-escape theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `QFORM-B17-20260922T144511Z-9b3d6a`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `NEW SUPPORTING THEOREM / SOURCE-VALID NON-LINDEBERG STRESS / FULL CONJECTURE OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source state

The target remains unrestricted: for every dimension, every vector of independent real coordinates with probability densities at most one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential-density bound for `X^T A X`, or give a valid counterexample. No moment, support, centering, sign, or post-rotation independence hypothesis is added here.

This run applies the completed partner theorem from `account03/B17`, canonical report `yspennstate/math-open-problems@3d0926c161ba4cbea4016bff63d89e34f87cb0e6`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/account03-B17-20260922T140220Z-r11/REPORT.md`: if `Y~N(m,Sigma)`, `Sigma >= v I`, and a symmetric quadratic form has at least three eigenvalues in modulus at least one, then its density is continuous and bounded by `1/(2 sqrt(2) v)`. In particular, at `v=1/12` the bound is `3 sqrt(2)` for arbitrary Gaussian mean.

The live correction `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1` is explicitly respected. The construction below is one source-valid finite-fragment stress class; it is **not** asserted to reduce arbitrary cap-one marginals to a uniformly bounded number of fragments.

## 2. Source-valid rare-fragment triangular arrays

Fix a bank `j`. Choose finitely many rates `alpha_(j,r)>0` and pairwise distinct nonzero offsets `b_(j,r)`. Put

`alpha_j = sum_r alpha_(j,r)`.

For all sufficiently large integers `m`, define the disjoint set

`E_(j,m) = I_(j,m) union (union_r F_(j,r,m))`,

where

`I_(j,m)=[-(1-alpha_j/m)/2,(1-alpha_j/m)/2]`

and

`F_(j,r,m)=[b_(j,r) sqrt(m)-alpha_(j,r)/(2m), b_(j,r) sqrt(m)+alpha_(j,r)/(2m)]`.

The density

`f_(j,m)=1_(E_(j,m))`

is an exact probability density bounded by one, because the total length is

`1-alpha_j/m + sum_r alpha_(j,r)/m = 1`.

Let `X_(j,1)^(m),...,X_(j,m)^(m)` be iid with this density and define

`S_(j,m)=m^(-1/2) sum_(k=1)^m X_(j,k)^(m)`.

Take three independent banks and the exact target matrix

`A_m = diag(J_m/m, J_m/m, -J_m/m)`.

Its nonzero spectrum is exactly `{1,1,-1}` and

`Q_m = X^T A_m X = S_(1,m)^2 + S_(2,m)^2 - S_(3,m)^2`.

Thus every finite member is an actual target-admissible product source; no rotated independence is assumed.

## 3. Exact limit theorem

### Theorem 3.1 — finite-compound-Poisson fragment limit

For each bank,

`S_(j,m) => Z_j + M_j`,

where `Z_j~N(0,1/12)`,

`M_j = sum_r b_(j,r) N_(j,r)`,

and the `N_(j,r)` are independent `Poisson(alpha_(j,r))`; all Gaussian and Poisson variables, and all three banks, are mutually independent. Consequently

`Q_m => Q_infty=(Z_1+M_1)^2+(Z_2+M_2)^2-(Z_3+M_3)^2`.

#### Proof

Write `sinc(u)=sin(u)/u`. For one bank, the characteristic function of one normalized physical summand is exactly

`psi_m(t)
 = (1-alpha/m) sinc(t(1-alpha/m)/(2 sqrt(m)))
   + sum_r (alpha_r/m) exp(i t b_r)
       sinc(t alpha_r/(2 m sqrt(m))).`

For fixed `t`, Taylor expansion at zero gives

`psi_m(t)
 = 1 + m^(-1)[-t^2/24 + sum_r alpha_r(exp(i t b_r)-1)]
   + O_t(m^(-2)).`

Therefore

`psi_m(t)^m -> exp(-t^2/24)
                  exp(sum_r alpha_r(exp(i t b_r)-1)).`

The first factor is the characteristic function of `N(0,1/12)` and the second is that of the finite compound-Poisson variable `sum_r b_r N_r`. Levy's continuity theorem gives the one-bank convergence. Independence of the physical banks gives joint convergence, and the displayed convergence of `Q_m` follows from the continuous mapping theorem. QED.

### Proposition 3.2 — these arrays are genuinely non-Lindeberg

If some `b_r !=0`, choose `epsilon<|b_r|/2`. For all large `m`, the whole rare interval `F_(r,m)` lies in `{|X|/sqrt(m)>epsilon}`. Its exact contribution to the triangular-row Lindeberg sum is

`m E[(X/sqrt(m))^2 1_(X in F_(r,m))]
 = integral_(F_(r,m)) x^2 dx
 = alpha_r b_r^2 + alpha_r^3/(12 m^3).`

Hence the Lindeberg quantity has a positive limiting contribution `alpha_r b_r^2`. This is a genuine mesoscopic/non-Lindeberg source family, not another diffuse-CLT perturbation.

## 4. Partner theorem closes the entire limiting class at `3 sqrt(2)`

### Theorem 4.1 — compound-Poisson no-escape ceiling

The limiting law `Q_infty` has a continuous density satisfying

`boxed( ||p_(Q_infty)||_infinity <= 3 sqrt(2) ).`

#### Proof

Condition on the compound-Poisson vector `M=(M_1,M_2,M_3)`. Then

`Y=(Z_1+M_1,Z_2+M_2,Z_3+M_3)`

is Gaussian with arbitrary mean `M` and covariance `(1/12)I_3`, while

`Q_infty = Y^T diag(1,1,-1) Y`.

Apply the completed `account03/B17` noncentral-Gaussian theorem with `v=1/12`. Every conditional density is continuous and has supremum at most

`1/(2 sqrt(2) (1/12)) = 3 sqrt(2)`.

The unconditional density is the countable probability mixture of these conditional densities. Since all summands have the same `L^infinity` bound, the mixture converges uniformly and is continuous, with the same supremum bound. QED.

This rules out a broad, explicitly source-valid mechanism for improving the known universal lower floor: replacing a vanishing `O(1/m)` fraction of each diffuse bank by finitely many fragments at the critical `O(sqrt(m))` displacement scale produces genuine non-Lindeberg compound-Poisson shifts, but **cannot create a limiting peak above `3 sqrt(2)`**.

This statement is about the limiting stress mechanism. It does not prove that every finite `Q_m` has norm at most `3 sqrt(2)`, and it does not rule out transient finite-m spikes or more general mesoscopic arrays.

## 5. Exact strict saddle penalty for one negative rare fragment

There is an exact quantitative subfamily. Leave the two positive banks unfragmented and give only the negative bank one rare fragment, with rate `alpha>0` and offset `b!=0`. Then

`M_1=M_2=0`, `M_3=bN`, `N~Poisson(alpha)`.

Conditional on `N=k`, let `Z_i~N(0,1/12)`. The positive sum

`U=Z_1^2+Z_2^2`

is exponential of rate `6`. Hence

`p_(Q_infty | N=k)(0)
 = 6 E exp(-6(Z_3+bk)^2)
 = 3 sqrt(2) exp(-3 b^2 k^2).`

Averaging gives the exact formula

`boxed(
 p_(Q_infty)(0)
 = 3 sqrt(2) e^(-alpha)
   sum_(k=0)^infinity alpha^k/k! * exp(-3 b^2 k^2)
 ).`

For every `alpha>0` and `b!=0`, this value is strictly below `3 sqrt(2)`. For small `alpha`,

`p_(Q_infty)(0)/(3 sqrt(2))
 = 1-alpha(1-exp(-3b^2))+O(alpha^2).`

Thus the most elementary critical rare-fragment perturbation lowers, rather than raises, the canonical zero saddle. For the concrete check `alpha=b=1`, the factor is `0.386196210224995...` and the zero density is `1.63849175471184...`.

## 6. What this changes, and what it does not

The preceding B17 run excluded ordinary first-order changes of bank size, `O(1/m)` translations and legal spectral anisotropy around the uniform diffuse witness. The partner then closed arbitrary mean shifts in the Gaussian limit. The present theorem changes mechanism and attacks the explicitly remaining non-Lindeberg branch: critical rare fragments of mass `Theta(1/m)` at displacement `Theta(sqrt(m))`.

That branch also fails to exceed `3 sqrt(2)` in the limit, even for an arbitrary fixed finite fragment alphabet. Therefore a stronger sharp-constant witness, if one exists, must use structure not reducible to Gaussian plus a finite compound-Poisson shift: for example a genuinely growing fragment alphabet, a different mesoscopic scaling with no such conditional Gaussian representation, a coherent mixed-leverage core/tail interaction, or a finite-dimensional transient spike that survives all target constraints.

This is **not** a proof that `3 sqrt(2)` is the universal sharp constant, and it is **not** a proof of the full quadratic-form conjecture. The full conjecture remains OPEN.

## 7. Correction and provenance status

Consumed live corrections include the pointwise-decay refutation, rotation/independence warning, local-minor and conditional-cap failures, fiberwise-trace failure, phase-Wiener failure, and the newest `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`. No refuted intermediate is used. In particular, this report makes no fixed-fragment extremality claim: it proves a theorem only for the explicitly constructed finite-fragment triangular arrays.

A deterministic checker in this run root verifies the sample compound-Poisson saddle value, the exact Lindeberg contribution formula, and the characteristic-function convergence numerically. Those checks support the algebra and are not substitutes for the analytic proof above.
