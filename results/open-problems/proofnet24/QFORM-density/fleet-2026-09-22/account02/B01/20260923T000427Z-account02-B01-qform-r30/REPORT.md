SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T00:04:27Z.
attacking: the N3 no-pivot class by testing D'/D5 against an exact rank-three hub-plus-square family and applying the mixed-hub averaged-frequency theorem before any tiny physical-pair payment.

# QFORM r30: an exact N3 hub obstruction to cross-volume-only closure

## Status

**ESSENTIAL_STEP_APPLIED + EXPLICIT_INTERMEDIATE_OBSTRUCTION + SELF-CORRECTION.** Full QFORM remains OPEN. This report gives an exact strict-no-pivot family on which every D'/D5 cross-volume currency vanishes, while Claude's completed mixed-hub theorem gives a uniform density bound. It also records and rejects a tempting but invalid shear extension of that theorem; the rejection preserves the original-coordinate product provenance required by the target.

Execution context: `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub retrieval was used; no native learned-memory receiver use was established.

## Sources actually consumed


Newest required Claude source:
- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`
- same commit/path `FOURIER_ROUTE_REPORT.md`
- same commit/path `COUNTEREXAMPLE_SEARCH.md`

Later geometric source actually checked:
- `yspennstate/math-open-problems@2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/GEOMETRIC_ROUTE_REPORT.md`
- `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`
- same commit/path `REPORT.md`

Assigned partner actually applied:

Corrections preserved: no law-uniform pointwise quadratic Fresnel decay; no post-rotation independence; no arbitrary-joint rank-three coarea; no worst-fiber conditional-density supremum; no assumption of a uniformly good physical pair or rank-three cross cut.

## 1. A tempting null-hub shear extension is NOT justified

There is a useful algebraic identity, but it does **not** by itself preserve the product structure needed by Claude's mixed-hub theorem.

Suppose an exact-rank-three homogeneous matrix has physical block form

`A=[[0,g^T],[g,B]]`, with `g!=0`.

Let `gamma=||g||_2`, put `e=g/gamma`, and decompose the leaf space as `span{e} direct_sum g^perp`. In this orthogonal basis,

```
A = [[0, gamma, 0],
     [gamma, b, c^T],
     [0, c, D]].
```

The leading block `H=[[0,gamma],[gamma,b]]` is invertible and `(H^{-1})_{22}=0`, so its Schur complement is exactly `D`. Hence

`rank A = 2 + rank D`.

Because `rank A=3`, `D` has rank one. Thus `D=lambda r r^T` for a unit `r in g^perp`. Choosing

`h=(b/(2 gamma))e+c/gamma`

gives the exact algebraic form

`B=g h^T+h g^T+lambda r r^T`

and therefore

`Q=2(X_0+h.X')(g.X')+lambda(r.X')^2`.

A first draft of this run tried to translate the physical hub variable to `z=X_0+h.X'` and then invoke mixed-hub Theorem H. That step is invalid in general. After the shear, the joint density is

`f_0(z-h.x') prod_j f_j(x_j)`,

which is bounded pointwise by the leaf product density but is **not** a product amplitude. The Fresnel/Brascamp-Lieb part of Theorem H needs the original leaf factorisation after the hub integration. A bounded nonseparable multiplier cannot simply be deleted inside an oscillatory integral after taking an absolute value. Equivalently, integrating `X_0` first in the original variables produces the nonseparable quadratic twist

`exp(2it(g.X')(h.X')) psi_0(2t g.X')`,

which is not covered by the stated rank-one-leaf hypothesis.

So this run does **not** claim a general shear-stable null-hub theorem. This self-correction is important: the exact target forbids replacing original-coordinate product provenance by a dependent post-shear law.

## 2. Exact N3 no-pivot stress family

Fix `tau in (0,1]`. Choose an even integer `m>=2` with `1/m<tau`. Use `2m+1` original coordinates

`X_0, Y_1,...,Y_m, Z_1,...,Z_m`,

all independent with arbitrary densities at most one, and define

`Q_m = 2 X_0 (m^(-1/2) sum_j Y_j) + (m^(-1/2) sum_k Z_k)^2`.

Equivalently the only nonzero matrix entries are

`A_{0,Y_j}=A_{Y_j,0}=m^(-1/2)` and `A_{Z_j,Z_k}=1/m`.

On the normalized span of `X_0`, `m^(-1/2)sum Y_j`, `m^(-1/2)sum Z_k`, the matrix is

```
[[0,1,0],
 [1,0,0],
 [0,0,1]].
```

