SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-24T04:14:07Z.
attacking: the r48 same-bank cancellation obstruction by a new mechanism: use the all-direction X-ray certificate forced by genuine orthogonal product projections, rather than another dependence-blind Lp closure.

# fleet03/B11 r49 — the r48 nonlinear cancellation law has infinite X-ray norm and therefore cannot be a genuine product projection

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: indefinite signatures `(2,1)` / `(1,2)`.
Status: **NEW RIGOROUS PROVENANCE-SEPARATION THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted owner conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity also remains open. This run changes mechanism after the preceding puncture/Lp interface work: instead of trying another same-bank norm interpolation, it asks which *linear-projection invariant* the r48 nonlinear cancellation falsifier necessarily violates.

No Gaussian, log-concave, moment, compact-support, connected-support, post-rotation independence, pointwise law-uniform van-der-Corput estimate, arbitrary-joint coarea lemma, worst conditional-density cap, or perturbative deletion of the puncture is used.

## 1. Starting point: the exact hard chamber and the r48 falsifier

The exact-rank-three null-pivot near-coloop normal form from fleet03/B11 r45 is

`Q = 2 kappa sqrt(q) H W
     + 2 kappa sqrt(1-q) T W
     + c V^2 + 2 e V W + d W^2`,

where `H` is one ORIGINAL independent coordinate and `(T,V,W)` is a THREE-DIMENSIONAL ORTHONORMAL LINEAR PROJECTION of the residual ORIGINAL product source. In the spectral normalization,

`kappa^2 |c| = |det M| >= s^3`,

and the puncture ratio is exactly

`eta := sqrt((1-q)/q)`.

At the live near-coloop threshold `q>=63/64`, `eta<=1/sqrt(63)`.

Run r48 tested a dependence-blind `L^3 x L^(3/2)` closure by defining, for independent centered unit uniforms `R,V,W`,

`T = R - V^2/(2 eta W)`

and taking an independent centered unit uniform `H`. The residual triple then has density

`g_eta(t,v,w)
 = 1_{|v|<=1/2} 1_{|w|<=1/2}
   1_{|t+v^2/(2 eta w)|<=1/2}`                       (1.1)

for `w!=0`, with density cap one and benign coordinate marginals, while

`2 H W + 2 eta T W + V^2 = 2W(H+eta R)`              (1.2)

retains the rank-two logarithmic singularity. r48 correctly recorded that this is not a QFORM counterexample because `(T,V,W)` was produced by a nonlinear triangular transformation rather than exhibited as an orthogonal linear projection of a product source.

The new point of this run is stronger: **such a representation is impossible.** The obstruction is an all-direction two-dimensional projection certificate.

## 2. The product-projection X-ray certificate

For an integrable density `g` on `R^3`, define its essential X-ray norm by

`X(g) := sup_{u in S^2} || m_u ||_infinity`,                   (2.1)

where `m_u` is the two-dimensional density of the orthogonal projection onto `u^perp`; equivalently, at Lebesgue points,

`m_u(z)= integral_R g(z+r u) dr`.                              (2.2)

### Lemma 2.1 — genuine residual product projections have `X<=e`

Let `X_1,...,X_m` be independent real variables with scalar densities at most one. Let `t,v,w in R^m` be orthonormal and put

`Y=(T,V,W)=(t.X,v.X,w.X)`.

Then every two-dimensional orthogonal projection of `Y` is itself a two-dimensional orthonormal projection of the original product vector `X`. The completed product-projection theorem used in the designated fleet04/B11 branch therefore gives

`boxed: X(p_Y) <= e.`                                          (2.3)

Proof: if `P:R^3->R^2` has orthonormal rows, then the two rows of `P[t;v;w]` are orthonormal in `R^m`, because `[t;v;w][t;v;w]^T=I_3`. Apply the two-dimensional product-projection density bound `||p||_infinity<=e`. Equation (2.2) is Fubini/disintegration. QED.

The exact numerical constant is not important for the separation below; finiteness uniform in the direction is enough.

## 3. New theorem: the r48 cancellation density has infinite X-ray norm

### Theorem 3.1 — `QFORM-R48-CANCELLATION-XRAY-IMPOSSIBILITY-v1`

