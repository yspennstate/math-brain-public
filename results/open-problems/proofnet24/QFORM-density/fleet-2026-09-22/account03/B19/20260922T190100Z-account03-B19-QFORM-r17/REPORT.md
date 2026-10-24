SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B19, 2026-09-22T19:01:00Z.
attacking: splice the O0 heavy-row packet theorem into the exact cross-bank Fourier payment, eliminating the three-or-more-heavy O0 branch without selecting a tiny physical minor.

# account03/B19 — O0 three-heavy cross-bank closure

**Run:** `20260922T190100Z-account03-B19-QFORM-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control used:** revision `2026-09-22.11`  
**Assignment:** Universal proof assembly  
**Status:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL O0 BRANCH CLOSED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

Let `X=(X_1,...,X_n)` have independent real coordinates, each with probability density `0<=f_i<=1`, and let `A` be real symmetric with at least three eigenvalues of absolute value at least one. The full target asks for one universal finite constant `C` such that `Q=X^TAX` has a density satisfying `||p_Q||_infinity<=C`, uniformly in dimension, matrix, signs, rotations, and the marginal laws. Continuity is a separate desired conclusion.

The full target remains **OPEN**. The theorem below closes one of the live full-matrix O0 overlap branches. It uses only original-coordinate product banks. It does not assume moments, Gaussianity, log-concavity, compact or connected support, independence after spectral rotation, a law-uniform pointwise quadratic-phase estimate, a uniformly good single physical minor, or a conditional-density cap after a non-product conditioning.

The live corrections are respected, in particular `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, the false arbitrary-joint coarea bound, the false positive conditional-projection moment, and the high-`s_2(A-diag A)` rank-two-cut counterexample.

## 2. Two completed inputs

### 2.1 O0 heavy-row packet isolation

Source: account03/B07, `QFORM-O0-HEAVY-PACKET-ISOLATION-v1`, canonical report

`yspennstate/math-open-problems@f2d3682e9f9d24d67ea14dc990d9f49bebeb5a6e`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T173711Z-account03-B07-qform-r13/REPORT.md`.

In the O0 branch there are disjoint original-coordinate sets `L,R` and a physical cross block

`B=A[L,R]`

with third singular-volume currency

`E=e_3(s_1(B)^2,s_2(B)^2,...)>=1/256`.                 (2.1)

At the effective-dimension-three ridge calibration, if at least three original rows have leverage at least `3/4`, B07 proves that there is a **physical three-row set** `H subset L` such that

`det(B_H B_H^T)>=E/16>=1/4096`.                        (2.2)

For the rank-exactly-three endpoint the stronger `det(B_HB_H^T)>=E/4` holds.

The key feature is that (2.2) is an aggregate row-Gram determinant. It is the sum of squares of all physical `3x3` column minors by Cauchy--Binet. No one minor is selected or inverted.

### 2.2 Exact-rank cross-bank Fourier payment

Source: account03/B19 r16, `QFORM-EXACT-CROSS-RANK-L2-v1`, canonical report

`yspennstate/math-open-problems@9d55d9ca5a7beaed6f693a57bd32b5fc9949b981`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T172719Z-account03-B19-QFORM-r16/REPORT.md`.

Let `I,J` be disjoint original-coordinate groups and condition on all coordinates outside `I union J`. Write the conditional form as

`Q_w(U,V)=F_w(U)+2U^T C V+G_w(V)+c_w`,                 (2.3)

where `C=A[I,J]` and the within-bank terms `F_w,G_w` are arbitrary quadratic-affine functions. If `rank(C)=r>=3`, with nonzero singular values `sigma_1,...,sigma_r` and

`Pi_r(C)=prod_{j=1}^r sigma_j`,

then the full ambient form has a bounded continuous density and

`||p_Q||_infinity <= e r/(r-2) Pi_r(C)^(-1/r)`.        (2.4)

If one active bank consists of exactly `r` original physical coordinates, the projection cap on that side is one rather than `e^(r/2)`, and (2.4) improves to

`||p_Q||_infinity <= sqrt(e) r/(r-2) Pi_r(C)^(-1/r)`.  (2.5)

Crucially, (2.5) uses **all** nonzero mixed singular directions of `C`. It is therefore legitimate for a `3 x m` bank of rank exactly three, even when `m` is arbitrarily large. It does not discard higher-rank mixed terms.

## 3. New splice: every O0 state with three heavy rows is paid

### Theorem 3.1 — `QFORM-O0-THREE-HEAVY-CROSSBANK-CLOSURE-v1`

