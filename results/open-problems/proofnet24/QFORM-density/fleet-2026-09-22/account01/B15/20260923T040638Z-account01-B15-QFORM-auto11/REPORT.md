SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T04:06:38Z.
attacking: target-level regularity through physical-block conditioning; derive a zero-loss continuity/stability lemma that converts completed partner one-sheet or block bounds into an actual global inequality without rotated independence.

# account01/B15 auto11 — exact fixed-annulus far-center normal form and one-sheet payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** absolute continuity and regularity  
**Run:** `20260923T040638Z-account01-B15-QFORM-auto11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_FIXED_ANNULUS_FAR_CENTER_NORMAL_FORM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and status

The unrestricted owner target remains OPEN. Let

`Q_A=X^T A X`

for independent original-coordinate inputs with one-dimensional probability densities bounded by one. Write

`s(A)=s_3(A)`

for the third largest eigenvalue modulus of the real symmetric matrix `A`. The target class is `s(A)>=1`.

This run proves a zero-loss normal form in which the sharp universal density constant is tested by one fixed annulus of width one on each side, centered arbitrarily far from the only critical output value of the homogeneous quadratic map. Thus neither a shrinking output window nor the cone vertex `Q=0` is an essential part of the universal-height problem.

I then apply the completed assigned-partner `account02/B15` ambient one-sheet theorem to this exact annular functional. It pays the majority-sign part of the fixed annulus inside every invertible indefinite physical `3 x 3` block while preserving all outside quadratic coefficients and cross couplings. Only the minority/two-sheet annular part remains in that branch.

No law-uniform pointwise Fourier decay, post-rotation independence, arbitrary-joint coarea bound, projection-only shortcut, conditional density supremum, or uniformly good physical minor is assumed.

## 2. Completed assigned-partner results actually used

### 2.1 Fixed-target C0 theorem

The first assigned-partner result is `account02/B15`:

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T160529Z-account02-B15-qform-r4/REPORT.md`.

A fresh independent review is `account03/B15`:

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260923T002819Z-account03-B15-qform-r22/REPORT.md`.

At the exact scope needed here, they prove:

> If `rank(A)>=3`, then every cap-one original product law gives `Q_A` an individually bounded density with a representative `p_A in C_0(R)`.

The bound may depend on the physical-coordinate geometry of `A`; this does not prove the owner constant. What I use below is the qualitative consequence that `p_A` is continuous and attains its finite maximum.

### 2.2 Ambient physical-three-block one-sheet theorem

The second assigned-partner result is `account02/B15`:

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T030440Z-account02-B15-QFORM-auto11/REPORT.md`, Theorem 6.1.

Write an ORIGINAL-coordinate partition as

`A=[[B,C],[C^T,D]]`,

where `B` is an invertible physical `3 x 3` principal block of signature `(2,1)` or `(1,2)`. Put

`kappa=sigma_min(B)`.

After conditioning on the outside original coordinates and completing the square only in the three physical coordinates, the theorem states that the conditional majority-sign one-sheet submeasure has interval density at most

`pi sqrt(2)/kappa`,

uniformly in the outside conditioner. Averaging therefore preserves exactly that interval bound. The theorem allows arbitrary outside quadratic terms and arbitrary cross couplings.

This is applied to the fixed annulus in Section 5.

## 3. Spectral homogeneity of the sharp constant

Let

`C_* = sup ||p_A||_infinity`,

where the supremum runs over all target instances `s(A)>=1` and all admissible product laws; allow `C_*=+infinity`.

For `a>0`,

`Q_(aA)=a Q_A`,
`p_(aA)(t)=a^(-1) p_A(t/a)`,
`s(aA)=a s(A)`.                                                     (3.1)

Hence

`boxed{ C_* = sup_(target A,f) s(A) ||p_A||_infinity. }`             (3.2)

Indeed, if `s=s(A)>=1`, then `B=A/s` has `s(B)=1`, and

`s ||p_A||_infinity = ||p_B||_infinity <= C_*`.                    (3.3)

Conversely the normalized subclass `s(A)=1` is contained in the target class. Thus all sharp-height questions may be normalized to `s(A)=1` and then rescaled back without loss.

## 4. Main theorem: one fixed annulus arbitrarily far from zero

For `y in R`, define the unit annulus

`S_y=(y-2,y-1) union (y+1,y+2)`.                                  (4.1)

It has total length two and excludes the entire unit neighborhood of its center.

### Theorem 4.1 — `QFORM-FIXED-ANNULUS-FAR-CENTER-v1`

For every fixed `R>2`,

`boxed{
 C_*
 = sup_{target A,f; y>=R}
     [s(A)/2] P{Q_A in S_y}.
}`                                                                  (4.2)

Equivalently,

`boxed{
 C_*
 = sup_{target A,f; y>=R}
 [s(A)/2] P{1<|Q_A-y|<2}.
}`                                                                  (4.3)

The equality is in the extended sense, so it is valid whether or not the full conjecture is true.

