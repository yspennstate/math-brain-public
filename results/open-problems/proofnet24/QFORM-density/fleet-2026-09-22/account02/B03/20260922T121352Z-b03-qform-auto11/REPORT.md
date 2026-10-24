# account02/B03 — overlap-collapse adversary to disjoint cross-packet aggregation

**Run:** `20260922T121352Z-b03-qform-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Decoupled time integral`  
**Classification:** `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Source pins and corrections actually used

Fresh control was resolved in `yspennstate/math-research-brain`; the start snapshot was `0d962a499ad69876cb875825d50db53590d4be92` and the pre-publication refresh was `25af4c31b7ba0d84440c74308e4490eb76f83f2a`, both under owner revision `2026-09-22.5`. The live target remains the arbitrary independent-density quadratic-form conjecture. The active check-in request `QFORM-CHECKIN-20260922T120815Z` was also read.

Corrections retained: law-uniform pointwise one-dimensional Fresnel decay is false; rotated spectral coordinates are not independent; fiber-supremum estimates can lose dimension; `QFORM-CROSSMINOR-ALONE-FALSE` forbids promoting a `2 x 2` cross minor to a universal density smoother; the newer `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH` shows that a universal constant, if it exists, must exceed `pi` and records a rank-three diffuse branch only.

The named partner result actually consumed and applied is

- `yspennstate/math-open-problems@32ac33a81e5b3b17a0016463f67e544adc474280:proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T121240Z-account03-B03-QFORM-r11/REPORT.md`.

Its theorem `QFORM-SQUARE-CROSSPACKET-PLANCHEREL-v1` says that for disjoint original-coordinate triples `I,J`, if `C=A[I,J]` is invertible and `delta=|det C|`, then

`||phi_Q||_1 <= 6*pi*delta^(-1/3)` and `||p_Q||_infinity <= 3*delta^(-1/3)`.

This theorem is used below on the exact family, not merely cited.

Two compatible supporting results are also used only in their proved scopes:

- account02/B04 `QFORM-BILINEAR-PLUS-SQUARE-v1`, source `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T114427Z-qform-product-rearrange-r1/ADDENDUM_ISOTROPIC_MODEL.md`, proving a uniform bound for `2cXY+lambda Z^2` under independent density-one inputs;
- account03/B01 `QFORM-ZERO-DIAGONAL-PAIR-BLOCK-v1`, source `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260922T113140Z-account03-B01-qform-r1/REPORT.md`, proving `||p_Q||_infinity <= C0 |det A_S|^(-1/3)`, `C0<7.90`, for a selected principal triple with its first two diagonal entries zero and nonzero determinant, uniformly over outside couplings.

## 2. The overlap-collapse family

Work in a three-dimensional spectral space with

`Lambda=diag(1,1,-1)`.

Define the orthonormal vectors

`e=(1,0,1)/sqrt(2)`, `p=(1,0,-1)/sqrt(2)`, `q=(0,1,0)`.

In the orthonormal basis `(e,p,q)`, the matrix of `Lambda` is exactly

```
[0 1 0]
[1 0 0]
[0 0 1],
```

so the spectral quadratic form is `2 y_e y_p + y_q^2`.

Fix `0<=epsilon<=1` and put `a=sqrt(1-epsilon^2)`. Let the six physical-coordinate rows of an isometry `U_epsilon` be

`u_1=a e`,
`u_6=epsilon e`,
`u_2=u_3=p/sqrt(2)`,
`u_4=u_5=q/sqrt(2)`.

Then

`sum_i u_i u_i^T=(a^2+epsilon^2)ee^T+pp^T+qq^T=I_3`.

Hence `U_epsilon^T U_epsilon=I_3`, and

`A_epsilon=U_epsilon Lambda U_epsilon^T`

has nonzero eigenvalues exactly `1,1,-1`. It is therefore a genuine target family for every `epsilon`, including the indefinite endpoint cases.

For independent physical inputs with densities at most one, define the disjoint-group aggregates

`E=a X_1+epsilon X_6`,
`P=(X_2+X_3)/sqrt(2)`,
`R=(X_4+X_5)/sqrt(2)`.

They are independent, and the quadratic form is exactly

`Q_epsilon=2 E P+R^2`.                                             (2.1)

A useful feature of this family is that every physical diagonal coefficient is small: the four rows in the `e` and `p` directions are `Lambda`-isotropic, while the two `q` rows have diagonal coefficient `1/2`. Thus

`max_i |(A_epsilon)_{ii}|=1/2`;                                  (2.2)

there is no hidden three-large-diagonal-coordinate shortcut.

## 3. Exact disjoint-crosspacket determinant collapse

A three-row determinant of `U_epsilon` is nonzero if and only if the triple contains exactly one `e`-row, one `p`-row and one `q`-row. Its absolute determinant is

`a/2` if the `e`-row is row 1, and `epsilon/2` if the `e`-row is row 6.

For disjoint triples `I,J` to have an invertible `3 x 3` cross block `A_epsilon[I,J]`, both row triples must have full rank. They must therefore split the two `e` rows, split the two `p` rows, and split the two `q` rows. By

`A[I,J]=U_I Lambda U_J^T`,

we obtain the exact identity

`boxed{ |det A_epsilon[I,J]| = a*epsilon/4 }`                    (3.1)

for every invertible disjoint `3 x 3` crosspacket. Every other disjoint packet is singular.

The same obstruction holds for arbitrary two-block partitions, not only triples. A cross block has spectral rank three only if each side receives one of the two `e` rows and has nonzero `p` and `q` content on both sides. Because the `p` and `q` copies have equal squared weights `1/2`, every rank-three partition has product of its three nonzero cross singular values

`Delta=a*epsilon/4`.                                              (3.2)

Thus the rank-three cross resource tends to zero as `epsilon->0` or `epsilon->1`, even though the spectrum stays identically `(1,1,-1)`.

### Direct application of the named partner theorem

Applying account03/B03 to any invertible packet gives the actual inequalities

`boxed{ ||p_Qepsilon||_infinity <= 3 (4/(a epsilon))^(1/3) }`,   (3.3)

and

`boxed{ ||phi_Qepsilon||_1 <= 6*pi (4/(a epsilon))^(1/3) }`.     (3.4)

These are correct source-valid bounds, but their constants blow up like `epsilon^(-1/3)` at the overlap-collapse endpoint. At `epsilon=0`, every cross block has rank at most two and the partner theorem is simply inapplicable.

Consequently the following proposed proof mechanism is refuted:

> infer a dimension-free bound from the three-large-eigenvalue hypothesis by selecting a disjoint rank-three original-coordinate cross packet (or a rank-three coordinate partition) and paying its reciprocal determinant/singular-product cost before any overlap-aware aggregation.

This is a counterexample to that mechanism, not to the owner conjecture.

## 4. The same family stays uniformly bounded after overlap-aware grouping

The crosspacket singularity is artificial. Equation (2.1) groups the overlapping spectral direction before any reciprocal determinant is paid.

The aggregate density caps are source-valid and elementary. Put `m=max(a,epsilon)`. Since `a^2+epsilon^2=1`, `m>=1/sqrt(2)`. The density of `E` is the convolution of two scaled input densities, hence

`||p_E||_infinity <= 1/m <= sqrt(2)`.                           (4.1)

Similarly

`||p_P||_infinity, ||p_R||_infinity <= sqrt(2)`.                 (4.2)

Scale `E,P,R` by their density caps to variables with density at most one and apply `QFORM-BILINEAR-PLUS-SQUARE-v1`. In the simple uniform cap `sqrt(2)` on all three aggregates, (2.1) becomes

`Q_epsilon = E_tilde P_tilde + (1/2) R_tilde^2`

with the three tilded variables independent and density at most one. Thus the B04 theorem with `c=1/2`, `lambda=1/2` gives

`boxed{ ||p_Qepsilon||_infinity <= 2 + 4*24^(1/3) < 13.538 }`    (4.3)

uniformly for every `0<=epsilon<=1` and every permitted collection of six input laws.

The sharper cap `||p_E||_infinity<=1/m` can improve (4.3), but the important point is that the constant does not deteriorate at either crosspacket-collapse endpoint.

There is also an overlapping principal certificate. Choose the larger of rows 1 and 6, whose `e` coefficient is `m`, together with one `p` row and one `q` row. The resulting principal block has its first two diagonal entries zero and

`|det A_S|=m^2/4 >= 1/8`.                                       (4.4)

Account03/B01 therefore gives the alternative uniform estimate

`||p_Qepsilon||_infinity <= 2 C0 < 15.80`.                      (4.5)

So the same family that makes every disjoint rank-three cross certificate degenerate retains a uniformly nondegenerate **overlapping principal** certificate.

## 5. Corrected sufficient statement suggested by the adversary

For this family, a correct local certificate must allow overlap before paying reciprocal determinant cost. One exact hybrid sufficient statement is:

- if a disjoint square crosspacket has determinant `delta_x>0`, use the partner bound `3 delta_x^(-1/3)`;
- if a zero-diagonal-pair principal triple has determinant `delta_p>0`, use the B01 bound `C0 delta_p^(-1/3)`;
- take the better certificate only after both are formed from the original product coordinates.

For `A_epsilon`,

`delta_x=a epsilon/4`,
`delta_p=m^2/4>=1/8`.                                           (5.1)

The disjoint certificate collapses, while the overlapping certificate remains uniformly strong. This demonstrates that determinant-mass aggregation must be **overlap-aware**; a Cauchy--Binet mass argument that first insists on two disjoint full-rank triples necessarily misses legitimate smoothing carried by a common hub coordinate.

A compact conditional full-target route is therefore now sharper:

1. diffuse rank-three curvature is already controlled by the current diffuse/cross-block theorems;
2. a disjoint rank-three crosspacket is controlled by the named partner theorem;
3. overlap-collapse states must be routed into a principal/hyperbolic or other hub-aware smoother before reciprocal determinant loss;
4. the first still-unpaid implication is a universal structural dichotomy/aggregation theorem that performs this routing for arbitrary admissible `A`, including extra eigendirections and nonseparable heavy branches.

The family above proves that item 3 is logically necessary; it is not merely a matter of improving constants in item 2.

## 6. Independent-copy interpretation

The exact independent-copy identity remains

`|phi_Q(t)|^2 = E exp(it[Q(X)-Q(X')])`.

For the grouped form (2.1), expanding differences creates dependent sum/difference pairs within each aggregate, so no independence of `E+E'` and `E-E'` (or of the analogous pairs) is used. The partner's Cauchy--Plancherel estimate is a legitimate block-level way of spending this `L^2` resource on a disjoint crosspacket. Equations (3.3)-(4.3) show the limitation: if the spectral direction is nearly shared through one common hub, spending the reciprocal cross determinant first loses the uniform scale. Grouping or a principal/hyperbolic certificate has to occur earlier.

This is consistent with the previous account02/B03 scalar-difference obstruction: a one-dimensional small-ball estimate for `Q-Q'` does not by itself recover linear scaling after square-root symmetrization.

## 7. Status

- `QFORM-FULL`: **OPEN**.
- `QFORM-OVERLAP-COLLAPSE-CROSSPACKET-ADVERSARY-v1`: **PROVED**.
- Pure disjoint-crosspacket selection as a universal spectral bridge: **CANDIDATE_REFUTED**.
- Named partner `QFORM-SQUARE-CROSSPACKET-PLANCHEREL-v1`: **APPLIED** to (3.3)-(3.4), with its exact determinant cost.
- Overlap-aware aggregate bound (4.3): **PROVED FROM SOURCE-PINNED B04 THEOREM**.
- Overlapping principal repair (4.4)-(4.5): **PROVED FROM SOURCE-PINNED B01 THEOREM**.
- Full structural overlap-aware aggregation/dichotomy for arbitrary `A`: **OPEN / first unpaid implication**.

No numerical simulation, moment assumption, support assumption, post-rotation independence, pointwise Fresnel lemma, public release, paid model/API call or native-memory claim is used. The only numerical decimal `13.538` is the rounded value of the displayed exact constant `2+4*24^(1/3)`.
