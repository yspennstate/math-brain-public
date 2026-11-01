# fleet02/B20 — spectral-window compiler for the remaining no-pivot problem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T123255Z-fleet02-B20-QFORM-auto11`  
Status: **ESSENTIAL_STEP_APPLIED / N3-LOWLEVERAGE-DEBT-REMOVED / SPECTRALWINDOW-OR-PHYSICALPAIR-OR-THREEBANK / PARTNER-R31-EXACTR3-AMPLIFIED / FULL-QFORM-OPEN**

## 1. Exact target and source discipline

The target remains: for every finite `n`, every independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has an essentially bounded density with one universal finite bound, or give a valid counterexample. No moment, support, log-concavity, diagonal-basis, or post-rotation-independence hypothesis is added. Continuity is separate.

The top-level reduction used below is the source-backed no-pivot equivalence in `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md` at `math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`: for **any fixed** `tau in (0,1]`, it is enough to prove a universal density bound on the class

`N3(tau): s_3(A)>=1, |A_ii|<tau, |det A[{i,j},{i,j}]|<tau for every i!=j`.

The auxiliary Gaussian variables in that reduction are only a proof device and do not impose a Gaussian assumption on the original inputs.

I choose throughout

`tau = 2^(-11) = 1/2048`.

This smaller fixed threshold is deliberate. It converts failure of the spectral-window diffuse gate into a quantitatively useful original-coordinate star while retaining the no-pivot reduction.

## 2. Completed inputs used at equation level

### 2.1 Spectral-window ridge payment

The complete supporting theorem `QFORM-SPECTRAL-WINDOW-DENSITY-v1` in `math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7` says: if `P` is the deterministic spectral projection onto **all** eigenspaces of `A` with `|lambda|>=1/64` and

`max_i P_ii <= 1/32`,

then, with arbitrary smaller-spectrum tails,

`||p_Q||_infinity <= 288 sqrt(3e)/13 = 63.2640518777... <64`.        (2.1)

This theorem acts only on deterministic matrix geometry; no projected random coordinates are declared independent. Its own independent review remains pending, as recorded by its source.

### 2.2 Determinant-only physical-pair payment

The same no-pivot synthesis proves that if an **original physical** indefinite `2x2` principal block `B` has `D=|det B|` and `s_3(A)>=s`, then

`||p_Q||_infinity <= D^(-1/2)[9.2+log_+(10000 sqrt(D)/s)]`.     (2.2)

No lower bound on `sigma_min(B)` is needed.

### 2.3 Required pinned interactive D5 payment

From the required record `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`, if a physical cross block `M=A[I,J]` on disjoint original-coordinate banks has

`Z5=e_5(M^T M)>=1/1024`,

then

`||p_Q||_infinity <=5 sqrt(2e) Z5^(-1/10) <=10 sqrt(2e)<23.317`. (2.3)

The self-blocks and outside couplings are arbitrary. Hence every survivor below may additionally be assumed to satisfy `e_5(A[I,J]^T A[I,J])<1/1024` for every disjoint physical cut on which D5 is invoked.

## 3. New theorem: spectral window or physical pair or three original star banks

### Theorem `QFORM-N3-SPECTRALWINDOW-OR-THREEBANK-v1`

Let `A in N3(tau)` with `tau=1/2048`. Put

`P = 1_{ {|A|>=1/64} }`,

the spectral projection onto the full `1/64` spectral window. Then one of the following holds.

1. **Diffuse-window payment:** `max_i P_ii<=1/32`, and (2.1) gives `||p_Q||_infinity<64`.

2. **Physical-pair payment:** there are original coordinates `h!=j` with

   `A_hj^2 >= 2 tau^2`,

   the physical pair is indefinite with `|det A[{h,j},{h,j}]|>tau^2`, and therefore

   `||p_Q||_infinity < C_pair`,

   where

   `C_pair = tau^(-1)[9.2+log(10000 tau)]`
   `       = 22089.1573982...`.                                  (3.1)

3. **Three-bank star:** there is an original coordinate `h` and three pairwise disjoint sets of original leaves `J_1,J_2,J_3 subset {1,...,n}\{h}` such that

   `sum_{j in J_k} A_hj^2 >= 8 tau^2 = 1/524288`,  `k=1,2,3`.    (3.2)

No change of random coordinates occurs in any branch.

### Proof

If `max_i P_ii<=1/32`, branch 1 is exactly (2.1). Otherwise choose an original physical coordinate `h` with

`P_hh>1/32`.                                                     (3.3)

By spectral calculus,

`A^2 >= (1/64)^2 P = P/4096`

as positive-semidefinite matrices. Therefore

`(A^2)_hh > 1/(4096*32)=1/131072=32 tau^2`.                     (3.4)

