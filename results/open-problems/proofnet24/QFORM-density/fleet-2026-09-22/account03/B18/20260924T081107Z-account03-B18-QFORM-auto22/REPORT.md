# account03/B18 auto22 — full cross-bank payment collapses the two-sided-anchor survivor to a rank-one collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T081107Z-account03-B18-QFORM-auto22`  
**Status:** `PROVED SUPPORTING REDUCTION / PRIOR ANALYTIC RECEIVER APPLIED / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Continuity:** essential boundedness only for the generic result below; no generic continuity assertion.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-24T08:11:07.709626Z.

attacking: literature-to-proof transfer for the remaining near-rank-two entangled carrier; seek a source-valid small-ball/fractional-moment inequality that retains nonzero anchors and arbitrary same-side curvature.

## 1. Target and correction discipline

The owner target is unchanged. For arbitrary independent real original coordinates with probability densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `Q=X^T A X`, or give a valid counterexample. Continuity is an additional requested conclusion and is tracked separately.

No Gaussian, log-concave, moment, compact-support, connected-support, iid, centering, symmetry, smoothness, or diagonal-basis assumption is added below. No rotated coordinates are declared independent. The proof does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, conditional-density-cap-as-independence, positive moments of worst conditional projection caps, deletion of a small nonzero coefficient, or a forced uniformly good fixed physical minor.


## 2. Primary literature transfer and prior receiver

The primary theorem is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1. If

`f(x)=prod_i f_i(x_i)`, `int f_i=1`, and `||f_i||_infinity<=1`,

then every `k`-dimensional orthogonal marginal has density cap at most `2^(k/2)`. In particular, a normalized scalar projection has density cap at most `sqrt(2)` and a two-dimensional orthogonal projection has joint-density cap at most `2`. The source imposes none of the forbidden moment, support, iid, log-concavity, centering, or smoothness hypotheses.

This primary theorem was already transferred by this slot in the completed result

`QFORM-ONE-SIDED-CROSS-NEGATIVE-MOMENT-v1`,

scientific commit `a2cf029c5c935d6eadf4216c073911fc8dc404ac`, exact report

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260924T005514Z-account03-B18-QFORM-auto15/REPORT.md`.

I make **no novelty claim** for that analytic receiver. The new work in this run is to apply it to the entire live two-sided-anchor packet of account04/B18, where the anchor variable belongs to the opposite ORIGINAL-coordinate product bank. This removes the apparent rank-two collar from that packet and replaces it by a rank-one collar.

For completeness, the exact two-dimensional receiver is rederived next so that the splice is auditable without any hidden independence assumption.

## 3. Source-valid full-cross receiver

Let `X in R^m` and `Z in R^N` be two disjoint banks of ORIGINAL independent coordinates, each scalar density bounded by one. Let `D` be an `m x N` real matrix with singular values

`d1 >= d2 > 0`,

and let `alpha in R^m` and measurable `G:R^N->R` be arbitrary. Put

`T = 2 X^T D Z + alpha^T X + G(Z)`.

Then `T` has a density and

`||p_T||_infinity <= 2 sqrt(pi) / sqrt(d1 d2)`.                 (3.1)

No continuity claim is made by this argument.

### Proof

Condition on the genuine original-coordinate bank `Z=z`. The conditional variable is

`(2Dz+alpha)^T X + G(z)`.

By the one-dimensional Livshyts--Paouris--Pivovarov/Rogozin--Ball marginal bound,

`||p_(T|Z=z)||_infinity <= sqrt(2)/||2Dz+alpha||`               (3.2)

whenever the coefficient is nonzero.

Let `U_2,V_2` be the top two left/right singular frames of `D`, and write `Sigma_2=diag(d1,d2)`. Projection of a vector cannot increase its norm, so

`||2Dz+alpha|| >= ||2 Sigma_2 V_2^T z + U_2^T alpha||`.         (3.3)

The random vector `V_2^T Z` is a two-dimensional orthogonal marginal of a genuine product density; LPP gives its joint-density cap at most `2`. Hence

`W = 2 Sigma_2 V_2^T Z + U_2^T alpha`

has density cap

`H <= 2 / det(2 Sigma_2) = 1/(2 d1 d2)`.                       (3.4)

For any probability density on `R^2` bounded by `H`, the centered radial bathtub principle gives

`E |W|^(-1) <= 2 sqrt(pi H)`.                                  (3.5)

Indeed the maximizing density is `H` on the centered disk of area `1/H`. Combining (3.2)--(3.5),

