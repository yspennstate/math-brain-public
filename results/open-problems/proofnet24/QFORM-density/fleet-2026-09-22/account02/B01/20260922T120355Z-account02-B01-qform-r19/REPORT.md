# account02/B01 — averaged quadratic gate, sharp L2 endpoint failure, and an indefinite projection stress test

**Run:** `20260922T120355Z-account02-B01-qform-r19`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** B01, “Oscillatory replacement”  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_AVERAGED_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source state and preserved correction

The exact target remains: independent real `X_i` with densities `0<=f_i<=1`; real symmetric `A`; at least three eigenvalues of `A` have absolute value at least one; prove a universal essential-supremum bound for the density of `Q=X^TAX`, or give a valid target counterexample. No moments, log-concavity, compact support, diagonal-basis independence, or post-rotation independence are assumed.

Consumed source control: `yspennstate/math-research-brain` main commit `5966a72ce5bd4455d39586a1960dbffd9454950b`, later refreshed to `04fee9e85f1fccdd01af7be0d68fa0d53dee168c`; `scheduled_tasks/README.md`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, `DELTAS.json`, `CORRECTION_INBOX.json`, `PATHWAYS.md`, `MEMORY_PROTOCOL.md`, and the exact account02/B01 assignment were read. Corrections consumed: `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, and live event `QFORM-CROSSMINOR-ALONE-FALSE` (not used positively).

The phase-aligned-density refutation is preserved. For any fixed nonzero frequency `s` and `delta>0`, the set

`{x : dist(s x^2, 2*pi*Z) <= delta}`

has infinite measure. Choosing a measurable subset of length one and taking its indicator as the input density makes the real part of the quadratic oscillatory integral at `s` at least `cos(delta)`. Therefore no law-uniform pointwise positive power decay in `|s|` can hold.

## 2. New averaged replacement: all L^q, q>2

### Theorem 2.1 — `QFORM-AVERAGED-QUADRATIC-GATE-v1`

Let `X` have a probability density `f` with `0<=f<=1`. Let `a!=0`, `b` be real and

`F(t)=E exp(i t (a X^2+bX))`.

For every `q>2`,

`||F||_q <= C_q |a|^(-1/q)`,

where

`C_q=(4*pi)^(1/q) ((q-1)/(q-2))^((q-1)/q)`.

In particular

`||F||_3^3 <= 16*pi/|a|`.

Consequently, for `0<eta<1`,

`Leb{t: |F(t)|>eta} <= 16*pi/(|a| eta^3)`.

A near-critical form obtained by optimizing `q` is

`Leb{t: |F(t)|>eta} <= 16*pi*e |a|^(-1) eta^(-2) max(1, log(1/eta))`.

Thus arbitrary phase-aligned peaks may be placed at selected frequencies, but their total frequency measure has a universal quantitative budget.

### Proof

Complete the square:

`a x^2+b x = a (x+b/(2a))^2 - b^2/(4a)`.

Translation preserves the density cap, and the final constant phase is irrelevant, so it suffices to treat `Y=X^2` and then scale by `a`.

Write

`h(r)=f(r)+f(-r)`, `r>0`.

Then `0<=h<=2`, `int_0^infty h(r)dr=1`, and `Y` has density

`g(y)=h(sqrt(y))/(2 sqrt(y))`, `y>0`.

Put `p=q/(q-1)`, so `1<p<2`. A change of variables gives

`int g(y)^p dy = 2^(1-p) int_0^infty h(r)^p r^(1-p) dr`.

Since `h<=2`, `h^p<=2^(p-1)h`. Therefore

`int g^p <= int_0^infty h(r) r^(1-p) dr`.

The weight `r^(1-p)` is decreasing. Under `0<=h<=2` and `int h=1`, the bathtub principle maximizes the last integral at `h=2 1_[0,1/2]`, hence

`int g^p <= 2 int_0^(1/2) r^(1-p)dr = 2^(p-1)/(2-p)`.

Thus

`||g||_p <= 2^(1/q) ((q-1)/(q-2))^((q-1)/q)`.

With Fourier convention `hat g(t)=int exp(i t y)g(y)dy`, Hausdorff--Young by interpolation between `L1->Linfinity` and Plancherel gives

`||hat g||_q <= (2*pi)^(1/q)||g||_p`.

Combining the last two displays yields the stated `C_q`; scaling `Y` by `a` contributes `|a|^(-1/q)`. Chebyshev gives the superlevel bound. For the logarithmic near-endpoint estimate, if `eta<=e^-1` set `L=log(1/eta)` and `q=2+1/L`; then `eta^(-q)=e eta^-2` and `(L+1)^(1+1/L)<=4L`. If `eta>e^-1`, use `q=3`. This proves the displayed bound. `QED`.

## 3. The exponent 2 endpoint genuinely fails

The preceding theorem cannot be extended uniformly to `q=2`. Take `X` uniform on `[0,1]`. Then `Y=X^2` has density

`g(y)=1/(2 sqrt(y)) 1_(0,1)(y)`,

which is not in `L^2`. If its characteristic function were in `L^2`, Plancherel/inversion would force the `L^1` density `g` to have an `L^2` representative, a contradiction. Hence

`int_R |E exp(i t X^2)|^2 dt = infinity`.

So `q>2` is the correct strong-Lq side of this elementary averaged mechanism; the logarithmic near-weak-L2 superlevel estimate is consistent with the endpoint obstruction.

## 4. Full coupled consequence by conditioning

Let `Q=X^TAX` with arbitrary dimension and arbitrary symmetric `A`. If some original-coordinate diagonal coefficient `a_ii` is nonzero, condition on all coordinates except `X_i`. The inner phase has the form

`a_ii X_i^2 + beta(X_-i) X_i + gamma(X_-i)`.

Theorem 2.1 is uniform in the induced linear coefficient `beta`. Minkowski therefore gives, for every `q>2`,

`||phi_Q||_q <= C_q |a_ii|^(-1/q)`.

In particular `||phi_Q||_3^3 <=16*pi/|a_ii|`. This is valid with all outside couplings retained; no rotation and no moment assumption is used.

## 5. Completed compatible partner result actually applied

Partner account03/B01 run `20260922T113140Z-account03-B01-qform-r1`, immutable report commit `c7a1ce265139092705e86c5a577523798291b964`, proved the common product envelope

`p_{UV}(w) <= H(w)=4 log(1+1/(2 sqrt(|w|)))`

for independent bounded-density `U,V`, with `||H||_3<6.266`, and used it to prove a non-diagonal block density theorem.

Apply that result conditionally to the present full form. If `a_ii=a_jj=0` and `b=a_ij!=0`, then after conditioning all other coordinates the `(X_i,X_j)` phase is

`2b X_iX_j + ell_i X_i + ell_j X_j + constant`.

Coordinatewise translations reduce this to `2bUV+constant`, preserving independence and the density cap. The partner bound plus interpolation and Hausdorff--Young yields the uniform conditional estimate

`||phi_cond||_3 < 3.67 |b|^(-1/3)`.

Minkowski then gives the same bound for the full `phi_Q`.

Combining this with Section 4 gives a finite `L^3` characteristic-function norm for every nonzero quadratic form under the product bounded-density hypotheses: use a nonzero diagonal entry if present; if all diagonal entries vanish, any nonzero off-diagonal entry supplies the partner hyperbolic gate. The constant currently depends on the chosen original-coordinate coefficient and is therefore not yet universal under the spectral hypothesis.

## 6. Exact indefinite stress test: projection L-infinity alone is insufficient

The correction `QFORM-NO-INDEPENDENCE-AFTER-ROTATION` can be made quantitative. Consider the three-eigenvalue form

`q(x,y,z)=x^2+y^2-z^2`

and, for `R>0`, set `delta=1/(pi R)` and

`E_R={R<=z<=2R, 0<=x^2+y^2-z^2<=delta}`.

In cylindrical coordinates `x=r cos(theta), y=r sin(theta)`, put `s=r^2-z^2`; then `r dr=ds/2`. Hence

`|E_R| = int_R^(2R) int_0^(2pi) int_0^delta (1/2) ds dtheta dz = pi R delta =1`.

Therefore `g_R=1_{E_R}` is a probability density bounded by one on `R^3`. Under `q`, the output density is exactly

`p_R(s)=pi R 1_[0,delta](s)`,

so `||p_R||_infinity=pi R -> infinity`.

This is **not** a counterexample to the owner target because `g_R` is not a product density. It is a rigorous counterexample to any proof step that replaces the rotated spectral projection by an arbitrary bounded joint density and then forgets the original product structure. The indefinite cone has enough longitudinal volume to concentrate the quadratic value arbitrarily strongly.

## 7. First unpaid universal implication

The averaged one-coordinate and hyperbolic-pair gates are now rigorous, correction-safe and retain arbitrary outside couplings. What is still unpaid is a dimension-free way to **aggregate many small original-coordinate gates using the product structure** under the sole spectral hypothesis of three eigenvalues with absolute value at least one. Selecting the largest coordinate coefficient loses dimension; replacing the three-dimensional spectral projection by only an `L-infinity` density bound is invalid by Section 6.

A useful next step is therefore an integrated/minor aggregation inequality of the schematic form

`three large singular directions + product input structure => integral-frequency control stronger than any single coefficient gate`,

without diagonalizing the input law. The partner product envelope is a natural two-coordinate atom for such an aggregation.

This run does not claim a universal `L^1` characteristic bound, a target density bound, or a full proof candidate.

## 8. Auxiliary checker

`CHECKER.py` verifies the constants `C_q`, the exact `q=3` value `C_3^3=16*pi`, the shell volume/output formulas for several `R`, and the numerical partner-derived hyperbolic constant `<3.67`. `CHECKER_OUTPUT.txt` ends `STATUS=PASS`. The checker is regression evidence only; Sections 2--6 are symbolic arguments.
