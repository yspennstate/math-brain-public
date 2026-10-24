SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-23T01:48:01Z.
attacking: the exact-rank-three hybrid/near-null physical direction: consume the ruled-side theorem, preserve product provenance, and close the exact-graph nonzero interpolation before the positive-residual collar.

# account02/B10 — exact-graph cross-transverse interpolation closes every scalar pivot

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T014801Z-account02-B10-QFORM-auto11`  
Assignment: Rank-three coupled case; complementary constructions/source-valid counterexamples  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full target remains OPEN: independent original coordinates have arbitrary real probability densities bounded by one; the symmetric matrix must have at least three eigenvalues of modulus at least one; no moment, support, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption is available. Continuity is tracked separately.

## 1. Source boundary and the first unpaid implication

The newest required Claude source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, is used at an actual inequality. Its ruled-level-set theorem gives, for an exact-rank-three indefinite form at spectral scale at least one,

`p_Q(t) <= pi sqrt(2)`

on the one-sheet side for every admissible product law. Therefore this report does not reprove that side and concentrates on the surviving near-null/two-sheet product-overlap geometry.

The designated partner actually consumed is account03/B10 r21,

`math-open-problems@3136d1f31dd7e723ddef05d06edce6fe769dc384`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T231827Z-account03-B10-QFORM-r21/REPORT.md`.

Its nonnull rank-one-bank theorem says that if a disjoint original-coordinate bank lies on a spectral ray `u`, has total squared row mass `m`, `q=u^T M u !=0`, and `D=|det M|`, then

`||p_Q||_infinity <=128 sqrt(2) m^(-1/2) D^(-1/4)|q|^(-1/4)`.       (1.1)

This report applies (1.1) quantitatively in Section 5.

A second completed input is account01/B16 r12,

