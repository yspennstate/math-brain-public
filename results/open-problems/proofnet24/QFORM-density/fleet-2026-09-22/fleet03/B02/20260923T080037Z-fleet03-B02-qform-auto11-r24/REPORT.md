SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T08:00:37Z.
attacking: the heavy-mixed-marginal residue left by the (3+2)-volume Fourier theorem; convert a heavy determinant row/column into a true scalar-Schur E2 resource before any reciprocal minor payment.

# fleet03/B02 r24 — heavy mixed marginal to physical-square/Schur-E2 receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Owner control:** revision `2026-09-22.15`; QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full QFORM target:** OPEN  
**Target-wide unweighted Fourier L1 criterion:** OPEN; neither proved nor refuted here  
**Continuity:** proved on the Fourier branch below; only essential boundedness is asserted on the new scalar-Schur branch.

The actual-hour login for this slot already existed when the mathematical continuation began and was preserved rather than overwritten. Start-control evidence in that login is brain commit `387609545d1ff08fbc115dbc068e4d7e3915b664`, revision `2026-09-22.15`. The control branch was reread before this report; the latest observed QFORM-only head at that checkpoint was `fbac081d06fd8ae4281130102a789d195a39cf4c`.

## 1. Exact scope and correction boundary

The target remains unrestricted: independent ORIGINAL coordinates with probability densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, arbitrary signs, arbitrary additional spectrum, arbitrary same-bank curvature, and no moment/support/log-concavity/iid hypothesis. No independence after rotating coordinates is used.

This run explicitly avoids the known false interfaces: law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, positive conditional projection-height moments, fiber-sup dimension-free bounds, deletion of a small nonzero quadratic coefficient, and the false claim that one physical square plus one heavy coefficient alone absorbs arbitrary same-bank curvature. The new argument retains a genuine aggregate second-compound smoother in the TRUE scalar Schur residual.

## 2. Completed inputs actually used

### 2.1 Previous B02 mixed (3+2)-volume Fourier theorem

Use the preceding own result

`QFORM-MIXED-3PLUS2-FOURIER-L1-v1`,

`yspennstate/math-open-problems@67f92f4e9110620b60f3ce49fd7738f00d285c87`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T072525Z-fleet03-B02-qform-auto11-r23/REPORT.md`.

For a physical cross block `B=A[I,J]`, fixed anchor row `x` and anchor column `y`, let `J3` be the squared `3x3`-minor mass containing both anchors and let `E2` be the squared `2x2`-minor mass of the block obtained by deleting the anchors. Let `alpha^(3),alpha^(2)` be the row inclusion marginals of these two normalized determinant laws and

`alpha_i=(alpha_i^(3)+alpha_i^(2))/2`.

Define the analogous column quantities `beta`. For every `1<=q<5/4`, if all row mixed marginals satisfy `alpha_i<=q/2`, or all column mixed marginals satisfy `beta_j<=q/2`, then

`||p_Q||_infinity <= C_32(q)(J3 E2)^(-1/10)`,

`C_32(q)=5e/[2^(1/5)(5-4q)sqrt(q)]`,

and `phi_Q in L1`, so the density is continuous and vanishes at infinity.

### 2.2 Unconditional aggregate-E2 half-Riesz theorem

Use fleet01/B01

`QFORM-PAIRVOLUME-HALF-RIESZ-UNCONDITIONAL-v1`,

`yspennstate/math-open-problems@1f3af9dc58afb9e902b972466d6da01cece89734`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T030821Z-fleet01-B01-qform-auto11/REPORT.md`.

For every quadratic-plus-affine residual `R` in independent cap-one ORIGINAL coordinates and every literal physical cross block `C` in that residual with

`Delta=E2(C)=e2(C^T C)>0`,

it proves

`H_(1/2)(R):=sup_s E|R-s|^(-1/2)
 <= C_E2 Delta^(-1/8)`,                                           (2.1)

where

`C_E2=12*2^(5/6)*e^(5/24)=26.334046180759735...`.               (2.2)

There is no E2 leverage/minor-marginal gate and no selected-minor reciprocal.

### 2.3 Designated partner fleet04/B02

The designated completed partner result is

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.

If a full/residual quadratic form contains a nonsingular physical `3x3` principal block `H0` with one exact zero diagonal entry, the partner proves a continuous density cap

`M_H=3*2^(2/3)|det H0|^(-1/3)`                                  (2.3)

