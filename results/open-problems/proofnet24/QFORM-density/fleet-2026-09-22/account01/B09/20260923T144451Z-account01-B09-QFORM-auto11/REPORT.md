SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T14:44:51Z.
attacking: the arbitrary-leaf-curvature two-hub survivor by converting aggregate *physical singleton-augmentation three-volume* into a quantitative distance from the exact diagonal-plus-hub-slope form, with the near-coloop row as the only denominator obstruction.

# account01/B09 — punctured three-volume stability for a physical two-hub block

## Status

**ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL THEOREM / FULL QFORM OPEN.**

The unrestricted owner target is not proved or disproved here. Full-target continuity remains open. The new theorem is deterministic and source-coordinate exact; it does **not** invoke stability of density under a small quadratic perturbation. Its purpose is to turn the remaining arbitrary same-side curvature in a rank-two two-hub packet into a quantitative dichotomy: either a literal physical leaf is a near-coloop, or all curvature not explained by a diagonal plus the two-hub slope span is controlled by the aggregate physical singleton-augmentation three-volume.

No rotation of the random vector, moment assumption, compact support, log-concavity, connected support, or Gaussian assumption is used.

## 1. Setup: literal physical two-hub packet

Fix two ORIGINAL physical hub coordinates

`H={h1,h2}`

and a disjoint ORIGINAL leaf bank `L`, `|L|=m`. Write

`C=A[L,H] in R^{m x 2}`,
`D=A[L,L] in R^{m x m}`.

Assume `rank C=2` and put

`G=C^T C`,
`Delta=det G>0`.

Write `c_i^T` for row `i` of `C`, and define the physical row leverage

`ell_i=c_i^T G^{-1}c_i`.

Thus `0<=ell_i<=1` and `sum_i ell_i=2`.

For every leaf `i`, actually elevate **that same physical coordinate** to the hub side and puncture it from the leaf side. Set

`J_i=L\{i}`

and define the actual physical singleton-augmentation cross matrix

`M_i=A[H union {i}, J_i]`.

Its first two rows are the two hub-to-punctured-leaf rows, while the third row is `D[i,J_i]`. Define the squared physical three-volume

`V_i=det(M_i M_i^T)`.

Equivalently, by Cauchy--Binet,

`V_i=sum_{T subset J_i, |T|=3} det A[H union {i},T]^2`.

Every determinant in this sum is therefore an ACTUAL source-coordinate `3x3` cross minor; no coordinate is used simultaneously on both sides of the cut.

## 2. New theorem

### Theorem `QFORM-TWOHUB-PUNCTURED-THREEVOLUME-STABILITY-v1`

Assume `ell_i<1` for every `i in L`. Then there exist a symmetric matrix `M in R^{2x2}`, a diagonal matrix `Lambda in R^{m x m}`, and a symmetric zero-diagonal matrix `E` such that

`D=C M C^T + Lambda + E`

and

`boxed:
 ||E||_F
 <= [ (2/Delta) sum_i V_i/(1-ell_i) ]^{1/2}.`                 (2.1)

In particular, if

`q=max_i ell_i <1`, `V=sum_i V_i`,

then

`boxed:
 ||E||_op <= ||E||_F
 <= [ 2V/(Delta(1-q)) ]^{1/2}.`                              (2.2)

At the exact endpoint `V=0` and `q<1`, one obtains the exact physical-coordinate classification

`boxed: D=C M C^T+Lambda.`                                   (2.3)

Thus exact vanishing of every physical singleton-augmentation three-volume forces all non-diagonal leaf curvature into the two-dimensional hub-slope span, unless deletion of some literal leaf destroys the rank-two hub frame (`ell_i=1`).

### Proof

Fix `i`. Let `C_(i)` be `C` with row `i` deleted. Then

`G_i=C_(i)^T C_(i)=G-c_i c_i^T`.

By the matrix determinant lemma,

`det G_i=Delta(1-ell_i)`.                                    (2.4)

Because `ell_i<1`, `G_i` is positive definite. Let `d_i` denote the full `i`th row of `D`, and define the punctured row-fitting error

`delta_i^2
 = inf_{u in R^2} sum_{j!=i} (D_ij-c_j^T u)^2`.             (2.5)

The Gram determinant of `M_i` is the determinant of the two-row Gram `G_i` times the squared distance of the third row from the span of the first two rows. Therefore

`V_i=det G_i * delta_i^2
    =Delta(1-ell_i) delta_i^2`.                               (2.6)

This is an exact identity, not an inequality. Summing gives

`sum_i delta_i^2
 = (1/Delta) sum_i V_i/(1-ell_i).`                     (2.7)

For each `i`, choose a minimizing vector `u_i in R^2` in (2.5). Define

