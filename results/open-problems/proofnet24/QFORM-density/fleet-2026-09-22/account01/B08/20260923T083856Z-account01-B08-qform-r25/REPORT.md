SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T08:38:56Z.
attacking: the k=1 self-dual diffuse survivor — convert the robust two-cross geometry into a uniform half-Riesz / square-root small-ball estimate, and replace bilateral hubs by fixed-anchor aggregate two-volume without selecting a tiny minor.

# account01/B08 r25 — diffuse k=1 half-Riesz closure and anchored pair-volume geometry

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** diffuse eigenvector case  
**Run:** `20260923T083856Z-account01-B08-qform-r25`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_ANALYTIC-STRUCTURAL-THEOREM / DESIGNATED_PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains OPEN. Continuity is proved only on the previously completed L1-Fourier branches explicitly cited below; the new half-Riesz statements by themselves do **not** imply a bounded or continuous density.

## 1. Exact target and correction boundary

For every finite `n`, every independent real `X_i` with probability density `f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, the owner asks for a universal finite bound on the essential supremum of the density of `Q=X^TAX`, or a valid counterexample. No moment, support, log-concavity, iid, Gaussian, or independence-after-rotation hypothesis is available.

This run does not use law-uniform scalar van-der-Corput decay, arbitrary-joint 3D coarea, positive moments of worst conditional projection heights, one-good-minor extraction, or law-uniform continuity under small matrix perturbations. In particular, every matrix tail appearing below is kept algebraically.

## 2. Source-pinned inputs actually used

### 2.1 Self-dual diffuse spectral transfer

Previous account01/B08 theorem `QFORM-SELF-DUAL-REDUCING-PROJECTION-LADDER-v1`:

`yspennstate/math-open-problems@5d2f07b086dec22993a28780c0e98fd7aef4c464`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T053638Z-account01-B08-QFORM-auto11/REPORT.md`.

Let `E` be a three-dimensional reducing subspace of a symmetric matrix `A`, with every eigenvalue of `A|E` of modulus at least `L`, and let `P_E` be its orthogonal projection. Put

`mu=max_i (P_E)_{ii}<1/sqrt(6)`,

`alpha=1/2-sqrt(3/2) mu`, `rho=sqrt(alpha/(1-alpha))`,

`d=L rho^2/(1+rho)`.

Then there is an ORIGINAL-coordinate cut `I sqcup J` such that, for either child `K=I,J` and every `m=1,2,3`, either `A[K,K]` has at least `m` eigenvalues of modulus at least `d`, or the actual physical cross block `B=A[I,J]` has

`s_{4-m}(B)>d`.

At the basis-invariant high-spectral-projector condition `max_i (P_L)_{ii}<=1/3`, one may choose the three-dimensional reducing subspace inside `Ran(P_L)` and

`rho=sqrt(3)-sqrt(2)`,

`tau:=d/L=(sqrt(3)-sqrt(2))^2/(1+sqrt(3)-sqrt(2))`

`=0.0766562902983029...`.

### 2.2 Unconditional pair-volume half-Riesz theorem

Account01/B01 theorem, canonical source

`yspennstate/math-open-problems@1f3af9dc58afb9e902b972466d6da01cece89734`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T030821Z-account01-B01-qform-auto11/REPORT.md`.

For any ORIGINAL-coordinate physical cross block `M` in an otherwise arbitrary quadratic form `R`, retaining arbitrary same-bank quadratic terms and outside couplings, put

`E_2(M)=e_2(M^T M)=sum_{|S|=|T|=2} det(M_{S,T})^2`.

Then

`H_{1/2}(R):=sup_s E |R-s|^{-1/2}`

`<= C_E2 E_2(M)^(-1/8)`,

where

`C_E2=12*2^(5/6)*e^(5/24)=26.3340461807597...`.

The same report proves the fixed-star version. If a fixed physical row `i` has incident two-volume

`H_i=sum_{k!=i} ||r_i wedge r_k||^2`,

then

`H_{1/2}(R)<=C_star H_i^(-1/8)`,

`C_star=12*2^(17/24)*e^(5/24)=24.1484268216952...`.

These are fractional-potential estimates, not density bounds.

### 2.3 Designated partner account02/B08 r23

Newest completed designated-partner result used here:

`yspennstate/math-open-problems@ab1940d32f6f758e7a355c128916a523e5519537`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T064247Z-account02-B08-qform-diffuse-r23/REPORT.md`.

