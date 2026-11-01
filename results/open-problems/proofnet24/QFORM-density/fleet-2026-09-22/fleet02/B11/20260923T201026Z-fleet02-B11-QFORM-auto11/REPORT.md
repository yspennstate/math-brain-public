SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-23T20:10:26Z.
attacking: the same-bank residual-shear punctured collar via a product-provenance Fourier crossing estimate, with the one-sheet ruled bound and rank-two logarithmic endpoint kept explicit.

# fleet02/B11 — same-bank punctured collar: exact nonzero-cross estimate and two-sheet localization

Programme: `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.15`, continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.

Status: **new source-composed collar implication / full QFORM OPEN / not a counterexample**.

No moment, support, log-concavity, connected-support, identical-law, post-rotation-independence, or small-random-perturbation assumption is used. Essential boundedness is the main target; continuity is asserted below only where an `L^1` Fourier estimate is obtained. Execution remains `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The designated partner fleet03/B11 r40 isolates the current exact-rank-three near-coloop collar. In its original-coordinate cut `H sqcup T`, the physical cross block has singular values

`σ1 >= σ2 >= σ3 >= 0`

with the uniform two-direction lower bound

`σ1 σ2 > κ_* s^2`,

`κ_* = (34/111)(17/288)^2 = 0.0010672564926037...`,                 (1.1)

where `s=min |lambda(M)| >= 1`. The only cross scale that can vanish is `σ3`. Partner r40 also proves that the natural spatial slicing bridge

`integral ||p_(v,W)(.,w)||_2 dw <= C`

is false even for an orthogonal transform of three independent cap-one coordinates. Thus one may not condition on the same-bank residual scalar and average a rank-two estimate by a universal `L1_W(L2_v)` norm.

The first unpaid implication is therefore the **uniform two-sheet interpolation through `σ3 -> 0`**. This report pays every fixed puncture `σ3 != 0` with the exact determinant cost, applies the partner's top-two lower bound at a real inequality, and shows that the one-sheet side is already uniformly paid. What remains is to remove the `σ3^(-1/3)` loss on the opposite two-sheet side by using the internal bilinear curvature before the full three-dimensional absolute-value step.

## 2. Three-dimensional product-projection crossing lemma

### Lemma `QFORM-3D-PROJECTION-CROSS-L2-v1`

Let `X` and `Y` be independent source banks. Let

`U = E_X^T X in R^3`, `V = E_Y^T Y in R^3`,

where `E_X,E_Y` have orthonormal columns in their respective original-coordinate spaces. Suppose the projected laws have densities `p_U,p_V` with

`||p_U||_infinity <= M_X`, `||p_V||_infinity <= M_Y`.

Let `C` be any invertible real `3 x 3` matrix and let `F(X),G(Y)` be arbitrary measurable real functions. Then

`Q = F(X) + 2 U^T C V + G(Y)`

has a bounded continuous density and

`||p_Q||_infinity <= 3 [M_X M_Y / |det C|]^(1/3)`.                (2.1)

For orthogonal projections of independent cap-one scalar inputs, the completed product-projection estimate recorded in the required pinned `math-open-problems@e5f71d79...` Fourier report gives

`M_X,M_Y <= 2^(3/2)`.

Hence

`boxed(||p_Q||_infinity <= 6 |det C|^(-1/3))`.                    (2.2)

#### Proof

For each frequency `t`, push the complex measure `exp(i t F(X)) dP_X` onto `U`. Its density `a_t` satisfies

`|a_t(u)| <= p_U(u)`,

so `||a_t||_2 <= M_X^(1/2)`. Likewise the push-forward of `exp(i t G(Y)) dP_Y` onto `V` has a density `b_t` with `||b_t||_2 <= M_Y^(1/2)`. This uses no independence among the three coordinates of either projection.

With Fourier convention `hat b(xi)=integral exp(i xi.v)b(v)dv`,

`phi_Q(t) = integral a_t(u) hat b_t(2 t C^T u) du`.

Cauchy-Schwarz, the change of variables `xi=2t C^T u`, and Plancherel give

`|phi_Q(t)|`
` <= ||a_t||_2 [integral |hat b_t(2t C^T u)|^2 du]^(1/2)`
` <= pi^(3/2) (M_X M_Y)^(1/2) |det C|^(-1/2) |t|^(-3/2)`.       (2.3)

Writing the right side as `B |t|^(-3/2)` and also using `|phi_Q|<=1`,

`integral_R min(1,B|t|^(-3/2)) dt = 6 B^(2/3)`.

Fourier inversion therefore yields

`||p_Q||_infinity <= (1/(2pi)) 6 B^(2/3)`
` = 3 [M_X M_Y/|det C|]^(1/3)`.

The same estimate proves `phi_Q in L1`, hence a bounded continuous representative. QED.

This is a source-valid use of projected dependence: the three projected coordinates may be highly dependent; only their joint density caps are used. It is also exactly why the third nonzero cross direction removes the rank-two logarithmic endpoint away from zero: rank two gives only the borderline `|t|^-1`, while three crossing directions give the integrable `|t|^-3/2`.

## 3. Application to the partner r40 punctured collar

In the r40 SVD normal form, the crossing term is

`2 u^T diag(σ1,σ2) v + 2 σ3 z W`,

with `(u,z)` and `(v,W)` three-dimensional orthogonal projections of disjoint original-coordinate product banks. All within-bank quadratic terms can be absorbed into the arbitrary phases `F(X)` and `G(Y)` in Lemma 2.1. Thus for every `σ3 != 0`, take

`C = diag(σ1,σ2,σ3)`.

The pinned `e5f71d79...` projection-density bound and (2.2) give the real full-line inequality

`||p_Q||_infinity <= 6 (σ1 σ2 |σ3|)^(-1/3)`.                    (3.1)

Now apply the designated partner's completed geometric result (1.1):

`||p_Q||_infinity`
` < 6 κ_*^(-1/3) s^(-2/3) |σ3|^(-1/3)`
` = 58.7121947444... s^(-2/3) |σ3|^(-1/3)`.                      (3.2)

This is the requested actual use of the newest compatible partner result. It proves that throughout the punctured collar the entire determinant deterioration comes from the single third cross singular value; the two directions carrying the logarithmic saddle are uniformly nondegenerate.

Partner r40's determinant identity

`σ1 σ2 σ3 = |det M| sqrt(det Γ_H det G_T rho_T)`

is consistent with this: a pure rank-three crossing argument must deteriorate as the graph defect tends to zero. The present proof identifies the exact analytic place where that loss enters: the Jacobian in the third Fourier coordinate.

## 4. Sign-specific ruled splice: only the two-sheet side remains

The required pinned `COUNTEREXAMPLE_SEARCH.md` proves Theorem C. For an exact-rank-three signature `(+,+,-)`,

`Q = lambda1 <r1,X>^2 + lambda2 <r2,X>^2 - mu <r3,X>^2`,

with all three magnitudes at least one,

`p_Q(s) <= pi sqrt(2)` for every `s >= 0`.                        (4.1)

This is the ruled one-sheet side and uses the original product-projection X-ray bound correctly. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids extending (4.1) to `s<0` from X-ray control alone. For signature `(+,-,-)`, apply the same theorem to `-Q`; the uniformly paid ruled side is `s<=0`.

Therefore, in the current exact-rank-three collar, the remaining interpolation is genuinely sign-specific:

- `(+,+,-)`: only the two-sheet side `s<0` is unpaid uniformly through `σ3 -> 0`;
- `(+,-,-)`: only the reflected two-sheet side `s>0` is unpaid uniformly.

The punctured estimate (3.2) pays that side for every fixed `σ3 != 0`, while the next section pays the exact endpoint `σ3=0`. The missing statement is uniformity between those two mechanisms.

## 5. Rank-two logarithmic endpoint and the two different third-direction mechanisms

The mandatory rank-two control remains literal. For independent centered unit uniforms,

`p_(2XY)(t) = log(1/(2|t|))`, `0<|t|<1/2`.                       (5.1)

So the rank-two saddle itself is not bounded.

There are now two rigorously distinct ways a third direction removes this singularity in the collar.

**Punctured collar, `σ3 != 0`.** The third cross coordinate contributes the additional Fourier half-power in (2.3): `|t|^-1` becomes `|t|^-3/2`. This yields a continuous density, but with the determinant cost `|σ3|^-1/3` after inversion.

**Exact graph endpoint, `σ3=0`.** The completed designated-partner r39 theorem does not pretend the rank-two density became bounded. Instead it keeps the exact rank-two crossing and uses the surviving within-bank term `2 z d^T u` as a dyadic frequency sweep. Its estimate is an integrated `L2(dt)` gain, not a false pointwise decay estimate, and gives a bounded continuous density at the endpoint without dividing by a third cross singular value.

Thus the third direction removes the logarithm in two different currencies: a genuine third crossing gives a literal extra stationary/Fourier half-power; at the null crossing endpoint, internal bilinear curvature supplies the missing aggregate half-power by dyadic averaging.

## 6. Why the remaining interpolation is not a routine perturbation

One might try to extend r39 by fixing the same-bank scalar `W`, applying the rank-two estimate to each slice, and averaging. Partner r40 proves the needed mixed norm can grow like a constant times `sqrt(N)` even for an orthogonal transform of three independent cap-one scalar laws. Hence that route is invalid.

The true Fourier-slice identity is instead

`integral ||b_(t,eta)||_2^2 d eta = 2 pi ||c_t||_2^2`,

where `c_t(v,w)` is the complex projected density and `b_(t,eta)` its Fourier transform only in `w`. This identity is uniformly bounded by the three-dimensional projection cap, but inserting the trajectory `eta=2t σ3 z` produces exactly the Jacobian `(|t σ3|)^(-1)` and hence (3.2). So the natural Hilbert replacement for the false spatial mixed norm is valid, but it does **not** close the endpoint uniformly.

This rules out a specific proof interface: taking absolute values and full `L2` in the third projected crossing before exploiting the internal bilinear sweep necessarily incurs the vanishing-cross Jacobian in this argument. A successful proof must combine the `z d^T u` sweep with the `zW` shear **before** that loss, or force an original-coordinate source-disjoint cut where the already-proved independent-residual theorem applies.

## 7. Exact remaining implication

`QFORM-TWOSHEET-SAMEBANK-SHEAR-INTERPOLATION-v3`:

> In the r40 punctured-collar normal form
> `F(u)+2 z d^T u+2u^T diag(σ1,σ2)v+2σ3 zW+G(Y)`,
> where `(u,z)` and `(v,W)` are orthogonal projections of two disjoint cap-one product banks, `σ1σ2 >= κ_* s^2`, and the r39 endpoint has `|d|` quantitatively nonzero in the null-ruling branch, prove a two-sheet density bound independent of `σ3`, or force a paid physical-pair/source-disjoint/ruled exit.

The proof may not condition on the dependent same-bank scalar `W`, replace the projection by an arbitrary joint density, assume moments or support, use post-rotation independence, or treat `σ3 zW` as a small random perturbation. The one-sheet side is already uniformly paid by the ruled theorem. Arbitrary additional nonseparable spectrum remains a separate full-QFORM bridge.

## Sources actually applied

- Required pinned `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`; the projection-density bound enters (2.2), and Theorem C enters (4.1).
- Designated partner fleet03/B11 r40: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T191401Z-fleet03-B11-QFORM-r40/REPORT.md`, report commit `2db0a7f81437b6e67efe800f129abebae0e10b4c`, verifier output `eb6031f9210b71fd099468fb86c94173b8b00c52`.
- Designated partner fleet03/B11 r39 exact-graph endpoint theorem: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T181640Z-fleet03-B11-QFORM-r39/REPORT.md`.

No task/schedule state, notification/email, permission, paid-call, cross-account-authentication, public-release, installation, benchmark, workflow, or unrelated-data action was performed.
