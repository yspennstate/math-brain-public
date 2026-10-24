# account02/B04 r25 supporting improvement — exact scalar kernel and the present nine-direction barrier

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **PROVED SUPPORTING REFINEMENT; DOES NOT LOWER THE MULTIPLICITY BELOW NINE.** The unrestricted three-eigenvalue conjecture remains open.

## 1. Exact scalar-pivot convolution kernel

The manuscript uses

`J(d)=int_{-1}^1 |x|^(-1/2)|x-d|^(-1/2) dx`.

By symmetry take `d>0`.

For `0<d<=1`, split at `0` and `d`. On `[0,d]`, put `x=d sin^2(theta)`; on `[d,1]`, put `x=d cosh^2(t)`; on `[-1,0]`, put `-x=d sinh^2(t)`. These substitutions give the exact identity

`J(d)=pi + 2 asinh(d^(-1/2)) + 2 acosh(d^(-1/2)).`              (1)

For `d>=1`, the singularity is outside or at the integration interval. The same negative-half substitution and `x=d sin^2(theta)` on `[0,1]` give

`J(d)=2 asinh(d^(-1/2)) + 2 asin(d^(-1/2)).`                    (2)

For `y=d^(-1/2)>=1`,

`asinh y + acosh y - 2 log y
 = log((y+sqrt(y^2+1))/y) + log((y+sqrt(y^2-1))/y)
 <= 2 log 2`.

Combining this with (1) yields

`J(d) <= pi + 4 log 2 + 2 log(1/d)` for `0<d<=1`.

For `d>=1`, (2) is increasing in `y=d^(-1/2)<=1`; its maximum at `d=1` is below `pi+4 log2`. Thus for all `d!=0`,

`boxed: J(d) <= C_J + 2 log_+(1/|d|),  C_J=pi+4 log2=5.914181375829574... .`    (3)

This improves the baseline safe estimate `8+3 log_+(1/|d|)` but does not change its validity.

## 2. The manuscript already chooses the optimal smoothing parameter in its quarter-power step

Before the manuscript fixes `v=1/8`, the Gaussian-smoothing proof of quarter-power concentration has a coefficient proportional to

`e^v v^(-1/8)`.

Differentiating its logarithm gives `1-1/(8v)`, so the unique minimizer is exactly

`v=1/8`.

At this value the exact coefficient is

`C_q = 2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)
     = 3.99525936158161409486... .`                                (4)

Consequently, for quadratic remainder operator norm at least one, layer cake gives the sharper logarithmic potential

`boxed: sup_a E log_+(1/|R-a|) <= L_q:=4+4 log C_q
       =9.54043399463305294902... .`                              (5)

## 3. Scalar subbranch constant

At the manuscript threshold `eta=1/100`, the scalar-pivot truncated half-potential proof combines (3) and (5) to give

`H_scalar <= eta^(-1/2) [C_J+2L_q]
          =249.9504936509568037... .`                              (6)

The corresponding full half-potential is at most `250.9504936509568...` after adding the unit tail.

This does not currently improve the best full nine-direction constant. Retaining the unrounded hyperbolic middle/tail estimate in the indefinite-pair pivot branch gives, at the endpoint `D=eta=1/100`, approximately

`10 [8+30 log2+4 log(1.6)] =306.7442993378130...`,                (7)

which still dominates (6). Thus the independent account03/B08 bound `<311` for the inner pivot half-potential, and hence `<3110 K^2/s` for the current nine-direction candidate, remains the relevant global constant. Any further constant reduction must first improve the indefinite-pair envelope, not the scalar kernel.

## 4. Exact barrier of the present interpolation/diagonal-dominance mechanism

The order-three spectral-to-volume proof can stop at sampled seed order `r=2`. At that seed the completion has

`rank R <=3r=6`, while `rank R[L,L]<=r=2`.

With `m` large singular values, the global rank perturbation forces at least `m-6` large diagonal entries of `D`. The restricted-rank contradiction needs at least `r+1=3` such entries in `L`. Therefore this proof mechanism needs

`m-6 >=3`, i.e. `m>=9`.                                             (8)

For `m=8`, only two large diagonal entries are forced, and a rank-two matrix can contain a two-by-two strictly diagonally dominant block; no contradiction follows. Hence nine is an exact bookkeeping barrier of this interpolation/rank/diagonal-dominance argument.

This is **not** a counterexample to an eight-eigenvalue density theorem. It identifies the next proof obligation: lowering below nine requires a new structural input that either improves the global/restricted rank relationship, forces an extra large coordinate outside the seed, or supplies a different product-preserving analytic endpoint when the `r=2` seed occurs.

## 5. Relation to the candidate threshold-nine theorem

The complete threshold-nine replacement is already written in `improvements/account03/B04/20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md`. Fresh repository state also contains separate independent PASS reports from account01/B16 and account03/B08. This note does not self-award release status; it only records the exact local constant refinement and the below-nine barrier after an independent complete baseline audit.
