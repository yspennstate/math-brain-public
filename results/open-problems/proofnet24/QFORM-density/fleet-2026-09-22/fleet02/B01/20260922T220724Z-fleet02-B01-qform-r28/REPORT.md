# QFORM fleet02/B01 r28 — near-singular row Fourier gate

Status: `PROVED_SUPPORTING_THEOREM / SHARP_ENDPOINT_OBSTRUCTION / PARTNER_APPLIED / FULL_TARGET_OPEN`.

Run: `20260922T220724Z-fleet02-B01-qform-r28`.


## 1. New theorem: arbitrary-pivot physical-row Fourier gate

### Theorem (`QFORM-ARBITRARY-PIVOT-ROW-FOURIER-L2PLUS-v1`)

Let `X` be independent of the pair `(U,R)`. Assume `X` has a probability density `f` with `0<=f<=1`, while `U` has a density `h` with `||h||_infinity<=M`. No independence between `U` and `R` is assumed. For an arbitrary real `delta`, put

`T = delta X^2 + 2 X U + R`.

Then, for every `t!=0`,

`|phi_T(t)| <= min(1, sqrt(pi M/|t|)).`  (1)

Consequently, for every `q>2`,

`integral_R |phi_T(t)|^q dt <= 2 pi M q/(q-2).`  (2)

In particular,

`integral_R |phi_T(t)|^3 dt <= 6 pi M.`  (3)

The critical weak endpoint and local strong endpoint are

`|{t: |phi_T(t)|>eta}| <= 2 pi M eta^(-2)` for `0<eta<=1`,  (4)

and, writing `a=pi M`,

`integral_{-L}^L |phi_T(t)|^2 dt <= 2L` if `L<=a`,

`integral_{-L}^L |phi_T(t)|^2 dt <= 2a[1+log(L/a)]` if `L>a`.  (5)

Every bound is uniform in the quadratic pivot `delta` and in the arbitrary dependence of the residual phase `R` on `U`.

### Proof

Fix `t!=0` and define

`F_t(u)=integral_R f(x) exp(i t delta x^2) exp(i 2 t u x) dx`.

Conditioning only on `(U,R)` gives exactly

`phi_T(t)=E[ exp(i t R) F_t(U) ].`

Cauchy--Schwarz therefore yields

`|phi_T(t)|^2 <= E |F_t(U)|^2 <= M integral_R |F_t(u)|^2 du.`

The factor `exp(i t delta x^2)` has modulus one. With the Fourier convention `hat g(xi)=integral g(x)e^{i xi x}dx`, Plancherel and the change of variables `xi=2tu` give

`integral_R |F_t(u)|^2 du
 = (1/(2|t|)) integral_R |hat g_t(xi)|^2 dxi
 = (pi/|t|) integral_R f(x)^2 dx
 <= pi/|t|`,

because `0<=f<=1` and `integral f=1`. This proves (1), together with the trivial characteristic-function bound `|phi_T|<=1`.

For (2), set `a=pi M` and integrate the envelope:

`integral_R |phi_T|^q
 <=2[ integral_0^a 1 dt + integral_a^infinity (a/t)^(q/2) dt ]
 =2a[1+2/(q-2)]
 =2 pi M q/(q-2).`

Equation (3) is `q=3`. Equation (4) follows immediately from (1). Squaring (1) and integrating separately over `0<t<a` and `a<t<L` gives (5). QED.

## 2. Full quadratic-form corollary with all couplings retained

Fix an original physical coordinate `i` in the owner's target and write

`Q = A_ii X_i^2 + 2 X_i U_i + R_i`,

`U_i = sum_{j!=i} A_ij X_j`,

where `R_i` contains every remaining diagonal, cross, and affine-after-conditioning term. Put

`sigma_i = (sum_{j!=i} A_ij^2)^(1/2)`.

The completed product-projection input used in the source-pinned fleet03/B01 r18 theorem gives

`||p_{U_i}||_infinity <= sqrt(2)/sigma_i` whenever `sigma_i>0`.

Substitution into the theorem above gives, uniformly in the physical diagonal `A_ii` (including zero, tiny nonzero, or large),

`|phi_Q(t)| <= min(1, sqrt(pi sqrt(2)/(sigma_i |t|))),`  (6)

and for every `q>2`,

`integral |phi_Q|^q <= (2 pi sqrt(2)/sigma_i) q/(q-2).`  (7)

In particular

`integral |phi_Q|^3 <= 6 pi sqrt(2)/sigma_i.`  (8)

This is a product-preserving averaged/distributional replacement exactly in the near-singular-pivot regime left open by the preceding B01 run. It does **not** assert an `L^1` characteristic-function bound or bounded density from one row alone.


