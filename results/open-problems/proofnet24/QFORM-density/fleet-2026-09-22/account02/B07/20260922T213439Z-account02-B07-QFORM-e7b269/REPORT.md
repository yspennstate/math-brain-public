SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-22T21:34:39Z.
attacking: the anchored two-star survivor — regroup the two ridge-coloop anchors into one physical side, pay any genuine two-cross wedge before reciprocal minor extraction, and characterize/stress the exact failure geometry.

# account02/B07 — checkerboard wedge payment and near-leaf obstruction

**Run:** `20260922T213439Z-account02-B07-QFORM-e7b269`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
**Classification:** **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED (intermediate checkerboard-two-cross shortcut); FULL TARGET OPEN**.

## 1. Exact target and correction discipline

The target is unchanged: for arbitrary independent real original coordinates with one-dimensional probability densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `X^T A X`, or construct a target-valid counterexample.

This report uses no moments, compact support, centering, log-concavity, post-rotation independence, arbitrary-joint rank-three coarea bound, positive conditional projection-density moment, worst conditional scalar-remainder density, or inference of one uniformly good local minor from an aggregate determinant bank. The current scalar-conditioning and arbitrary-joint/coarea corrections were refreshed immediately before publication.

## 2. Completed inputs actually used

### Designated partner account03/B07 r17

Complete proof:

`yspennstate/math-open-problems@a20d669ff2c433cc70cb70234f49431da4518fa5`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T203738Z-account03-B07-qform-r17/REPORT.md`.

At the unique effective-dimension-two ridge scale `tr K=2`, it proves the following. If one physical ridge side has maximum leverage at most `23/24`, then

`H_(1/2)(R) <= 79.98514376669046 E_2(B)^(-1/8)`.

If both physical sides instead have a coordinate of ridge leverage `>23/24`, there are physical anchors `i,j` for which, writing

`B = [[b, r^T], [c, C]],`

one has

`M_ij = ||b C-c r^T||_F^2 > E_2(B)/2`,

hence either

`b^2 ||C||_F^2 > E_2(B)/8`

or

`||r||_2^2 ||c||_2^2 > E_2(B)/8`.

### Compatible account01/B07 compound transfer

Complete report read at immutable source

`yspennstate/math-open-problems@c2bc78fc4f8e642f5d8c85fcc7d53956730b5cb1`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260922T210652Z-r11/REPORT.md`.

It proves

`E_2(B)^3 >= (9/2) E_3(B)^2`.

Thus the current O0 currency `E_3(B)>=1/256` implies

`E_2(B)>=c_2=(9/2^17)^(1/3)>1/25`.

Consequently the partner's near-coloop alternative improves on O0 to

`b^2||C||_F^2>1/200`

or

`P:=||r||_2^2||c||_2^2>1/200`.                                  (2.1)

The present run attacks the second, genuine two-star alternative.

### Two-cross analytic payment

I use account03/B09 `QFORM-HALFRIESZ-TWO-CROSS-v1`, read from

`yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T184648Z-account03-B09-QFORM-r15/REPORT.md`.

For any full quadratic-affine form and any disjoint ORIGINAL-coordinate cut with cross block `D` having two nonzero singular values,

`H_(1/2) <= 8 (sigma_1(D)sigma_2(D))^(-1/4)`.                    (2.2)

Arbitrary same-side quadratic terms, affine terms, outside couplings and extra spectrum remain present.

## 3. First new theorem: put the two anchors on one physical side

Let `S` be any real symmetric residual matrix with an original-coordinate cut `L|R`. Fix the partner anchors `i in L`, `j in R`. Put

`L0=L\{i}`, `R0=R\{j}`,

and write the old cross block as

`B=S[L,R] = [[b, r^T], [c, C]]`,                               (3.1)

where `r` is indexed by `R0` and `c` by `L0`. The old cross block does not contain the same-side central couplings, so define them separately by

`u=S[L0,i]`, `v=S[R0,j]`.                                      (3.2)

Now form the **checkerboard physical cut**

`I={i,j}`, `J=L0 union R0`.                                    (3.3)

Its actual cross block, with no terms suppressed, is the two-row matrix

`D=S[I,J] = [[u^T, r^T], [c^T, v^T]].`                         (3.4)

This is an original-coordinate cut, hence it preserves the product-law provenance needed by (2.2).

### Theorem 3.1 — `QFORM-TWOSTAR-CHECKERBOARD-WEDGE-v1`

For the block (3.4),

`E_2(D)=e_2(DD^T)` obeys the exact identity

`boxed:
E_2(D)
 = ||u wedge c||_2^2
 + ||r wedge v||_2^2
 + ||u v^T-c r^T||_F^2.
`                                                                (3.5)

Equivalently, if

`a=(u,r)`, `q=(c,v)`,

then

`E_2(D)=||a||^2||q||^2-<a,q>^2`.                               (3.6)

For every `eta in (0,1]`, if the incoming two-star currency is

`P=||r||^2||c||^2>0`,                                           (3.7)

then there is the rigorous dichotomy:

**Wedge-paid branch**

