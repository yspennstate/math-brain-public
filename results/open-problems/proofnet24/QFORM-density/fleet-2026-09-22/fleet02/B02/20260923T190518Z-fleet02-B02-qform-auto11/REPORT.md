SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-23T19:05:18Z.

# fleet02/B02 auto11 — sharp disjoint-compound L1 exit and exact overlap-compound identities

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T190518Z-fleet02-B02-qform-auto11`  
Role: Integrated Fourier estimate / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER L1 OPEN-NOT-REFUTED**

The exact owner target is unchanged: independent original-coordinate real variables with one-dimensional densities at most one, arbitrary dimension, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moments, support, log-concavity, iid, diagonal-basis, or post-rotation-independence hypothesis is added. Continuity is recorded only on branches where the characteristic function is proved integrable.

## 1. Sources and live corrections actually used

Required Claude Fourier package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Reviewed q-dependent sharp Hausdorff--Young theorem: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Newest projected-Fisher source requested for B02 review: `yspennstate/math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2`, `proofnet24/QFORM-density/interactive/20260923T184054Z-fisher-continuation/FISHER_INFORMATION.md`.

Latest completed designated partner `fleet03/B02` results used here:
- r36 `QFORM-3x2-KERNELCURVATURE-L1-v1`, math commit `c41a5ae669366b253862aa15277c401b932954ad`;
- r37 `QFORM-DISJOINT-COMPOUND-E3-L1-v1`, math commit `c2a842f9cd113aa20d792ca1692a358fdc1be356`, with checker output through `e22022bcf95596195a701305e6841116815e8b48`.

Fresh correction retained: `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` at brain event source commit `b2a0ccad9d4f4d654e0fc84dd0323ce84230ebc4`. In particular I do not infer a universally large singleton hub/star, individual minor, or tiny-tail deletion from the three-large-eigenvalue hypothesis.

## 2. Requested independent review of the projected-Fisher proof

**Verdict for the B02-assigned analytic scope: PASS.** This covers weak integration by parts, cutoff limits, the inverse-distance inequality, centered primitive normalization, and the resulting density-domination factor. It does not review the separate convolution/smoothing package assigned to fleet03/B04, and it does not remove the extra Fisher/H1 hypothesis.

Assume `sqrt(f_i) in H^1`, let `S_i=f_i'/f_i` on `{f_i>0}`, and let `U` span an invariant `r`-dimensional spectral subspace with `|lambda_j|>=s`. Put `J_E=E|U^T S|^2`, `z=U^TX-z0`, `R=|z|`.

First, `sqrt(f_i) in H^1` implies `f_i in W^{1,1}` and

`f_i'=2 sqrt(f_i)(sqrt(f_i))'`, `E S_i=0`, `E S_i^2=I_i`.

Independence gives `E|U^TS|^2=J_E`. For

`W_delta=Uz/(R^2+delta)`

one has

`div W_delta = r/(R^2+delta)-2R^2/(R^2+delta)^2 >= (r-2)/(R^2+delta)`.

Insert a smooth compact cutoff before integrating by parts. For fixed `delta>0`, the field and its divergence are bounded, the score is integrable, and the cutoff-gradient error is bounded by `O(1/N)` times a probability/integrable factor. Hence it vanishes without any moment hypothesis. Cauchy--Schwarz gives, with `K_delta=E(R^2+delta)^(-1)`,

`(r-2)K_delta <= sqrt(J_E K_delta)`,

so

`K_delta <= J_E/(r-2)^2`,

and monotone convergence yields

`D:=E R^(-2) <= J_E/(r-2)^2`.                                      (2.1)

Now set

`V_delta=U Lambda^(-1)z/[2(R^2+delta)]`.

The source centering `z0=-(1/2)Lambda^(-1)U^Tb` gives the exact contraction

`grad Q . V_delta = R^2/(R^2+delta)`.                              (2.2)