and the Fourier consequence

`||phi||_2^2 <= 6*pi*2^(2/3)|det H0|^(-1/3)`.                    (2.4)

Section 7 applies (2.3) to an actual new hybrid inequality.

## 3. Exact exterior identity for one physical row

Let a real physical cross block be written, after a permutation of ORIGINAL coordinates, as

`M=[ b^T ; N ]`,                                                  (3.1)

where `b` is the distinguished physical row. Define the complete third-volume incident to that row by

`J_b := sum_{R contains row 1, |R|=3, |T|=3} det M[R,T]^2`.      (3.2)

If `J_b>0`, then `b!=0`. Let `P_b` be the orthogonal projection in coefficient space onto `b^perp`.

### Lemma 3.1 — `QFORM-INCIDENT-E3-EXTERIOR-IDENTITY-v1`

`boxed: J_b = ||b||_2^2 E2(N P_b).`                              (3.3)

#### Proof

For every residual row pair `r<s`, summing the squared `3x3` minors over all column triples is exactly the squared exterior norm

`|| b wedge N_r wedge N_s ||^2`.

Decompose both residual rows into their components parallel and perpendicular to `b`. Parallel components disappear from the wedge, hence

`|| b wedge N_r wedge N_s ||^2
 =||b||^2 ||(N_r P_b) wedge (N_s P_b)||^2`.

Summing over all residual row pairs gives (3.3), since the sum of squared two-row exterior norms is exactly `E2(NP_b)=||wedge^2(NP_b)||_HS^2`. QED.

This identity is deterministic. The projection `P_b` is used only inside matrix algebra; no random coordinate is rotated and no independence claim is made after this projection.

## 4. The TRUE scalar Schur residual preserves the projected second compound

Now let the distinguished row correspond to an actual original coordinate `X_i`, with physical diagonal

`d=A_ii !=0`.                                                     (4.1)

Let `I\{i}` be the remaining row bank and keep the disjoint original column bank `J`. In the full symmetric matrix write

`u=A[I\{i},i]`, `b=A[i,J]`, `N=A[I\{i},J]`.                     (4.2)

Complete the **actual original-coordinate scalar square** in `X_i`. The true Schur residual on the remaining original coordinates has physical cross block

`C=N-u b^T/d`.                                                    (4.3)

Because `b^T P_b=0`,

`C P_b=N P_b`.                                                    (4.4)

Moreover exterior powers contract under an orthogonal projection:

`||wedge^2(CP_b)||_HS <= ||wedge^2 C||_HS`.

Therefore Lemma 3.1 gives the exact correction-safe lower bound

`boxed:
 E2(C) >= E2(CP_b)=E2(NP_b)=J_b/||b||^2.
}`                                                                  (4.5)

This is the key implication. The rank-one Schur correction can destroy individual physical minors, but it cannot destroy the entire projected second-compound currency generated by the incident third volume.

## 5. Scalar-square kernel plus aggregate Schur E2

After completing the square, conditional on all remaining original coordinates `W`,

`Q=d(X_i+s(W))^2+R(W)`.                                          (5.1)

The original coordinate `X_i` is independent of `W` and still has density at most one. For each fixed `W`, the density of the first term is bounded by

`|d|^(-1/2)|t-R(W)|^(-1/2)`.                                    (5.2)

Indeed the two possible roots have total Jacobian contribution at most

`2 / [2 sqrt(|d||t-R|)]`.

Averaging (5.2),

`||p_Q||_infinity
 <= |d|^(-1/2) H_(1/2)(R)`.                                     (5.3)

Apply the unconditional E2 half-Riesz theorem (2.1) to the **literal physical** residual cross block `C` in (4.3), then use (4.5).

### Theorem 5.1 — `QFORM-INCIDENT-E3-PHYSICAL-SQUARE-RECEIVER-v1`

