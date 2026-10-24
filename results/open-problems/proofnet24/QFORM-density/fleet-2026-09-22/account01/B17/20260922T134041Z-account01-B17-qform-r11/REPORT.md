# account01/B17 — exact rotated tetrahedral witness and Gaussian-extremizer rigidity

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Run:** `20260922T134041Z-account01-B17-qform-r11`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `AUXILIARY_ONLY / EXACT_ROTATED_STRESS_AND_RIGIDITY`  
**Full conjecture:** OPEN / NOT PROVED  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and source dependencies

The target is the unrestricted quadratic-form density conjecture: for arbitrary independent real coordinates with densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues with modulus at least one, prove one universal finite `L^infinity` density bound for `X^T A X`, or give a valid counterexample. Continuity is a separate issue.

This report consumes the completed partner theorem `account02/B17`, canonical report

- `yspennstate/math-open-problems@cdd32fd16a694a5f8acc7ba758e0db6596a3e4a1`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T125054Z-account02-B17-QFORM-r11/REPORT.md`.

The partner proves the sharp centered-Gaussian envelope

`||p_{Z^T B Z}||_infinity <= 1/(2 sqrt(2) s)`

when `B` has at least three eigenvalues of modulus at least `s`, with equality for `s(G1^2+G2^2-G3^2)`, and hence the exact diffuse Gaussian ceiling `3 sqrt(2)` under the density-one variance floor `Var X >=1/12`.

Fresh corrections consumed through brain commit `b614c7ff658d5e2e7038282dfa132f483df11b83`, including the failures of cross-minor-only, fiberwise trace, bounded-diameter localization, conditional-cap substitution, local-cross-rank3 dichotomy, and phase-Wiener absolute-value mechanisms. Nothing below uses those refuted interfaces.

## 2. Exact finite rotated witness in four physical coordinates

Let `X_1,...,X_4` be iid `Uniform[-1/2,1/2]`, and set

```
A = (1/4) [ -1   3  -1  -1
             3  -1  -1  -1
            -1  -1   3  -1
            -1  -1  -1   3 ].