All remaining eigenvalues and the affine component orthogonal to the selected eigenspace cancel from (2.2), rather than being discarded from the random form. Further,

`|div V_delta| <= r/(2sR^2)`,
`|V_delta.S| <= |U^TS|/(2sR)`,

which are integrable by (2.1) and Cauchy--Schwarz.

For nonnegative `psi in C_c^infinity`, let `m=int psi` and

`Phi(t)=int_{-infinity}^t psi(u)du-m/2`.

Then `||Phi||_infinity<=m/2`. The same cutoff-first weak integration by parts gives

`E[psi(Q) R^2/(R^2+delta)]
 = -E[Phi(Q)(div V_delta+V_delta.S)]`.

The projection `U^TX` is absolutely continuous, so `P(R=0)=0`. Sending `delta downarrow0` therefore yields

`E psi(Q) <= m [rD+sqrt(J_E D)]/(4s)`.                             (2.3)

The factor `1/4` is correct: one `1/2` is in `V_delta`, and the other is the centered-primitive bound `m/2`. Domination (2.3) for every nonnegative smooth test function implies domination of the pushforward measure by the displayed multiple of Lebesgue measure, so a density exists and has that essential bound.

The cap-one improvement also checks. The projection-density bound `2^(r/2)` implies

`P(R<t)<=min(1,2^(r/2)v_r t^r)`,

and layer cake gives exactly

`E R^(-2)<=D_r=2r v_r^(2/r)/(r-2)`.

Thus the requested analytic part of the Fisher theorem is internally consistent.

### Why this does not close the rough-input target

The newer fleet02/B15 calculation at math commit `4ae555c379a6f87e7af74c01fff215986650ffb4` supplies a source-valid obstruction to a bounded-information approximation closure. If `u=1_[0,1]`, `sqrt f in H^1`, and `eta=||f-u||_1<=1/8`, then

`I(f)>=1/(4 eta)`.                                                  (2.4)

Hence no common finite Fisher budget is dense at the interval law, even before confronting the full matrix problem. On the exact normalized target matrix

`[[0,1,0],[1,0,0],[0,0,1]]`

with spectrum `{1,-1,1}`, product approximation to the cube forces `J_E>=3/(4 eta)`. The Fisher theorem is therefore a valid extra-regularity branch, not a smoothing proof of arbitrary cap-one QFORM.

Still, it has a real application to the prior B02 low-cross-rank collar: if `I_i<=J`, then the full-matrix theorem gives `||p_Q||_infinity<=3J` under `s3(A)>=1`, irrespective of how close a physical cross block is to rank one or two. For the compact-kernel convolution class in the source, the stronger source constant is `<18`. Thus the low-cross-rank obstruction is specifically a rough-input obstruction, not a matrix-only obstruction.

## 3. Sharpened disjoint third-compound integrated-Fourier exit

For `r=0,1,2,3`, define the ordered third-compound intersection strata

`V_r(A)=sum det(A[I,J])^2`,                                        (3.1)

where the sum is over all 3-subsets `I,J` with `|I cap J|=r`.
Cauchy--Binet gives

`V_0+V_1+V_2+V_3=e_3(A^2)`.                                      (3.2)

Therefore `s3(A)>=1` implies

`V_0+V_1+V_2+V_3>=1`.                                             (3.3)

The designated partner r37 observes that for a fair random original-coordinate cut `[n]=L disjoint-union R`,

`E_cut Z3(L,R)=V_0/64`,
`Z3(L,R):=E3(A[L,R])`.                                            (3.4)

Hence some actual physical cut satisfies

`Z3(L,R)>=V_0/64`.                                                 (3.5)

This is the live physical cross block used below.

### 3.1 D' plus the reviewed sharp-HY refinement on this cut

For a physical cross block `M`, the sharp q-dependent theorem gives, whenever the third-volume row marginals satisfy `alpha_i<=q/2`, `1<=q<3/2`,