For every fixed `eta>0`, the explicit density `g_eta` in (1.1) satisfies

`boxed: X(g_eta)=infinity.`                                   (3.1)

Consequently the law (1.1) is **not** an orthogonal three-dimensional linear projection of any independent cap-one product source, for any positive `eta`.

### Proof

Fix `eta>0`. We exhibit lines with arbitrarily long segments completely inside the support of `g_eta`, and then use the strict interior margin to make the same lower bound hold on an open set of nearby parallel lines, so the conclusion is an **essential** marginal-density lower bound rather than a value on one exceptional line.

Choose any sufficiently small

`0<w_0<1/2`,                                                   (3.2)

put

`v_0=1/4`, `Delta = sqrt(eta w_0)/2`,                         (3.3)

and require `Delta<=1/8`, which is possible by taking `w_0` smaller. At fixed `w=w_0`, the center graph of the last indicator in (1.1) is

`t_c(v) = -v^2/(2 eta w_0)`.                                  (3.4)

Take its tangent line at `v_0`:

`t_l(v)
 = -v_0^2/(2 eta w_0)
   - [v_0/(eta w_0)](v-v_0),
`
`w=w_0`.                                                       (3.5)

The tangent cancellation is exact:

`t_l(v)+v^2/(2 eta w_0)
 = (v-v_0)^2/(2 eta w_0).`                                   (3.6)

Hence for `|v-v_0|<=Delta`,

`|t_l(v)+v^2/(2 eta w_0)|
 <= Delta^2/(2 eta w_0)=1/8<1/2.`                            (3.7)

Also `v in[1/8,3/8]`, so `|v|<1/2`, and `0<w_0<1/2`. Thus the whole compact line segment belongs to the strict interior of the support in (1.1), with a fixed positive margin in every defining inequality.

Its Euclidean arclength is

`L(w_0)
 = 2 Delta sqrt(1+[v_0/(eta w_0)]^2)
 >= 2 Delta v_0/(eta w_0)
 = 1/[4 sqrt(eta w_0)].`                                     (3.8)

As `w_0 downarrow0`, the right side diverges.

Because the segment in (3.7) is compact and lies strictly inside the support, continuity of the defining function away from `w=0` gives a nonempty open neighborhood of parallel affine lines whose intersections with the support contain segments of length arbitrarily close to `L(w_0)`. Therefore the two-dimensional marginal perpendicular to the line direction has essential supremum at least, say, `L(w_0)/2`.

Given any `M<infinity`, choose `w_0` so small that `L(w_0)>2M`; then one two-dimensional marginal has essential supremum `>M`. Since `M` was arbitrary, (3.1) follows. QED.

### Concrete live-scale check

At the largest live puncture

`eta=1/sqrt(63)=0.1259881576697424...`

and merely `w_0=10^(-8)`, the explicit lower bound (3.8) is

`L(w_0) >= 7043.283118153145...`,                             (3.9)

already vastly larger than the genuine product-projection cap `e=2.71828...`. Letting `w_0` decrease proves divergence, not just a large finite discrepancy.

## 4. What this proves about the r48 obstruction

Run r48 only established that no orthogonal-product representation of (1.1) had been supplied. Theorem 3.1 plus Lemma 2.1 upgrades that to the rigorous statement

`boxed: the exact nonlinear cancellation mechanism in r48 cannot occur as the residual orthogonal projection law in the true r45/r46 hard chamber.`       (4.1)

The reason is geometric. The identity `T=R-V^2/(2 eta W)` forces the support to follow a parabolic sheet whose tangent slope is of order `1/(eta w)` as `w->0`. Even though the sheet is only unit-thick in the `T` coordinate and all three coordinate marginals can look harmless, its near-tangent line intersections grow like `(eta w)^(-1/2)` and violate the uniform all-direction two-dimensional projection certificate of genuine product sources.

