# fleet03/B18 auto15 — one-sided cross-bank density via LPP negative moments

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T005514Z-fleet03-B18-QFORM-auto15`  
Status: `NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-24T00:55:14Z.
attacking: transfer the sharp product-marginal theorem into a direct negative-moment bound for a zero-self-curvature cross bank, then splice the fleet04/B18 bounded-window null-hub exit.

## 1. Exact target and correction discipline

The full owner target remains open: independent real coordinates with probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, centered, diagonal-basis, or smoothness assumption is added here.

This run does not rotate random coordinates and declare them independent; does not use arbitrary-joint coarea; does not infer independence from a conditional density cap; does not use the refuted law-uniform pointwise quadratic van-der-Corput bound; and does not assert that the three-large-eigenvalue hypothesis forces the structural block below.


## 2. Primary literature transfer

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1, proves the following exact input used below. If `Y=(Y_1,...,Y_n)` has product density `prod f_i` with every `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. In particular every normalized scalar projection has density at most `sqrt(2)`.

No moment, iid, support, log-concavity, centering, symmetry, or regularity assumption occurs in this theorem. The application below uses it only for genuine linear projections of an original-coordinate product bank.

As a scope comparison, Herry--Malicet--Poly, arXiv:2303.09488, studies quadratic forms in iid variables whose common law has a sufficiently smooth Gaussian-field representation, with further normalization/spectral assumptions in its strong regularity applications. It therefore does not subsume the owner's arbitrary rough non-iid cap-one target and is not used as a universal closure theorem.

## 3. A sharp capped-density negative-moment lemma

Let `W` be an `R^k`-valued random vector, `k>=2`, with probability density bounded by `H`. Let `v_k` denote the volume of the Euclidean unit ball in `R^k`. Then

`E ||W||^(-1) <= [k/(k-1)] (H v_k)^(1/k).`  (3.1)

Proof. Since `w -> ||w||^(-1)` is radial decreasing, the bathtub principle maximizes its integral among probability densities bounded by `H` by taking density `H` on a centered ball of volume `1/H`. If its radius is `R=(H v_k)^(-1/k)`, then

`H int_{|w|<=R} |w|^(-1) dw = H [k v_k/(k-1)] R^(k-1) = [k/(k-1)](H v_k)^(1/k)`.

This is finite exactly because `k>=2`.

## 4. New theorem: `QFORM-ONE-SIDED-CROSS-NEGATIVE-MOMENT-v1`

Let `X in R^m` and `Y in R^n` be independent original-coordinate product banks, every scalar density bounded by one. Let `M` be an `m x n` real matrix. Let `alpha in R^m` be arbitrary and let `G:R^n->R` be arbitrary measurable. Define

`R = X^T M Y + alpha^T X + G(Y).`

For any integer `2<=k<=rank(M)`, let `sigma_1>=...>=sigma_k>0` be any chosen `k` singular values (in particular the top `k`), and put `Delta_k=prod_{j=1}^k sigma_j`. Then `R` has a density satisfying

`||p_R||_infinity <= 2 [k/(k-1)] v_k^(1/k) Delta_k^(-1/k).`  (4.1)

In particular, if `rank(M)>=2`,

`||p_R||_infinity <= 4 sqrt(pi) [sigma_1(M) sigma_2(M)]^(-1/2).`  (4.2)

No continuity claim is made.

### Proof

Condition on `Y=y`. The conditional random variable is the original-coordinate linear form

`(My+alpha)^T X + G(y)`.

By the one-dimensional case of the LPP/Rudelson--Vershynin marginal bound and scaling,

`||p_{R|Y=y}||_infinity <= sqrt(2)/||My+alpha||`  (4.3)

whenever the coefficient is nonzero. The exceptional coefficient-zero set has zero `Y`-probability once the rank used below is positive, and the final finite majorant also handles it by approximation.

Take a thin singular decomposition and retain the chosen `k` singular directions: write the corresponding left/right singular-vector matrices as `U_k,V_k` and `Sigma_k=diag(sigma_1,...,sigma_k)`. Orthogonal projection cannot increase norm, so

`||My+alpha|| >= ||Sigma_k V_k^T y + U_k^T alpha||.`  (4.4)

Set `Z=V_k^T Y`. LPP gives `||p_Z||_infinity<=2^(k/2)` (if `k=n`, the original product density itself is bounded by one, which is even stronger). Therefore

`W=Sigma_k Z+U_k^T alpha`

has density cap

`H <= 2^(k/2)/Delta_k.`  (4.5)

Equations (4.3)--(4.5), Tonelli, and (3.1) imply

`||p_R||_infinity <= sqrt(2) E ||W||^(-1)
 <= sqrt(2) [k/(k-1)](2^(k/2) v_k/Delta_k)^(1/k)
 = 2 [k/(k-1)]v_k^(1/k) Delta_k^(-1/k).`

This proves (4.1); for `k=2`, `v_2=pi`, giving (4.2). Absolute continuity follows by the same conditional-mixture argument. QED.

## 5. Ambient quadratic-form corollary

Partition the ORIGINAL coordinates into disjoint sets `I,J,K`. Suppose the physical principal block on `I` is exactly zero,

`A_II=0`,

and let `B=A_IJ`. Let `beta_1>=beta_2>0` be the two largest singular values of `B`. Then the FULL ambient quadratic form `Q=X^T A X`, with arbitrary `A_JJ`, arbitrary `A_KK`, and arbitrary couplings to `K`, has a density obeying

`||p_Q||_infinity <= 2 sqrt(pi) (beta_1 beta_2)^(-1/2).`  (5.1)

Proof. Condition only on the original coordinates `X_K`. The retained `I`- and `J`-banks remain genuinely independent cap-one product banks, and

`Q | X_K = 2 X_I^T B X_J + alpha(X_K)^T X_I + G_{X_K}(X_J)+c(X_K)`.

Apply (4.2) with `M=2B`. Its top two singular-value product is `4 beta_1 beta_2`, yielding (5.1). The bound is uniform in the conditioning; average over `X_K`.

More generally, if `B` has `k>=2` selected singular values with product `Delta_B,k`, then

`||p_Q||_infinity <= [k/(k-1)] v_k^(1/k) Delta_B,k^(-1/k).`  (5.2)

This result keeps arbitrary curvature on the opposite bank and arbitrary outside spectrum/couplings. It is therefore not just a pure bilinear-form statement.

### Target-valid stress family

For

`A_t = [[0,0,1,0], [0,0,0,1], [1,0,t,0], [0,1,0,0]]`,  `t>=0`,

take `I={1,2}`, `J={3,4}`. Then `A_II=0` and `B=I_2`, so (5.1) gives

`||p_{X^T A_t X}||_infinity <= 2 sqrt(pi) = 3.544907701811...`  (5.3)

for every cap-one product input law, uniformly in `t`. The spectrum is the union of `{1,-1}` and the two roots of `lambda^2-t lambda-1=0`; for every `t>=0`, the positive root is at least one. Hence at least three eigenvalues have modulus at least one. The fourth eigenvalue may become arbitrarily small as `t` grows, showing that the theorem tolerates a strongly curved opposite bank and arbitrary extra spectral scale.

Continuity is not asserted by this conditional negative-moment proof.

## 6. Designated partner fleet04/B18 applied at an actual inequality

Read and applied the completed partner theorem `QFORM-4COORD-NULLHUB-WINDOW-EDGE-DICHOTOMY-v1` from

`yspennstate/math-open-problems@84fa5922df082f90064dea4d22a600a60e799803`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260923T221534Z-fleet04-B18-QFORM-r5/REPORT.md`.

