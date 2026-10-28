SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-24T01:17:06Z.
attacking: the exact rank-one-pair / diffuse rank-one-star collar with arbitrary same-leaf curvature; compile curvature transverse to the star into one original-coordinate disjoint cross packet before any reciprocal minor payment.

# account03/B09 r43 — rank-one star curvature stability and disjoint crossing compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: bilinear block mechanism / quantitative inequalities  
Run: `20260924T011706Z-account03-B09-QFORM-r43`  
Status: **NEW SUPPORTING STRUCTURAL THEOREMS, PENDING INDEPENDENT REVIEW; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and exact debt attacked


The immediate new source motivating this run is account01/B09's exact singular-pair collar report, read at

`yspennstate/math-open-problems@e8b5b25d32c90397bfa90c586eb44564798cf193`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260924T005202Z-account01-B09-QFORM-auto11/REPORT.md`.

It proves that for an exact rank-one physical pair with rank-one pair-to-leaf cross bank, the anchored overlap-two compound matrix is blind to the same-bank leaf block `D`. It also closes the physically concentrated star branch: at overlap scale at least `1/4`, failure of the principal-triple payment forces the normalized star leverage `q<1/16`. Its first remaining implication is exactly the diffuse-star / arbitrary-leaf-curvature exit.

The other source used below is account02/B09 r15,

`yspennstate/math-open-problems@57b57dc6fa114b1c782a91599bdfbe94a358b2cb`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T224553Z-account02-B09-QFORM-r15/REPORT.md`.

That report pays the exact collinear zero-active-leaf star but leaves general curvature on the same leaf bank open.

