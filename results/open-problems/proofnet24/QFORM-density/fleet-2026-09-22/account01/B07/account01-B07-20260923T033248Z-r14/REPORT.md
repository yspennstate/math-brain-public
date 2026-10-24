SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T03:32:48Z.
attacking: coordinate-minor selection by combining the q=4/3 fractional three-volume gate with the designated partner's determinant-marginal core theorem, to force either a <=4x4 physical core or a quantitatively diffuse bi-anchor packet.

# account01/B07 r14 — fractional-volume gate forces a four-coordinate core or a diffuse bi-anchor survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL REDUCTION / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

The full conjecture is not proved here. The result below is a supporting reduction for the existing cross-block third-compound branch. Continuity is proved only in the fractional-volume exit; the bounded physical-core exit below gives essential boundedness from the cited finite-dimensional spectral theorem, not a new continuity claim.

## 1. Sources and correction boundary actually used

Fresh control before publication: `yspennstate/math-research-brain@b843043239faef761d407578ccef778013611d8b`, OWNER CONTROL revision `2026-09-22.15`. Live correction inbox blob: `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

The proof uses these completed/scoped inputs.

1. **Newest fractional three-volume theorem.** `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`, Theorem (10): for an original-coordinate cross block `M`, with `Z=E3(M)>0`, if every row volume marginal `alpha_i<=q/2`, `1<=q<3/2`, then the full ambient quadratic-plus-affine form has a continuous `C_0` density satisfying

`||p_Q||inf <= 3e/[(3-2q)sqrt(q)] Z^(-1/6)`.

All self blocks, outside couplings and affine terms remain arbitrary.

2. **Designated partner account02/B07.** `QFORM-DETERMINANT-MARGINAL-TAIL-CORE-v1`, `yspennstate/math-open-problems@1f5ab2ddba6e99675fb9177666c5e64e396e54e5`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T023322Z-r11/REPORT.md`. For any determinant-weighted packet of physical `3x3` minors of total squared mass `P0`, supports `R0,C0`, and inclusion-marginal tails `delta_R,delta_C` with `theta=1-delta_R-delta_C>0`,

`E3(A[R0,C0]) >= theta P0`.

In the no-pivot class with parameter `tau`, its physical-core receiver gives

`||p_Q||inf <= 2 sqrt(6 pi d) sqrt(binomial(r,3)) p q (tau+tau^2)/sqrt(theta P0)`,

where `p=|R0|`, `q=|C0|`, `r=min(p,q)`, `d=|R0 union C0|`.

3. **Finite-dimensional spectral receiver.** `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Corollary 4.1: on `d` original independent cap-one coordinates, three actual eigenvalues of magnitude at least `sigma` imply

`||p||inf <= 2 sqrt(6 pi d)/sigma`,

uniformly in affine terms.

4. Existing B07 O0 resource used only for the final numerical specialization: `E3(B)>=1/256`, source `yspennstate/math-open-problems@d3f557ea222c6d353a33291a02d39302556728af`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/a01-b07-20260922T200312Z-qform-minors-r12/REPORT.md`.

No pointwise stationary-phase bound, arbitrary-joint coarea bound, post-rotation independence, conditional projection-density positive moment, or reciprocal single-minor selection is used.

## 2. Determinant law and the first exit

Let `B=A[I,J]` be any original-coordinate cross block with `I cap J=empty`, rank at least three, and

`P=E3(B)=sum_{|R|=|C|=3} det(B[R,C])^2>0`.

Normalize the squared minor weights:

`w(R,C)=det(B[R,C])^2/P`.

Let

`alpha_i=P_w(i in R)`, `beta_j=P_w(j in C)`.

Then exactly

`sum_i alpha_i=sum_j beta_j=3`.                                      (2.1)

Apply the newest fractional-volume theorem with `q=4/3`. If

`max_i alpha_i <= 2/3`,                                               (2.2)

then

`boxed: ||p_Q||inf <= (9 sqrt(3)e/2) P^(-1/6).`                       (2.3)

The density is continuous and vanishes at infinity. If instead the column marginals satisfy `max_j beta_j<=2/3`, apply the same theorem after swapping the two original-coordinate banks, i.e. to `B^T`; the identical conclusion follows.

Thus the only branch not already paid by (2.3) has physical anchors `i in I`, `j in J` with

`alpha_i>2/3`, `beta_j>2/3`.                                          (2.4)

Let