It states: for an original-coordinate exact-rank-three `4x4` null-hub block whose three nonzero eigenvalues satisfy `s<=|mu_j|<=L`, if one hub edge has magnitude at least `a`, then

`||p_Q||_infinity <= 576^(1/3) L^(2/3)/(s a^(2/3)).`  (6.1)

Apply it to the literal principal block

`C = [[0,1,0,0], [1,0,0,0], [0,0,1,0], [0,0,0,0]].`

Its nonzero spectrum is `{1,-1,1}`, the hub edge is one, and we may take `s=L=a=1`. Thus the partner theorem gives the concrete target-level inequality

`||p_{X^T C X}||_infinity <= 576^(1/3) = 8.3203352922076...`  (6.2)

and the same bound after arbitrary outside original coordinates are conditioned as permitted by that theorem. Continuity is not claimed by the partner result.

Combining (5.1) and (6.1) supplies two complementary, source-valid compiler exits: a zero-self-curvature bank carrying two aggregate cross singular directions, or a bounded-window exact-rank-three null-hub core carrying a non-tiny physical edge. Neither exit is asserted to be forced by `s_3(A)>=1` alone.

## 7. Literature scope and remaining implication

No exact published theorem located in the checked primary sources settles the owner's full quantifiers. LPP supplies the linear marginal theorem used above. Herry--Malicet--Poly has materially stronger input-law assumptions and cannot be imported. Results for sums or tensor small-ball probabilities likewise do not by themselves turn into a translation-uniform density theorem for the full indefinite quadratic pushforward.

The unrestricted QFORM conjecture remains `OPEN / NOT PROVED`; unrestricted continuity remains open. The first remaining structural implication for this mechanism is:

> starting only from `s_3(A)>=1`, force at universal scale either a product-preserving zero-self bank with two-dimensional cross volume, or one of the already-paid hub/ridge/grouped-coordinate certificates, without extracting a fictitious uniformly good fixed minor.

A failure of `A_II=0` cannot be treated perturbatively under the arbitrary cap-one laws; the self-curvature must be spent by another exact receiver.

## 8. Source pins

- Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1: product marginal density cap `2^(k/2)`.
- Herry--Malicet--Poly, arXiv:2303.09488: quadratic-form regularity under iid / smooth Gaussian-field-representation hypotheses; scope comparison only.
- Partner: `yspennstate/math-open-problems@84fa5922df082f90064dea4d22a600a60e799803`, exact report path above.
- Control refresh: `yspennstate/math-research-brain@e54bb99afabe21870e4be39fac48783b9556cc56`.