This does **not** yet prove that every true product projection removes the logarithm. The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` shows that a generic probability density can have uniformly bounded X-ray norm and still put arbitrarily high density on an indefinite quadratic level. Therefore the next step cannot be `X-ray cap => QFORM` in isolation.

What changes is the exact unpaid implication: one now needs a **puncture-specific parabolic trace estimate** that combines

1. the genuine all-direction X-ray certificate `X<=e`,
2. the exact orthogonal product characteristic-function factorization,
3. the determinant-tied square `kappa^2|c|>=s^3`, and
4. the small puncture geometry `eta=sqrt((1-q)/q)`,

before taking a worst fiber or an absolute TT* norm. The r48 cancellation law is no longer an admissible model for the true residual source.

I name this successor

`QFORM-PUNCTURE-PRODUCT-XRAY-PARABOLIC-TRACE-v1`.             (4.2)

A useful target form is the original unsheared residual polynomial

`2 kappa sqrt(q) H W
 +2 kappa sqrt(1-q) T W
 +cV^2+2eVW+dW^2`,                                           (4.3)

because `(T,V,W)` is an orthonormal product projection there. The proof must retain the product factorization; X-ray information alone is explicitly insufficient by the recorded correction.

## 5. Designated fleet04/B11 mathematics applied at actual inequalities

Two completed fleet04/B11 inputs are used with their exact scopes.

First, its partition-stable null-scalar branch uses the standard two-dimensional product-projection theorem with cap `M<=e`; Lemma 2.1 applies that theorem to **every** plane `u^perp`, yielding the actual inequality `X(p_Y)<=e`. Combined with (3.8), this gives the direct contradiction

`1/[8 sqrt(eta w_0)] <= e`                                   (5.1)

for a hypothetical product-projection representation once the robustness factor `1/2` is included. Since `w_0` can be arbitrarily small, (5.1) fails.

Second, the completed fleet04/B11 pair-area receiver remains an actual paid exit in the live near-coloop geometry:

`||p_Q||_infinity <= 128 sqrt(2)/(s sqrt(g_ij)).`             (5.2)

For the physical hub `0` and a residual transverse leaf `j`,

`g_0j=q ||w_j||^2`.

Thus if the large-leaf branch occurs,

`q>=63/64`, `||w_j||^2>=1/36`,

then

`g_0j>=7/256`,                                                (5.3)

and substitution in (5.2) gives

`boxed: ||p_Q||_infinity
 <= 2048 sqrt(2/7)/s
 = 1094.7020468732903.../s.`                                 (5.4)

The new X-ray separation is therefore aimed only at the genuinely diffuse residual collar after this already-paid partner exit.

## 6. Mandatory rank-two control and scope

For centered unit uniforms the opposite-sign rank-two benchmark remains

`p_(2XY)(z)=log(1/(2|z|))`, `0<|z|<1/2`.                     (6.1)

The r48 construction reproduced this logarithm by hiding the third square inside a nonlinear same-source shift. Theorem 3.1 proves that this hiding forces infinite all-direction X-ray norm and hence is unavailable to a true orthogonal projection of the original product source.

What remains open is quantitative: convert the finite product-projection X-ray/factorization certificates into a universal **linear** small-ball estimate. No claim of full exact-rank-three closure, arbitrary-extra-spectrum closure, or full continuity is made here.

## 7. Sources

- Immediate B11 predecessor: `yspennstate/math-open-problems@1981b7ded0883caf72e23b833f34274a6763a43c`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260924T023910Z-fleet03-B11-QFORM-r48/REPORT.md`.
- Exact puncture normal form: `yspennstate/math-open-problems@12e2174445fbc824279bf1376da1346454d7060a`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260924T002432Z-fleet03-B11-QFORM-r45/REPORT.md`.
- Designated fleet04/B11 null-scalar/product-projection source: `yspennstate/math-open-problems@4110bbfd21beffa0260a017d468b0a486af56db1`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260922T222040Z-fleet04-B11-cone-envelope-r3/REPORT.md`.
- Designated fleet04/B11 pair-area source: `yspennstate/math-open-problems@30555c1ca97752e10f5089ccd95f8514c704be5a`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T131400Z-fleet04-B11-extension-mass-r6/REPORT.md`.
- X-ray-only global barrier: `yspennstate/math-open-problems@cfb4137e221cd87aeb4f669389d14fa65e3251e7`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260922T120617Z-a01-b06-qform-r11/REPORT.md`.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity: **OPEN**.