```

The spectrum is exactly `{1,1,-1,0}`. Thus this is a genuine non-diagonal target-admissible finite witness.

### Theorem 2.1

For `Q=X^T A X`, the density at the origin is

`boxed(p_Q(0)=4 log(1+sqrt(2))=3.5254943480781721009...)`.

In particular this finite rotated example already exceeds the diagonal three-square value `pi`, although it remains below the partner's sharp diffuse lower bound `3 sqrt(2)`.

### Proof

Use the orthogonal Hadamard coordinates

`y1=(x1+x2-x3-x4)/2`,

`y2=(x1-x2+x3-x4)/2`,

`y3=(x1-x2-x3+x4)/2`,

`s =(x1+x2+x3+x4)/2`.

The Jacobian is one and direct multiplication gives

`Q = y1^2 - 2 y2 y3`.

For fixed `y=(y1,y2,y3)`, the `s`-fiber through the cube has length

`L(y)=2(1-D(y))_+`,

where

`D(y)=` the sum of the two largest numbers among `|y1|,|y2|,|y3|`.

Indeed, the four cube inequalities become four intervals in `s`, and the difference between the largest and smallest tetrahedral linear forms is exactly twice that sum-of-two-largest norm.

Write the quadratic form in spectral form `q(y)=y^T B y` with

`B=[[1,0,0],[0,0,-1],[0,-1,0]]`.

Its negative unit eigenvector is `v=(0,1,1)/sqrt(2)`. On the unit sphere the zero cone consists of two circles

`omega_+(phi)=( cos(phi)/sqrt(2), (1+sin(phi))/2, (1-sin(phi))/2 )`,

`omega_-(phi)=( cos(phi)/sqrt(2), -(1-sin(phi))/2, -(1+sin(phi))/2 )`,

up to the harmless signs generated as `phi` runs through `0..2pi`. Each circle has speed `1/sqrt(2)`, and on the cone `|grad_{S^2} q|=2`.

Because `D` is homogeneous,

`int_0^infinity L(r omega) dr = 1/D(omega)`.

Spherical coarea therefore gives

`p_Q(0)=(1/(2sqrt(2))) sum_{+,-} int_0^{2pi} dphi / D(omega_+(phi))`.

The two sheets have the same `D`. On a quadrant,

`D(omega)=cos(phi)/sqrt(2)+(1+sin(phi))/2`, `0<=phi<=pi/2`.

Hence

`p_Q(0)=(4/sqrt(2)) int_0^{pi/2} [cos(phi)/sqrt(2)+(1+sin(phi))/2]^{-1} dphi`.

With `u=tan(phi/2)`,

`int_0^{pi/2} [cos(phi)/sqrt(2)+(1+sin(phi))/2]^{-1} dphi`

`= int_0^1 4 du / [(1+sqrt(2))+2u+(1-sqrt(2))u^2]`

`= sqrt(2) log(1+sqrt(2))`.

Multiplication by `4/sqrt(2)` yields the stated value.

This is an exact analytic calculation; no histogram or asymptotic approximation is used.

## 3. Quantitative stability of the density-one variance floor

The next theorem leaves the fixed-uniform-support setting and applies to arbitrary density-one laws.

### Theorem 3.1 — sharp interval stability

Let `X` have density `0<=f<=1`, finite mean `m`, and finite variance. Put

`I=[m-1/2,m+1/2]`,

`delta=Var(X)-1/12 >=0`,

`d=||f-1_I||_1`.

Then

`boxed(delta >= d^2/8)`

or equivalently

`boxed(||f-1_I||_1 <= sqrt(8 delta))`.

Thus equality in the variance floor occurs iff `f=1_I` almost everywhere.

### Proof

Let `alpha=int_{I^c} f = int_I (1-f)=d/2`. Relative to the centered unit interval,

`delta = int_{I^c}(x-m)^2 f(x)dx - int_I (x-m)^2(1-f(x))dx`.

For fixed outside mass `alpha`, the first term is minimized by placing density one on the two closest outside shells of total length `alpha`; the second term is maximized by placing the missing mass on the two interior edge shells of total length `alpha`. Therefore

`delta >= 2 int_{1/2}^{1/2+alpha/2} r^2 dr - 2 int_{1/2-alpha/2}^{1/2} r^2 dr = alpha^2/2 = d^2/8`.

The shell comparison is the one-dimensional bathtub principle and uses only `0<=f<=1`.

## 4. Leverage-weighted intervalization

Let `R` be an `n x 3` matrix with `R^T R=I_3`, with rows `r_i` and leverages `ell_i=||r_i||^2`. Let the independent coordinates have variances

`v_i=1/12+delta_i`.

Then the projected covariance is

`Sigma = R^T diag(v_i) R = (1/12) I_3 + E`,

`E=sum_i delta_i r_i r_i^T >=0`,

and

`tr E=sum_i ell_i delta_i`.

For `I_i=[EX_i-1/2,EX_i+1/2]`, Theorem 3.1 and Cauchy-Schwarz give the quantitative identity

`boxed(sum_i ell_i ||f_i-1_{I_i}||_1 <= sqrt(24 tr E)).`

Indeed, `d_i^2<=8 delta_i` and `sum_i ell_i=3`, so

`sum ell_i d_i <= sqrt((sum ell_i)(sum ell_i d_i^2)) <= sqrt(24 sum ell_i delta_i)`.

This is useful because it is weighted by the actual spectral leverage; irrelevant physical coordinates cost nothing.

## 5. Applying the partner Gaussian envelope: rigidity of a sharp diffuse sequence

Consider a rank-three centered diffuse/Lindeberg sequence with spectral frame `R_N`, independent density-one coordinates, covariance convergence

`Sigma_N=R_N^T diag(v_{N,i}) R_N -> Sigma`,

and projected law converging to `N(0,Sigma)`. Let the limiting quadratic form have signature `(2,1)` and eigenvalue magnitudes one, so its Gaussian quadratic-form density is bounded by the partner theorem.

If the limiting quadratic-form density attains the sharp value `3 sqrt(2)`, then necessarily

`boxed(Sigma=(1/12) I_3)`.

Reason: write `s=1/12`. Since every `v_{N,i}>=s`, one has `Sigma>=sI`. The partner theorem gives `||p||_infinity<=1/(2sqrt(2)s)=3sqrt(2)`. Equality in its mixed-sign theorem forces the three eigenvalue magnitudes of `Sigma^{1/2} J Sigma^{1/2}` to equal `s`. Hence

`det Sigma = s^3`.

But all eigenvalues of `Sigma` are at least `s`; product `s^3` therefore forces all three to equal `s`.

Consequently `tr E_N=tr(Sigma_N-sI)->0`. The leverage-weighted stability theorem yields

`boxed(sum_i ell_{N,i} ||f_{N,i}-1_{I_{N,i}}||_1 ->0).`

So every centered diffuse extremizing sequence for the exact Gaussian ceiling must become a unit-interval product source in the only sense relevant to the rank-three projection: leverage-weighted `L^1` distance.

This is a rigidity statement, not a universal localization theorem. It does not contradict the live bounded-diameter correction: laws far from the variance floor may have fragmented supports, and no bounded-diameter reduction is claimed for them.

## 6. What changed and what remains unpaid

New exact facts from this run:

1. An explicit four-variable rotated admissible matrix has the exact finite value
   `p_Q(0)=4 log(1+sqrt(2))`, strictly above the diagonal `pi` control.
2. The density-one variance floor has the sharp quantitative stability
   `Var(X)-1/12 >= ||f-1_I||_1^2/8`.
3. Combining that stability with the completed `account02/B17` Gaussian envelope proves leverage-weighted intervalization of every sharp centered diffuse extremizing sequence.

The universal lower bound itself remains the partner's stronger

`C >= 3 sqrt(2)`.

The exact four-variable stress value is therefore a finite rotated control, not a stronger lower bound.

The first unpaid sharp-witness implication is now genuinely non-Gaussian/mesoscopic: either construct a density-one product family whose output peak exceeds `3 sqrt(2)`, or prove that variance excess plus non-Gaussian shape always pays enough to keep such families below the Gaussian ceiling. The interval-stability theorem reduces any near-floor attempt to a small `L^1` perturbation of unit intervals in leverage-weighted coordinates, but turning that into a quadratic-form density bound requires a new stability inequality for the curved trace; plain bounded-diameter localization is refuted and is not used here.

## 7. Verification

`check_exact.py` verifies the explicit matrix spectrum, the exact transformed integral, the numerical comparisons, and the shell identity underlying Theorem 3.1. The checker is only a consistency check; the proof above is analytic.
