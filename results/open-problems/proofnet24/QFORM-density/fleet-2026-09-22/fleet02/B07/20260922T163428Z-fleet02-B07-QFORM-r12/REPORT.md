# fleet02/B07 — q=0 overlap-stratum payment by ridge leverage or a four-coordinate determinant core

**Run:** `20260922T163428Z-fleet02-B07-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`; later owner control observed at revision `2026-09-22.7`  
**Assignment:** Coordinate minor selection / complementary constructions and source-valid counterexamples  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and the first unpaid implication

The full target remains open. For arbitrary dimension, independent real coordinates `X_i` with probability densities bounded by one, and an arbitrary real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a density with one universal finite `L^infinity` bound, or give a valid target-level counterexample. No moments, bounded support, sign restriction, Gaussianity, or independence after spectral rotation may be introduced.

The incoming fleet02/B07 theorem was `QFORM-EXTERIOR-PACKET-ENERGY-TRANSFER-v1`, source

`yspennstate/math-open-problems@92802adbc9d6fd13ba3be5ab3abea17fa8c49e19`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T160205Z-fleet02-B07-QFORM-r11/REPORT.md`.

It says that if three selected large eigenvectors have Pluecker packet mass `m` on a family `R` of physical row triples, then the full matrix, including arbitrary complementary spectrum, has an overlap stratum

`E_q(R)=sum_{I in R} sum_{J: |I cap J|=q} det(A_{I,J})^2`

of size at least `m/4`, for some `q in {0,1,2,3}`. Thus arbitrary extra spectrum can redistribute the determinant resource but cannot erase it. In the generic B07 collar `m>=1/8`, so some stratum has `E_q>=1/32`.

The first unpaid implication was therefore:

`QFORM-OVERLAP-STRATUM-ANALYTIC-PAYMENT-v1` — turn one aggregate squared-minor resource `E_q(R)>=c` into a dimension-free density/small-ball bound without selecting a single potentially tiny physical minor and while preserving the original-coordinate product law.

This run pays the entire **disjoint `q=0` overlap stratum up to a bounded four-coordinate determinant core**. The result is dimension-free and retains arbitrary self blocks, outside couplings, and additional spectrum.

## 2. Dependencies actually read and used

### 2.1 Ridge density theorem

The analytic input is the complete source `QFORM-RIDGE-DENSITY-v1`,

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For a cross block `B=A[L,R]` between disjoint sets of **original coordinates**, put for `gamma>0`

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`,
`theta_gamma=tr K_gamma`,
`D_gamma=det(I+BB^T/gamma^2)`.

If `1<=q<=2`, `max_i (K_gamma)_ii<=q/2`, and `theta_gamma>2q`, then the full quadratic form has a continuous `C_0` density and

`||p_Q||_infinity
 <= e/(sqrt(2q) gamma) * theta_gamma/(theta_gamma-2q)
    * D_gamma^(-1/(2 theta_gamma)).`                         (2.1)

The theorem conditions only on original coordinates and explicitly allows arbitrary self blocks and outside couplings. This is why it is compatible with the present full-spectrum overlap resource.

### 2.2 Designated partner fleet03/B07

The completed designated partner theorem actually applied is

`QFORM-NESTED-HEAVY-DISJOINT-BANK-COLLAR-v1`,