Its theorem `QFORM-DIFFUSE-POST-2/3-CORE-ROUTER-v1` applies when a physical cross block satisfies

`Z_3=e_3(B^T B)>=zeta^6`.

It yields either a full-ambient continuous bound `<987/zeta`, or a physical row/column star `>zeta`, or one of the explicit product-preserving S/R1/E2/BICORE core currencies stated in that report. No small tail is deleted.

## 3. New exact structural identity: anchored pair-volume lower bound

Let `B` be any real `m x n` matrix with rows `r_1,...,r_m`. For a fixed row `i`, define

`H_i(B):=sum_{k!=i} sum_{a<b} det B[{i,k},{a,b}]^2`

`=sum_{k!=i} ||r_i wedge r_k||^2`.

Let

`T_1(B):=sum_{nu>=2} s_nu(B)^2`

be the squared Frobenius distance from `B` to the rank-one matrices.

### Theorem 3.1 — `QFORM-ANCHOR-PAIRVOLUME-LOWER-v1`

For every row `i`,

`boxed: H_i(B) >= ||r_i||_2^2 T_1(B).`                     (3.1)

The transpose statement holds for every physical column `j`:

`boxed: K_j(B) >= ||B[:,j]||_2^2 T_1(B),`                 (3.2)

where `K_j` is the total squared two-minor volume incident to column `j`.

In particular, if `s_2(B)>=d` and a row star satisfies `||r_i||>=h`, then

`H_i(B)>=h^2 d^2`;                                           (3.3)

and the same holds for columns.

#### Proof

If `r_i=0` there is nothing to prove. Otherwise set

`u=r_i/||r_i||`.

For every other row `r_k`, Lagrange's identity gives

`||r_i wedge r_k||^2`
`=||r_i||^2 (||r_k||^2-<r_k,u>^2)`
`=||r_i||^2 ||r_k(I-uu^T)||^2`.

The row `i` itself is killed by `I-uu^T`, so summing over all `k` gives the exact identity

`H_i(B)=||r_i||^2 ||B(I-uu^T)||_F^2`.                       (3.4)

But

`B-B(I-uu^T)=(Bu)u^T`

has rank at most one. Therefore Eckart-Young implies

`||B(I-uu^T)||_F^2 >= dist_F(B,{rank<=1})^2`
`=sum_{nu>=2}s_nu(B)^2=T_1(B)`.

This is (3.1). Apply the same argument to `B^T` for (3.2). QED.

This identity is useful precisely because it never selects one physical `2x2` minor: a high physical star plus a second singular direction forces a **complete fixed-anchor aggregate packet**.

## 4. New analytic estimate for the self-dual k=1 diffuse branch

Use the self-dual physical cut from Section 2.1. Let `k` be the smaller number of child eigenvalues of modulus at least `d`. Consider the branch `k=1`.

For the child attaining this minimum, the `m=2` alternative in the self-dual theorem fails. Hence the same actual physical cross block satisfies

`s_2(B)>d`.                                                    (4.1)

Therefore

`E_2(B)>=s_1(B)^2 s_2(B)^2>d^4`.                              (4.2)

Apply the unconditional B01 theorem from Section 2.2 directly to the **full ambient quadratic form**, with all same-bank curvature, all remaining cross singular directions and all outside couplings retained.

### Theorem 4.1 — `QFORM-DIFFUSE-K1-HALF-RIESZ-v1`

On the self-dual `k=1` branch,