`math-open-problems@7140ff63d4ff7c092cdc18ce7ad8a95e4e03e388`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260923T003846Z/REPORT.md`.

Its `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1` theorem is the dependence-safe receiver used below: if a cap-one scalar `X` is genuinely independent of a two-dimensional vector `Y` of joint density cap `M_2`, and an invertible symmetric active matrix is

`H=[[a,b^T],[b,C]]`,

then after rotating only inside the already-joint `Y` plane so that `b=(beta,0)` and writing `C=[[c,d],[d,e]]`, with

`D_H=|det H|`, `P=beta^2 |e|>0`,

arbitrary affine terms satisfy

`||p_Q||_infinity <= C_CT M_2^(2/3)(D_H P)^(-1/6)`,               (1.2)

where

`C_CT=103680^(1/3)=46.9784116940...`.

This retains the nonzero cross-transverse determinant resource `P`; it does not invoke the refuted cap-only nonlinear receiver interface.

The immediate unpaid B10 implication before this run was the nonzero-near-null interpolation in a high-leverage physical direction. The theorem below closes that interpolation whenever one quantitative transverse bank is an exact graph. The positive regression-residual collar remains afterward.

## 2. Exact-graph state and product provenance

Write the exact-rank-three form as

`A=R M R^T`, `R^T R=I_3`,                                      (2.1)

where `M` is real symmetric invertible and

`sigma_min(M)>=s>0`, `D:=|det M|`.                              (2.2)

Let physical coordinate `0` be heavy,

`r_0=sqrt(c) u`, `||u||=1`, `0<c<=1`.                           (2.3)

Let `B` be a disjoint bank of original coordinates. Assume its spectral rows form an exact graph over `u^perp`: for every `j in B`,

`r_j=(w dot p_j)u+p_j`, `p_j in u^perp`,                        (2.4)

for one fixed `w in u^perp`. Let

`G=sum_(j in B) p_j p_j^T`, `G>=kappa I_2`, `h:=det G>0`,        (2.5)

and put

`q:=u^T M u`.                                                    (2.6)

The exact graph hypothesis is the zero-regression-residual endpoint `rho_B=0` in the preceding one-heavy/two-bank reduction; it is not an assumption of independence inside the projected bank.

Parseval for the full spectral frame gives

`sum_(j!=0) (r_j dot u)^2=1-c`.                                  (2.7)

Hence, using only the rows in `B`,

`w^T G w=sum_(j in B)(w dot p_j)^2 <=1-c`,                       (2.8)

and therefore

`||w||^2 <=(1-c)/kappa`.                                        (2.9)

Now condition on every original coordinate outside `{0} union B`. This is product-safe conditioning: `X_0` is still an original cap-one scalar, and it is genuinely independent of the entire bank `X_B`. Define the bank projection

`Z=sum_(j in B) p_j X_j in u^perp`.                              (2.10)

The source-valid two-dimensional product-projection theorem gives

`||p_Z||_infinity <=2/sqrt(h)`.                                  (2.11)

No independence between the two coordinates of `Z` is asserted or used. Outside conditioning contributes only affine and constant terms to the active polynomial.

## 3. Exact cross-transverse invariant

Choose an oriented orthonormal basis `(u,e_1,e_2)` of spectral space and define the graph map

`Tz=z+(w dot z)u`.                                                (3.1)

The active spectral map from the variables `(X_0,Z_1,Z_2)` is

`F=[sqrt(c)u, T e_1, T e_2]`.                                    (3.2)

Since this graph map has determinant one in the `u` direction,

`det F=sqrt(c)`,                                                  (3.3)

so for the active quadratic matrix

`H=F^T M F`                                                       (3.4)

we have the exact determinant and pivot identities

`|det H|=cD`, `H_00=cq`.                                         (3.5)

Write the receiver block and scalar-receiver cross vector as

`C=T^T M T`, `b=sqrt(c) T^T M u`.                                (3.6)

The cross-transverse theorem (1.2) uses

`P=|b^T adj(C)b|`.                                                (3.7)

The block determinant identity gives

`P=|cq det C-det H|`.                                            (3.8)

The key new calculation is an exact coordinate-free formula for `det C`. Embed `w` in the plane `u^perp` and put

`n:=u-w`.                                                         (3.9)

The oriented cross product of the two graph columns is exactly

`(T e_1) cross (T e_2)=n`.                                      (3.10)

For every invertible `3 x 3` matrix `M`, the two-dimensional compression determinant identity is

`det(T^T M T)=det(M) n^T M^(-1)n`.                               (3.11)

One way to see (3.11) is to use `adj(M)=det(M)M^(-1)`: the determinant of the bilinear form on the span of the two graph columns equals the adjugate quadratic form evaluated on their cross product.

Combining (3.8), (3.11), `det H=c det M`, and taking absolute values yields the exact invariant

`boxed: P=cD |1-q n^T M^(-1)n|.`                                (3.12)

This is the interpolation currency missing from the exact-null theorem: at `q=0`, `P=cD`; for small nonzero `q`, the resource cannot disappear unless the scalar pivot has moved a quantitatively non-small distance from zero.

Since `||M^(-1)||_op<=1/s`, (2.9) gives

`|q n^T M^(-1)n|
 <=(|q|/s)||n||^2
 =(|q|/s)(1+||w||^2)
 <=(|q|/s)(1+(1-c)/kappa).`                                     (3.13)

Define

`eta:= (|q|/s)(1+(1-c)/kappa).`                                  (3.14)

Whenever `eta<1`, (3.12) implies

`boxed: P>=cD(1-eta).`                                           (3.15)

No coefficient-smallness is being treated as a small random perturbation; (3.15) is a deterministic matrix identity plus an operator-norm bound.

## 4. Near-null exact-graph density theorem

### Theorem 4.1 — `QFORM-EXACTGRAPH-CROSS-TRANSVERSE-INTERPOLATION-v1`

Under (2.1)--(2.6), if `eta<1`, then for arbitrary cap-one original product inputs and arbitrary outside affine terms,

`boxed:
 ||p_Q||_infinity
 <= C_CT 2^(2/3) h^(-1/3)(cD)^(-1/3)(1-eta)^(-1/6).
