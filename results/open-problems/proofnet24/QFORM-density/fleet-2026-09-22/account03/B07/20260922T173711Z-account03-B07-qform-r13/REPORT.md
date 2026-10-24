SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B07, 2026-09-22T17:37:11Z.
attacking: O0 effective-dimension-three heavy ridge packets; isolate aggregate coordinate third-volume and pay the transpose-diffuse subbranch.

# account03/B07 — O0 three-quarter ridge packet isolation and two-sided coordinate collar

**Run:** `20260922T173711Z-account03-B07-qform-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh final owner control used:** revision `2026-09-22.10` at `yspennstate/math-research-brain@47b9f97c9260868b87b9c5b7e7d92af0bf5c4fb4`  
**Assignment:** Coordinate minor selection  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED O0 STRUCTURAL COLLAR + PAID SUBBRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, current correction, and source state

The full target remains: for every dimension, independent real coordinates `X_i` with probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a valid counterexample. Continuity is a separate desired conclusion.

The final owner refresh advanced the control to revision `2026-09-22.10`. In particular, the owner correction records the correct rank-three coarea scaling `||rho||_infinity^(2/3)` and reports the rank-exactly-three case as proved. This run therefore does not attempt to re-prove that case; it attacks the full-rank O0 coordinate-overlap obstruction from the preceding B07 reduction. Revision `.10` also requires the explicit sign-in line above and a matching RESULTS-inbox record.

No post-rotation independence, law-uniform pointwise van-der-Corput decay, conditional-density-cap surrogate, raw fiber supremum, or single-good-minor hypothesis is used. In particular, the live correction `QFORM-CROSSMINOR-ALONE-FALSE` remains in force: a uniformly nonsingular cross minor by itself is not promoted to a density theorem.

The preceding B07 theorem is source-pinned at

`yspennstate/math-open-problems@685929d9daee92a164dbf6ba6f9305d2e6550826`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T163733Z-account03-B07-qform-r12/REPORT.md`.

It proves the full-matrix third-compound overlap reduction. In the O0 branch there are disjoint original-coordinate sets `L,R` and the cross block `B=A[L,R]` satisfies

`E:=e_3(s_1(B)^2,s_2(B)^2,...) >= 1/256`.                 (1.1)

The designated partner `account04/B07` still had no completed current-QFORM canonical directory or shared handoff at the fresh source check. No result is fabricated. The completed compatible result actually applied below is account01/B04's `QFORM-O0-EFFECTIVE3-ADAPTIVE-Q-v1`, source-pinned at