`||p_T||_infinity`
` <= sqrt(2) E ||2DZ+alpha||^(-1)`
` <= sqrt(2) E |W|^(-1)`
` <= sqrt(2) * 2 sqrt(pi/(2 d1 d2))`
` = 2 sqrt(pi)/(d1 d2)^(1/2).`

The finite majorant also shows that the exceptional affine set on which `2Dz+alpha=0` has zero `Z`-probability. Mixing the conditional densities proves absolute continuity and (3.1). QED.

This is precisely the `k=2` specialization of the prior auto15 theorem after the physical quadratic normalization `M=2D`.

## 4. New synthesis: `QFORM-TWOSIDED-ANCHOR-FULLCROSS-PAY-OR-RANK1-COLLAR-v1`

Use the exact physical packet from account04/B18 r6. Let `X`, `Y`, and scalar `W` be disjoint ORIGINAL-coordinate banks, and after conditioning any other original coordinates write

`A_S = [[0, C, r], [C^T, B, h], [r^T, h^T, a]]`,              (4.1)

where `B,h,a` are completely arbitrary. Equivalently, with the opposite product bank

`Z=(Y,W)`

and the full cross matrix

`D=[C r]`,

we have

`Q = 2 X^T D Z + alpha^T X + G(Z)`                            (4.2)

for an arbitrary measurable quadratic-plus-affine `G` on the `Z` bank. Thus (3.1) applies to the **whole** anchor packet, not merely to the component of `C` transverse to `r`.

Let `d1>=d2>=...` be the singular values of `D=[C r]`. For every threshold `theta>0`, the packet obeys the exhaustive dichotomy

`d1 d2 >= theta`

implies

`||p_Q||_infinity <= 2 sqrt(pi)/sqrt(theta)`,                  (4.3)

while

`d1 d2 < theta`

implies

`dist_op(D,{R:rank R<=1}) = d2 < sqrt(theta)`.                 (4.4)

### Proof of the structural alternative

The paid branch is (3.1). On the other branch, `d2<=d1`, hence

`d2^2 <= d1 d2 < theta`,

so `d2<sqrt(theta)`. Eckart--Young gives exactly

`dist_op(D,rank<=1)=d2`.

This proves (4.4). QED.

At the live numerical threshold `theta=2^(-12)`, either

`||p_Q||_infinity <= 128 sqrt(pi) = 226.874092915906...`,       (4.5)

or

`dist_op([C r], rank<=1) < 1/64`.                              (4.6)

The result retains arbitrary `B,h,a`, arbitrary signs, arbitrary input tails, and arbitrary outside spectrum/couplings converted to affine terms by conditioning ORIGINAL coordinates.

## 5. Exact comparison with the designated partner account04/B18 r6

The completed designated-partner result is

`QFORM-TWOSIDED-ANCHOR-PAY-OR-RANK2-COLLAR-v1`,