`||p_Q||_infinity <= 3e/[(3-2q)sqrt(q)] E3(M)^(-1/6)`.             (3.6)

The previous B02 incident-third-volume cascade pays the complementary heavy-row branch. At the rational threshold `h=9/16`, `q=9/8`, the two branches combine to the marginal-free coefficient

`C_* = 10.345083232147514`,

so every physical cross block with `E3(M)>0` satisfies

`||p_Q||_infinity <= C_* E3(M)^(-1/6)`,                           (3.7)
`int_R |phi_Q(t)|dt <= 2 pi C_* E3(M)^(-1/6)`.                    (3.8)

Substitute (3.5):

`boxed: ||p_Q||_infinity <= 20.69016646429503 V_0(A)^(-1/6),`     (3.9)

`boxed: int_R |phi_Q(t)|dt <= 130.00014993155833 V_0(A)^(-1/6).` (3.10)

This strictly improves the coefficient in the partner's r37 disjoint-stratum theorem by applying the sharper completed B02 E3 receiver to the partner's actual cut.

If the exact target satisfies `V_0>=1/4`, then

`boxed: ||p_Q||_infinity < 26.06797625419429,`                    (3.11)

`boxed: int_R |phi_Q(t)|dt < 163.7899253882599.`                  (3.12)

Thus the entire disjoint third-compound branch has a universal unweighted Fourier-L1 bound, hence a continuous density vanishing at infinity.

### 3.2 D5 on the same live cut

The reviewed sharp-HY fifth-volume theorem is available with no marginal gate:

`||p_Q||_infinity <= (5e/sqrt(2)) E5(M)^(-1/10)`.                 (3.13)

For the same cut selected in (3.5), therefore,

`||p_Q||_infinity <= min{
 C_* Z3^(-1/6),
 (5e/sqrt(2)) Z5^(-1/10)
}`                                                               (3.14)

with `Z5=E5(A[L,R])`. The D5 term is smaller precisely when

`Z5 >= 0.4788009378679107 Z3^(5/3)`.                              (3.15)

Equation (3.15) is an actual complementary exit on the live block. No lower bound for `Z5` follows from `V_0` alone, so D5 is not being misrepresented as part of the unconditional disjoint-compound reduction.

## 4. New exact identities for the overlap third-compound strata

The disjoint branch leaves `V_1,V_2,V_3`. These have a clean original-coordinate packet representation which makes the next unpaid mechanism precise.

Fix a physical 3-set `L`, write

`P_L=A[L,L]`.

### 4.1 One-index overlap

For a physical 2-set `R={r,s}` disjoint from `L`, let

`c_r=A[L,r]`, `c_s=A[L,s]`, `w_{L,R}=c_r cross c_s`.

For `h in L`, the `V_1` minor with row set `L` and column set `{h,r,s}` is, up to orientation,

`det[P_L e_h,c_r,c_s] = e_h^T P_L w_{L,R}`.                      (4.1)

Summing the three squared choices of `h` gives the exact identity

`boxed: V_1(A)
 = sum_{|L|=3} sum_{R subset L^c, |R|=2}
   ||P_L w_{L,R}||_2^2.}`                                       (4.2)

This is directly related to the partner r36 receiver. Since

`||w_{L,R}||^2=det(A[L,R]^T A[L,R])=Delta^2`,

r36 pays a literal packet whenever

`|w_{L,R}^T P_L w_{L,R}|>0`,                                    (4.3)

with

`||p_Q||_infinity <= (5/4)3^(6/5)
 |w_{L,R}^T P_L w_{L,R}|^(-1/5)`.                               (4.4)

But (4.2) also displays the exact unresolved piece: a large `||P_L w||` need not force a large quadratic curvature `|w^T P_L w|`; the latter can vanish while `P_L w` lies transversely in `w^perp`. Indeed

`||P_L w||^2
 = |w^T P_L w|^2/||w||^2
   + ||Proj_(w^perp)(P_L w)||^2`.                                (4.5)

