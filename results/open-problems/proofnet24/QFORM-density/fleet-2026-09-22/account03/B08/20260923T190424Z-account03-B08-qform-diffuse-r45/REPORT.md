SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T19:04:24Z.
attacking: the r44 nonzero common-plane edge/tail by exact physical-hub Schur completion: prove the tail cannot cancel a full-rank common-plane mismatch, and pay the exact zero-hub-curvature endpoint without moment assumptions.

# account03/B08 r45 — tail-immune common-plane Schur mismatch and zero-hub arbitrary-edge receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Owner control at startup / pre-write refresh: revision `2026-09-22.15`, QFORM only  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW SUPPORTING THEOREMS / FULL QFORM OPEN`  
Continuity: proved on the zero-hub theorem below; the Schur-mismatch theorem gives essential boundedness only.

The full owner target remains open. Every random coordinate below is an ORIGINAL independent coordinate with one-dimensional density bounded by one. No moments, Gaussianity, log-concavity, bounded or connected support, post-rotation independence, arbitrary-joint coarea, coefficient-small random-error deletion, law-uniform pointwise quadratic-phase decay, or one-good-minor selection is used.

## 1. Source-pinned incoming state

The immediate B08 predecessor is

`yspennstate/math-open-problems@b67617d493939430685adfa2ebf5e943d9094b56`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T181656Z-account03-B08-qform-diffuse-r44/REPORT.md`.

Its exact two-arm theorem pays the vanishing light-light edge/tail branch continuously, and its incoming r43 common-plane state retains two physical hub coordinates `H`, two disjoint original-coordinate banks `J_1,J_2`, full-row-rank physical hub arms

`M_r=A[H,J_r] in R^(2 x m_r)`,

with

`S_r := s_1(M_r)s_2(M_r) > L^2/(64 sqrt(896)),  r=1,2.`          (1.1)

The r43 structural source is

`yspennstate/math-open-problems@87f0f4b7b8a9b5dc4f1050ecef61e527dac7a541`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T172004Z-account03-B08-qform-diffuse-r43/REPORT.md`.

Write `P_r` for the orthogonal projection in `R^(J_r)` onto `row(M_r)`. Its common-plane branch gives the EXACT decomposition

`C:=A[J_1,J_2] = M_1^T R M_2 + T`,                              (1.2)

with a deterministic `2 x 2` matrix `R` and

`P_1 T P_2 = 0.`                                                  (1.3)

The predecessor also has `||T||_F<L/8`, but the main theorem of this run will not use that smallness at all.

The analytic receiver used below is B08's completed post-Schur aggregate-E2 theorem from

`yspennstate/math-open-problems@3c4c6882813d9530dc5c3884ce3e25f5993c7062`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T115108Z-account03-B08-qform-diffuse-r36/REPORT.md`.

For an ACTUAL original-coordinate invertible indefinite physical pair `B`, put

`Delta=|det B|`, `kappa=sigma_min(B)`.

If the exact Schur remainder contains a literal physical cross block `N` with

`Gamma=E_2(N):=e_2(NN^T)>0`,

then

`||p_Q||_infinity
 < C_pair Delta^(-9/38) kappa^(-5/19) Gamma^(-5/76),`             (1.4)

where

`C_pair=16.510052499365923... .`                                  (1.5)

This source retains arbitrary remaining same-bank curvature and couplings. It proves essential boundedness, not continuity.

The current owner/Claude continuation `c4c23b784395630c094ba299a50712209921d1ae` was also read. Its proposed adapted single-hub `(SP)` estimate remains explicitly open; it is not used here.

## 2. First essential implication: the physical tail cannot cancel a full-rank common-plane Schur mismatch

Let the actual physical two-hub principal block be

`B=A[H,H] in R^(2 x 2)`,                                         (2.1)

and first assume `B` is invertible. Exact completion of the two physical hub coordinates changes the `J_1-J_2` cross block to

`C_B = C - M_1^T B^(-1) M_2`.                                   (2.2)

Using (1.2),

`C_B = M_1^T K M_2 + T`,
`K := R - B^(-1).`                                                (2.3)

Choose orthonormal two-frames `U_r in R^(m_r x 2)` spanning `row(M_r)` and put

`N_r=M_r U_r in R^(2 x 2).`                                      (2.4)

Then `N_r` is invertible and

`|det N_r| = sqrt(det(M_rM_r^T)) = S_r.`                          (2.5)

Because (1.3) is exact,

`U_1^T T U_2=0.`                                                  (2.6)

Therefore the exact row-space compression of the post-Schur physical cross block is

`U_1^T C_B U_2 = N_1^T K N_2.`                                   (2.7)

This identity is the key point: the retained physical tail `T`, no matter how large outside the common plane, has ZERO component in the only compression used below.

### Lemma 2.1 — `QFORM-COMMONPLANE-SCHUR-MISMATCH-E2-v1`

For the post-Schur physical cross block (2.2),

`boxed:
 E_2(C_B) >= S_1^2 S_2^2 |det(R-B^(-1))|^2.