In particular, choosing `R=4`, every tested output value lies in `(2,infinity)`. Thus the full universal-height problem is exactly equivalent to a fixed-scale positive-output shell estimate uniformly separated by distance at least two from the homogeneous critical value `Q=0`.

### Proof: upper bound

For any target instance,

`P(Q_A in S_y) <= |S_y| ||p_A||_infinity
                 =2 ||p_A||_infinity`.                              (4.4)

Therefore

`[s(A)/2] P(Q_A in S_y)
 <=s(A)||p_A||_infinity
 <=C_*`                                                             (4.5)

by (3.2). Hence the right side of (4.2) is at most `C_*`.

### Proof: reverse bound

By (3.2), it is enough to take matrices normalized by

`s(A)=1`.                                                            (4.6)

Fix one such target instance and write

`M=||p_A||_infinity`.

The completed `account02/B15` fixed-target theorem gives

`p_A in C_0(R)`.                                                     (4.7)

Hence `p_A` attains its maximum. For every `eta>0`, choose a nonzero point `t` with

`p_A(t)>M-eta`.                                                      (4.8)

If a maximizer is nonzero, use it. If every chosen maximizer is zero, continuity in (4.7) supplies arbitrarily small nonzero `t` satisfying (4.8). If `t<0`, replace `A` by `-A`; the target hypothesis and `s(A)=1` are unchanged and

`p_(-Q)(-t)=p_Q(t)`.                                                 (4.9)

Thus we may assume `t>0`.

For `r>0`, set

`a_r(t)= [1/(2r)] P{r<|Q_A-t|<2r}`.                                (4.10)

Because `p_A` is continuous at `t`,

`a_r(t)
 = [1/(2r)] [int_(t-2r)^(t-r) p_A(u)du
             +int_(t+r)^(t+2r) p_A(u)du]
 -> p_A(t)`                                                         (4.11)

as `r downarrow0`.

Choose `r` sufficiently small that

`r<=1`, `t/r>=R`, and `a_r(t)>p_A(t)-eta`.                         (4.12)

Now scale the matrix by

`A_r=A/r`.                                                          (4.13)

Then

`s(A_r)=1/r>=1`, `Q_(A_r)=Q_A/r`, and `y=t/r>=R`.                  (4.14)

Consequently

`[s(A_r)/2] P{1<|Q_(A_r)-y|<2}
 = [1/(2r)] P{r<|Q_A-t|<2r}
 = a_r(t)
 > M-2eta`.                                                         (4.15)

The right side of (4.2) is therefore at least `M-2eta`. Letting `eta downarrow0`, then taking the supremum over normalized target instances, proves the reverse inequality and hence (4.2).

QED.

### What was used, and what was not

The only regularity used in the reverse direction is the **instancewise** `C_0` theorem from assigned partner `account02/B15`. There is no common continuity modulus, derivative bound, support bound, tail rate or compactness assumption. This is important because the B15 correction programme already contains smooth fixed-matrix target families with no target-uniform positive Hölder/BV/Sobolev regularity.

## 5. Actual application of the completed partner one-sheet theorem

Theorem 4.1 is a target-level normal form. It now interfaces directly with the completed ambient one-sheet result in original coordinates.

Let an admissible target matrix have an invertible physical principal block

`B=A[I,I]`, `|I|=3`,                                                (5.1)

of signature `(2,1)`; the `(1,2)` case follows by sign reversal. Put

`kappa=sigma_min(B)`.                                                (5.2)

Partition the original independent variables as `X=(U,W)`, `U=X_I`, and write

`A=[[B,C],[C^T,D]]`.                                                 (5.3)

Conditional on `W=w`,

`Q_A
 = U^T B U + 2U^T Cw + w^T D w
 = (U+B^(-1)Cw)^T B (U+B^(-1)Cw) + R(w)`,                          (5.4)

where

`R(w)=w^T(D-C^T B^(-1)C)w`.                                        (5.5)

No spectral rotation of the source is made. The shift in (5.4) is coordinatewise in the original physical triple and preserves each cap-one conditional density.

For signature `(2,1)`, define the conditional majority sheet by

`Maj={Q_A-R(W)>0}`                                                   (5.6)

and minority sheet by `Min={Q_A-R(W)<0}`. For signature `(1,2)` reverse these inequalities.

The completed `account02/B15` ambient theorem gives for every interval `J`

`P{Q_A in J, Maj} <= (pi sqrt(2)/kappa) |J|`.                       (5.7)

Apply (5.7) to the two disjoint unit intervals in `S_y`. Their total length is two, hence

`boxed{
 P{Q_A in S_y, Maj} <= 2 pi sqrt(2)/kappa.
}`                                                                  (5.8)

Therefore the exact sharp annulus functional satisfies the actual inequality

`boxed{
 [s(A)/2] P{Q_A in S_y}
 <= pi sqrt(2) s(A)/kappa
    + [s(A)/2] P{Q_A in S_y, Min}.
}`                                                                  (5.9)