If

`E_2(D)>=eta P`,                                                 (3.8)

then, because `D` has only two rows,

`(sigma_1(D)sigma_2(D))^2=E_2(D)`,                              (3.9)

and (2.2) gives the full residual estimate

`boxed:
H_(1/2)(R)<=8 (eta P)^(-1/8).
`                                                                (3.10)

In the O0 two-star branch (2.1), choose `eta=1/16`. Then (3.8) gives

`boxed: H_(1/2)(R)<8*3200^(1/8)=21.9398540541... .`             (3.11)

This spends an **aggregate two-row second compound**, not one reciprocal `2x2` minor.

**Near-leaf branch**

If instead

`E_2(D)<eta P`,                                                  (3.12)

let

`alpha=<a,q>/||q||^2`.

The exact least-squares identity gives

`||a-alpha q||^2=E_2(D)/||q||^2`.                               (3.13)

Since `||q||^2=||c||^2+||v||^2>=||c||^2`, (3.7) and (3.12) imply

`boxed:
||u-alpha c||^2+||r-alpha v||^2 < eta ||r||^2.
`                                                                (3.14)

Symmetrically, for `beta=<a,q>/||a||^2`,

`boxed:
||c-beta u||^2+||v-beta r||^2 < eta ||c||^2.
`                                                                (3.15)

At `eta=1/16`, every unpaid two-star state therefore has one central outside-coupling row within relative Euclidean defect `<1/4` of a scalar multiple of the other at the natural star scale.

If `E_2(D)=0`, the conclusion is exact: `a=alpha q` for a nonzero scalar `alpha`, so

`S[J,{i,j}] (1,-alpha)^T=0`.                                    (3.16)

Thus one nonzero linear combination of the two anchor coordinates has **zero coupling to every outside coordinate**. The true obstruction is an exact/near two-coordinate leaf, not a generic two-star cloud.

### Proof of (3.5)-(3.16)

Because `D` has two rows, Cauchy--Binet says `E_2(D)` is the sum of squares of all its `2x2` minors. Split column pairs into three disjoint classes.

* Two columns in `L0` give the squared wedge `||u wedge c||^2`.
* Two columns in `R0` give `||r wedge v||^2`.
* One column `k in L0` and one column `l in R0` give minor `u_k v_l-c_k r_l`; summing their squares gives `||uv^T-cr^T||_F^2`.

This proves (3.5). Equation (3.6) is the two-row Gram determinant identity. If (3.8) holds, (3.9) is exact because `rank(D)<=2`, so (3.10) follows directly from the source-pinned two-cross theorem. For (3.13), orthogonal projection of `a` onto the line spanned by `q` gives

`min_t ||a-tq||^2
 = ||a||^2-<a,q>^2/||q||^2
 = E_2(D)/||q||^2`.

The denominator comparisons give (3.14)-(3.15). Equality `E_2(D)=0` means the two nonzero rows of `D` are proportional, yielding (3.16). QED.

## 4. A target-valid stress shows the near-leaf branch is real

The tempting next claim would be:

> a large partner two-star reserve automatically produces a genuine two-cross checkerboard block when the two anchors are placed on one physical side.

That claim is false even inside the **full O0-v2 numerical collar**, including constant third-compound mass and two-sided `23/24` ridge near-coloops.

Fix `K=100`. Let

`L={i,k,m1,m2,m3}`, `R={j,l,n1,n2,n3}`.

Define a symmetric matrix `S_K` as follows. The only nonzero same-side entries are

`S_ik=S_ki=K`, `S_jl=S_lj=K`.                                  (4.1)

Its `L|R` cross block is

`B_K =
[[0,K,0,0,0],
 [K,0,0,0,0],
 [0,0,1,0,0],
 [0,0,0,1,0],
 [0,0,0,0,1]].`                                                 (4.2)

All omitted entries and all diagonals are zero.

The nonzero singular values of `B_K` are

`K,K,1,1,1`.                                                     (4.3)

Therefore

`rank(B_K)=5`,

`E_2(B_K)=K^4+6K^2+3=100060003`,                                (4.4)

`E_3(B_K)=3K^4+6K^2+1=300060001`.                               (4.5)

At the unique effective-dimension-two scale, writing `x=gamma^2`,

`2K^2/(K^2+x)+3/(1+x)=2`,                                      (4.6)

so exactly

`x=(1+sqrt(1+24K^2))/4`.                                       (4.7)

For `K=100`,

`x=122.72474229407466...`,

and the ridge leverage of both physical anchor coordinates `i` and `j` is

`K^2/(K^2+x)=0.9878763134019327... >23/24`.                     (4.8)

For these anchors,

`b=0`,
`r=(K,0,0,0)`,
`c=(K,0,0,0)`,                                                  (4.9)

so the partner anchored packet is

`M_ij=||c r^T||_F^2=K^4`,                                      (4.10)

and indeed

`M_ij/E_2(B_K)=0.9994003298200981... >1/2`.                     (4.11)

This is purely the two-star alternative; its star product is `P=K^4`.