Hence the complete nonzero spectrum is exactly `{-1,1,1}`. This is a genuine full-target family.

It also lies in the strict N3 no-`tau`-pivot class:
- every diagonal is `0` or `1/m<tau`;
- a hub-Y physical pair has determinant `-1/m`, hence magnitude `1/m<tau`;
- every other physical `2x2` principal determinant is zero.

Thus no large scalar or pair pivot is available.

## 3. D' and D5 are identically blind to this N3 family

For every coordinate cut `I union J`, the cross block `A_IJ` is the sum of two matrices:
- the split part of the hub-Y star, rank at most one;
- the split part of the Z-bank rank-one matrix `J_m/m`, rank at most one.

Therefore

`rank A_IJ <=2`

for every cut. Consequently

`e_3(A_IJ^T A_IJ)=0` and `e_5(A_IJ^T A_IJ)=0`

for every cut.

Thus the completed Claude D' and D5 theorems cannot produce a finite bound on this family: their respective volume currencies vanish identically. This is an exact obstruction to any proposed proof of N3 using only those cross-volume certificates. It is not an obstruction to QFORM itself.

## 4. Claude's completed mixed-hub theorem closes the same family uniformly

This is the required application of the newest report to an actual inequality.

Take `H={0}`, `I={all Y and Z coordinates}`, and `J=empty`. The leaf quadratic block is the single rank-one square

`r=(0_Y,m^(-1/2)1_Z)`, with `lambda=1`,

and the hub coupling vector is

`g=(m^(-1/2)1_Y,0_Z)`.

The augmented leaf rows are `(r_j,g_j)`. Their Gram matrix is exactly `G=I_2`, and every normalized augmented row leverage equals `1/m<=1/2`. Theorem H in the Claude source therefore gives

`|phi_{Q_m}(t)| <= 4 pi^(3/2) |t|^(-3/2)`.

Keeping the small-frequency cap `|phi|<=1`,

`integral_R min(1,K|t|^(-3/2)) dt = 6 K^(2/3)`.

With `K=4 pi^(3/2)`, Fourier inversion yields

`||p_{Q_m}||_infinity <= 3*2^(4/3) < 7.560`.

The bound is uniform in `m` and in **all** input laws satisfying only the density-cap-one assumption. This is a joint averaged-frequency mechanism: it leaves intact the phase-aligned-density refutation of law-uniform one-dimensional pointwise Fresnel decay.

The newer geometric report independently identifies the same structural phenomenon: hub configurations can be invisible to off-diagonal rank-three volume while remaining controllable by a third, hub-sensitive tool. The family above places that phenomenon inside the exact strict N3 class.

## 5. Assigned partner r20 applied to the same family

Use the physical endpoint pair `(X_0,Y_1)`. Its matrix is

`[[0,m^(-1/2)],[m^(-1/2),0]]`,

so

`D=|det P|=1/m`, `kappa=sigma_min(P)=m^(-1/2)`.

Completing this pair leaves the unchanged Z-bank rank-one block `J_m/m`. Split the Z bank into two equal halves. The corresponding Schur cross block has Frobenius norm

`F=1/2`.

The completed account03/B01 r20 endpoint-pair theorem therefore gives the valid but nonuniform estimate

`||p_{Q_m}||_infinity <11.021 D^(-2/5) kappa^(-1/10) F^(-1/10)`

`=11.021*2^(1/10) m^(9/20) <11.813 m^(9/20)`.

Its logarithmic alternative is, for `m>=64`,

`||p_{Q_m}||_infinity <=22.648 sqrt(m)`,

because `4D/(kappa F)=8/sqrt(m)<=1`.

Thus the partner theorem is fully compatible but quantitatively confirms that paying one tiny physical pair before grouped hub/square aggregation is the wrong currency on this N3 family. The mixed-hub estimate removes that loss entirely.

## 6. Consequence for the live N3 reduction

The first unpaid structural implication is sharpened to

**QFORM-N3-HUB-OR-VOLUME-ROUTING-v1.** In the strict no-pivot class, a complete proof cannot rely only on D'/D5 cross-volume. It must route rank-three-cross-blind configurations into a hub/mixed-Fresnel or equivalent grouped-coordinate certificate **before** paying any tiny physical-pair determinant. The exact family above is already paid by the hub route. The live debt is a quantitative routing theorem covering clustered hub leverage, hybrid hub-plus-dense-tail configurations, and arbitrary higher-rank no-pivot residuals without destroying original-coordinate product provenance.

This narrows the N3 mechanism but is not a full solution. Full QFORM remains OPEN and has not received two end-to-end reviews.