The designated account04/B09 partner theorem is

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`.

For a literal invertible physical `3 x 3` cross block `K`, it proves

`||p_Q||_infinity <= 3 |det K|^(-1/3)`,

with arbitrary dense same-side curvature and a continuous density. I apply it to an actual target-valid matrix in Section 7.

## 2. Physical rank-one star setup

Let `H={h1,h2}` be a literal pair of original coordinates and `I` a disjoint active leaf bank. Assume only that the physical pair-to-leaf block has rank one:

`A[H,I] = g r^T`,                                                (2.1)

where `g in R^2` and nonzero `r in R^I`. Let

`D=A[I,I]`                                                       (2.2)

be an **arbitrary real symmetric matrix**. No assumption is made on its norm, rank, sign, support, or relation to `r`.

Put

`R=||r||_2`,
`q=max_(k in I) r_k^2/R^2`.                                     (2.3)

The diffuse branch supplied by account01/B09 has `q<1/16`; for the algebra below it is enough that `q<1`. Then `r_{I\{k}}` is nonzero for every `k`.

For each leaf `k`, define the literal physical cross block

`M_k = A[H union {k}, I\{k}]`.                                  (2.4)

Define the rowwise transverse defect

`delta_k = dist(D[k,I\{k}], span(r_{I\{k}}))`,                  (2.5)

and the physical singleton-augmented second-volume currency

`Xi_k = e_2(M_k M_k^T)`,
`Xi = sum_k Xi_k`.                                                (2.6)

Here `e_2` is the second elementary symmetric polynomial of the eigenvalues, equivalently by Cauchy-Binet the sum of squares of every literal `2 x 2` minor of `M_k`.

Finally define the physical leaf-curvature distance

`d_* = inf_(lambda in R, Lambda diagonal)
       ||D-lambda r r^T-Lambda||_F`.                             (2.7)

The set in (2.7) is unchanged under the nonunique rescaling `r -> c r`, `g -> g/c`, and the product `||g|| R` is invariant under the same rescaling.

## 3. Exact local exterior identity

### Theorem 3.1 — `QFORM-RANKONE-STAR-LOCAL-E2-IDENTITY-v1`

For every `k in I`,

`boxed:
 Xi_k = ||g||_2^2 ||r_{I\{k}}||_2^2 delta_k^2.`                 (3.1)

### Proof

The rows of `M_k` are

`g_1 r_{-k}^T`, `g_2 r_{-k}^T`, `D[k,-k]`.                      (3.2)

The first two are collinear, so all `2 x 2` minors using those two hub rows vanish. For a fixed hub row `h`, the sum of squares of all `2 x 2` minors formed with the leaf row is the Gram determinant of the two row vectors:

`g_h^2 [ ||r_{-k}||^2 ||D[k,-k]||^2
         - <r_{-k},D[k,-k]>^2 ]
 =g_h^2 ||r_{-k}||^2 delta_k^2`.                                (3.3)

Summing over the two physical hub rows gives (3.1). No random coordinate has been rotated. QED.

The key point is conceptual: although the anchored singular-pair compound matrix from account01/B09 literally deletes `D`, the **singleton-augmented disjoint cross volume does not**. It measures exactly the part of each physical leaf row transverse to the star direction.

## 4. Dimension-free stability of the exact aligned leaf model

### Theorem 4.1 — `QFORM-RANKONE-STAR-LEAFCURVATURE-STABILITY-v1`

Under `q<1`,

`boxed:
 sqrt(Xi)/(||g|| R)
 <= d_*
 <= sqrt(2/(1-q)) sqrt(Xi)/(||g|| R).`                           (4.1)

In particular,

`Xi=0  <=>  D=lambda r r^T+Lambda`

for some scalar `lambda` and physical-coordinate diagonal `Lambda`. Thus exact vanishing has no hidden high-dimensional curvature survivor.

### Proof: lower bound

For any scalar `lambda` and diagonal `Lambda`, the `k`th off-diagonal row of

`D-lambda rr^T-Lambda`

is

`D[k,-k]-lambda r_k r_{-k}`.                                    (4.2)

The second term belongs to `span(r_{-k})`; hence the squared norm of (4.2) is at least `delta_k^2`. Summing the physical rows,

`||D-lambda rr^T-Lambda||_F^2 >= sum_k delta_k^2`.               (4.3)

On the other hand, by (3.1),

`Xi
 =||g||^2 sum_k (R^2-r_k^2) delta_k^2
 <=||g||^2 R^2 sum_k delta_k^2`.                                 (4.4)

Taking the infimum in (4.3) proves the left inequality in (4.1).

### Proof: upper bound

For each `k`, perform the physical rowwise least-squares decomposition

`D[k,-k]=alpha_k r_{-k}+e_{k,-k}`,
`e_{k,-k} perpendicular r_{-k}`.                                (4.5)

Set `e_kk=0`, stack the coefficients as `alpha=(alpha_k)`, and let `E=(e_k)` and `A_0=alpha r^T`. Off the diagonal,

`D=A_0+E`.                                                       (4.6)

Because `D` is symmetric,

`skew(A_0)=-skew(E)`.                                            (4.7)

Let

`lambda=<alpha,r>/R^2`,
`z=alpha-lambda r`, so `z perpendicular r`.                     (4.8)

Then

`A_0-lambda rr^T = z r^T`.                                      (4.9)

For orthogonal `z,r`, the symmetric and skew parts of `z r^T` have exactly the same Frobenius norm:

`||sym(zr^T)||_F
 =||skew(zr^T)||_F
 =R||z||/sqrt(2)`.                                               (4.10)

Since subtracting `lambda rr^T` changes no skew part, (4.7)-(4.10) give

`||sym(A_0)-lambda rr^T||_F=||skew(E)||_F`.                      (4.11)

Choose the diagonal matrix `Lambda` so that the diagonal of `D-lambda rr^T-Lambda` is zero. Off the diagonal, `D` equals `sym(A_0)+sym(E)`, because (4.6) is symmetric there. Therefore

`d_*
 <= ||sym(A_0)-lambda rr^T||_F+||sym(E)||_F
 =  ||skew(E)||_F+||sym(E)||_F
 <= sqrt(2)||E||_F`.                                             (4.12)

By construction,

`||E||_F^2=sum_k delta_k^2`.                                     (4.13)

Equation (3.1) and `R^2-r_k^2 >= R^2(1-q)` give

`Xi >= ||g||^2 R^2(1-q) sum_k delta_k^2`.                        (4.14)

Combining (4.12)-(4.14) proves the right inequality of (4.1). If `Xi=0`, the constructed residual in (4.12) is zero, giving the exact model; the converse is immediate. QED.

This is a coefficient-space stability theorem only. In particular, no claim is made that a small Frobenius residual is a small random quadratic perturbation for unbounded inputs.

## 5. Compile the aggregate defect into one original-coordinate disjoint cut

The stability theorem still sums singleton packets. The next step is to aggregate **before** any reciprocal individual minor is paid.

For a partition `I=S disjoint union T`, define

`Z(S,T)
 =sum_(k in S) sum_(h in H) sum_(i<j; i,j in T)
   det A[{h,k},{i,j}]^2`.                                       (5.1)

Every determinant in (5.1) is a literal physical `2 x 2` minor of the one disjoint cross matrix

`A[H union S,T]`.                                                (5.2)

### Theorem 5.1 — `QFORM-RANKONE-STAR-CURVATURE-CROSSCOMPILER-v1`

There is a physical partition `I=S disjoint union T` such that

`boxed:
 e_2(A[H union S,T] A[H union S,T]^T)
 >= Z(S,T)
 >= (4/27) Xi.`                                                   (5.3)

Consequently,

`boxed:
 e_2(A[H union S,T] A[H union S,T]^T)
 >= [2(1-q)/27] ||g||^2 R^2 d_*^2.`                             (5.4)

In the account01/B09 unpaid diffuse-star chamber `q<1/16`, this sharpens numerically to

`boxed:
 e_2(A[H union S,T] A[H union S,T]^T)
 >= (5/72)||g||^2 R^2 d_*^2.`                                  (5.5)

### Proof

Expand each `Xi_k` by Cauchy-Binet. The hub-hub row pair contributes zero because the two hub rows are collinear. Hence

`Xi_k
 =sum_(h in H) sum_(i<j; i,j in I\{k})
   det A[{h,k},{i,j}]^2`.                                       (5.6)

Randomly place every leaf independently into `S` with probability `p` and into `T` otherwise. A fixed summand in (5.6), indexed by three distinct leaves `k,i,j`, appears in `Z(S,T)` exactly when `k in S` and `i,j in T`, with probability

`p(1-p)^2`.                                                      (5.7)

This is maximized at `p=1/3`, where it equals `4/27`. Therefore

`E Z(S,T)=(4/27)Xi`.                                             (5.8)

Some deterministic partition has at least the expectation. Since (5.1) is a subset of the squared `2 x 2` minors of the physical cross matrix (5.2), the first inequality in (5.3) follows. Finally rearrange the upper half of (4.1):

`Xi >= [(1-q)/2] ||g||^2 R^2 d_*^2`,                            (5.9)

and substitute into (5.3). If `q<1/16`, then

`2(1-q)/27 > 2(15/16)/27 =5/72`.                                (5.10)

QED.

This is the first essential implication attempted in this run: **arbitrary same-leaf curvature in the diffuse singular-pair collar either collapses exactly/quantitatively toward diagonal plus one aligned square, or it creates a dimension-free aggregate disjoint physical rank-two crossing currency.** No square-root decoupling appears.

## 6. Apply the compiler to the newest diffuse-star stress family

Account01/B09 exhibits a family showing that the singular-pair overlap-two ledger is blind to arbitrarily large dense leaf curvature. Let `m` be even and

`B=diag(1,0)`,
`g=e_2`,
`r=(1,...,1)/sqrt(m)`,                                          (6.1)

and choose a flat Walsh vector `v` with entries `+/-1/sqrt(m)` and `v perpendicular r`. Put

`D=t vv^T`.                                                      (6.2)

The anchored overlap-two packet is independent of `t`, while `q=1/m`. But the new disjoint-cross currency sees the curvature exactly. A direct calculation gives

`delta_k^2=t^2 (m-2)/[m(m-1)]`,
`Xi_k=t^2(m-2)/m^2`,                                            (6.3)

and therefore

`boxed: Xi=t^2 (m-2)/m.`                                        (6.4)

The exact distance from `D` to the aligned model is

`boxed:
 d_*=|t| sqrt((m-2)/(m-1)).`                                    (6.5)

Thus the curvature remains order one as the star becomes arbitrarily diffuse, and Theorem 5.1 produces one literal disjoint cut with

`boxed:
 e_2(A[H union S,T]A[H union S,T]^T)
 >= (4/27) t^2 (m-2)/m.`                                       (6.6)

At `m=64`, the source's diffuse condition is very strong:

`q=1/64<1/16`,
`Xi=(62/64)t^2=0.96875 t^2`,
`d_*=sqrt(62/63)|t|=0.9920317...|t|`,                           (6.7)

and some physical disjoint cut has second cross-volume at least

`boxed: 0.1435185185... t^2.`                                   (6.8)

So the exact family previously used to show that `Omega_(2,H)` cannot see `D` is **not** curvature-invisible once the correct disjoint-cross ledger is used. The remaining difficulty is analytic rather than geometric: spend an order-one rank-two crossing jointly with the nonzero rank-one pair core, without selecting a dimension-degrading tiny individual packet.

## 7. Designated account04/B09 theorem applied at an actual inequality

Use six physical coordinates: the hub pair `H={h1,h2}` and four leaves. Set

`B=A[H,H]=[[1,1],[1,1]]`,
`g=(1,-1)`,
`r=(1,1,1,1)`,                                                  (7.1)

and

`D = [[0,0,1,0],
      [0,0,0,1],
      [1,0,0,0],
      [0,1,0,0]].`                                               (7.2)

This is an exact rank-one physical pair and rank-one pair-to-leaf star with genuinely nonaligned leaf curvature. The full symmetric matrix has eigenvalues

`{-2.372281323269,-1,-1,1,2,3.372281323269}`,                   (7.3)

so it satisfies the owner's spectral target. The new currency is

`Xi=16`,
`q=1/4`,
`d_*=sqrt(8/3)=1.632993161855...`,                               (7.4)

with optimal aligned coefficient `lambda=1/3`.

More importantly, the literal disjoint physical row/column triple

rows `{h1, leaf1, leaf2}`,
columns `{h2, leaf3, leaf4}`

has cross matrix

`K=[[1,1,1],
    [-1,1,0],
    [-1,0,1]]`,                                                  (7.5)

so

`det K=3`.                                                       (7.6)

The completed **account04/B09** theorem therefore gives the actual target inequality

`boxed:
 ||p_Q||_infinity <= 3*3^(-1/3)=3^(2/3)
 =2.080083823052...`,                                            (7.7)

and

`boxed:
 P{Q in J} <= 3^(2/3)|J|`                                       (7.8)

for every interval `J`, with a **continuous density**. This is a direct O(interval length) payment on a nonaligned-curvature member of the exact collar, not a histogram or asymptotic heuristic.

## 8. Deterministic checks

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory execute 100 seeded random tests. They verify:

- the local identity (3.1), maximum relative error `2.561e-15`;
- both stability inequalities in (4.1), with no violation;
- by exhaustive leaf partitions for dimensions 5 through 9, `max Z/Xi >=4/27`; the smallest observed ratio was `0.292894865616`, above the required `0.148148148148`;
- the exact aligned regression `D=1.7 rr^T+diagonal` gives `Xi=9.646e-31` and `d_*=5.608e-16` numerically;
- the six-coordinate stress spectrum, `Xi=16`, `d_*=sqrt(8/3)`, `det K=3`, and the partner constant `2.080083823052`.

The computation is a regression check, not a proof; Sections 3-5 are the proofs.

## 9. What is and is not closed

The newest account01/B09 singular collar can now be sharpened as follows at overlap scale `Omega_(2,H)>=1/4`:

1. **Concentrated star `q>=1/16`:** already paid by the physical-principal-triple theorem in the source report, with arbitrary `D`.
2. **Diffuse star `q<1/16`, nonaligned leaf curvature:** Theorems 4.1 and 5.1 force a dimension-free original-coordinate disjoint second cross-volume, quantitatively (5.5). The stress family (6.1)-(6.2) has this currency at order `t^2` even though the anchored overlap ledger is exactly blind to `t`.
3. **Diffuse star, exactly aligned curvature `D=lambda rr^T+diagonal`:** the leaf geometry collapses to one aligned square plus physical diagonal phases. The zero-curvature subcase is already paid by account02/B09 r15, but the full aligned-square-plus-diagonal rough-law endpoint is not proved here.

A positive `e_2` crossing is **not** by itself a universal density theorem: the crossing can have exact rank two. It cannot be fed into the account04/B09 rank-three theorem unless a genuine rank-three physical subcut is present. Likewise, a small value of `d_*` cannot be dropped as a small random quadratic error because the admissible inputs have no moments.

The first unpaid B09 implication is therefore

`QFORM-SINGULARPAIR-DIFFUSESTAR-E2-PLUS-CORE-RECEIVER-v1`:

> In the exact rank-one physical-pair / diffuse rank-one-star branch, combine the compiled original-coordinate rank-two cross volume from Theorem 5.1 with the nonzero rank-one pair-core square to obtain a universal O(|J|) estimate before selecting a tiny physical minor; alternatively show that failure of such a grouped receiver forces the exact aligned model `D=lambda rr^T+diagonal` and pay that model while retaining all diagonal rough phases.

This is narrower than the previous generic “arbitrary same-leaf curvature” debt. Full unrestricted QFORM remains **OPEN**. Full-target continuity remains **OPEN**; continuity is proved only in paid branches such as Section 7. No full-target counterexample was found.

## 10. Source and execution record


Repository transport and mathematical source use were verified. Separate native learned-memory receiver ingestion was not available/verified, so execution remains `WITHOUT_VERIFIED_BRAIN` and `full_brain_connected=false`.

No task identity, schedule, cadence, enabled/paused state, email, push notification, public release, permission, paid model/API/Codex call, or cross-account authentication state was changed. Notification controls were not exposed through the repository connector and were not guessed.