`boxed: sup_s E|Q-s|^(-1/2) <= C_E2 d^(-1/2).`                (4.3)

Consequently, for every `epsilon>0`,

`boxed: sup_s P(|Q-s|<=epsilon)`
`       <= C_E2 sqrt(epsilon/d).`                             (4.4)

Indeed, on the event `|Q-s|<=epsilon`, one has

`|Q-s|^(-1/2)>=epsilon^(-1/2)`,

and (4.4) follows from (4.3).

At the basis-invariant diffuse threshold `max_i(P_L)_{ii}<=1/3`, the exact self-dual scale obeys `d>=tau L`, so

`boxed: sup_s E|Q-s|^(-1/2) <95.114 L^(-1/2),`                (4.5)

and

`boxed: sup_s P(|Q-s|<=epsilon)<95.114 sqrt(epsilon/L).`      (4.6)

For the owner's target normalization `L=1`, this is a completely dimension-free square-root small-ball estimate on the entire `k=1` diffuse branch, including the genuine rank-two tube and arbitrary nonzero higher singular tail.

This is **not** yet the required linear-in-`epsilon` small-ball estimate. An unbounded density with a mild singularity may still have finite `H_{1/2}`. Thus (4.3)-(4.6) are a genuine analytic advance, not a claim that the target is solved.

## 5. Bilateral hubs become bilateral anchored pair-volume packets

The previous account01/B08 two-cross router left a branch in which

`s_2(B)>=d`,

and there are a physical row `i` and a physical column `j` with

`||B[i,*]||>d/sqrt(2)`,

`||B[*,j]||>d/sqrt(2)`.

Theorem 3.1 immediately upgrades this from two large one-dimensional stars to two fixed-anchor exterior currencies:

`boxed: H_i(B)>d^4/2,`                                       (5.1)

`boxed: K_j(B)>d^4/2.`                                       (5.2)

No bound on the number of physical leaves appears.

Applying the fixed-star B01 theorem in either orientation gives again

`H_{1/2}(Q)`
`< C_star (d^4/2)^(-1/8)`
`=2^(1/8) C_star d^(-1/2)`
`<26.335 d^(-1/2)`.                                           (5.3)

More importantly for subsequent localized-coordinate routing, (5.1)-(5.2) preserve the **location** of the aggregate two-volume at both physical anchors, rather than forgetting it in the total `E_2(B)`.

There is an exact internal dichotomy at each anchor. Normalize the row packet by

`q_k=||r_i wedge r_k||^2/H_i`.

If some `q_k>1/2`, then a fixed physical row pair has

`||r_i wedge r_k||^2>H_i/2>d^4/4`.                            (5.4)

If no such partner exists, all partner marginals are at most one half and the B01 mixed-order star argument spends the full packet without selecting a small minor. Thus the hub branch is now compatible with both localized-pair and diffuse-star receivers.

## 6. Actual application of the designated account02/B08 result

Return to the robust-third subbranch of the preceding B08 router and set

`zeta=s_3(B)`.

There `s_3(B)>d/120`, and hence

`Z_3=e_3(B^T B)`
`>=s_1(B)^2 s_2(B)^2 s_3(B)^2`
`>=s_3(B)^6=zeta^6`.                                          (6.1)

Therefore the designated account02/B08 r23 theorem applies at the **actual** scale `zeta`.

If its continuous branch occurs, then

`||p_Q||_infinity<987/zeta<118440/d`.                          (6.2)

If its physical-star exit occurs, say a row has norm `>zeta`, then because `s_2(B)>=s_3(B)=zeta`, Theorem 3.1 gives the actual inequality

`H_i(B)>zeta^4`.                                               (6.3)

The fixed-star half-Riesz theorem therefore yields

`H_{1/2}(Q)<C_star zeta^(-1/2)`
`<C_star sqrt(120/d)`
`<264.533 d^(-1/2)`.                                          (6.4)

