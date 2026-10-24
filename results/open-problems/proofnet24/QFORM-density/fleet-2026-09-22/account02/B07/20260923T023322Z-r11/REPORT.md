SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T02:33:22Z.
attacking: bounded-dimensional spectral receiver integrated with determinant-weighted coordinate-core extraction; isolate and stress the genuinely diffuse bi-anchor survivor without selecting one tiny minor.

# account02/B07 r11 — determinant marginal tails give a real physical core; exact diffuse bi-anchor obstruction is mixed-hub paid

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `ESSENTIAL_STEP_APPLIED / BOUNDED-MARGINAL-TAIL CORE PAID / INTERMEDIATE CORE-EXTRACTION OBSTRUCTION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and live correction boundary

The target remains the unrestricted theorem: independent original real coordinates with marginal probability densities bounded by one, arbitrary dimension, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moments, support bound, log-concavity, iid assumption, spectral-coordinate independence, or post-rotation product assumption is introduced. Essential boundedness is the target; continuity is separate.

The proof below respects the current corrections: no law-uniform pointwise quadratic-phase decay, no arbitrary-joint three-dimensional coarea cap, no conditional projection-density-moment gate, and no assertion that global compound mass contains one universally useful physical minor.

## 2. Sources actually used

1. Required e5 source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. I use its proved Theorem MF exactly at its diagonal-plus-low-rank light-block scope. If `H` is a heavy physical set, `A_LL=D_L+S Lambda S^T`, and the mixed Gram `Gamma` has physical row leverages at most `1/2`, then

`|phi(t)| <= (4 pi)^(|H|+r/2) 2^(-|H|) |t|^(-|H|-r/2) prod |lambda_k|^(-1/2) det(Gamma)^(-1/2)`.

2. Finite-dimensional spectral receiver: `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Corollary 4.1. On `d` independent cap-one ORIGINAL coordinates, if the actual symmetric quadratic matrix has three eigenvalues of modulus at least `sigma`, uniformly over arbitrary affine terms,

`||p_q||_infinity <= 2 sqrt(6 pi d)/sigma`.                         (2.1)

3. Designated partner account03/B07, latest completed r21b: `yspennstate/math-open-problems@614efa23e499755678e37d2825a10938074a7021`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T013716Z-account03-B07-qform-r21b/REPORT.md`. It supplies colored third-compound packet masses

`P0>=1/5184, P1>=1/3125, P2>=1/512, P3>=1/18`,                       (2.2)

and the positive-motif ledger plus the exact singular-q2 pair-star factorization. I use (2.2) below to turn bounded determinant-marginal tails into actual physical spectral cores. This application is before any reciprocal local-pair payment.

The current sufficient no-pivot class uses `tau=1/128`; hence for distinct original coordinates

`|A_uv|^2 < tau+tau^2`, and `|A_uu|<tau`.                           (2.3)

## 3. First unpaid implication attacked immediately

The coordinate-minor problem is not merely to find one nonzero determinant. The correct bounded-dimensional question is:

> If a constant third-minor packet is mostly carried by bounded sets of physical row and column coordinates, does that aggregate fact itself force a true bounded physical spectral core?

Yes, with an exact quantitative answer that never selects an individual minor.

## 4. `QFORM-DETERMINANT-MARGINAL-TAIL-CORE-v1`

Let `R,C` be physical coordinate banks and let `P>0` be the squared determinant mass of any selected packet of physical `3x3` minors `A[S,T]`, `S subset R`, `T subset C`:

`P = sum_(S,T in packet) det(A[S,T])^2`.

Normalize to the determinant law

`w(S,T)=det(A[S,T])^2/P`.

For physical subsets `R0 subset R`, `C0 subset C`, define the determinant-inclusion marginal tails

`delta_R = sum_(i in R\R0) P_w(i in S)`,
`delta_C = sum_(j in C\C0) P_w(j in T)`,
`theta = 1-delta_R-delta_C`.

Assume `theta>0`. Then

`boxed:
 Z_3(A[R0,C0]) >= theta P,
`                                                                    (4.1)

where `Z_3(M)=sum_{|S|=|T|=3} det(M[S,T])^2=e_3(M M^T)`.

### Proof of (4.1)

By the union bound under `w`,

`P_w(S not subset R0 or T not subset C0)
 <= E_w |S\R0| + E_w |T\C0|
 = delta_R+delta_C`.

Therefore the packet mass whose entire row triple lies in `R0` and entire column triple lies in `C0` is at least `theta P`. Those minors are among the terms defining `Z_3(A[R0,C0])`. QED.

Now put

`p=|R0|`, `q=|C0|`, `r=min(p,q)>=3`, `M=A[R0,C0]`, `L=||M||op`.

If `s_1>=...>=s_r` are the singular values of `M`, Cauchy-Binet gives

`Z_3(M)=sum_(a<b<c) s_a^2 s_b^2 s_c^2
       <= binom(r,3) L^4 s_3(M)^2`.

Thus

`boxed:
 s_3(M) >= sqrt(theta P)/(sqrt(binom(r,3)) L^2).