`yspennstate/math-open-problems@494c999fc67d230fff7e2079b1867216253b35bc`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T154026Z-fleet03-B07-qform-r11/REPORT.md`.

Its nested-heavy exact-rank-three packet has fixed-pair Pluecker mass `ch>1/4`; in its `eta=1/16` two-coloop alternative it has `ch>3/4`. The preceding B07 exterior-transfer theorem promotes these to an actual full-`A` overlap stratum of size respectively `>1/16` or `>3/16`. Section 7 below inserts these exact constants into the new q=0 theorem.

### 2.3 Correction respected

I also re-read the source of fleet02/B06's correction `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1`,

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

It forbids identifying same-sign Pluecker support with useful physical pair-pivot support. The argument below never performs that identification. It averages the **actual full-matrix disjoint minors** into a cross block, then keeps their complete determinant weight through a ridge determinantal law.

## 3. First averaging step: a q=0 packet produces a cross block with large third determinant coefficient

Assume for a family `R` of physical row triples that

`E_0(R)
 = sum_{I in R} sum_{J: I cap J=empty, |J|=3} det(A_{I,J})^2
 >= c >0.`                                                        (3.1)

Choose a random ordered bipartition `(L,Rc)` of all physical coordinates by independently sending each coordinate to `L` or `Rc` with probability `1/2`. Let

`B=A[L,Rc]`                                                         (3.2)

be the resulting original-coordinate cross block. Write

`e_3(BB^T)`

for the third elementary symmetric polynomial of the eigenvalues of `BB^T`. By principal-minor Cauchy--Binet,

`e_3(BB^T)
 = sum_{I subset L, |I|=3} det((BB^T)_{I,I})
 = sum_{I subset L, |I|=3} sum_{J subset Rc, |J|=3} det(B_{I,J})^2.`  (3.3)

For each ordered disjoint pair `(I,J)` in (3.1), the event `I subset L`, `J subset Rc` has probability exactly `2^(-6)=1/64`. All summands are nonnegative. Therefore

`E_{partition} e_3(BB^T) >= E_0(R)/64 >= c/64.`                      (3.4)

Consequently there exists a deterministic original-coordinate bipartition satisfying

`boxed( e_3(BB^T) >= c/64. )`                                       (3.5)

This is already the first required dimension-free selection. No single `3x3` minor was extracted: the entire squared-minor packet is retained in `e_3`.

## 4. Ridge normalization at effective dimension three

Fix a cross block `B` satisfying (3.5), and let `r=rank(B)>=3`. Denote the nonzero eigenvalues of `BB^T` by `s_1,...,s_r>0`. Then

`theta_gamma = sum_j s_j/(gamma^2+s_j)`                              (4.1)

is continuous and strictly decreasing in `gamma>0`, with limits `r` at zero and `0` at infinity.

If `r>3`, there is a unique `gamma_*>0` such that

`theta_{gamma_*}=3.`                                                 (4.2)

If `r=3`, use the limiting scale `gamma downarrow0`; then `K_gamma` converges to the orthogonal projection `P_B` onto the row range of `B`, and `theta_gamma->3`.

The determinant expansion is

`D_gamma=det(I+BB^T/gamma^2)
       = sum_{k>=0} gamma^(-2k) e_k(BB^T)
       >= gamma^(-6) e_3(BB^T).`                                     (4.3)

This inequality is the bridge that lets the ridge theorem spend an aggregate third-order determinant coefficient rather than one singular value or one minor.

## 5. Main theorem: q=0 ridge payment or a four-coordinate determinant core

### Theorem 5.1 — `QFORM-Q0-RIDGE-FOUR-HEAVY-DPP-v1`

Assume (3.1). Then there is an original-coordinate bipartition with cross block `B` satisfying (3.5) and one of the following alternatives.

**(D) Diffuse ridge payment.** At the effective-dimension-three scale, all row ridge leverages are at most `3/5`. Then the **full** quadratic form has a continuous density and

`boxed(
 ||p_Q||_infinity
 <= 10 e sqrt(5/12) c^(-1/6).
)`                                                                   (5.1)

**(H) Four-heavy determinant core.** At that scale some row ridge leverage exceeds `3/5`. If

`H={i:(K_*)_ii>3/5}`                                                 (5.2)

(with `K_*=P_B` in the rank-three limit), then

`boxed( 1<=|H|<=4. )`                                                (5.3)

Moreover, the ridge leverage `(K_*)_ii` is exactly the inclusion probability of physical coordinate `i` in a determinant-weighted law on row subsets whose expected cardinality is three. Thus every `i in H` belongs to more than `3/5` of the total regularized determinant weight. In the rank-three limit this law becomes ordinary third-volume sampling from the cross block.

So a q=0 overlap packet cannot remain both analytically unpaid and spread over arbitrarily many physical rows: failure of the ridge payment compresses the determinant obstruction into at most four original coordinates.

### Proof of alternative (D)

First suppose `r>3` and use the exact scale (4.2). Apply the ridge theorem (2.1) with

`q=6/5`, so `q/2=3/5` and `2q=12/5<3=theta_*`.                      (5.4)

The hypothesis of (D) is exactly its coordinate-leverage condition. Since `theta_*=3`, (2.1) gives

`||p_Q||_infinity
 <= [e/(sqrt(12/5) gamma_*)] * [3/(3-12/5)] * D_*^(-1/6)
 = [5e/sqrt(12/5)] gamma_*^(-1) D_*^(-1/6).`                        (5.5)

By (4.3),

`gamma_*^(-1) D_*^(-1/6)
 <= e_3(BB^T)^(-1/6).`                                               (5.6)

Using (3.5),

`||p_Q||_infinity
 <= 5e sqrt(5/12) (c/64)^(-1/6)
 = 10e sqrt(5/12)c^(-1/6),`                                         (5.7)

because `64^(1/6)=2`. This proves (5.1) for `r>3`.

If `r=3`, assume the limiting projection satisfies `max_i(P_B)_ii<=3/5`. Since `0<=K_gamma<=P_B`, the leverage condition holds for every positive `gamma`; and for sufficiently small `gamma`, `theta_gamma>12/5`. Apply (2.1) and let `gamma downarrow0`. From (4.3),

`gamma^(-1)D_gamma^(-1/(2theta_gamma))
 <= e_3(BB^T)^(-1/(2theta_gamma))
    gamma^(-1+3/theta_gamma).`                                      (5.8)

As `gamma->0`, `theta_gamma=3+O(gamma^2)` and hence

`gamma^(-1+3/theta_gamma)->1`;                                      (5.9)

also `1/(2theta_gamma)->1/6` and `theta_gamma/(theta_gamma-12/5)->5`. Thus the same limit (5.5)-(5.7) follows. Since the ridge theorem gives a continuous `C_0` density for each sufficiently small `gamma` and the law is the same, the resulting density bound is valid for the rank-three case as well.

### Proof of alternative (H) and the determinant-weight interpretation

For positive `gamma`, put

`M_gamma=I+BB^T/gamma^2`, `D_gamma=det M_gamma`.                     (5.10)

Its principal-minor expansion and Cauchy--Binet give

`D_gamma
 = sum_{S subset L} gamma^(-2|S|) det((BB^T)_{S,S})`
` = sum_{S subset L} gamma^(-2|S|)
       sum_{T subset Rc, |T|=|S|} det(B_{S,T})^2.`                    (5.11)

Normalize these nonnegative weights to a probability law `nu_gamma` on row subsets `S`:

`nu_gamma(S)
 = D_gamma^(-1) gamma^(-2|S|) det((BB^T)_{S,S}).`                    (5.12)

For a physical row `i`, let `M_gamma^{(-i)}` denote the principal matrix with row and column `i` deleted. Jacobi's cofactor identity and

`K_gamma=I-M_gamma^(-1)`                                             (5.13)

give

`det M_gamma^{(-i)}/D_gamma=(M_gamma^(-1))_ii=1-(K_gamma)_ii.`        (5.14)

But the determinant on the left expands exactly as the part of (5.11) coming from subsets not containing `i`. Hence

`boxed( nu_gamma(i in S)=(K_gamma)_ii. )`                            (5.15)

Summing (5.15) over `i` gives

`E_{nu_gamma}|S|=tr K_gamma=theta_gamma.`                            (5.16)

At the effective-dimension-three scale, the expected cardinality is exactly three. Therefore the set

`H={i:(K_*)_ii>3/5}`

obeys

`(3/5)|H| < sum_{i in H}(K_*)_ii <=3`,                              (5.17)

so `|H|<5`, proving `|H|<=4`.

When `r=3` and `gamma->0`, the highest nonzero degree in (5.11) is three. After normalization all lower-degree terms vanish, and `nu_gamma` converges to the three-volume-sampling law

`nu_0(S)
 = det((BB^T)_{S,S})/e_3(BB^T),  |S|=3,`                            (5.18)

with

`det((BB^T)_{S,S})=sum_{|T|=3}det(B_{S,T})^2.`                       (5.19)

Thus (H) is literally a determinant-weighted physical-coordinate core, not an abstract spectral leverage statement. QED.

## 6. A sharper optional tier

The threshold `3/5` was chosen because it is the smallest clean threshold that forces the exceptional set down to four rows while keeping the ridge exponent integrable. There is also a stronger-constant but weaker structural tier: if `max_i K_ii<=1/2`, use `q=1` at `theta=3` to get

`||p_Q||_infinity
 <= (3e/sqrt(2)) e_3(BB^T)^(-1/6)
 <= 3 sqrt(2)e c^(-1/6).`                                           (6.1)

If this fails, rows with leverage `>1/2` number at most five. The `3/5` choice trades a larger universal constant for a four-coordinate residual core.

More generally, any threshold `alpha in [1/2,3/4)` can be paid by choosing `q=2alpha`, while rows with leverage `>alpha` have cardinality strictly smaller than `3/alpha`. The barrier `alpha=3/4` is exactly where `theta=3` meets the nonintegrable endpoint `theta=2q`; no endpoint density claim is made there.

## 7. Direct application of designated partner fleet03/B07

The partner's nested-heavy fixed-pair Pluecker packet has mass `ch>1/4`. Applying fleet02/B07's exterior-transfer theorem first gives some full-matrix overlap class with energy `>1/16`. Conditional on the winning class being `q=0`, Theorem 5.1 gives the following source-valid dichotomy:

* either the full quadratic form already has a continuous density with

  `||p_Q||_infinity
    < 10e sqrt(5/12) (1/16)^(-1/6)
    = 27.853227398120...`;                                           (7.1)

* or the corresponding full-matrix cross-volume determinant law has at most four physical rows of inclusion marginal `>3/5`.

In the partner's `eta=1/16` two-coloop alternative, `ch>3/4`, so the transferred winning overlap class has energy `>3/16`. If that class is `q=0`, the direct analytic bound improves to

`||p_Q||_infinity <23.192913897831...`                               (7.2)

unless the same four-heavy determinant core appears.

Likewise the generic preceding B07 packet `m>=1/8` gives `c=1/32`; on a q=0 winner the direct branch is

`||p_Q||_infinity <=31.264190677321...`                              (7.3)

or a four-heavy determinant core.

This is an actual application of the partner's quantitative packet, not a citation-only mention. No conclusion is drawn when its exterior-transfer winner is `q=1,2,3`; those remain separate debts.

## 8. Why the new result avoids the live counterexamples

1. It does **not** select the largest individual cross minor. The random partition keeps the whole q=0 sum and produces `e_3(BB^T)`.
2. It does **not** infer useful pivot support from selected-eigenspace Pluecker support. The input is already the actual full-matrix overlap energy produced by exterior transfer.
3. It does **not** require post-rotation independence. The selected `L,Rc` are sets of original coordinates, exactly the setting of the ridge theorem.
4. It does **not** assume small complementary spectrum. Every self block and all extra spectral directions are left inside the full conditional quadratic form handled by the ridge theorem.
5. It does **not** pay a reciprocal smallest singular value. The determinant coefficient `e_3` survives even if the cross block has many other singular values or is full rank.
6. The singleton-plus-two-banks obstruction to a universal rank-three cross cut is not contradicted: the theorem is conditional on the q=0 overlap packet. If the exterior resource sits in `q=1` or `q=2` instead, this theorem says nothing.

## 9. Exact diagnostic computation

`CHECK.py` and `CHECK_OUTPUT.txt` are committed beside this report. The checker uses only the Python standard library. It verifies two identities used in the proof.

First, on a symmetric integer `6x6` matrix and the family of all row triples, exact arithmetic gives

`E0=560`,
`sum_over_all_64_partitions e3(BB^T)=560`,
`average=35/4=E0/64`,

confirming the `2^-6` random-partition factor exactly.

Second, at `gamma=1` it checks the determinant-subset law for two diagonal cross-block fixtures. For `B=I_6`,

`theta=3`, `max K_ii=1/2`, `e3=20`, `D=64`.

For

`B=diag(2,2,2,1/2,1/2,1/2)`,

`theta=3`, `max K_ii=4/5`, exactly three coordinates are above the `3/5` threshold,

`e3=6545/64`, `D=15625/64`,

and the exact normalized determinant-subset marginals equal the ridge leverages with expected subset size three.

Terminal output:

`QFORM_Q0_RIDGE_DPP_CHECK_PASS`.

The checker is diagnostic; Sections 3-5 are the proof.

## 10. Conditional end-to-end route and next unpaid implication

A compact conditional route now reads as follows.

1. Three large eigenvectors supply Pluecker mass one.
2. The preceding B07 localization/packet machinery gives either an already paid diffuse/separable branch or a coordinate packet of mass at least `1/8`.
3. `QFORM-EXTERIOR-PACKET-ENERGY-TRANSFER-v1` sends this through arbitrary complementary spectrum to one actual overlap stratum `E_q>=1/32`.
4. **New in this run:** if the winning stratum is `q=0`, `QFORM-Q0-RIDGE-FOUR-HEAVY-DPP-v1` either pays the full form directly with a universal continuous-density bound or compresses the determinant obstruction to at most four original rows.
5. The remaining universal proof must pay the mixed `q=1,2` strata, the principal aggregate `q=3` stratum, and the four-heavy q=0 determinant core without invoking a single tiny reciprocal minor. The exact stress `A=I_4-J_4/3` from the preceding run sits purely in `q=2`, so `q=2` is unavoidable.

The sharpened first next implication is therefore

`QFORM-MIXED-STRATUM-OR-FOUR-HEAVY-PAYMENT-v1`:

> derive an original-coordinate analytic payment for aggregate `q=1` or `q=2` determinant energy, or show that its failure also compresses the determinant weight into a bounded physical-coordinate core that can be merged with the new q=0 four-heavy branch; separately pay the q=3 aggregate without selecting one dimension-dependent tiny principal minor.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The present theorem is a strict supporting advance on the assigned coordinate-minor/averaging mechanism and does not claim the universal theorem.

## 11. Provenance and scope

Fresh brain controls were read before this work; later owner revisions kept QFORM as the sole target and introduced no B07 stop. No FEI, installation, benchmark, email, notification, scheduler mutation, cross-account authentication, paid model/API/Codex call, public release, remote workflow, permission change, unrelated private data, or benchmark-gold access was used. Repository transport is not treated as verified native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