`                                                                    (2.8)

#### Proof

Extend `U_1,U_2` to orthogonal bases of their physical bank spaces. The quantity `E_2(C_B)` is invariant under left/right orthogonal changes of basis and, by Cauchy--Binet, is the sum of the squares of ALL physical `2 x 2` minors in the new bases. Hence it is at least the square of the leading `2 x 2` compression minor:

`E_2(C_B) >= |det(U_1^T C_B U_2)|^2.`                            (2.9)

By (2.7),

`det(U_1^T C_B U_2)
 =det(N_1) det(K) det(N_2).`                                      (2.10)

Use (2.5) and `K=R-B^(-1)` to obtain (2.8). QED.

This is deliberately not a claim that arbitrary pre-Schur E2 survives a Schur update. It is a new exact compression identity for the special common-plane decomposition (1.2)-(1.3), and is therefore compatible with the live Schur-cancellation corrections.

## 3. Full ambient receiver for an indefinite physical hub pair

Assume now that the actual physical hub block `B` is invertible INDEFINITE. Let

`Delta=|det B|`, `kappa=sigma_min(B)`,
`K=R-B^(-1)`, and suppose `det K !=0`.                             (3.1)

Apply the source theorem (1.4) to the exact Schur remainder using the literal physical `J_1-J_2` cross block `C_B`. Lemma 2.1 gives

`Gamma=E_2(C_B)>=S_1^2S_2^2|det K|^2.`                            (3.2)

### Theorem 3.1 — `QFORM-R2-COMMONPLANE-SCHUR-MISMATCH-LEAKAGE-STABLE-v1`

Under the preceding hypotheses, the FULL ambient quadratic form has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 < 16.511 Delta^(-9/38) kappa^(-5/19)
   [S_1 S_2 |det(R-B^(-1))|]^(-5/38).
`                                                                    (3.3)

Arbitrary same-bank curvature, all other Schur-remainder coefficients, outside conditioned couplings, and the entire physical tail `T` are retained. The bound does NOT contain `||T||`; in particular it remains valid for the r43 state without using `||T||_F<L/8`.

#### Quantitative r43 normalization

Put

`s_* := 1/(64 sqrt(896)) = 0.0005219946131102039... .`            (3.4)

Then (1.1) gives `S_r>s_*L^2`. Suppose additionally

`kappa>=tau L`,
`delta := L^2 |det(R-B^(-1))| >0.`                                (3.5)

Because `Delta>=kappa^2`, (3.3) yields

`boxed:
 ||p_Q||_infinity
 < 120.649 tau^(-14/19) delta^(-5/38) L^(-1).
`                                                                    (3.6)

Using the unrounded source constant gives

`120.64811862204725...`                                           (3.7)

in place of `120.649`.

The dimensions check exactly: `S_1S_2 det K` has coefficient scale two, and together with the powers of `Delta` and `kappa` the total homogeneity in `L` is `-1`.

Continuity is NOT claimed for Theorem 3.1 because the analytic source (1.4) currently proves essential boundedness only.

### Definite hub pair

If the same actual physical `B` is invertible definite, the direct two-coordinate ellipse estimate already gives

`||p_Q||_infinity <= pi/sqrt(|det B|).`                            (3.8)

Thus if `kappa>=tau L`,

`||p_Q||_infinity <= pi/(tau L).`                                 (3.9)