`yspennstate/math-open-problems@48c914d1bd070cad090d6d5deac743bd8465bc15`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260924T032058Z-account04-B18-QFORM-r6/REPORT.md`.

For `r!=0`, let `P_r` be projection in the `X` coefficient space onto `r^perp` (and `P_r=I` for `r=0`). If `c1>=c2` are the top singular values of `P_r C`, the partner theorem proves

`c1 c2 >= theta  =>  ||p_Q||_infinity <= 2 sqrt(2 pi)/sqrt(theta)`, (5.1)

and otherwise

`dist_op([C r], rank<=2) < sqrt(theta)`.                        (5.2)

The present source transfer applies directly to the same physical packet. More precisely,

`P_r C = P_r D J`,

where `J` is the isometric inclusion of the `Y` column space into the `Y plus W` column space. Since left and right multiplication by contractions cannot increase any singular value,

`c_j <= d_j` for every j, and in particular

`c1 c2 <= d1 d2`.                                               (5.3)

Therefore every packet paid by the partner's transverse gate is also paid by (4.3), with the smaller constant `2 sqrt(pi)` in place of `2 sqrt(2 pi)`. More importantly, packets entering the partner's rank-two collar can still be paid whenever their **full** cross matrix has two-dimensional volume. Only a rank-one collar survives (4.4).

At `theta=2^(-12)`, the combined statement is therefore:

`either ||p_Q||_infinity <=128 sqrt(pi),`

`or dist_op([C r],rank<=1)<1/64`.                              (5.4)

This is the requested equation-level application of a completed account04/B18 result: its live two-sided-anchor packet is taken as the input geometry, its transverse singular values are compared to the full cross singular values by (5.3), and its rank-two survivor is sharpened to a rank-one survivor by the source-valid full-bank receiver.

This synthesis means duplicate effort on the **near-rank-two** carrier is unnecessary for this exact zero-`X-X` source geometry. The successor geometry is the exact/near-rank-one full cross carrier with arbitrary complement curvature, while retaining the nonzero tail exactly.

## 6. Concrete owner-target witness inside the partner's former rank-two collar

Reuse the already source-checked target family from auto15,

`A_t = [[0,0,1,0],`
`       [0,0,0,1],`
`       [1,0,t,0],`
`       [0,1,0,0]],      t>=0`.                                (6.1)

Take `X=(X1,X2)`, `Y=(Y1)`, `W=X4`, so

`C=e1`, `r=e2`, `D=[C r]=I_2`, `B=[t]`, `h=0`, `a=0`.

The spectrum is the union of `{+1,-1}` and the two roots

`lambda^2-t lambda-1=0`.

For every `t>=0`, the positive root is at least one, so the form has at least three eigenvalues of modulus at least one and is a literal owner-target family.

For the partner transverse geometry, `P_r C=C` has rank one, hence

`c2=0`.

Thus the partner paid gate (5.1) is unavailable and the packet sits in its exact rank-two survivor: `D=I_2` has rank two. But the full-bank theorem sees

`d1=d2=1`

and gives the uniform target-level bound

`||p_(X^T A_t X)||_infinity <= 2 sqrt(pi)`
`                           = 3.5449077018110318...`             (6.2)

for every `t>=0` and every admissible cap-one product law.

This example is not claimed as a new family; it was already used in auto15. Its role here is to show concretely that the account04/B18 rank-two collar contains packets that are completely paid once the anchor `W` is grouped with `Y` **before** selecting transverse singular directions.

## 7. Literature scope audit

The only external theorem promoted to a premise here is LPP Theorem 1.1, whose product-density hypotheses match the owner input exactly. The report does not use results requiring moments or smoothness. In particular, the current quadratic-form regularity literature with iid/smooth Gaussian-functional hypotheses is not imported as a solution of the arbitrary rough non-iid target.

A fresh repository search did not find a prior fleet report explicitly making the rank-two-to-rank-one collar splice (4.3)--(4.6) for the account04/B18 packet. That search miss is **not** a claim of external novelty. The analytic receiver itself is explicitly prior fleet work.

## 8. What remains

The unrestricted conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Unrestricted continuity also remains open.

For the live two-sided-anchor packet with zero `X-X` block, however, the first unpaid geometry is now strictly narrower:

1. `D=[C r]` is exact rank one, with arbitrary quadratic curvature on the opposite product bank; or
2. `D` has a small but nonzero second singular value and lies in a fixed operator-norm collar of rank one, and that tail must be retained exactly.

The bare global hypothesis `s_3(A)>=1` does not itself force this zero-self source packet, so a full proof still needs the global product-preserving compiler. Within this packet, the natural next step is to combine the existing exact rank-one active-plane receiver with an arbitrary complement-active dimension argument, or derive a source-valid fractional smoothing estimate uniform as `d2 downarrow0` without deleting the `d2` tail.

## 9. Checks

The finite algebra checks used in this report are:

- `128 sqrt(pi) = 226.87409291590603`;
- `128 sqrt(2 pi) = 320.84841915276803` (partner r6 reference constant);
- `2 sqrt(pi) = 3.5449077018110318`;
- for (6.1), numerical spectra at `t=0,1,10` are respectively `{-1,-1,1,1}`, `{-1,-0.61803399,1,1.61803399}`, and `{-1,-0.09901951,1,10.09901951}`, matching the exact block factorization.

These numerical checks only verify algebra/constants; they are not evidence for the universal conjecture.

## 10. Source pins

- Primary: Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1.
- Prior exact receiver: `yspennstate/math-open-problems@a2cf029c5c935d6eadf4216c073911fc8dc404ac`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260924T005514Z-account03-B18-QFORM-auto15/REPORT.md`.
- Designated partner: `yspennstate/math-open-problems@48c914d1bd070cad090d6d5deac743bd8465bc15`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260924T032058Z-account04-B18-QFORM-r6/REPORT.md`.

Manual changed-file review found only mathematical/source metadata in this report. No credentials, account secrets, scheduler IDs, personal archives, or unrelated data are included. A repository-local automated secret scanner was not exposed through the connector in this run, so this was a narrow manual fallback review of the exact changed file.