`lambda_i=D_ii-c_i^T u_i`,
`Lambda_0=diag(lambda_i)`,

and let `U in R^{m x 2}` have row `u_i^T`. Put

`S=D-Lambda_0`.

The full-coordinate residual in row `i` of `S-U C^T` vanishes at coordinate `i`, while its remaining squared norm is exactly `delta_i^2`. Hence

`||S-U C^T||_F^2=sum_i delta_i^2`.                           (2.8)

Let

`P=C G^{-1} C^T`, `Q=I-P`.

`P` is the orthogonal projection onto the physical hub-slope span `range(C)`. Since `(U C^T)Q=0`, (2.8) gives

`||S Q||_F <= [sum_i delta_i^2]^{1/2}.`                      (2.9)

Because `S` is symmetric, `||Q S||_F=||S Q||_F`. Define

`M=G^{-1} C^T S C G^{-1}`.

Then `M=M^T` and

`C M C^T=P S P`.                                             (2.10)

In the orthogonal decomposition `range(P) direct-sum range(Q)`, the three blocks

`P S Q`, `Q S P`, `Q S Q`

are Frobenius-orthogonal. Therefore

`||S-P S P||_F^2
 =2||P S Q||_F^2+||Q S Q||_F^2
 <=2( ||P S Q||_F^2+||Q S Q||_F^2 )
 =2||S Q||_F^2`.                                             (2.11)

Combining (2.7), (2.9), and (2.11),

`||S-C M C^T||_F
 <= [ (2/Delta) sum_i V_i/(1-ell_i) ]^{1/2}.`                (2.12)

Finally absorb the diagonal of `S-C M C^T` into `Lambda_0`. Namely set

`Lambda=Lambda_0+diag(S-C M C^T)`,
`E=offdiag(S-C M C^T)`.

Then `E` is symmetric and zero-diagonal, `D=C M C^T+Lambda+E`, and deleting the diagonal cannot increase Frobenius norm. This proves (2.1). Since `1-ell_i>=1-q`, (2.2) follows. If `V=0`, (2.1) gives `E=0`, proving (2.3). QED.

## 3. Interpretation: the only denominator failure is a physical coloop

The factor `1-ell_i` is not an artifact of the proof. From (2.4),

`ell_i=1 iff det(C_(i)^T C_(i))=0`.

Thus `ell_i=1` says that deleting the literal physical leaf `i` collapses the two-hub cross frame from rank two to rank at most one: `i` is an exact physical coloop. The weighted instability in (2.1) is therefore geometrically sharp in kind.

Moreover `sum_i ell_i=2`, so for every `gamma in (0,1)` there are fewer than `2/(1-gamma)` leaves with `ell_i>=1-gamma`. In particular the previously isolated `ell_i>0.98399` near-coloop state is a genuinely finite physical collar, not a diffuse high-dimensional failure.

## 4. Spectral routing corollary (not a density perturbation claim)

Define

`A0=[[A[H,H], C^T], [C, C M C^T+Lambda]]`

on `H union L`, with the same outside blocks if outside coordinates were conditioned. Then

`A-A0`

has only the leaf-leaf error block `E`, hence

`||A-A0||_op<=||E||_F`.

Consequently singular/eigenvalue information can be routed by Weyl. For example, if the relevant full principal packet has `s_3(A)>=1` and the right side of (2.1) is `epsilon<1`, then

`s_3(A0)>=1-epsilon`.                                        (4.1)

**Important correction-aware limitation.** Equation (4.1) is only a deterministic spectral reduction. We do NOT throw away `X_L^T E X_L` as a 'small random error', and we do NOT infer any density estimate for `A` from a density estimate for `A0`. The arbitrary-density problem does not permit such an unproved perturbative step. The next analytic mechanism has to retain the actual residual curvature or route its physical volume directly.

## 5. Exact endpoint recovered from physical minors

The exact statement (2.3) is the source-coordinate form one expects in the rank-two / no-singleton-augmentation survivor. The proof above strengthens it quantitatively and explains the correct stability parameter: not the maximum singleton minor, but the **aggregate punctured physical three-volume weighted by the inverse deletion Gram factors**.

This matters because a small maximum augmentation minor alone is not enough for dimension-free low-rank closeness. Formula (2.1) instead uses the full aggregate volume and explicitly exposes the only possible conditioning loss, `1-ell_i`.

## 6. Deterministic four-leaf regression

Take

`C=[(1,0),(0,1),(1,0),(0,1)]^T`.

Then

`G=2 I_2`, `Delta=4`, and every `ell_i=1/2`.

Let `D` be symmetric with only

`D_12=D_21=1`

nonzero. Direct punctured least squares gives