This is a direct equation-level application of the assigned partner result.

In particular, whenever

`kappa >= c s(A)`                                                    (5.10)

for some fixed `c>0`, the entire majority contribution is paid by

`pi sqrt(2)/c`,                                                      (5.11)

and the only remaining contribution from that block is the minority/two-sheet annular mass.

For a definite physical triple, the earlier local `account02/B15` block theorem instead gives the full conditional density bound

`||p_Q||_infinity <= C_3/kappa`, `C_3=2pi+3sqrt(3)`,                (5.12)

so the full annulus is paid at the corresponding matrix-dependent scale. Equation (5.9) is specifically useful in the indefinite case because it isolates exactly the two-sheet part rather than discarding the already-paid one-sheet geometry.

## 6. Consequence for the current proof map

Taking `R=4`, define

`F(A,f,y)=[s(A)/2]P{Q_A in (y-2,y-1) union (y+1,y+2)}`.             (6.1)

Then

`boxed{ C_* = sup_{target A,f; y>=4} F(A,f,y). }`                   (6.2)

Every event in (6.1) lies in the positive-output region `Q_A>2`. The test also removes the unit center band `|Q_A-y|<=1`. Thus a universal proof may work exclusively on noncritical, fixed-scale shells.

This does **not** make the remaining indefinite geometry trivial. The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` produces arbitrarily large two-sheet traces at noncritical levels for arbitrary joint projected densities, so moving away from the cone vertex does not permit a projection-only estimate. Product provenance remains essential.

Combining (6.2) and (5.9), the unpaid indefinite physical-block implication can be written cleanly as follows: control

`[s(A)/2] P{Q_A in S_y, Min}`                                       (6.3)

uniformly on `y>=4`, after aggregating original-coordinate product structure before paying reciprocal near-singular block costs. If a block has `kappa` comparable to `s(A)`, its majority sheet is already uniformly paid by (5.11). If all useful physical blocks are near singular, one must use the fleet's bank/ridge/mixed-frame mechanisms rather than selecting one minor and inverting it.

This is exactly consistent with the current no-pivot and aggregate-before-inversion corrections.

## 7. Logical regularity ledger

The relevant implications are now sharply separated.

1. `A!=0` and an absolutely continuous joint input imply **absolute continuity** of `Q_A` by the elementary coarea/preimage-null argument. This has no height content.
2. `rank(A)>=3` plus the cap-one original product structure imply, for every fixed `A`, an individually bounded density in `C_0(R)` by the completed and independently reviewed B15 regularity theorem. Its bound may depend badly on `A`.
3. The owner conjecture is the strictly stronger uniform statement `sup ||p_A||_infinity<infinity` over the target class.
4. Theorem 4.1 shows that this uniform statement has exactly the same sharp constant as a fixed unit-annulus probability inequality whose centers can be required to satisfy `y>=4`.
5. Equation (5.9) then pays the majority one-sheet part of that exact functional whenever an indefinite physical `3 x 3` block is available, without rotating the product law.

Thus continuity is not being used as a surrogate for the central `L^infinity` estimate; it is used only as a zero-loss localization device for the exact far-center normalization.

## 8. Corrections respected

No step uses:

- law-uniform pointwise quadratic Fourier decay;
- independence after orthogonal diagonalization;
- the false arbitrary-joint rank-three coarea inequality;
- positive moments of worst conditional spectral-projection caps;
- an unrestricted fiber supremum;
- a projection-only X-ray criterion for the two-sheet trace;
- a uniformly conditioned physical minor forced by the three-large-eigenvalue assumption.

Theorem 4.1 is purely based on spectral homogeneity plus the completed fixed-target `C_0` theorem. Equation (5.9) uses original-coordinate conditioning exactly within the stated scope of the assigned-partner ambient one-sheet theorem.

## 9. First unpaid implication after this run

A particularly clean exact target is now

`boxed{
 sup_{s(A)>=1, f_i<=1, y>=4}
 [s(A)/2]
 P{Q_A in (y-2,y-1) union (y+1,y+2)} < infinity.
}`                                                                  (9.1)

By Theorem 4.1, proving (9.1) proves the full universal density theorem with exactly the same optimal constant.

For every well-conditioned indefinite physical triple, its majority component is already bounded by (5.11). The genuinely hard part is therefore to control the minority/two-sheet component in (6.3), or to force an alternative bank/ridge/mixed-frame/definite exit, while keeping original product provenance until after the singular geometry is integrated.

Full QFORM remains OPEN.

## 10. Source/control pins

Fresh control before the substantive write: `yspennstate/math-research-brain@38a94fb87e7d855c60a9fb0b9f23504249d996b6`, OWNER CONTROL revision `2026-09-22.15`; no later B15 stop observed.

Peer mathematical sources were read from the private `yspennstate/math-open-problems` repository at a master state containing the cited immutable paths, with master observed at `0da7f3ef78f89efa33d2014211323fcda3d3214b` before publication.

Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