Because `A in N3(tau)`, `|A_hh|<tau`. Hence the physical off-diagonal star energy satisfies

`S_h := sum_{j!=h} A_hj^2`
`     = (A^2)_hh-A_hh^2`
`     >32 tau^2-tau^2`
`     =31 tau^2`.                                               (3.5)

If some leaf satisfies `A_hj^2>=2 tau^2`, then, writing `a=A_hh`, `c=A_jj`, `b=A_hj`,

`|ac|<tau^2<b^2`,

so the physical pair determinant is negative and

`D=|ac-b^2|>=b^2-|ac|>tau^2`.                                  (3.6)

Apply (2.2) with `s=1`. The right-hand side there is decreasing as a function of the determinant lower bound, so `D>tau^2` gives (3.1). This is branch 2.

It remains to assume

`A_hj^2<2 tau^2` for every `j!=h`.                              (3.7)

Greedily accumulate leaves into `J_1` until its energy first reaches `8 tau^2`. Because every atom is below `2 tau^2`, its final energy is below `10 tau^2`. Repeat for `J_2`; again its energy is below `10 tau^2`. By (3.5), after removing those two banks the remaining star energy is strictly larger than

`31 tau^2-10 tau^2-10 tau^2=11 tau^2`,

so a third disjoint bank can be accumulated to energy at least `8 tau^2`. This proves (3.2). QED.

## 4. A second deterministic resource survives every three-bank state

### Lemma `QFORM-HUB-REMOVAL-LEAF-NORM-v1`

For any symmetric `A` with `s_3(A)>=1` and any physical hub `h`, let `B=A[h^c,h^c]`. Then

`||B||_op >=1`.                                                  (4.1)

Proof. Let `R` be the matrix obtained from `A` by keeping only the physical row and column `h` and setting the complementary principal block to zero. The range of `R` is contained in the span of `e_h` and the leaf star vector, hence `rank(R)<=2`. Since

`A-R = diag(0,B)`,

Eckart--Young for the third singular value gives

`1<=s_3(A)<=||A-R||_op=||B||_op`.

Thus the three-bank branch is not a pure star: it always carries an additional order-one leaf operator, even though that operator may be dense, indefinite, and badly aligned with the star banks. QED.

This is exactly the interface left open by the newest grouped-hub work: one hub plus general leaf curvature, rather than diagonal-plus-low-rank leaf curvature.

## 5. Product-valid scalar currencies on the three banks

Let `b^(k)=(A_hj)_{j in J_k}`. Then (3.2) says

`||b^(k)||_2 >= sqrt(8) tau`.                                   (5.1)

The source-valid Rogozin/Chasapis--Koenig--Tkocz half-Riesz transfer (`QFORM` fleet01/B18, theorem (2.1) in its report) gives, for each original bank,

`sup_s E |<b^(k),X_{J_k}>-s|^(-1/2)`
` <= K_* ||b^(k)||_2^(-1/2)`
` <= K_* 8^(-1/4) tau^(-1/2)`
` = 86.1462606341...`,                                         (5.2)

where `K_*=6^(1/4) Gamma(1/4)/sqrt(pi)=3.2014295649...`.

Because `J_1,J_2,J_3` are disjoint sets of original coordinates, these three scalar linear statistics are genuinely independent of one another. This does not promote any rotated vector of coordinates to an independent vector, and it does not say that the general leaf quadratic form is measurable with respect to only these three statistics.

## 6. Newest designated partner fleet03/B20 r31, consumed exactly

A fresh partner refresh after the initial discovery found the completed fleet03/B20 r31 handoff, canonical mathematics `math-open-problems@c6e058c3d4aa36e89ad433c1f4d41b6f82739bf`. Its theorem `QFORM-EXACTR3-18ANCHOR-DIFFUSE-OR-NEARCOLOOP-v1` states that for an exact-rank-three factorization

`A=R M R^T`, `R^T R=I_3`, `s_min(M)>=1`,

either

`||p_Q||_infinity <=192e<522`,                                  (6.1)

or there is a set `S` of at most 18 original physical coordinates and a spectral unit vector `v` with

`sum_{i in S}<r_i,v>^2>63/64`.                                  (6.2)

### Corollary `QFORM-R31-EXACTR3-STAR-AMPLIFICATION-v1`

Inside `N3(1/2048)`, every exact-rank-three state is either paid by (6.1), paid by the physical-pair branch (3.1), or has an original physical hub `h` and three disjoint original leaf banks `J_1,J_2,J_3` with the much stronger bounds

`sum_{j in J_k} A_hj^2 >=1/64`, `k=1,2,3`.                     (6.3)

Proof. If (6.2) holds, `|S|<=18`, so for some `h in S`,