So the genuinely difficult invertible-pair portion of the common-plane chamber is indefinite and close to the Schur-matched surface `det(R-B^(-1))=0`.

## 4. Exact zero hub curvature: arbitrary edge and arbitrary physical tail are paid continuously

There is another endpoint where the nonzero light-light edge causes no difficulty at all.

Assume

`B=A[H,H]=0`                                                      (4.1)

on the two actual physical hubs. Condition on all original coordinates outside `H union J_1 union J_2`. Any resulting hub-linear term can be absorbed into a deterministic translation of the vector below. The remaining form is

`Q = G(X,Y) + 2 H^T W(X,Y)`,                                     (4.2)

where `G` is an ARBITRARY quadratic-affine function of the two light banks, including their full common-plane edge, the physical tail `T`, all same-bank curvature and induced affine terms, while

`W=M_1 X + M_2 Y + eta`,                                         (4.3)

for a deterministic `eta in R^2` depending on the conditioned coordinates.

The two random vectors `M_1X` and `M_2Y` are independent. The same source-pinned two-dimensional projection bound used in r44 gives

`||p_(M_r X_r)||_infinity <= 2/S_r.`                              (4.4)

Therefore the convolution law of `W` has a two-dimensional density bounded by

`M_W <= min(2/S_1,2/S_2)=2/max(S_1,S_2).`                         (4.5)

### Lemma 4.1 — reciprocal radius for a bounded two-dimensional density

If a random vector `W in R^2` has probability density at most `M`, then

`E ||W||^(-1) <= 2 sqrt(pi M).`                                   (4.6)

#### Proof

Among all densities bounded by `M` and having mass one, the radially decreasing kernel `|w|^(-1)` is maximized by placing density `M` on the centered disk of area `1/M`. If its radius is `r=(pi M)^(-1/2)`, then

`M int_(|w|<=r) |w|^(-1)dw
 = M * 2pi r
 = 2 sqrt(pi M).`                                                (4.7)

Equivalently this follows from the bathtub principle/layer-cake argument. QED.

### Theorem 4.2 — `QFORM-ZERO-TWOHUB-ARBITRARY-LIGHT-EDGE-v1`

Under (4.1)-(4.3), with both physical arms of row rank two,

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(pi/max(S_1,S_2)).
`                                                                    (4.8)

Moreover `Q` has a continuous density in `C_0(R)`.

#### Proof

Condition on the complete light state `(X,Y)`. For a realized `W=w !=0`, the random part in the two independent cap-one physical hubs is

`2w_1H_1+2w_2H_2`.                                                (4.9)

Conditioning one hub coordinate and then convolving with the other shows that its density is bounded by

`1/[2 max(|w_1|,|w_2|)] <=1/(sqrt(2)||w||).`                     (4.10)

Because `W` has a two-dimensional density, `P(W=0)=0`. Averaging (4.10) and applying Lemma 4.1 with (4.5) gives

`||p_Q||_infinity
 <= (1/sqrt(2))*2 sqrt(pi M_W)
 <= 2 sqrt(pi/max(S_1,S_2)),`                                    (4.11)

which is (4.8).

For almost every `w`, both coordinates of `w` are nonzero, and the conditional density in (4.9) is a convolution of two scaled `L^1` densities, hence belongs to `C_0(R)`. The bound in (4.10) is integrable over the light state by (4.6). Dominated convergence therefore gives a continuous `C_0` representative after averaging over the arbitrary shift `G(X,Y)` and then over the previously conditioned original coordinates. QED.

#### r43 numerical scale

Using `max(S_1,S_2)>s_*L^2` gives

`boxed:
 ||p_Q||_infinity < 155.158/L,
 p_Q in C_0(R).