Under (3.1)--(4.3), if `d!=0` and `J_b>0`, then the full ambient quadratic form has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_E2 |d|^(-1/2) ||b||^(1/4) J_b^(-1/8).
}`                                                                  (5.4)

Numerically,

`C_E2=26.334046180759735...`.                                    (5.5)

No individual `2x2` or `3x3` minor is inverted. All additional spectrum, same-bank curvature, and affine leakage remain inside the completed theorem scopes. The result proves essential boundedness only; it does not prove `phi_Q in L1` or continuity.

The homogeneity is correct: under `A -> sA`, the right side scales by `s^(-1)`.

The transpose statement holds verbatim for a distinguished physical column coordinate.

## 6. Main splice with the previous mixed-(3+2) Fourier theorem

The new result closes the first analytic step after a mixed marginal becomes heavy.

### Theorem 6.1 — `QFORM-MIXED32-FOURIER-OR-HEAVYSQUARE-v1`

Retain the exact r23 setup with `J3 E2>0`. Fix any

`1<q<5/4`.                                                        (6.1)

Then at least one of the following holds.

**A. Integrated-Fourier exit.**  
All mixed row marginals are at most `q/2`, or all mixed column marginals are at most `q/2`. Then

`||p_Q||_infinity <= C_32(q)(J3E2)^(-1/10)`,                    (6.2)

and the density is continuous and vanishes at infinity.

**B. Two-sided heavy-incidence survivor.**  
There is a non-anchor physical row `i` and a non-anchor physical column `j` such that

`alpha_i^(3)>q-1`, `alpha_i^(2)>q-1`,                            (6.3)

`beta_j^(3)>q-1`, `beta_j^(2)>q-1`.                              (6.4)

In particular the complete physical third-volume incident to row `i` obeys

`J_i >(q-1)J3`,                                                   (6.5)

and similarly for the heavy column.

If `d=A_ii!=0`, writing `b=A[i,J]`, Theorem 5.1 gives

`boxed:
 ||p_Q||_infinity
 < C_E2 (q-1)^(-1/8)
   |d|^(-1/2)||b||^(1/4)J3^(-1/8).
}`                                                                  (6.6)

There is an identical column version with `A_jj` and the corresponding column norm.

#### Proof of the compiler

If the row gate fails, some `alpha_i>q/2`. Since

`alpha_i=(alpha_i^(3)+alpha_i^(2))/2`,

we have `alpha_i^(3)+alpha_i^(2)>q`. Each summand is at most one, so each is strictly larger than `q-1`. The fixed anchor row has mixed marginal exactly `1/2`, hence for `q>1` this heavy row is non-anchor. The same argument on columns proves (6.3)-(6.4) whenever both row and column Fourier gates fail. Equation (6.5) follows because the r23 incident-three family is a subset of the complete third-volume incident to row `i`. Then apply Theorem 5.1. QED.

### Concrete choice `q=6/5`

At `q=6/5`, the Fourier threshold is `3/5`. The alternative becomes:

- if one side has all mixed marginals `<=3/5`, then

`boxed:
 ||p_Q||_infinity
 <=54.005485 (J3E2)^(-1/10),
}`                                                                  (6.7)

with a continuous density;

- otherwise there is a heavy row and heavy column each carrying **more than one fifth** of both determinant families, and any nonzero heavy-row diagonal obeys

`boxed:
 ||p_Q||_infinity
 <32.202445
 |A_ii|^(-1/2)||A[i,J]||^(1/4)J3^(-1/8).
}`                                                                  (6.8)

This is strictly stronger structural information than merely saying that the sharp-Hausdorff--Young gate failed.

### Endpoint interpretation

If `max_i alpha_i<5/8` on one side, some `q<5/4` satisfies the Fourier gate. Thus a genuinely non-Fourier survivor can be confined to mixed marginals at least `5/8`; at such a coordinate both determinant-family inclusions are at least `1/4`. Equality at `5/8` is kept on the heavy side rather than hidden in a limiting Fourier constant.

## 7. Actual designated-partner application

Suppose the scalar Schur residual `R` in Theorem 5.1 also contains a nonsingular physical zero-diagonal `3x3` principal block `H0`. The designated fleet04/B02 theorem (2.3) gives the residual density cap

`M_H=3*2^(2/3)|det H0|^(-1/3)`.

For any probability density bounded by `M`, centered rearrangement yields

`sup_t int p(s)|s-t|^(-1/2) ds <=2sqrt(2M)`.                    (7.1)

Consequently the partner gives the genuine half-Riesz credit

`H_(1/2)(R)
 <=2sqrt(2M_H)`,                                                  (7.2)

and the exact scalar-square kernel (5.3) gives

`||p_Q||_infinity
 <=6.172327377 |d|^(-1/2)|det H0|^(-1/6)`.                      (7.3)

On the heavy mixed-row branch we simultaneously have (6.6). Therefore one may take the minimum of (6.6) and (7.3). Using `min(A,B)<=sqrt(AB)` gives the new hybrid inequality

`boxed:
 ||p_Q||_infinity
 <=12.749210 (q-1)^(-1/16)
 |d|^(-1/2)||b||^(1/8)J3^(-1/16)|det H0|^(-1/12).
}`                                                                  (7.4)

At `q=6/5`,

`boxed:
 ||p_Q||_infinity
 <14.098370
 |d|^(-1/2)||b||^(1/8)J3^(-1/16)|det H0|^(-1/12).
}`                                                                  (7.5)

This is an equation-level application of the designated partner result to the new heavy-marginal receiver. The partner residual density is continuous, but the final correlated scalar-square mixture is recorded only as essentially bounded; no continuity upgrade is asserted without an independent argument.

## 8. Application to the preceding compound-hub constants

The r23 compound-hub edge/E2 branch at `tau=delta_r=delta_c=1/64` has

`J3 >=(31/288) Z`,
`E2 >(992/585) Z`,

hence

`J3E2>0.182526115859449 Z^2`.                                    (8.1)

At `q=6/5`, Theorem 6.1 therefore gives the following explicit dichotomy.

**Fourier side:**

`boxed:
 ||p_Q||_infinity <64.018482 Z^(-1/5),
}`                                                                  (8.2)

with a continuous density.

**Heavy side:** there are a physical row and column each carrying more than `1/5` of both determinant laws. If the heavy row has `d=A_ii!=0`, then

`boxed:
 ||p_Q||_infinity
 <42.549327 |d|^(-1/2)||A[i,J]||^(1/4) Z^(-1/8).
}`                                                                  (8.3)

This is not yet a universal target-scale bound because `d` may be arbitrarily small and the star norm may be large relative to the third-volume scale. The remaining geometry has therefore been narrowed rather than silently discarded.

For example, if a later structural compiler supplies the scale relations

`|d| >= tau Z^(1/6)`, `||A[i,J]|| <= L Z^(1/6)`,                (8.4)

then (8.3) immediately becomes the scale-correct payment

`boxed:
 ||p_Q||_infinity
 <42.549327 tau^(-1/2)L^(1/4) Z^(-1/6).
}`                                                                  (8.5)

Thus the only heavy-marginal obstruction to this receiver is a genuinely near-zero physical diagonal and/or a star whose size is anomalously large compared with the determinant volume. This matches, rather than contradicts, the live correction showing that a physical square plus one heavy off-diagonal coefficient alone is insufficient.

On overlap with a partner zero-diagonal residual triple, (7.5) and `J3>31Z/288` give

`||p_Q||_infinity
 <16.205813
 |d|^(-1/2)||b||^(1/8)Z^(-1/16)|det H0|^(-1/12).`              (8.6)

## 9. Deterministic regression

`CHECK.py` performs 500 seeded random matrix tests of the exact identity (3.3) and the Schur monotonicity (4.5). The largest scaled discrepancy in (3.3) was below `2.5e-15`; every tested Schur inequality had positive slack. The numerical check is only a regression; the exterior-algebra proof above is the proof.

## 10. Fourier status and first unpaid implication

This run does **not** establish the target-wide universal unweighted estimate

`int_R |E exp(it X^T A X)| dt <= universal constant`.

It also does not produce a valid exact-target counterexample to that stronger criterion. The criterion therefore remains OPEN. The new theorem instead proves a correction-safe bounded-density exit precisely where the previous mixed Fourier proof loses its Hausdorff--Young marginal gate.

The first B02 debt is now sharper:

`QFORM-MIXED32-DOUBLEHEAVY-NEARZERO-TRANSDUCER-v1`:

> In the two-sided heavy mixed-incidence branch, where the heavy row and heavy column each carry a fixed positive fraction of both the incident third-volume and residual second-volume laws, treat the case in which every available heavy physical diagonal is near zero at the determinant-volume scale. Use the simultaneous row/column stars and residual determinant currency jointly, rather than perturbing a small nonzero square to zero or conditioning away product provenance.

This should be spliced with the current B07 four-hub/two-star compiler and the exact-zero partner theorem. A merely heavy coefficient is not enough; the new incident-E3 identity shows exactly what extra aggregate Schur currency must be preserved.

**Status:** supporting analytic theorem proved; mixed-Fourier gate failure compiled to a genuine scalar-Schur E2 receiver; full QFORM OPEN; full continuity OPEN; target-wide Fourier L1 OPEN.