`                                                                    (4.2)

Let `H=R0 union C0`, `d=|H|`. The rectangular block `M` is a row/column compression of the symmetric physical principal block `A_H=A[H,H]`, so singular-value contraction yields

`s_3(A_H) >= s_3(M)`.                                                (4.3)

Since `A_H` is symmetric, it has three **actual eigenvalues** of modulus at least the right side of (4.2). Condition only on original coordinates outside `H`; the remaining coordinates retain independence and cap one, while outside variables generate arbitrary deterministic affine terms. Applying (2.1) gives the full-form aggregate receiver

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(6 pi d) sqrt(binom(r,3)) L^2 / sqrt(theta P).
`                                                                    (4.4)

No physical minor is inverted or even selected.

### No-pivot specialization

From (2.3), every entry of `M` has magnitude below `sqrt(tau+tau^2)`, hence

`L^2 <= p q (tau+tau^2)`.

Therefore

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(6 pi d) sqrt(binom(r,3)) p q (tau+tau^2)/sqrt(theta P).
`                                                                    (4.5)

This closes the actual bounded-coordinate spectral subproblem in the form needed by coordinate-core extraction: **approximate determinant support**, not a single good minor, is enough.

## 5. Partner r21b applied: only support-diffuse colored packets survive

Apply (4.5) to the latest partner packets (2.2). For example, in the active `q=2` branch take any row support `R0` and column support `C0` of four physical coordinates each. If their determinant-marginal tails satisfy

`delta_R+delta_C <= 1/2`,                                           (5.1)

then `theta>=1/2`, `p=q=r=4`, `d<=8`, and `P2>=1/512`. Consequently

`||p_Q||_infinity < 198.014`.                                      (5.2)

Thus the latest partner's aggregate singular-pair issue no longer needs local reciprocal `|a|` payment whenever half of the q2 determinant packet is supported on a `4 x 4` physical coordinate core. The genuinely unpaid singular-q2 bank must instead satisfy the concrete support-diffuse obstruction: for every such bounded pair of supports, the two marginal tails sum to more than `1/2`.

The same calculation applies before the permutation-motif split in every overlap class. With `p=q=4`, `theta=1/2`, `d<=8`, the respective conditional caps from (2.2) are approximately

`q=0: 630.076`, `q=1: 489.199`, `q=2: 198.014`, `q=3: 37.128`.      (5.3)

These constants are not claimed sharp. Their purpose is structural: every colored packet is now either paid by a true bounded physical core or has quantitatively nontrivial determinant-inclusion mass outside every fixed small support.

## 6. Exact target-class obstruction: a maximally diffuse fixed-bi-anchor packet

The support-diffuse alternative is real and cannot be eliminated by a better deterministic core selection.

For even `N`, define four vectors in `R^N`

`v_j=u_j=1/sqrt(N)`,
`x_j=y_j=(-1)^j/sqrt(N)`.

Each pair `(v,x)` and `(u,y)` is orthonormal and has uniform two-frame leverage `2/N`. Set

`M_N = [[0,u^T],[v,x y^T]]`,                                      (6.1)
`A_N = [[0,M_N],[M_N^T,0]]`.                                     (6.2)

In the orthonormal row basis `(e0,v,x)` and column basis `(e0,u,y)`, `M_N` is represented exactly by

`[[0,1,0],[1,0,0],[0,0,1]]`.                                     (6.3)

Hence its three nonzero singular values are `1,1,1`, and the symmetric target matrix `A_N` has nonzero spectrum

`{+1,+1,+1,-1,-1,-1}`.                                            (6.4)

So this is a genuine target-level family, not merely a matrix obstruction.

Every physical `3x3` minor of `M_N` that omits the anchor row has determinant zero because `[v,xy^T]` has rank at most two; every one that omits the anchor column is zero because `[u^T;xy^T]` has rank at most two. For residual row pair `{j,k}` and residual column pair `{p,q}`,

`boxed:
 det M_N[{0,j,k},{0,p,q}]
 = -(v_j x_k-v_k x_j)(u_p y_q-u_q y_p).
