SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-24T01:10:09Z.

# Independent scoped review of FISHER_INFORMATION.md

Source reviewed: `yspennstate/math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2:proofnet24/QFORM-density/interactive/20260923T184054Z-fisher-continuation/FISHER_INFORMATION.md`, blob `8a562d0d8c8c47679b83c33d1e0bbe9390387f4d`.

Assigned account02/B02 scope: weak integration by parts, cutoff limits, inverse-distance estimate, primitive normalization, and the resulting density-domination factor. Verdict: **PASS on this assigned analytic scope**. This is not a review of the separate spectral/constant/convolution/smoothing items assigned to account03/B04, and it is not an end-to-end review of full QFORM.

## 1. Weak product score identity

For `sqrt(f_i) in H^1(R)`, one has `f_i in W^{1,1}` with weak derivative

`f_i'=2 sqrt(f_i) (sqrt(f_i))'`.

Hence `int |f_i'| <= 2 ||sqrt(f_i)||_2 ||(sqrt(f_i))'||_2 < infinity` and `int f_i'=0`. With

`S_i=f_i'/f_i` on `{f_i>0}`, zero elsewhere,

the standard Sobolev zero-set fact makes `f_i'=0` a.e. on `{f_i=0}`, so `partial_i F=F S_i` for the product density `F=prod_i f_i`. Also

`E S_i=0`, `E S_i^2=I_i`.

Independence therefore gives, for an orthonormal-column `U`,

`E |U^T S|^2 = sum_i (UU^T)_ii I_i = J_E`.

No moment assumption on `X` is used.

## 2. Inverse-distance field and cutoff

Let `z=U^T x-z0`, `R=|z|` and

`W_delta=U z/(R^2+delta)`.

Direct differentiation gives

`div W_delta = r/(R^2+delta)-2R^2/(R^2+delta)^2 >= (r-2)/(R^2+delta)`.

Insert a smooth radial cutoff `chi_N` equal to one on the radius-`N` ball, supported in the radius-`2N` ball, with `|grad chi_N|<=C/N`. For fixed `delta>0`, `W_delta` is bounded. The boundary term is bounded by `C ||W_delta||_infinity/N` against a probability density and vanishes as `N->infinity`; the score term is integrable because `E|S_i|<=sqrt(I_i)`. Thus weak integration by parts is justified without moments.

Writing

`K_delta=E(R^2+delta)^(-1)`,

one obtains

`(r-2)K_delta <= E |z dot U^T S|/(R^2+delta)`

and Cauchy--Schwarz yields

`E |z dot U^T S|/(R^2+delta)
 <= sqrt( J_E * E[R^2/(R^2+delta)^2] )
 <= sqrt(J_E K_delta)`.

Therefore

`K_delta <= J_E/(r-2)^2`.

Monotone convergence as `delta downarrow 0` gives

`D:=E R^(-2) <= J_E/(r-2)^2`.

The projected law `U^T X` is absolutely continuous (indeed one can condition on a nonsingular `r x r` coordinate minor of `U`), so `P(R=0)=0`; no atom at the chosen center spoils the limit.

## 3. Inverse-spectral field and the exact factor 1/4

Set

`V_delta=U Lambda^(-1) z/[2(R^2+delta)]`.

Since `U^T grad Q = 2 Lambda z`, including arbitrary affine components and all other spectral directions,

`grad Q dot V_delta = R^2/(R^2+delta)`.

Also

`div V_delta = tr[Lambda^(-1)(I-2zz^T/(R^2+delta))]/[2(R^2+delta)]`.

The matrix in brackets has operator norm at most one, hence

`|div V_delta| <= r/(2s R^2)`

and

`|V_delta dot S| <= |U^T S|/(2sR)`.

Both are integrable after the preceding inverse-distance estimate and Cauchy--Schwarz.

For nonnegative `psi in C_c^infinity(R)`, let `m=int psi` and use the centered primitive

`Phi(t)=int_{-infinity}^t psi(u)du-m/2`.

Then exactly `||Phi||_infinity<=m/2`. The same fixed-`delta`, cutoff-first integration by parts gives

`E[psi(Q)R^2/(R^2+delta)]
 = -E[Phi(Q)(div V_delta+V_delta dot S)]`.

After `N->infinity` and then `delta downarrow 0`, dominated convergence applies to the left side, while the right side is controlled by the integrable bounds above. Consequently

`E psi(Q)
 <= (m/2)[ rD/(2s) + sqrt(J_E D)/(2s) ]
 = m [rD+sqrt(J_E D)]/(4s)`.

Thus the source's factor `1/4` is correct: one `1/2` comes from the definition of `V_delta`, and the other from centering the primitive.

## 4. Density domination

If `mu_Q` denotes the pushforward law, the preceding inequality holds for every nonnegative compactly supported smooth `psi`:

`int psi dmu_Q <= C int psi dt`,

with `C=[rD+sqrt(J_E D)]/(4s)`. By regular approximation/Riesz representation, this is exactly the measure domination `mu_Q<=C Lebesgue`; hence `mu_Q` has a density with essential supremum at most `C`.

Substituting `D<=J_E/(r-2)^2` gives

`C <= (r-1)J_E/[2s(r-2)^2]`,

matching the source theorem.

## 5. Scope boundary

This review does **not** remove the Fisher-information hypothesis. The source's cap-preserving mollification obstruction remains relevant. It also does not review the compact-kernel convolution class, the numerical constants in the cap-one refinement, or the smoothing counterexample beyond noting that none is needed for the assigned integration-by-parts proof.

Full rough-input QFORM remains OPEN.