The identical conclusion holds for a column-star exit by transposition. Thus the designated partner's former bare star exit is now converted into a quantitative aggregate two-volume and a full-ambient fractional-potential estimate. Its S/R1/E2/BICORE core currencies remain exactly as in the source report when those branches occur.

At the worst self-dual diffuse scale `d>=tau L`, (6.4) becomes

`H_{1/2}(Q)<955.445 L^(-1/2)`.                                (6.5)

This partner application is equation-level: (6.1) verifies its hypothesis and (6.3)-(6.4) consume one of its literal output branches.

## 7. A target-valid obstruction to the naive two-hub leaf-rank receiver

It is tempting to replace the bilateral anchored packets by a two-hub rank-two slope matrix after regrouping coordinates. Arbitrary same-bank leakage makes that false even inside the target.

Let

`A_4 = [[0,1,0,1],`
`       [1,0,1,0],`
`       [0,1,0,1],`
`       [1,0,1,0]]`

and set

`A=A_4 direct_sum [1]`.

The spectrum is

`{-2,0,0,1,2}`,

so this is a valid three-large-eigenvalue target matrix.

Take the physical cut

`I={1,2}`, `J={3,4}`.

Then

`B=A[I,J]=[[0,1],[1,0]]`,

so `s_2(B)=1`, row `1` has star norm one, and column `3` has star norm one. The anchored two-volume packets are both exactly one.

Now regroup the two hubs as `{1,3}` and the two leaves as `{2,4}`. Their hub-to-leaf coefficient matrix is

`[[1,1],[1,1]]`,

which has rank one, not two. Thus

> `s_2(B)` plus bilateral physical stars does **not** force a rank-two two-hub leaf-slope block once arbitrary same-bank leakage is retained.

This is not a counterexample to QFORM; it refutes only that proposed intermediate receiver. The aggregate anchored pair-volume statements (5.1)-(5.2) survive exactly and are therefore the safer currency.

## 8. What changed and what remains unpaid

Before this run, the `k=1` diffuse state was split among a genuine rank-two tube, collective-tail payment, bilateral hubs, robust-third payment, and the partner core tree. The new results do two things that hold uniformly across those internal subdivisions:

1. **Every self-dual k=1 survivor now carries a full-ambient dimension-free fractional estimate**

   `H_{1/2}(Q)<=26.335 d^(-1/2)`,

   equivalently the square-root small-ball bound (4.4), with no moments and no tail deletion.

2. **Every bilateral-hub survivor now carries two fixed physical anchored two-volume packets** of size `>d^4/2`, one in each orientation. A hub is therefore no longer merely a large row/column norm.

The first genuinely unpaid implication is now

`QFORM-K1-HALF-RIESZ-TO-DENSITY-v1`:

> combine the diffuse child's remaining one-direction curvature with the full-ambient half-Riesz / anchored-pair-volume currency so as to improve `P(|Q-s|<=epsilon)=O(sqrt(epsilon))` to `O(epsilon)` while preserving ORIGINAL-coordinate product provenance and arbitrary same-bank leakage.

The stress matrix in Section 7 shows that one cannot do this merely by declaring the two hubs to form a rank-two leaf-slope block. A viable next receiver must use the aggregate incident two-volume itself (or a genuine physical pivot/curved pair when one is actually present). The self-dual `k=2` and bilateral-retained-three `k=3` branches remain parallel debts.

## 9. Regularity status

- The new Theorems 3.1 and 4.1 prove structural and fractional-potential/small-ball estimates.
- They do **not** establish a density or continuity by themselves.
- The designated partner branch (6.2) is an existing L1-Fourier branch and therefore has a continuous `C_0` density.
- Full QFORM density boundedness and global continuity remain OPEN.

## 10. Finite checks

`CHECKS.py` in this run directory verifies the exact anchored identity on deterministic random finite matrices, checks the lower bound against singular values, confirms the target-valid stress spectrum and rank-one regrouped hub/leaf matrix, and recomputes all displayed constants. These computations are sanity checks only; the proof is the algebra above.