`yspennstate/math-open-problems@c03349badbdfce229ca3a1548d3de8615d1028c5`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260922T171055Z-account01-B04-QFORM-r14/REPORT.md`.

That theorem calibrates a physical cross block to effective dimension three and proves a continuous density whenever the maximum physical ridge leverage is strictly below `3/4`.

## 2. Effective-dimension-three ridge setup

Let

`K_gamma = B B^T (gamma^2 I + B B^T)^(-1)`.

If `rank B>3`, choose the unique `gamma_*>0` with

`tr K_{gamma_*}=3`.                                           (2.1)

If `rank B=3`, use the limit `gamma downarrow 0`; then `K_*` is the orthogonal projection onto `range(B)` and again has trace three. Write simply `K=K_*` below.

Account01/B04 pays O0 whenever

`max_i K_ii < 3/4`.                                           (2.2)

Thus the only O0 geometry needing further work has at least one original row with `K_ii>=3/4`. The goal is to convert such high ridge leverage into aggregate coordinate determinant currency without selecting a reciprocal tiny minor.

## 3. A contraction determinant lemma

### Lemma 3.1

Let `M` be an `h x h` positive semidefinite contraction, `0<=M<=I`. Then

`det M >= tr M -(h-1)`.                                      (3.1)

#### Proof

If `mu_1,...,mu_h in[0,1]` are the eigenvalues, then

`1-product_j mu_j <= sum_j (1-mu_j)`,

which is the elementary union-bound inequality for products in `[0,1]`. Rearranging gives (3.1). QED.

Consequently, if `H` is a set of `h<=3` physical rows with `K_ii>=3/4` for all `i in H`, then

`det K_H >= 1-h/4`.                                          (3.2)

In particular a three-row heavy packet has

`det K_H>=1/4`.                                               (3.3)

There can be at most four `3/4`-heavy rows because `tr K=3`. If there are exactly four, their diagonal sum is already at least three, hence exactly three and every outside diagonal is zero. The four-by-four supported contraction has eigenvalues in `[0,1]` summing to three. The elementary-symmetric concentration lemma gives `e_3>=1`, so among its four physical triples there is a triple `H` with

`det K_H>=1/4`.                                               (3.4)

Therefore whenever there are at least three `3/4`-heavy rows, there is a physical triple `H` satisfying (3.3).

## 4. Main new theorem: a heavy ridge triple carries constant aggregate third volume

### Theorem 4.1 — `QFORM-O0-HEAVY-PACKET-ISOLATION-v1`

Assume (1.1), calibrate to effective dimension three as in Section 2, and suppose there are at least three physical rows with ridge leverage at least `3/4`. Then there is a three-row set `H subset L` such that

`boxed(
  sum_{T subset R, |T|=3} det B[H,T]^2
  = det(B_H B_H^T)
  >= E/16
  >= 1/4096.
)`                                                            (4.1)

If `rank B=3`, the stronger bound `det(B_HB_H^T)>=E/4` holds.

#### Proof: finite ridge scale

Assume first `rank B>3`, so `gamma_* >0`. Put

`L_0 = B B^T/gamma_*^2`,
`D = det(I+L_0)`.

The `L`-ensemble determinantal law

`P(S)=det L_0[S,S]/D`                                        (4.2)

has marginal kernel `K=L_0(I+L_0)^(-1)`. Choose `H` as in (3.3), so

`P(H subset S)=det K_H >=1/4`.                               (4.3)

Condition this DPP on inclusion of `H`. Its conditional kernel on `C=H^c` is

`K^H = K_CC-K_CH K_H^(-1) K_HC`,                             (4.4)

hence, since the second term is positive semidefinite,

`tr K^H <= tr K_CC = tr K-tr K_H <=3-9/4=3/4`.              (4.5)

The conditional expected number of extra selected rows is therefore at most `3/4`. Markov's inequality gives

`P(S=H | H subset S)
 =P(no extra row | H subset S)
 >=1-E[# extras | H subset S]
 >=1/4`.                                                       (4.6)

Combining (4.3) and (4.6),

`P(S=H)>=1/16`.                                               (4.7)

But by (4.2), because `|H|=3`,

`P(S=H)=gamma_*^(-6) det(B_HB_H^T)/D`.                       (4.8)

The regularized determinant expansion gives

`D=det(I+BB^T/gamma_*^2)
  >= gamma_*^(-6)e_3(s(B)^2)
  = gamma_*^(-6)E`.                                          (4.9)

Equations (4.7)--(4.9) imply

`det(B_HB_H^T)>=E/16`.                                       (4.10)

Finally Cauchy--Binet gives the equality in (4.1). QED for finite scale.

#### Rank exactly three endpoint

Write `B=U Sigma V^T` with `U^TU=I_3`. Then the limiting kernel is `K=UU^T`, while

`E=det(Sigma^2)`.

For a physical triple `H`,

`det(B_HB_H^T)=det(Sigma^2) det(U_HU_H^T)
              =E det K_H`.                                  (4.11)

Using (3.3) gives `det(B_HB_H^T)>=E/4`. QED.

### Interpretation

The old O0 residual was merely “some row has ridge leverage at least `3/4`.” Theorem 4.1 shows that three heavy rows force a fixed row packet carrying a universal fraction of the entire third-volume currency. It is still an aggregate over all original columns; no single tiny `3x3` minor is inverted.

## 5. Actual application of the completed account01/B04 theorem

Fix a triple `H` supplied by Theorem 4.1 and put

`G=B_HB_H^T`.

Then `G` is positive definite and `det G>=1/4096`. Define the column-side rank-three projection

`P = B_H^T G^(-1) B_H`                                       (5.1)

on the untouched original coordinates in `R`, and let

`tau=max_{j in R} P_jj`.                                     (5.2)

The transposed cross block `B_H^T=A[R,H]` has rank exactly three, and its third elementary singular-value mass is exactly

`E_H=e_3(s(B_H)^2)=det G>=1/4096`.                            (5.3)

If

`tau <=11/16`,                                                (5.4)

apply account01/B04's completed `QFORM-O0-EFFECTIVE3-ADAPTIVE-Q-v1` to this actual original-coordinate cross block. Its parameter satisfies

`q_*=max(1,2tau)<=11/8`.

The theorem's coefficient is increasing over this interval, so

`||p_Q||_infinity
 <= [3e/(sqrt(2q_*)(3-2q_*))] E_H^(-1/6)
 <= [24e/sqrt(11)] * 4
 = 96e/sqrt(11)
 <79`.                                                        (5.5)

Thus:

> **`QFORM-O0-HEAVY-TRIPLE-TRANSPOSE-DIFFUSE-PAYMENT-v1`.** If O0 has at least three `3/4`-heavy row leverages and the isolated packet has column projection leverage at most `11/16`, then the full quadratic form, with arbitrary self blocks, outside couplings, extra eigenvalues and signs, has a continuous density satisfying `||p_Q||_infinity<79`.

This is a direct application of a completed peer result to an explicit inequality, not merely a citation.

## 6. If the transpose is also localized: a two-sided six-coordinate collar

The remaining case in Section 5 has `tau>11/16`. Suppose, more strongly, that at least three original columns satisfy

`P_jj>=11/16`.                                               (6.1)

Choose any three of them and call the set `T`. Since `P_T` is a three-by-three positive contraction,

`tr P_T>=33/16`,

so Lemma 3.1 gives

`det P_T>=33/16-2=1/16`.                                     (6.2)

Let

`U=B_H^T G^(-1/2)`,

so `U^TU=I_3`, `P=UU^T`, and `B_H=G^(1/2)U^T`. Hence

`det B[H,T]^2 = det G det P_T`.                              (6.3)

Using (4.1) and (6.2),

`boxed(
 |det B[H,T]|^2 >= E/256 >=1/65536,
 |det B[H,T]| >=1/256.
)`                                                            (6.4)

This is a dimension-free two-sided coordinate collar: three physical rows and three physical columns carry a uniformly nonsingular cross block.

Crucially, (6.4) is not declared to solve the branch. The live correction `QFORM-CROSSMINOR-ALONE-FALSE` shows exactly why: a good cross block without compatible pivot-side structure can still have an unbounded quadratic pushforward in lower spectral rank. The value of (6.4) is that the remaining obstruction is now supported on six named original coordinates while the third-volume scale is fixed; an additional grouped-square/rank-two/overlap payment is still needed.

## 7. If fewer than three rows are heavy: exact aggregate skeleton

Let

`J={i in L: K_ii>=3/4}`,

so the branch not covered by Theorem 4.1 has `|J|=1` or `2`. Define the nonnegative row-triple weights

`m(S)=det(B_SB_S^T),  |S|=3`,

so by Cauchy--Binet

`sum_{|S|=3}m(S)=E`.                                         (7.1)

Partition by `r=|S cap J|`.

* If `|J|=1`, either the triples avoiding the heavy row carry at least `E/2`, or the triples containing that fixed heavy row carry at least `E/2`.
* If `|J|=2`, one of `r=0,1,2` carries at least `E/3`. In the `r=1` alternative, one of the two heavy rows itself carries at least `E/6` in triples containing it and two nonheavy rows. In the `r=2` alternative, the fixed heavy pair carries at least `E/3` together with one nonheavy row.

This is elementary, but it is the right surviving geometry: after the three-heavy packet is handled, the O0 obstruction has a one- or two-coordinate heavy skeleton plus constant aggregate third-volume currency. No reciprocal single-minor selection is introduced.

## 8. Updated smallest conditional proof deduction

The preceding B07 theorem reduced every target matrix to O0/O1/O2/O3. The completed account01/B04 theorem now pays O0 whenever its effective-dimension-three ridge kernel has maximum row leverage `<3/4`.

The present run sharpens the remaining O0 branch as follows.

1. If at least three rows are `3/4`-heavy, isolate a fixed row triple with aggregate third volume at least `E/16`.
2. On that packet, if the transpose rank-three projection has maximum leverage `<=11/16`, the completed peer theorem gives a continuous density `<79`.
3. If instead at least three transpose coordinates have leverage `>=11/16`, there is a six-coordinate cross packet with determinant at least `1/256`; an additional source-valid pivot/grouped-coordinate payment is still required and cannot be replaced by the refuted cross-minor-alone shortcut.
4. Otherwise the obstruction has at most two heavy coordinates on the transpose side.
5. If the original side started with fewer than three `3/4`-heavy rows, Section 7 already reduces to a one-/two-heavy-coordinate aggregate skeleton.

Thus the first unpaid O0 implication is now the finite-heavy-skeleton problem:

`QFORM-O0-ONE-TWO-HEAVY-SKELETON-PAYMENT-v1`:

> starting from one or two heavy original coordinates on one side, and after the packet reduction at most one or two on the other side, combine the retained aggregate third-volume with a product-preserving rank-two half-Riesz, grouped-square, or overlap-transfer argument. If a six-coordinate collar occurs, use self-block/sign information or a grouped smoother before invoking a local cross block.

The separate O1/O2/O3 aggregate overlap branches also remain unpaid in the complete synthesis.

## 9. Status

* `QFORM-O0-HEAVY-PACKET-ISOLATION-v1`: **PROVED**.
* `QFORM-O0-HEAVY-TRIPLE-TRANSPOSE-DIFFUSE-PAYMENT-v1`: **PROVED**, by direct application of completed account01/B04 mathematics; full form and continuous density, bound `<79`.
* `QFORM-O0-TWOSIDED-COLLAR-v1`: **PROVED structural certificate**, not a density theorem by itself.
* one-/two-heavy skeleton payment: **OPEN**.
* O1/O2/O3 aggregate payments: **OPEN**.
* full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
* full continuity conclusion: **OPEN**; continuity is obtained only on the peer-paid subbranch above.

The final control and corrections were refreshed before publication. No task identity, schedule, enabled/paused state, quiet delivery, email/push setting, cross-account scheduler state, public release, paid model/API/Codex call, credential, or unrelated private material was changed or used.