`|<r_h,v>|^2 > (63/64)/18 = 7/128`.                            (6.4)

Because `s_min(M)>=1`,

`(A^2)_hh=||M r_h||^2>=||r_h||^2>=|<r_h,v>|^2>7/128`.           (6.5)

The no-pivot diagonal bound gives

`sum_{j!=h}A_hj^2 > 7/128-tau^2`.                               (6.6)

If an edge has square at least `2tau^2`, branch (3.1) pays. Otherwise every edge square is below `2tau^2`. Greedily fill `J_1` to energy `1/64`; its final energy is below `1/64+2tau^2`. Do the same for `J_2`. The remaining energy is strictly larger than

`7/128-tau^2-2(1/64+2tau^2)=3/128-5tau^2>1/64`,                (6.7)

so a third disjoint bank reaches `1/64`. This proves (6.3). QED.

This is a direct equation-level application of the newest partner expression. It makes the exact-rank-three part of the remaining star problem substantially more robust than the arbitrary-extra-spectrum part, without asserting independence after spectral rotation.

For comparison, r30's predecessor packet formula

`sum_{i in B_k}<r_i,e_k>^2>=453/4096`

still supplies, via the source-valid half-Riesz transfer, genuinely independent original-packet scalar statistics with half-Riesz cap `8K_*/453^(1/4)=5.55148777493...`; r31 is now the designated newest partner and supersedes r30 as the main closure input.

## 7. Strongest current conditional end-to-end graph

By the no-pivot equivalence, it suffices to pay `N3(1/2048)`. The new theorem exhausts that class as follows:

- spectral-window diffuse branch: paid by `<64`;
- one physical hub--leaf edge of square at least `2 tau^2`: paid by the determinant-only physical-pair theorem with `<22090`;
- otherwise: one original physical hub, three disjoint original leaf banks each with star energy at least `1/524288`, plus a complementary physical leaf block `B` with `||B||>=1`.

On every branch, any physical cross block with fifth volume at least `1/1024` is separately paid by (2.3). Existing grouped-hub/Pluecker, ridge, physical-pair, support-defect, compatibility-currency, grouped-square and hyperbolic receivers may further discharge structured subcases of the last branch.

In the exact-rank-three subcase, r31 further says that either the density is `<522` or the surviving three star banks can be taken at energy `1/64` each by (6.3).

Therefore the previous first global debt `QFORM-N3-LOWLEVERAGE-EXTRASPECTRUM-PAYMENT-v1` is no longer needed as a separate case: low leverage at the `|lambda|>=1` projection does not block this compiler because the compiler uses the larger deterministic `|lambda|>=1/64` spectral window and a smaller fixed no-pivot threshold.

## 8. First unpaid universal implication

`QFORM-N3-THREEBANK-GENERAL-LEAF-PAYMENT-v1`:

> Let `tau=1/2048`. Let `A` be symmetric with `s_3(A)>=1`, `|A_ii|<tau`, and every physical `2x2` principal determinant of magnitude `<tau`. Assume there is an original hub `h` and three disjoint original leaf banks `J_1,J_2,J_3` with
> 
> `sum_{j in J_k} A_hj^2 >= 8 tau^2` for `k=1,2,3`,
> 
> and let `B=A[h^c,h^c]`, so automatically `||B||>=1`. After all fixed-scale D5 and physical-pair exits fail, prove a universal linear interval bound
> 
> `P(X^TAX in I)<=C |I|`,
> 
> uniformly over all independent cap-one input laws and all remaining same-side/ambient couplings; or reduce this state source-preservingly to an already-paid grouped-square, mixed-hub, ridge/volume, compatibility-currency or bounded-core receiver.

For exact rank three, the same implication may be strengthened by replacing `8tau^2` with `1/64` in each bank, unless r31 has already paid the state by `<522`.

The exact quantitative replacement supplied here is the three-bank energy plus (4.1) plus the independent bankwise half-Riesz currencies (5.2). A bare one-hub estimate alone is not enough: it gives only the borderline `|t|^-1` Fourier decay, while the general leaf operator prevents direct use of the diagonal-plus-low-rank Theorem H factorization. This is why the next mechanism must spend the leaf operator collectively rather than delete it or select a vanishing local minor.

## 9. Corrections and status

Preserved throughout:

- no uniform pointwise quadratic-phase decay;
- no unrestricted worst-fiber supremum;
- no post-rotation/projected-coordinate independence;
- no arbitrary-joint three-dimensional coarea lemma;
- no deletion of a small quadratic matrix on unbounded inputs;
- no inference from aggregate Pluecker/volume mass to one universally good reciprocal minor.

This report does **not** prove the full QFORM conjecture and makes no full-target continuity claim. A full candidate still requires every target quantifier and two independent end-to-end reviews.