`                                                                    (4.1)

#### Proof

After conditioning outside `{0} union B`, `X_0` is genuinely independent of `Z` and (2.11) gives receiver cap

`M_2<=2/sqrt(h)`.                                                   (4.2)

The active matrix has determinant scale `D_H=cD` by (3.5), and its cross-transverse invariant obeys `P>=cD(1-eta)` by (3.15). Applying the completed cross-transverse projection-product theorem (1.2), including its affine extension, gives

`||p_(Q|outside)||_infinity
 <=C_CT (2/sqrt(h))^(2/3)
       [(cD)(cD(1-eta))]^(-1/6)`,                                (4.3)

which is exactly (4.1). The right side is independent of the outside conditioning value, so averaging proves the unconditional estimate. QED.

The theorem is two-sided in the output value. In particular it closes the small-nonzero-pivot interpolation without using the one-sheet geometry. The newest ruled theorem is nevertheless still useful globally because it removes the entire one-sheet side before one reaches this local branch.

## 5. Quantitative splice with the designated partner: every pivot is paid on an exact graph bank

Apply Theorem 4.1 to the live one-heavy/two-bank constants from the completed B13 reduction:

`c>3/10`, `kappa=7/800`, `s=1`, `D>=1`.                          (5.1)

Since `h=det G>=kappa^2` and

`1+(1-c)/kappa < 1+(7/10)/(7/800)=81`,                           (5.2)

throughout

`|q|<=1/162`                                                      (5.3)

we have `eta<1/2`. Thus (4.1) gives

`||p_Q||_infinity
 < C_CT 2^(5/6)[(3/10)(7/800)^2]^(-1/3)
 =2944.7213536314... .`                                          (5.4)

Now use the designated partner account03/B10 theorem (1.1) on the complementary nonnull regime. The single heavy physical coordinate itself is a rank-one original-coordinate bank on the ray `u`, of squared mass `m=c`. For

`|q|>=1/162`,                                                     (5.5)

(1.1), `c>3/10`, and `D>=1` give the actual inequality

`||p_Q||_infinity
 <=128 sqrt(2)(3/10)^(-1/2)(1/162)^(-1/4)
 =1179.0795140088... .`                                          (5.6)

Therefore the two branches overlap and give the following full scalar-pivot closure.

### Corollary 5.1 — `QFORM-ONEBANK-EXACTGRAPH-ALLPIVOT-CLOSURE-v1`

In the live exact-rank-three one-heavy/two-transverse-bank geometry, if **either one** quantitative light bank has zero longitudinal regression residual `rho_B=0`, then for every value of the heavy spectral Rayleigh quotient `q=u^T M u`, every admissible original product law satisfies

`boxed: ||p_Q||_infinity <2945.`                                 (5.7)

This strictly extends the prior exact-graph closure, which paid the exact-null point `q=0` but not the nonzero near-null interpolation. It also consumes the designated partner at a real inequality, not as a bibliography item.

## 6. Why the next gap is genuinely the positive-residual collar

For a general bank in the same geometry write the exact regression decomposition

`t_j=w^T p_j+e_j`,
`sum_j e_j p_j=0`,
`rho=sum_j e_j^2`.                                                (6.1)

Its full spectral Gram in the splitting `R u direct_sum u^perp` is

`S_B=
 [[w^T G w+rho, (G w)^T],
  [G w,          G       ]]`.                                     (6.2)

Taking the Schur complement of `G` gives the exact determinant identity

`boxed: det S_B=rho det G.`                                      (6.3)

Thus `rho>0` immediately creates genuine three-dimensional bank volume, while `rho=0` is exactly the graph endpoint closed above. But all known full-volume/Fresnel estimates deteriorate by a negative power of `rho` as `rho downarrow0`; simply saying that (6.3) is positive therefore does not interpolate uniformly with Corollary 5.1.

Moreover the residual scalar

`E=sum_j e_j X_j`                                                (6.4)

is generally dependent on the transverse projection `Z=sum_j p_j X_j`, despite the coefficient orthogonality `sum e_jp_j=0`. Treating a small `rho` as a small random perturbation would require forbidden moment/support assumptions. The cap-only nonlinear receiver shortcut is also explicitly refuted by the current correction record.

Therefore the first unpaid B10 implication is now

**`QFORM-NEARNULL-POSITIVE-REGRESSION-RESIDUAL-v1`.**  
In the one-heavy/two-quantitative-transverse-bank reduction, close the collar in which every usable bank has `0<rho<<1` and the heavy spectral pivot is near null, by a product-preserving inequality that interpolates uniformly between the exact-graph theorem above and a genuine three-dimensional bank-volume/Fresnel exit. The natural currency is the joint coefficient geometry `(G,w,e)` before projection, not a conditional density supremum or a small-random-error argument.

The earlier B13 theorem already pays `rho>=1/100` and `|q|>=1/100`, so the concrete surviving collar may be taken with both quantities small. The new result removes the entire boundary `rho=0` for all `q`.

## 7. Regression check and scope

A numerical algebra regression on 1000 random symmetric invertible `M`, random unit `u`, random graph slopes `w`, and random `c` checked the exact identities

`det C=det(M)n^TM^(-1)n`,
`P=|cq det C-det H|=cD|1-q n^TM^(-1)n|`,
`det H=c det M`.

The largest absolute errors were respectively `1.42e-14`, `2.93e-14`, and `1.42e-14`. These are regression checks only; the proof is the exact adjugate/block-determinant calculation above.

The result is an exact-rank-three supporting branch. It does not close arbitrary positive residual, arbitrary additional spectrum, or the full QFORM conjecture. Essential boundedness is proved on this branch; no new global continuity claim is promoted.