But the checkerboard cross block (3.4) has **two identical rows**. Indeed the same-side vectors are

`u=c=(K,0,0,0)`, `v=r=(K,0,0,0)`.                              (4.12)

Hence

`boxed: E_2(D)=0.`                                               (4.13)

So even `E_3(B)>>1`, rank five, and both ridge anchors above `23/24` do not force positive checkerboard two-cross mass.

This is a target-class matrix obstruction, not a counterexample to QFORM. The spectrum of `S_K` is exactly

`{2K,-2K,1,1,1,-1,-1,-1,0,0}`.                                (4.14)

Thus

`A_K=[1] direct_sum S_K`                                        (4.15)

has many eigenvalues of modulus at least one. Moreover the already-proved own-slot theorem `QFORM-CROSS-FIBER-PLANCHEREL-v1` applies directly to (4.2): with rank five and product of nonzero cross singular values `K^2`,

`||p_Q||_infinity <= (5e/3) K^(-2/5)`.                         (4.16)

At `K=100` this is `0.7180310608525814...`. Thus the construction decisively refutes only the intermediate checkerboard extraction, while the full target instance is already paid by a different product-preserving mechanism.

Classification of (4.1)-(4.16):

**`QFORM-TWOSTAR-CHECKERBOARD-TWOCROSS-FALSE-v1` — CANDIDATE_REFUTED for the intermediate implication; QFORM itself not refuted.**

## 5. Conditional proof map after this run

The coordinate-minor O0 chain is now sharper.

1. The existing O0 structural route gives `E_3(B)>=1/256`.
2. The previous account02/B07 effective-dimension-three theorem pays exact rank three and every rank `>3` state with one ridge side `<=2/3`.
3. account01/B07 transfers the same third-compound currency to `E_2(B)>1/25`.
4. account03/B07 pays the effective-dimension-two moderate branch by `H_(1/2)<120`; otherwise it forces an anchored edge-bank or two-star reserve `>1/200`.
5. **New:** in the two-star branch, form the physical checkerboard cut (3.3). If its complete two-row second compound is at least `P/16`, the full residual is paid by `H_(1/2)<21.940` with arbitrary same-bank curvature retained.
6. The only surviving two-star subbranch is the quantitatively near-leaf geometry (3.14)-(3.15). The exact stress in Section 4 proves that this subbranch cannot be deleted by a stronger structural assertion based only on the current O0 currency.

The edge-bank alternative remains a sibling debt. A full density conclusion from a half-Riesz bound still requires the appropriate already-proved physical-square/pivot transducer in the parent branch; I do not relabel a fractional-potential estimate as a density theorem.

## 6. First unpaid implication

`QFORM-O0-NEARLEAF-OR-EDGEBANK-PAYMENT-v1` (OPEN):

> In the O0 near-coloop state with `E_3(B)>=1/256`, either spend the edge-bank reserve `b^2||C||_F^2>1/200`, or, in the two-star state `P>1/200`, exploit the new quantitative near-leaf relation
> `min_alpha ||(u,r)-alpha(c,v)||^2 < P/(16|| (c,v) ||^2)`
> to obtain a translation-uniform product-preserving half-Riesz/density estimate, or route it to a completed scalar-pivot, pair-log, grouped-coordinate, exact-cross-rank, or zero-self branch.

The near-leaf argument must retain the two original anchor variables and the outside product coordinates; rotating the anchors and then asserting independence is not allowed. The exact family (4.1)-(4.15) should remain a regression control: any proposed payment must accept it rather than assuming checkerboard rank two.

## 7. Exact computation and regression output

The standard-library exact checker `CHECK.py` is saved beside this report. It checks the full rational wedge identity and least-squares formula, then checks the target-valid `K=100` stress, ridge threshold and constants. Exact executed output:

```text
identity_E2 = 369 expansion = 369 equal True
least_squares = 41/3 E2/||q||^2 = 41/3 equal True
K = 100
E2 = 100060003
E3 = 300060001
M/E2 = 0.9994003298200981
theta2_gamma_sq = 122.72474229407466
anchor_ridge_leverage = 0.9878763134019327 threshold 0.9583333333333334 passes True
checkerboard_E2 = 0
two_star_P = 100000000
paid_branch_if_E2D>=P/16: H_half < 21.939854054096585
crossfiber_density_bound = 0.7180310608525814
QFORM_TWOSTAR_CHECKERBOARD_WEDGE_CHECK_PASS
```

The finite checker is a regression aid; the proofs are the exact algebra above.

## 8. Status and provenance

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The new theorem is a supporting structural/analytic reduction, and the stress is a refutation of one intermediate extraction only. No independent review of this run is claimed.

Sources were read through the authorized repository connector. Repository retrieval is not verified native learned-memory ingestion, so status remains `WITHOUT_VERIFIED_BRAIN`. No email, notification, task/schedule, permission, public-release, paid-model, remote-workflow or cross-account-authentication action was taken. The changed mathematical files contain only source-pinned mathematics and harmless deterministic checks; a manual scoped privacy review found no credentials, machine paths, scheduler identifiers, unrelated private data or benchmark material.