## 3. The `L^2` endpoint genuinely fails

The logarithm in (5) cannot in general be replaced by a finite global `L^2` bound. Take independent

`X,U ~ Uniform[-1/2,1/2]`, `delta=1`, `R=U^2`.

Then

`T=X^2+2XU+U^2=(X+U)^2`.

The triangular density of `W=X+U` is

`g(w)=(1-|w|) 1_{|w|<1}`.

Hence `Y=W^2` has density

`p_Y(y)=y^(-1/2)-1`, `0<y<1`.

Thus `p_Y` is not in `L^2`; by Plancherel its characteristic function is not in `L^2`. The range `q>2` in (2) is therefore sharp at the critical exponent under these hypotheses. This construction is not a QFORM counterexample: it is a two-variable row mechanism with only the familiar rank-two obstruction.

This endpoint obstruction is compatible with fleet03/B01 r18's density-side example; the new content here is the exact arbitrary-pivot Fourier-side theorem (1)--(8), which remains valid for every `delta` even though the density-side `L^2` endpoint fails.

## 4. Completed named partner fleet03/B01 r19 applied quantitatively

The fresh completed partner handoff `fleet03/B01 r19` proves that a scalar pivot `a` whose Schur residual contains a disjoint physical cross block `B` with `E_3=e_3(BB^T)>0` satisfies

`||p_Q||_infinity <= 9.841 |a|^(-1/2) E_3^(-1/12)`.

Canonical source: `yspennstate/math-open-problems@7df1461e33f7ea4e6026a650391822a16e56e987`, report blob `9cb96b24ad0e118a42bb74ca9e167b48f1028d79`; source-bound handoff at brain commit `3290f29a3c319f449c346431430151cccd34fb38`.

Apply it to the explicit four-bank positive-semidefinite family, for even `m`,

`A_m = (J_m/m) direct_sum (J_m/m) direct_sum (J_m/m) direct_sum ((1/2) J_m/m).`  (9)

The nonzero spectrum is exactly `{1,1,1,1/2}`, so (9) is a valid target matrix with three eigenvalues at least one. Every physical diagonal pivot satisfies `0<a<=1/m`.

Choose a pivot from one of the first three banks. Its Schur complement deletes that rank-one bank direction and leaves three rank-one banks with eigenvalues `1,1,1/2`. Split each remaining bank into two halves and take the corresponding residual cross block. Its three nonzero singular values are exactly

`1/2, 1/2, 1/4`,

so

`E_3 = (1/2)^2 (1/2)^2 (1/4)^2 = 1/256.`

The partner theorem therefore gives only

`||p_Q||_infinity <= 9.841 * 2^(2/3) * sqrt(m),`  (10)

which diverges with `m`. If the pivot lies in the fourth bank, the remaining three singular values are all `1/2`, hence `E_3=1/64` and the partner bound is `19.682 sqrt(m)`.

More invariantly, after any physical pivot the Schur residual in (9) is positive semidefinite of rank at most three and operator norm at most one. Hence every residual cross block has all singular values at most one, so `E_3<=1`; since `a<=1/m`,

`a^6 E_3 <= m^(-6).`  (11)

Therefore the scale condition `a^6 E_3 >= c>0` cannot be demanded uniformly from the bare three-large-eigenvalue hypothesis. This does not contradict the partner result: the family must be routed to a grouped/diffuse branch instead of a single scalar-pivot branch. It also shows why the new row estimate (6)--(8), which does not pay `a^(-1/2)`, is the more stable interface in the near-zero-pivot regime.

## 5. What remains unpaid

The new theorem turns **one physical row** into a uniform Fourier `L^{2+}` gate without any loss as the diagonal pivot crosses zero. It also proves that the critical `L^2` endpoint cannot close by itself. To obtain the owner's full density conclusion one still has to spend the third spectral direction *jointly* with this row gate before taking absolute values that destroy dependence.

A precise next implication is:

`QFORM-ROW-L3-PLUS-TRANSVERSE-L3OVER2-v1` — from the bare three-large-eigenvalue hypothesis, in every branch not already closed by physical triples, diffuse/ridge/grouped-square theorems, or the partner's aggregate `E_3` half-Riesz gate, produce a product-preserving transverse mechanism that pairs with (8) at the Hölder exponents `3` and `3/2`, without asserting post-rotation independence or conditioning on a rare fiber.

One row alone cannot do this: Section 3 proves the critical obstruction. The partner scalar-pivot theorem alone cannot do it uniformly either: Section 4 gives the exact high-cardinality scale degeneration. Thus the next mechanism must be genuinely grouped/joint.

Full QFORM remains OPEN. This report is not a full-proof candidate and has not received two independent end-to-end reviews.