`                                                                    (6.5)

By Cauchy-Binet for the two orthonormal two-frames,

`sum_(j<k) (v_jx_k-v_kx_j)^2 = 1`,
`sum_(p<q) (u_py_q-u_qy_p)^2 = 1`.

Thus the anchored third-minor mass is exactly

`Z=1`.                                                              (6.6)

For the alternating-sign frame, a row-pair wedge is nonzero exactly for opposite parities and then has squared magnitude `4/N^2`; therefore every residual coordinate has pair-inclusion marginal exactly `2/N`. The row and column anchored laws factor, so the same holds on both sides. This is a maximally diffuse conditional bi-anchor packet.

Moreover every entry of `A_N` has magnitude at most `N^(-1/2)`. Hence every principal block on at most `m` physical coordinates obeys

`||A_N[H,H]||op <= m/sqrt(N) -> 0`                                (6.7)

for fixed `m`. No universal bounded-cardinality physical spectral core can be extracted from the constant mass (6.6).

For `N>128`, all diagonals vanish and every physical principal-pair determinant has magnitude at most `1/N<1/128`; thus the family lies inside the live no-pivot class `N3(1/128)`. This refutes only the intermediate idea that a constant bi-anchor third-compound packet must concentrate on a bounded physical core. It does **not** refute QFORM.

## 7. Required e5 theorem pays the exact diffuse obstruction

The family (6.1)-(6.2) is instead exactly in the proved mixed-hub scope of e5 Theorem MF.

Take the two physical anchors as the heavy set `H`. On the remaining `2N` original coordinates,

`A_LL = [[0,xy^T],[yx^T,0]]`

has rank two and eigenvalues `+1,-1`. Choose the corresponding orthonormal eigenvectors

`s_+=(x,y)/sqrt(2)`, `s_-=(x,-y)/sqrt(2)`.

The two heavy-to-light coupling columns are `(0,u)` and `(v,0)`. Since `u perp y` and `v perp x`, they are orthogonal to the light rank-two eigenspace. Therefore the mixed Gram from Theorem MF is exactly

`Gamma=I_4`,                                                       (7.1)

and each generalized physical light-row leverage equals

`v_j^2+x_j^2=2/N` on the left,
`u_p^2+y_p^2=2/N` on the right.                                   (7.2)

For `N>=4` these are at most `1/2`. With `|H|=2`, `r=2`, `lambda_1=1`, `lambda_2=-1`, `det Gamma=1`, Theorem MF gives the real inequality

`|phi_Q(t)| <= 16 pi^3 |t|^-3`.                                  (7.3)

Using also `|phi_Q|<=1`,

`integral_R min(1,16 pi^3 |t|^-3) dt
 = 3 (16 pi^3)^(1/3)`.

Fourier inversion therefore yields

`boxed:
 ||p_Q||_infinity <= 3*2^(1/3) = 3.779763... .
`                                                                    (7.4)

This bound is uniform in `N` and in all independent cap-one input laws. In this scoped family e5 also gives a continuous density because (7.3) is integrable.

This is the required completed e5 result applied to an actual obstruction: the exact family defeating bounded-core extraction is nevertheless paid by a product-preserving physical mixed-hub Fourier mechanism.

## 8. What changed in the proof map

The bounded-dimensional B07 obligation is now genuinely closed in aggregate form: whenever a third-minor packet has most of its determinant-inclusion mass on bounded physical row/column supports, (4.4)-(4.5) produce three actual eigenvalues in that physical core and the completed finite-dimensional spectral receiver pays the **full ambient form**, including arbitrary outside couplings and affine shifts generated by conditioning.

Latest partner r21b is narrowed correspondingly. Its q1/q2/q3 positive-motif receivers and its singular-q2 star factorization only need an aggregate-before-inversion analytic transducer in the **support-diffuse** regime. Bounded-support singular-pair packets are already paid without choosing a pair.

The construction (6.1) shows that this surviving support-diffuse regime is unavoidable even with six eigenvalues of modulus one and no physical pivot. It also identifies the correct model mechanism: heavy physical anchors plus a diffuse low-rank light block. The special model is paid by Theorem MF, but the live partner branch retains arbitrary same-side light-bank quadratic curvature, which Theorem MF does not permit.

## 9. First unpaid implication

**`QFORM-SUPPORT-DIFFUSE-ANCHOR-WITH-CURVATURE-v1`.** Starting from a partner colored/anchored determinant packet whose bounded marginal tails fail the core criterion (4.1), combine that genuine support diffusion with the r21/r21b transverse four-bank or positive-motif reserve to obtain an MF-type or fractional-potential receiver while retaining **arbitrary same-side quadratic curvature** on the light banks. It is not legitimate to delete that curvature, call it a small random perturbation, rotate the light banks and preserve independence, or extract one reciprocal residual minor.

A valid next step would be a decoupled mixed-hub estimate in which Weyl differencing removes same-side curvature while the two anchor variables retain enough unsquared Fourier gain, or a proof that the support-diffuse packet forces one of the already-completed D'/tail/ridge exits. The exact family (6.1) is now a regression model: a proposed receiver must pay it for the correct product-structure reason, not by a bounded-core assertion.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Global continuity remains open. Independent review of the new marginal-tail theorem and construction is not claimed in this run.