`delta_1^2=delta_2^2=1/2`, `delta_3^2=delta_4^2=0`.

Hence by the exact identity (2.6),

`V_1=V_2=1`, `V_3=V_4=0`, `V=2`.

The coarse theorem bound is therefore

`||E||_F <= sqrt( 2*2/(4*(1/2)) )=sqrt(2)`.

The two-sided projected construction in the proof gives explicitly

`M=[[0,1/4],[1/4,0]]`

and an error with

`||E||_F^2=3/2<2`,

consistent with the theorem. This regression uses exact physical puncturing; no illegal minor contains leaf `i` on both sides of the cut.

## 7. Designated partner account02/B09 actually applied

I read the complete canonical proof of account02/B09's newest completed theorem

`QFORM-ONE-ANCHOR-THREEVOLUME-HYBRID-v1`

at

`yspennstate/math-open-problems@59ccddd0766b466b30abd645926887f907b0bcd7`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T134326Z-account02-B09-QFORM-r13/REPORT.md`.

It states that for an actual source-coordinate cross matrix, if every selected physical `3x3` minor contains one distinguished physical row `h`, the total selected determinant-square mass is `Z>0`, and every other selected row marginal is at most `1/2`, then

`||p_Q||_inf
 <=5*2^(4/5)*sqrt(e) ||a||_2^(1/5) Z^(-1/5)`,              (7.1)

with a continuous density and the identical coefficient multiplying every interval length.

Here is a fresh literal target-valid application. For `s>=1`, let `M_s` be the `5x3` physical cross matrix with rows

`(s,0,0)`,
`(0,1/sqrt(2),0)`,
`(0,1/sqrt(2),0)`,
`(0,0,1/sqrt(2))`,
`(0,0,1/sqrt(2))`.

Take the symmetric cross-only matrix

`A_s=[[0,M_s],[M_s^T,0]]`.

Its nonzero eigenvalues are exactly

`{+s,-s,+1,-1,+1,-1}`,

so the owner's three-large-eigenvalue hypothesis holds for every `s>=1`.

Select the four physical `3x3` minors formed from the first row, one of rows 2--3, one of rows 4--5, and all three columns. Each squared determinant is `s^2/4`, hence

`Z=s^2`.

The distinguished row norm is `||a||=s`, and every other selected row marginal is exactly `1/2`. Therefore (7.1) gives, for every admissible product law,

`boxed:
 ||p_(X^T A_s X)||_inf
 <=5*2^(4/5)*sqrt(e) s^(-1/5).`                              (7.2)

At `s=32`,

`boxed: ||p_(X^T A_32 X)||_inf <7.177`,
`boxed: P{X^T A_32 X in I}<7.177 |I|`                        (7.3)

for every interval `I`; this branch has a continuous density. This is an actual use of the designated partner theorem, not a restatement of it.

## 8. What this closes, and what it does not

The new theorem closes the **deterministic missing implication** in the arbitrary-leaf-curvature rank-two two-hub state:

- aggregate physical singleton-augmentation three-volume zero + no physical coloop => exact `D=C M C^T+Lambda`;
- small aggregate volume + no near-coloop => quantitative Frobenius/operator proximity to that exact form;
- failure of the denominator condition is itself a literal physical near-coloop, already the previously isolated finite-collar state.

It does **not** yet pay the full arbitrary-leaf-curvature branch probabilistically. In particular, `E` cannot simply be deleted because it is small in operator norm.

The first unpaid B09 implication is now

`QFORM-TWOHUB-SLOPEFORM-PLUS-RESIDUAL-PAYMENT-v1`:

> Starting from `D=C M C^T+Lambda+E` with the exact weighted identity behind (2.1), either spend the actual residual `E` through its physical singleton-augmentation volume by a direct conditional-linear / grouped-cross estimate, or pay the exact slope-form endpoint `E=0` using the third spectral resource from the physical hub core/diagonal bank. The proof must not use post-rotation independence or a perturbative 'small random quadratic error' step.

A promising next split is: (i) exact slope-form endpoint, where the non-diagonal leaf curvature factors entirely through `z=C^T X_L`; (ii) positive residual volume, where the same physical augmentations used in `V_i` should be fed directly into a source-coordinate linear anti-concentration compiler. The near-coloop rows stay explicit rather than being averaged away.

## 9. Full-target status

The universal bounded-density conjecture remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**. The new theorem is a correction-aware structural reduction on a key rank-two survivor and the partner application supplies a genuine continuous-density `O(|I|)` branch.

Execution label for this run: `WITHOUT_VERIFIED_BRAIN` unless later current-run evidence proves authenticated native receiver ingestion; repository transport alone is not such evidence.