Thus failure of the r36 kernel-curvature receiver is not an undefined degeneracy: it is a **kernel-shear** packet, the second term of (4.5). A valid full proof must aggregate that shear before taking reciprocal individual scales.

### 4.2 Two-index overlap

For `r notin L`, put `c=A[L,r]`. If the column triple shares the two columns `L\{h}` with `L`, the corresponding determinant is, up to orientation, the `h`-th component of `adj(P_L)c`. Summing the three choices gives

`boxed: V_2(A)
 = sum_{|L|=3} sum_{r notin L}
   ||adj(P_L) A[L,r]||_2^2.}`                                   (4.6)

### 4.3 Three-index overlap

The fully overlapping stratum is simply

`boxed: V_3(A)=sum_{|L|=3} det(P_L)^2.}`                         (4.7)

Equations (4.2), (4.6), and (4.7) are coefficient identities only; they do not assert that one packet has universal scale. They were independently regressed on 240 deterministic random symmetric matrices of sizes 3 through 8; the maximum relative errors were `4.47e-15` for (4.2), `2.83e-15` for (4.6), and machine-zero for (4.7).

## 5. The first unpaid implication is now a three-way aggregate overlap receiver

By (3.3), if the already-paid disjoint branch fails at target scale, `V_0<1/4`, then

`V_1+V_2+V_3>3/4`,                                               (5.1)

so at least one of

`V_1>1/4`, `V_2>1/4`, `V_3>1/4`                                 (5.2)

holds.

This gives a concrete global trichotomy after the disjoint integrated-Fourier exit:

1. **kernel/shear aggregate:** `sum ||P_L(c_r cross c_s)||^2>1/4`; r36 already pays the radial kernel-curvature component, while the transverse kernel-shear aggregate remains;
2. **adjugate-column aggregate:** `sum ||adj(P_L)A[L,r]||^2>1/4`;
3. **principal-determinant aggregate:** `sum det(P_L)^2>1/4`.

The fresh `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` correction explains why the next step must remain aggregate: a three-large-eigenvalue matrix can have every relevant singleton star or fixed small physical coefficient tending to zero while a grouped Pluecker mechanism still controls the law. Likewise, no dimension-free lower bound on one summand of (5.2) follows from its aggregate sum.

I therefore name the next B02 obligation

`QFORM-OVERLAP-COMPOUND-V123-TO-INTEGRATED-RECEIVER-v1`:

> From one of the three aggregate alternatives in (5.2), produce a product-preserving integrated-Fourier/grouped-hub/principal-curvature receiver with a universal bound, without selecting a dimension-degrading individual minor and without deleting nonzero tails.

For the `V_1` branch the most immediate new analytic target is a grouped receiver for the transverse term in (4.5). For `V_2,V_3`, a grouped adjugate/principal-minor compiler is needed unless an existing semidefinite/physical-pair theorem applies at a quantitative aggregate scale.

## 6. Counterexample and Fourier-criterion status

The required Claude counterexample search supplies no exact-target QFORM counterexample. This run also found no exact-target counterexample to the stronger target-wide assertion `int |phi_Q|<infinity` with a universal bound. The pointwise law-uniform decay criterion remains refuted and is not used.

The new disjoint-compound branch proves a universal L1 estimate on one full spectral-energy stratum; the overlap trichotomy (5.2) is the precise remaining compound-energy obstruction. Therefore the full conjecture and the target-wide Fourier-L1 criterion both remain OPEN.

## 7. Write/readback and integrity note

Changed-file allowlist for this run is restricted to this B02 run directory in `math-open-problems`, this run's B02 handoff/memory files in `math-research-brain`, and the matching B02 finish record. No unrelated repository files, permissions, task definitions, notifications, or scheduler state are changed. No dedicated privacy scanner is exposed in this runtime; a limited manual content review found only mathematical/source metadata and no unrelated private data.