`M_ij=sum_{R contains i, C contains j} det(B[R,C])^2`.

Under `w`, the events `i in R` and `j in C` have probabilities `alpha_i,beta_j`. The elementary union bound therefore gives the exact determinant-weighted localization

`boxed: M_ij/P >= alpha_i+beta_j-1 > 1/3,`                            (2.5)

hence

`boxed: M_ij>P/3.`                                                     (2.6)

This is aggregate localization: no individual physical minor is selected or inverted.

## 3. Conditional residual marginals and a <=4x4 core

Condition the determinant law on the event in (2.5), i.e. on triples containing row anchor `i` and column anchor `j`. For residual coordinates define

`rho_k=P(k in R | i in R,j in C)`, `k != i`,
`sigma_l=P(l in C | i in R,j in C)`, `l != j`.

Every selected row triple has exactly two residual rows and every selected column triple exactly two residual columns, so

`sum_{k!=i} rho_k = 2`, `sum_{l!=j} sigma_l = 2`.                     (3.1)

Define the heavy residual supports at the natural half threshold

`R0={i} union {k!=i: rho_k>1/2}`,
`C0={j} union {l!=j: sigma_l>1/2}`.                                  (3.2)

Because the residual marginal sums are two, there can be at most three residual coordinates with marginal strictly above `1/2`. Hence

`boxed: |R0|<=4, |C0|<=4.`                                            (3.3)

Let

`delta_R=sum_{k notin R0} rho_k`,
`delta_C=sum_{l notin C0} sigma_l`.                                  (3.4)

There are now exactly two cases.

### Case A: small residual marginal tail

If

`delta_R+delta_C<1/2`,                                                 (3.5)

apply the designated partner theorem `QFORM-DETERMINANT-MARGINAL-TAIL-CORE-v1` to the anchored packet of total mass `M_ij`. It gives

`E3(B[R0,C0]) >= (1-delta_R-delta_C) M_ij
               > (1/2)(P/3)=P/6`.                                    (3.6)

Therefore a physical cross core of at most `4x4` coordinates carries more than one sixth of the entire third-compound mass.

This is the requested actual application of account02/B07 at an inequality; it does not merely cite the partner result.

### Case B: large residual marginal tail

If

`delta_R+delta_C>=1/2`,                                                 (3.7)

the anchored packet is quantitatively support-diffuse. Every residual coordinate outside the at-most-three heavy residual coordinates on its side has conditional inclusion marginal at most `1/2`, while the combined light marginal currency is at least `1/2`.

A useful mass version follows. Let

`Y=|R\R0|+|C\C0|`

under the conditional anchored law. Then `0<=Y<=4` and

`E Y=delta_R+delta_C>=1/2`.

Hence

`P(Y>=1)>=E Y/4>=1/8`.                                                 (3.8)

Multiplying by the anchored mass (2.6), the original squared-minor packet containing both anchors and at least one light residual coordinate has mass

`boxed: > P/24.`                                                       (3.9)

This is a concrete diffuse bank, not a qualitative statement.

Equations (2.3), (3.6), and (3.7)-(3.9) prove the structural theorem:

> **`QFORM-E3-VOLUME-GATE-FOURCORE-OR-DIFFUSE-BIANCHOR-v1`.** For every original-coordinate cross block with `P=E3(B)>0`, either the full ambient form is continuously density-paid by (2.3), or there are physical row/column anchors carrying `>P/3` of the third-minor mass and then either a `<=4x4` physical cross core carries `>P/6`, or a light residual subpacket carries `>P/24` while every individual light residual inclusion marginal is at most `1/2`.

## 4. N3 numerical specialization: the four-core branch is genuinely paid

Use the live no-pivot parameter `tau=1/128`. For distinct physical coordinates the N3 constraints give

`|A_uv|^2 < tau+tau^2`.

Thus for the core `M=B[R0,C0]` from Case A,

`||M||op^2 <= |R0||C0|(tau+tau^2)
            <=16(1/128+1/128^2)
            =129/1024`.                                               (4.1)

By Cauchy-Binet,

`E3(M) <= binomial(r,3)||M||op^4 s3(M)^2`, `r<=4`.

Using `E3(M)>P/6`, `sqrt(binomial(r,3))<=2`, and (4.1),

`boxed: s3(M) > (512/129) sqrt(P/6).`                                 (4.2)

