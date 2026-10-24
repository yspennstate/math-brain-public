SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B20, 2026-09-22T18:23:14Z.
Attacking: the account02/B20 strong P1 physical-pivot packet by rank-one singular-value deletion, product-preserving cut extraction, and immediate physical-pair payment.

# account01/B20 QFORM r15 — pivot packet amplification to star / disjoint bank / coherent triangle

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control applied:** revision `2026-09-22.11` (later than the assignment card's historical `.5`)  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL P1 REFINEMENT PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** no new full-branch continuity claim.

## 1. Exact target and correction boundary

The target is the unrestricted statement: for every finite `n`, independent real coordinates `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three singular/eigenvalue magnitudes at least one (`s_3(A)>=1`), prove that `Q=X^TAX` has a density whose essential supremum is bounded by one universal finite constant, or give a valid counterexample.

No Gaussian, moment, iid, compact-support, log-concavity, spectral-coordinate independence, or rotated-input hypothesis is used below. The proof uses no law-uniform pointwise quadratic oscillatory decay, no fiberwise density cap, no generic conditional-cap surrogate, no one-good-minor inference, and no same-square absorption of arbitrary bank curvature. The full conjecture remains open.

I also do **not** use the scalar `sup_b ||p_{Q_3|Q'=b}||_infinity` proposal from the verbatim owner message. A fresh account02/B15 source-valid construction on current main shows that this worst-level scalar conditional-height route can fail even for an exact target matrix; only a weighted/averaged scalar-conditioned route survives there. This report is independent of that route.

## 2. Completed account02/B20 result actually applied

The designated partner is account02/B20 run `20260922T172846Z-account02-B20-QFORM-r14`, canonical main report

`yspennstate/math-open-problems@6f93c551ec92438379a2b1d6a59fb58683064bf9`

with pivot refinement

`yspennstate/math-open-problems@c03349badbdfce229ca3a1548d3de8615d1028c5`.

Combining the paid `s_2(A-diag A)<=499/1000` branch with its balanced nested-cut reduction, every unresolved target matrix has one of three source-realizable packets. The P1 packet used here supplies a physical coordinate `i` with

`|a|:=|A_ii| >= alpha := 3501/8000 = 0.437625`.                 (2.1)

The partner also had an outer cross bank of singular value `>beta=499/4000` and the row-heavy/disjoint-bank fork at `beta/sqrt(2)`, with the row-heavy aggregate density cap `sqrt(2)/||r||_2`. I use that projection inequality below after proving a stronger row threshold from the global `s_3(A)>=1` hypothesis itself.

A second completed input is account01/B19 `QFORM-OPPOSITE-DIAGONAL-PAIR-v1` and its definite physical-pair lemma, source report

`yspennstate/math-open-problems@e0b9c9e351dba6dc8472fb7de2afe373dc46b0cd`

at `proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260922T165145Z-b19-qform-r11/REPORT.md`.

It proves, under the exact owner target, that two opposite-sign physical diagonal entries of magnitudes at least `m` imply

`||p_Q||_infinity <= 50 m^(-3/4)`,                              (2.2)

and that a same-sign physical pair with both diagonal magnitudes at least `m` and cross entry at most `r<m` has

`||p_Q||_infinity <= pi/sqrt(m^2-r^2)`.                         (2.3)

Both statements permit arbitrary outside coordinates and couplings.

## 3. New theorem: a target pivot forces a much stronger residual packet

### Theorem `QFORM-PIVOT-RANKONE-DELETION-AMPLIFICATION-v1`

Let `A` be real symmetric with `s_3(A)>=1`, and let `i` be any physical coordinate with `a=A_ii !=0`. Then at least one of the following holds:

**(D2) Two complementary physical squares.** There are distinct `j,k != i` with

`|A_jj|>=1/2`, `|A_kk|>=1/2`.                                  (3.1)

**(STAR) Strong physical pivot row.** There is an original-coordinate bank `R` not containing `i` such that

`||A[i,R]||_2 > eta := 1/(4 sqrt(2))`.                          (3.2)

**(BANK) Strong cross bank disjoint from the pivot.** There are disjoint original-coordinate sets `L_0,R`, neither containing `i`, such that

`s_1(A[L_0,R]) > eta := 1/(4 sqrt(2))`.                         (3.3)

Numerically `eta=0.1767766952...`.

#### Proof

Delete only the physical diagonal pivot, not its row:

`B := A-a e_i e_i^T`.                                          (3.4)

The perturbation `A-B` has rank one. Singular-value interlacing for a rank-one perturbation gives

`s_2(B) >= s_3(A) >=1`.                                        (3.5)

The `i`th diagonal entry of `B` is zero and all other diagonal entries equal those of `A`.

If (D2) holds we are done. Suppose it fails. Then among the diagonal entries of `B` at most one has magnitude at least `1/2`. Choose `j_0` with maximal `|B_{j_0j_0}|` and put

`D_0=B_{j_0j_0}e_{j_0}e_{j_0}^T`, `R_0=B-D_0`.                 (3.6)

Again `B-R_0` has rank at most one, so by (3.5)

`||R_0||_op=s_1(R_0) >= s_2(B) >=1`.                           (3.7)

Write

`H:=A-diag(A)=B-diag(B)`                                      (3.8)

and `D_small:=diag(B)-D_0`. Since (D2) fails,

`||D_small||_op <1/2`.                                        (3.9)

Because `R_0=H+D_small`, (3.7)-(3.9) imply

`||H||_op >1/2`.                                               (3.10)

Now take independent Rademacher signs `eps_l`, put `D_eps=diag(eps)`, and define

`M_eps=(H-D_eps H D_eps)/2`.                                  (3.11)

For the physical cut `L={l:eps_l=1}`, `R={l:eps_l=-1}`, the matrix `M_eps`, after merely reordering the original coordinates, is

`[[0,C],[C^T,0]]`, `C=A[L,R]`.                                (3.12)

Also `E M_eps=H/2`. Convexity of the operator norm gives a deterministic physical cut with

`s_1(C)=||M_eps||_op >= ||H||_op/2 >1/4`.                     (3.13)

Assume first `i in L`; the other orientation is identical after transposition. Split the pivot row from the cut block:

`C = [ r ; C_0 ]`,

where `r=A[i,R]` and `C_0=A[L\{i},R]`. Then

`C^T C = r^T r + C_0^T C_0`,

hence

`s_1(C)^2 <= ||r||_2^2+s_1(C_0)^2`.                           (3.14)

Together with (3.13), (3.14) forces

`||r||_2 > 1/(4sqrt(2))`

or

`s_1(C_0)>1/(4sqrt(2))`.                                      (3.15)

These are respectively (STAR) and (BANK), and in (BANK) both coordinate banks exclude the pivot. QED.

### Quantitative comparison with the designated partner

The partner's P1 refinement had threshold

`beta/sqrt(2)=499/(4000sqrt(2))=0.08821157...`.

The new universal pivot threshold is

`eta=1/(4sqrt(2))=0.17677669...`,                              (3.16)

more than twice as large. In the (STAR) branch, applying the partner's source-valid product-projection inequality to

`Y=A[i,R] X_R`

gives the actual marginal estimate

`||p_Y||_infinity <= sqrt(2)/||A[i,R]||_2 <8`.                 (3.17)

This is a marginal cap only. It is **not** promoted to a conditional cap and is not used to absorb arbitrary same-bank quadratic curvature.

## 4. Immediate analytic payment of most of the (D2) branch

Now specialize to the account02/B20 P1 pivot (2.1), so

`alpha=3501/8000`.                                             (4.1)

If alternative (D2) occurs, choose the two complementary indices `j,k`. Then the three physical diagonal magnitudes on `i,j,k` are at least

`alpha, 1/2, 1/2`,

so each is at least `m:=alpha`.

### 4.1 Mixed diagonal signs are completely paid

If the three diagonal signs are not all equal, some pair has opposite signs. Applying (2.2) with `m=alpha` gives

`||p_Q||_infinity <= 50 alpha^(-3/4)
                   < 92.928`.                                 (4.2)

Thus an unresolved (D2) branch must have all three diagonal signs equal.

### 4.2 A small edge in the same-sign triple is completely paid

Assume all three diagonal signs agree. If any pair `p,q` among `i,j,k` satisfies

`|A_pq| <= alpha/2`,                                           (4.3)

then (2.3), with `m=alpha` and `r=alpha/2`, gives

`||p_Q||_infinity
 <= pi/sqrt(alpha^2-alpha^2/4)
 = 2pi/(sqrt(3) alpha)
 < 8.290`.                                                     (4.4)

Therefore every still-unpaid (D2) packet is forced into the sharply constrained physical triangle

`sign(A_ii)=sign(A_jj)=sign(A_kk)`,                            (4.5)

`|A_ii|>=alpha`, `|A_jj|,|A_kk|>=1/2`,                        (4.6)

and

`|A_ij|, |A_ik|, |A_jk| > alpha/2
 = 3501/16000
 = gamma`.                                                     (4.7)

The final equality is notable: the surviving edge threshold is exactly the account02/B20 nested-bank constant `gamma`.

Call (4.5)-(4.7) the **coherent same-sign triangle packet**.

## 5. Upgraded P1 branch in the current full-target assembly

Account02/B20 r14 reduces every still-unpaid target matrix to T2, P1, or N1. The P1 alternative can now be replaced by the strictly sharper source-valid trichotomy:

1. **coherent same-sign triangle:** (4.5)-(4.7);
2. **strong physical star:** `||A[i,R]||_2>1/(4sqrt(2))`, with the genuine aggregate marginal cap `||p_{A[i,R]X_R}||_infinity<8`;
3. **strong disjoint cross bank:** `s_1(A[L_0,R])>1/(4sqrt(2))`, with both banks disjoint from the pivot source.

The broad alternatives “two large complementary diagonals” and “partner-scale pivot row/disjoint bank” no longer need to be carried as unpaid cases.

This is a target-level structural implication, not merely a re-labeling: it uses the global third-singular-value hypothesis through rank-one perturbation interlacing, pays all mixed-sign diagonal triples with the completed quarter-Riesz Schur theorem, pays a uniform same-sign definite-pair subbranch, and improves the partner's physical row/bank scale by a factor exceeding two.

## 6. What remains unpaid

The full conjecture is still open. The first P1 analytic debt is now one of only three concrete packets above.

- In the **STAR** packet, (3.17) is a source-valid marginal cap but cannot be substituted for a conditional cap; the live same-square correction prevents treating arbitrary bank curvature as harmless.
- In the **BANK** packet, singular-vector coordinates are not declared independent. One must use a product-preserving ridge/grouped-coordinate payment or recurse on localization.
- In the **coherent triangle** packet, all three physical diagonals have the same sign and all three mutual edges exceed `gamma`; if a physical pair is quantitatively definite it is already paid by (2.3), so the remaining difficulty is the near-degenerate/indefinite strongly-coupled triangle interacting with the rest of the matrix.

A useful next step is to combine the coherent-triangle packet with the already-proved binary-indefinite `L^3` theorem and rank-two Schur inheritance, splitting according to the three principal pair determinants, while keeping every pivot physical. In the STAR/BANK packets, combine the stronger `eta` scale with the current ridge/localization gates rather than selecting a tiny individual edge.

## 7. Scope/status

- **New status:** `ESSENTIAL_STEP_APPLIED`.
- **Full QFORM:** `OPEN / NOT PROVED / NOT DISPROVED`.
- **Continuity:** open on these new residual packets; no new claim.
- **No forbidden assumptions:** all variables remain the original independent coordinates; no moment/support/iid/log-concavity assumption is added.
- **No refuted mechanism used:** in particular no pointwise oscillatory decay, rotated independence, generic conditional density cap, one-good-minor selection, or same-square absorption.

## 8. Operational/source provenance

Fresh account01 native inventory contained the same twenty managed B01-B20 QFORM tasks, all enabled, hourly-valid and quiet. No missing authorized native slot, duplicate, deliberate pause, or capacity issue required a mutation, so zero scheduler mutations were made and no mutation lease was needed. Native assignment state is kept separate from worker check-ins and substantive mathematics; missing login is not an outage.

Source control was read fresh before work. Repository retrieval occurred through the connected GitHub source, but no authenticated native brain receiver/learned-memory use was observed, so execution remains `WITHOUT_VERIFIED_BRAIN`.

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported. Configured reasoning effort and provider usage/thinking counters were not exposed and are recorded as `UNKNOWN/null`, not zero.