`                                                                    (4.12)

The exact constant from (3.4) is

`2 sqrt(pi/s_*)=155.1571956381265... .`                           (4.13)

This branch is completely insensitive to the common-plane matrix `R` and the physical tail `T`. Thus the r44 leakage problem is now fully closed when the physical two-hub quadratic block vanishes exactly.

## 5. What has actually been removed from the r44 obstruction

For the r43/r44 two-arm common-plane state, the nonzero physical light-light edge/tail is no longer by itself the obstruction.

1. **Exact zero physical hub curvature `B=0`:** arbitrary common-plane edge, arbitrary physical tail and arbitrary light-bank curvature are paid continuously by (4.12).
2. **Invertible definite physical hub pair with `sigma_min(B)>=tau L`:** paid by (3.9).
3. **Invertible indefinite physical hub pair with `sigma_min(B)>=tau L` and full-rank Schur mismatch `det(R-B^(-1)) !=0`:** paid by (3.6), with the physical tail unable to cancel the decisive compressed E2.

The surviving finite-dimensional common-plane debt is therefore concentrated on:

- singular or near-singular nonzero physical hub blocks;
- indefinite pairs near the Schur-matched hypersurface `det(R-B^(-1))=0`;
- especially rank-one Schur mismatch, where one common-plane direction survives but the determinant currency vanishes.

Those states must still be combined with the retained original-coordinate product provenance. No claim is made that they are solved here.

## 6. Designated partner account04/B08 applied at an actual inequality

The designated partner result is

`QFORM-ANISOTROPIC-RANK1-E2-DIRECTSUM-RECEIVER-v1`

from

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T091414Z-account04-B08-QFORM-r1/REPORT.md`.

For its exact anisotropic family

`Q_(R,L)=L X_0^2 + 2LR U_1V_1 + 2L R^(-1) U_2V_2`, `R>=3`,       (6.1)

scaling the partner's proved `L=1` theorem gives the actual inequality

`boxed: ||p_(Q_(R,L))||_infinity < 7.251/L.`                     (6.2)

This endpoint is maximally localized and anisotropic. It complements the present run: Theorem 4.2 handles the opposite two-hub diffuse geometry with arbitrary light-light coupling when hub curvature vanishes, while Theorem 3.1 handles full-rank Schur mismatch under arbitrary retained tail.

No extension of the partner theorem beyond its stated direct-sum scope is made.

## 7. Correction safety

The new argument uses only original-coordinate conditioning/completion and deterministic orthogonal frames for coefficient algebra. The frames `U_r` are never treated as producing independent random coordinates.

Theorem 3.1 does NOT assert that pre-Schur aggregate E2 survives. It computes one exact post-Schur compression that the r43 tail cannot alter because `P_1TP_2=0`, and only then applies the post-Schur E2 theorem.

Theorem 4.2 does not discard a small coefficient tail or use moments. It allows the full light quadratic function `G(X,Y)` to be arbitrary because it is frozen when the two physical hubs are conditioned last.

No law-uniform scalar pointwise oscillatory decay, arbitrary-joint coarea bound, conditional-density-cap-to-independence step, fiber supremum, or numerical extremality premise appears.

## 8. Regression checks

A companion exact-algebra/numerical regression script generates random full-row-rank physical arms, random indefinite hub pairs, arbitrary common-plane matrices and arbitrary tails projected to satisfy `P_1TP_2=0`. Over 5,000 seeded tests it checks

`U_1^T C_B U_2 = N_1^T(R-B^(-1))N_2`                             (8.1)

and

`E_2(C_B) >= |det(N_1^T(R-B^(-1))N_2)|^2.`                       (8.2)

Observed:

- maximum compression identity error: `2.842170943040401e-14`;
- minimum observed E2/compression-minor-square ratio: `0.9999999994970219`;
- violations: `0`;
- normalized mismatch constant: `120.64811862204725`;
- zero-hub r43 constant: `155.1571956381265`.

These are regression checks only; the proofs above are analytic.

## 9. Remaining implication

The unrestricted conjecture remains **OPEN / NOT DISPROVED**. Full-target continuity remains open.

The next B08 target is now sharper:

`QFORM-R2-SCHUR-MATCHED-RANK1-OR-SINGULAR-HUB-RECEIVER-v1`.

Starting from the same physical two-arm state, pay the finite-dimensional cases in which the two-hub block is singular/near singular or the exact mismatch `R-B^(-1)` has rank at most one, while retaining the complete light-bank curvature, the physical tail, arbitrary rough cap-one laws and all unused spectrum. The exact-zero `B` endpoint should be treated as already paid by Theorem 4.2 rather than folded back into that debt.

A full candidate still needs every target quantifier and two independent end-to-end reviews.