Assume the exact QFORM target hypotheses and the O0 state (2.1). At the effective-dimension-three ridge calibration, suppose at least three physical rows have leverage at least `3/4`. Then `Q=X^TAX` has a bounded **continuous** density and

`boxed(||p_Q||_infinity <= 3 sqrt(e) 2^(2/3) E^(-1/6)).`  (3.1)

In particular, since `E>=1/256`,

`boxed(||p_Q||_infinity <= 12 sqrt(e) < 19.785.)`         (3.2)

At the rank-exactly-three endpoint the B07 stronger packet bound improves (3.2) to

`||p_Q||_infinity <= 3 sqrt(e) 2^(5/3) <15.704`.         (3.3)

#### Proof

Apply the B07 packet theorem and choose the physical triple `H subset L` satisfying (2.2). Set

`C=B_H=A[H,R]`.                                             (3.4)

Because `H` contains exactly three rows and `det(CC^T)>0`, the matrix `C` has **exact rank three**. Thus the one-sided exact-rank theorem (2.5) applies with `r=3`, `I=H`, `J=R`. The product of the three nonzero singular values is

`Pi_3(C)=sqrt(det(CC^T))`.                                  (3.5)

From (2.2),

`Pi_3(C)>=sqrt(E/16)=E^(1/2)/4`.                            (3.6)

Substitution into (2.5) yields

`||p_Q||_infinity
 <=3 sqrt(e) Pi_3(C)^(-1/3)
 <=3 sqrt(e) (4 E^(-1/2))^(1/3)
 =3 sqrt(e) 2^(2/3) E^(-1/6)`,                            (3.7)

which is (3.1). With `E>=2^(-8)`,

`2^(2/3) E^(-1/6) <=2^(2/3)2^(8/6)=2^2=4`,               (3.8)

so (3.2) follows.

For the exact-rank-three endpoint, B07 gives `det(CC^T)>=E/4`, hence

`Pi_3(C)>=E^(1/2)/2`

and (2.5) gives

`3sqrt(e) 2^(1/3)E^(-1/6)<=3sqrt(e)2^(5/3)`,             (3.9)

which is (3.3). Continuity is inherited from the exact-cross-rank theorem. QED.

### Why this is not the refuted good-minor shortcut

The proof never infers a single large `3x3` physical column minor from (2.2). Cauchy--Binet may spread the row-Gram determinant among arbitrarily many tiny minors. The analytic theorem consumes the **entire three-row by many-column bank** at once. This is exactly the group-before-inversion operation required by the live corrections.

## 4. Designated partner account04/B19 applied to an actual inequality

The designated partner source is account04/B19 `QFORM-FINITE-UNION-CORE-v1`, canonical mathematics

`yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T122030Z-account04-B19-QFORM-r1/REPORT.md`.

It proves that for any fixed measurable map, the interval-concentration supremum over arbitrary independent cap-one densities equals the supremum over products of indicators of bounded finite unions of intervals of measure one, with no loss in the concentration constant.

Apply it to the actual new branch. Restrict first to finite-union product indicators. The proof of Theorem 3.1 gives, for every interval `I`,

`P{X^TAX in I} <= 12 sqrt(e) |I|`.                          (4.1)

The partner theorem transfers **this exact inequality** with the same coefficient to every arbitrary independent cap-one marginal law:

`P{X^TAX in I} <= 12 sqrt(e) |I|`.                          (4.2)

Thus the designated partner is applied to a concrete target-level inequality, not merely cited. The direct Fourier proof of Theorem 3.1 already has arbitrary-law scope, so this partner transfer is redundant analytically but supplies an independent exact extremal-law interface with no support assumption.

## 5. Immediate structural consequence: O0 heavy count collapses to at most two

The completed O0 diffuse ridge branch already pays states with no `3/4`-heavy row obstruction. Theorem 3.1 now pays every O0 state with **three or more** `3/4`-heavy rows. Therefore an unpaid O0 state may be reduced to a one- or two-heavy physical skeleton.

The newest B07 fixed-skeleton theorem (run r14) gives the exact identities, for a fixed heavy set `J` of size `r=1` or `2`,

`sum_{S superset J, |S|=3} det(B_S B_S^T)
 =det(B_JB_J^T) e_(3-r)(C_J C_J^T)`,                         (5.1)

where `C_J` is the row family projected orthogonally to `span(B_J)`. Its one-heavy exclusion collar also pays all moderate one-heavy states except a near-coloop or a genuinely nested-heavy state.