The symmetric physical principal block on `H=R0 union C0`, `|H|<=8`, has at least three actual eigenvalues of modulus at least the right side of (4.2), by singular-value contraction from the rectangular compression. The finite-dimensional spectral receiver therefore gives

`||p_Q||inf
 <= 2 sqrt(48 pi) * (129/512) sqrt(6/P).`                             (4.3)

On the existing O0 resource `P>=1/256`, this becomes

`boxed: s3(M) >= 32/(129 sqrt(6)) =0.101270893758...`                 (4.4)

and

`boxed: ||p_Q||inf <= (129/16)sqrt(288 pi)
                    =242.516285571... .}`                            (4.5)

This establishes essential boundedness on the physical-core branch. Corollary 4.1 itself proves absolute continuity plus an essential density bound; I do not promote (4.5) to a continuity claim.

On the fractional-volume branch, the same O0 resource gives the much smaller continuous bound

`boxed: ||p_Q||inf <= (9sqrt(3)e/2)256^(1/6)
                    =53.387667941... .}`                             (4.6)

The sole O0 survivor after this run is therefore the support-diffuse bi-anchor branch with

`M_ij>P/3>=1/768`,                                                    (4.7)

and an actual light-residual determinant packet of mass

`>P/24>=1/6144`.                                                      (4.8)

## 5. Stress against the designated partner's exact obstruction

Account02/B07's exact diffuse model

`M_N=[[0,u^T],[v,xy^T]]`

has total third-minor mass one, fixed anchor row and column, and every residual coordinate has conditional inclusion marginal exactly `2/N`. For `N>4`, the heavy sets (3.2) contain only the anchors, so

`delta_R=delta_C=2`.

It lands squarely in Case B, not falsely in a bounded-core branch. This is important: the partner proved that no bounded physical core exists in that family. The new dichotomy respects that obstruction. The partner also showed that this special rank-two-light-block family is paid by its mixed-hub theorem; the live unresolved branch permits arbitrary within-light-bank curvature and therefore remains strictly broader.

## 6. Why this changes the proof map

Previously the O0 third-compound bank was known to carry constant aggregate mass, but the useful local alternatives involved either leverage gates, a selected pair, or a bi-anchor packet whose residual dispersion still had to be classified.

The present argument uses the newest fractional-volume theorem **before** any local reciprocal selection. Consequently:

1. if either side's third-volume law is genuinely diffuse at threshold `2/3`, the full form is already continuously paid;
2. otherwise two physical anchors are automatic and carry at least one third of all third-compound mass;
3. after those anchors, the designated partner theorem converts small residual marginal tails into an actual `<=4x4` physical core, which N3 pays by a dimension-eight spectral estimate;
4. the only survivor has a quantitative light-residual determinant packet with every individual light marginal at most one half.

Thus coordinate-minor selection is reduced to a sharply described **bi-anchor + residual diffusion + arbitrary curvature** problem; no universally good single minor is asserted.

## 7. First unpaid implication

The next precise B07 obligation is

**`QFORM-DIFFUSE-BIANCHOR-CURVATURE-PAYMENT-v1`.** In N3, start from physical anchors `i,j` carrying third-minor mass `M_ij>P/3` and a conditional residual packet satisfying `delta_R+delta_C>=1/2`, with every light residual row/column inclusion marginal at most `1/2`. Prove a product-preserving density or half-Riesz bound while retaining arbitrary within-light-bank quadratic curvature and the full remaining spectrum.

The determinant mass `>P/24` in (3.9) is the available diffuse currency. The designated partner's exact rank-two-light-block stress is already paid, so the new work must exploit the arbitrary-curvature residual rather than delete it, rotate it, or call it a small random perturbation.

A natural next mechanism is to apply Weyl differencing only to same-bank curvature while keeping the two original anchors unsquared, and then route the surviving light determinant law through the q-dependent Brascamp-Lieb exponents. This remains unproved here.

## 8. Verification and review status

`check_core_or_diffuse.py` and `check_results.json` in this run directory enumerate 60 random rank-at-least-three packet examples and verify the determinant-law identities, joint-anchor lower bound, heavy-set cardinalities, partner core inequality in every triggered small-tail case, and the constants (4.1)-(4.6). Terminal marker: `QFORM_CORE_OR_DIFFUSE_CHECK_PASS`. These finite checks are not a universal proof.

Independent end-to-end review of the theorem in this report is **not claimed**. Full QFORM and global continuity remain OPEN.
