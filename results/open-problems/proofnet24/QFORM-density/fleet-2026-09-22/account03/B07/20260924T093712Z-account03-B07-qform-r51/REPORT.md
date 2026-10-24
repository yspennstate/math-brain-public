SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B07, 2026-09-24T09:37:12Z.
attacking: the r50 rank-54 coupler over an arbitrary physical T-block — first separate a genuine three-curvature T-block from a near-rank-two T-block, then convert diffuse leverage of the resulting rank-56 carrier into one literal physical E3 crossing.

# account03/B07 r51 — near-rank-two T-block / finite-rank diffuse-carrier compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW SUPPORTING STRUCTURAL LEMMA / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, iid, post-rotation independence, pointwise quadratic-phase decay, arbitrary-joint coarea, fiber-supremum, or deletion of a nonzero coefficient tail is used. Every analytic receiver is invoked on literal original-coordinate sets.

## 1. Fresh source state and exact incoming branch

Fresh control was resolved from `yspennstate/math-research-brain` main at startup commit `d5ca60b7ab996112fa4eed1bd3ff80f18a903f2b`; immediately before publication it was refreshed to `c4f38d1a98d7d8a7e77cccf901943a2aa7c59d20`. OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no account03/B07 pause or reassignment. The live correction inbox and CURRENT_RESEARCH were reread; no refuted conditional-cap, arbitrary-joint-coarea, one-good-minor, post-rotation-independence, or pointwise-oscillatory claim is used below.

Incoming worker-owned state:

`yspennstate/math-open-problems@4155f9884b4eaa0aee96da4e148c7303e6d6cc6a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T074025Z-account03-B07-qform-r50/REPORT.md`.

R50 reduced its moderate-energy survivor to the literal original-coordinate decomposition

`A = diag(C,0_S) + P_54 + G`,                                     (1.1)

where `C=A[T,T]` is an arbitrary symmetric physical T-side block,

`rank P_54 <= 54`,                                                (1.2)

and

`||G||_op < eps0 := 1.6467608693485e-3`.                         (1.3)

The target hypothesis gives

`s_3(A) >= 1`                                                     (1.4)

for singular values ordered decreasingly.

Two completed dependencies are used in exact scope.