Thus the three-heavy branch and its formerly necessary transpose-leverage/six-coordinate-collar split can be deleted from the live proof tree. The O0 obstruction is now concentrated in one/two physical rows plus **aggregate** transverse currency.

## 6. Direct attack on the new first unpaid implication

The current first O0 implication is

`QFORM-O0-ONE-TWO-HEAVY-CURRENCY-TO-SMOOTHER-v1`:

> Starting from a one- or two-heavy original-coordinate skeleton and its fixed aggregate exterior currency, convert that currency into a product-preserving smoothing mechanism without demanding a zero self block, a uniformly good single minor, or a conditional density cap.

A fresh compatible result from account03/B08 supplies an especially sharp near-coloop currency. In its unpaid fine-scale branch, for an almost-coloop physical row `j` in an actual residual cross bank `H`,

`sum_{k != j} sum_{r<s} det H[{j,k},{r,s}]^2
 > (4191/281804800) gamma^4`.                                (6.1)

This quantity is invariant under a second scalar Schur shear through row `j`.

A second fresh compatible result from account01/B08, `QFORM-ZERO-SELF-GROUPED-CROSSBANK-v1` (canonical report recorded under its r17 run), proves that if a two-row physical bank has zero self block and cross matrix `M` of rank two, then

`||p_Q||_infinity
 <= C_lin^2 sqrt(pi)
    [sum_{r<s}det M[:,{r,s}]^2]^(-1/4)`,                     (6.2)

with a continuous `C_0` density; `C_lin` is the universal bounded-density projection constant in that theorem.

Therefore (6.1) is already quantitatively sufficient in the **zero-self endpoint**:

`||p_Q||_infinity
 < C_lin^2 sqrt(pi)
   (281804800/4191)^(1/4) gamma^(-1)
 < 28.542 C_lin^2 gamma^(-1)`.                               (6.3)

This does not close the general near-coloop state because its physical two-row self block is arbitrary and the calibration scale `gamma` still has to be matched to an outer target-scale resource. But it identifies the exact remaining algebraic debt: the aggregate transverse pair currency itself is no longer the obstacle; the obstacle is a **self-block/scale splice** that must either (i) pay a sufficiently nondegenerate physical self pair, or (ii) remove/absorb its rank-one part without destroying original-coordinate independence, leaving (6.2), or (iii) feed one more independent grouped direction into the half-Riesz transducer.

This is strictly narrower than the previous generic “high-offdiagonal aggregate” gap.

## 7. Compact conditional end-to-end proof tree after r17

A correction-safe assembly is now:

1. **Low offdiagonal.** If `s_2(A-diag A)<=499/1000`, B19 r15 gives `||p_Q||_infinity<84` for every allowed product law.
2. **High offdiagonal.** Use the completed third-compound overlap reduction into O0/O1/O2/O3; do not infer a rank-two cut merely from high `s_2`.
3. **O0 diffuse ridge.** Paid by the completed ridge-window / effective-dimension theorem in its exact stated scope.
4. **O0 with >=3 heavy rows.** Paid by Theorem 3.1 here with continuous density `<=12sqrt(e)<19.785`.
5. **O0 with <=2 heavy rows.** B07 r14 pays the moderate one-heavy exclusion collar and leaves only nested-heavy / near-coloop aggregate skeletons. B08 r17 supplies the fixed pair currency (6.1). Equation (6.3) pays its zero-self endpoint. The arbitrary-self-block/scale splice is the first remaining O0 implication.
6. **O1/O2/O3.** Their aggregate singular-hyperbolic / bordered-polynomial / principal-triple packets remain to be joined to already-proved product-preserving analytic payments.

No step above treats a rotated eigen-coordinate law as independent or replaces a biased conditional law by the original product law.

## 8. Status

`QFORM-O0-THREE-HEAVY-CROSSBANK-CLOSURE-v1`: **PROVED**, with continuous density bound `12sqrt(e)` at the live O0 normalization `E>=1/256`.

Designated partner account04/B19: **APPLIED** to the explicit interval inequality (4.1)-(4.2).

First remaining O0 implication: **arbitrary-self-block / scale splice on a one/two-heavy skeleton**.

Full QFORM target: **OPEN / NOT PROVED / NOT DISPROVED**.

Full continuous-representative conclusion: **OPEN**. Continuity is proved only on the new cross-bank branch and other branches whose source theorems explicitly provide it.

Native learned-memory ingestion: **not verified**. Repository retrieval/write does not establish native ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