**Physical E3 receiver.** account02/B03, `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`:

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T184716Z-account02-B03-QFORM-auto11/REPORT.md`.

For any literal physical cross cut `B=A[I,J]` with

`Z3=e_3(BB^T)>0`,                                                 (1.5)

it proves a continuous `C_0` density and

`||p_Q||_infinity <= C3 Z3^(-1/6)`,                              (1.6)

`C3=3*2^(4/3)*e^(1/3)=10.550168831164775...`,                    (1.7)

with arbitrary same-side blocks, affine terms, outside coordinates, signs, and additional spectrum retained.

**Designated partner.** account04/B07:

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

If a literal physical principal block `A[I,I]`, `|I|=m`, has

`s_3(A[I,I]) >= gamma > 0`,                                      (1.8)

then the full ambient law satisfies

`||p_Q||_infinity <= 2 sqrt(6 pi m)/gamma`.                      (1.9)

This partner gate establishes essential boundedness; continuity is not claimed there.

The only external deterministic input used below is the two-part MSS frame partition already source-pinned and proved applicable in the completed ridge-window package `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`. If a Parseval frame `sum_i u_i u_i^T=I` has `||u_i||^2<=mu`, there is a physical partition `I union J` for which each partial Gram matrix is at most `(1/sqrt(2)+sqrt(mu))^2 I`; since the two partial sums add to `I`, each is therefore at least

`g(mu) I`, `g(mu)=1-(1/sqrt(2)+sqrt(mu))^2`.                    (1.10)

No random-variable rotation is involved.

## 2. General finite-rank diffuse-carrier lemma

### Theorem 2.1 — `QFORM-FINITERANK-DIFFUSE-CARRIER-E3-v1`

Let

`A=H+E`,                                                         (2.1)

where `H=H^T` has finite rank `r>=3`, `||E||_op<=eta`, and

`s_3(A)>=1`.                                                     (2.2)

Let `U` have orthonormal columns spanning `range(H)` and define the physical carrier leverage

`mu=max_i (UU^T)_{ii}=max_i ||U(i,:)||_2^2`.                    (2.3)

If `mu<1/2` and

`sigma(mu,eta):=g(mu)(1-eta)-eta >0`,                            (2.4)

with `g` from (1.10), then there is a literal original-coordinate cut `[n]=I disjoint_union J` such that

`boxed: s_3(A[I,J]) >= sigma(mu,eta).`                           (2.5)

Consequently

`boxed: ||p_Q||_infinity <= C3/sigma(mu,eta),}`                  (2.6)

and the density on this branch is continuous and vanishes at infinity.

### Proof

Write the nonzero spectral representation

`H=U Lambda U^T`,                                                (2.7)

where `Lambda` is an invertible `r x r` symmetric matrix. Weyl applied to `A=H+E` gives

`s_3(H)>=s_3(A)-||E||_op>=1-eta`.                               (2.8)

Apply the two-part MSS frame partition to the physical rows `u_i=U(i,:)`. There is a literal partition `I,J` with

`U_I^T U_I >= g(mu) I_r`,
`U_J^T U_J >= g(mu) I_r`.                                      (2.9)

Put

`Q_I=U_I (U_I^T U_I)^(-1/2)`,
`Q_J=U_J (U_J^T U_J)^(-1/2)`.                                  (2.10)

Both have orthonormal columns, and

`H[I,J]
 =Q_I (U_I^T U_I)^(1/2) Lambda (U_J^T U_J)^(1/2) Q_J^T`.      (2.11)

Therefore multiplication by the two positive square roots can decrease every nonzero singular value by at most the product of their minimum singular values, namely `g(mu)`, so

`s_3(H[I,J]) >= g(mu) s_3(H) >= g(mu)(1-eta)`.                 (2.12)

The retained tail is spent only deterministically:

`||E[I,J]||_op <= ||E||_op <= eta`.                             (2.13)

A second Weyl inequality gives (2.5). If `B=A[I,J]`, then

`Z3=e_3(BB^T) >= s_1(B)^2 s_2(B)^2 s_3(B)^2 >= s_3(B)^6`.     (2.14)

The completed account02/B03 theorem (1.6) now gives

`||p_Q||_infinity <= C3 Z3^(-1/6) <= C3/s_3(B)`,               (2.15)

which is (2.6), including continuity. QED.

This lemma is an aggregate-before-inversion coordinate selector: the whole finite-rank carrier is balanced by a physical cut before any determinant is selected, and the nonzero operator tail remains present.

## 3. Application to the r50 rank-54 coupler

Let

`tau:=s_3(C)`.                                                   (3.1)

If

`tau > 1/64`,                                                    (3.2)

then the arbitrary physical T-block itself retains three singular directions above `1/64`. This branch is recorded, not declared solved: conditioning on `S` generates arbitrary affine terms on `T`, and no unrestricted affine spectral theorem is assumed here.

Now assume the complementary **near-rank-two T-block branch**

`tau <= 1/64`.                                                   (3.3)

Because `C` is symmetric, let `C_2` be its spectral truncation to the two eigenvalues of largest absolute value. Then

`rank C_2<=2`,
`||C-C_2||_op<=1/64`.                                           (3.4)

Define

`H := diag(C_2,0_S)+P_54`,
`E := diag(C-C_2,0_S)+G`.                                       (3.5)

Then

`boxed: rank H <=56`,                                           (3.6)

and

`boxed: ||E||_op < eta0 := 1/64+eps0
                       = 0.0172717608693485.`                   (3.7)

By (1.4),

`s_3(H)>1-eta0=0.9827282391306515`.                             (3.8)

Let `P_H` be the orthogonal projection onto `range(H)` and

`mu_H=max_i (P_H)_{ii}`.                                       (3.9)

### 3.1 Diffuse carrier exit

If

`mu_H <= 1/16`,                                                 (3.10)

then

`g(1/16)
 =1-(1/sqrt(2)+1/4)^2
 =(7-4sqrt(2))/16
 =0.0839466094067262...`.                                       (3.11)

Theorem 2.1 gives a literal physical cut with

`s_3(A[I,J])
 > g(1/16)(1-eta0)-eta0
 =: sigma0
 =0.0652249427739121...`.                                       (3.12)

Therefore

`Z3>sigma0^6`                                                   (3.13)

and the full ambient law has a continuous `C_0` density with

`boxed: ||p_Q||_infinity < C3/sigma0
                           =161.750526447139... .}`              (3.14)

This pays the entire near-rank-two-T / diffuse-rank-56-carrier branch.

### 3.2 Heavy carrier exit is a bounded physical packet

If (3.10) fails, define the literal physical heavy set

`K={i:(P_H)_{ii}>1/16}`.                                       (3.15)

Since

`sum_i (P_H)_{ii}=rank H<=56`,                                 (3.16)

we obtain the dimension-free cardinality bound

`boxed: |K|<16*56=896, hence |K|<=895.`                         (3.17)

Thus the formerly global rank-54-coupler obstruction has been reduced, on the near-rank-two T-side branch, either to the paid diffuse physical crossing (3.14) or to a bounded original-coordinate carrier-heavy packet of at most 895 coordinates.

## 4. Actual application of the designated account04/B07 theorem

Apply the completed partner theorem (1.8)-(1.9) to the **actual heavy set produced in (3.15)**, not to an abstract spectral subspace.

If `|K|>=3` and

`s_3(A[K,K]) >= 1/64`,                                         (4.1)

then with `m=|K|<=895` and `gamma=1/64`, the full ambient law satisfies

`boxed:
 ||p_Q||_infinity
 <= 128 sqrt(6 pi |K|)
 <= 128 sqrt(6 pi*895)
 =16625.3979253295... .}`                                       (4.2)

This is an essential-density bound; continuity is not asserted by the partner gate.

Hence every still-unpaid near-rank-two-T state obeys all of

`mu_H>1/16`,                                                     (4.3)

`1<=|K|<=895`,                                                   (4.4)

and either `|K|<=2` or

`s_3(A[K,K])<1/64`.                                             (4.5)

The remaining high spectrum must therefore interact with the complement of a bounded physical heavy packet; it cannot hide inside a diffuse rank-56 carrier or a strong principal core on that packet.

## 5. Quantitative routing of the r50 obstruction

The r50 debt `QFORM-R54-COUPLER-PLUS-ARBITRARY-TBLOCK-RECEIVER-v1` is sharpened to the following exhaustive three-way routing:

1. **T-side three-curvature:** `s_3(C)>1/64`. This remains unpaid because conditioning on `S` creates arbitrary affine terms; no silent translation/independence claim is made.
2. **Near-rank-two T + diffuse finite carrier:** `s_3(C)<=1/64` and `mu_H<=1/16`. This branch is fully paid by the literal physical E3 crossing, with continuous density `<161.751`.
3. **Near-rank-two T + finite heavy carrier packet:** `s_3(C)<=1/64`, `mu_H>1/16`. Then there is an actual physical set `K` with `|K|<=895`. If `s_3(A[K,K])>=1/64`, the designated account04/B07 theorem pays the full ambient law by `<16625.398`; otherwise the only residual is the bounded-heavy/weak-core packet (4.3)-(4.5).

No dimension-growing tiny coordinate minor appears anywhere in this routing.

## 6. Rigorous constant checks

The constants used above are

`eps0 = 0.0016467608693485`,
`eta0 = 1/64+eps0 = 0.0172717608693485`,
`g0 = (7-4sqrt(2))/16 = 0.0839466094067262...`,
`sigma0 = g0*(1-eta0)-eta0 = 0.0652249427739121...`,
`C3 = 10.550168831164775...`,
`C3/sigma0 = 161.750526447139...`,
`128 sqrt(6 pi*895)=16625.3979253295...`.

A separate checker in this run folder recomputes these values and tests the singular-value compression inequalities on seeded finite-rank examples. Those finite computations are regression evidence only; the proof is the deterministic frame-partition/Weyl/Cauchy-Binet argument above.

## 7. Remaining obstruction and next step

This does **not** solve full QFORM. The exact next coordinate-selection debt is

`QFORM-R51-FINITE-HEAVY-PACKET-OR-TSIDE-THREECURVATURE-RECEIVER-v1`:

* either consume the `s_3(C)>1/64` physical T-side spectral branch in the presence of conditioning-generated affine terms;
* or, in the near-rank-two branch, use the at-most-895-coordinate heavy packet together with the retained cross coupler to force a paid principal core, pair/square receiver, or physical E3 cut.

The separate r49 `E_star>1` same-bank physical-star branch, the earlier near-rank-one matched branch, and other previously preserved packets remain distinct.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.**
