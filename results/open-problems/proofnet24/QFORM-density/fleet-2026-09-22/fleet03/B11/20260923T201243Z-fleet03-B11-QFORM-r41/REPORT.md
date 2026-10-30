SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-23T20:12:43Z.
attacking: the punctured near-coloop collar; prove that the third internal curvature stays uniformly nondegenerate while the third cross singular value vanishes, and quantify partner extension-mass diffusion in the hard small-leaf branch.

# fleet03/B11 r41 — persistent third internal curvature and diffuse hub-leaf extension mass

Status: **two new exact structural lemmas / designated-partner result applied / full unrestricted QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Regularity: this run does not close the punctured collar, so it proves no new unrestricted continuity statement. Existing exact-graph continuity from r39 remains valid.

The target remains: for independent real coordinates with densities bounded by one and arbitrary symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal density bound or give a valid counterexample. No Gaussianity, log-concavity, moments, compact/connected support, post-rotation independence, law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea bound, or small-random-quadratic-error assumption is used below.

## 1. Mandatory rank-two logarithmic control

For independent centered unit uniforms,

\[
p_{2XY}(t)=\log\frac1{2|t|},\qquad 0<|t|<\frac12.
\]

Thus two opposite-sign directions are genuinely at the logarithmic endpoint. The purpose of this run is to locate, quantitatively and without rotating away product provenance, the third curvature resource in the punctured true-near-coloop chamber from r37--r40.

## 2. Setup inherited from r40

Retain the exact-rank-three factorization

\[
A=RMR^T,\qquad R^TR=I_3,\qquad s:=\min_a|\lambda_a(M)|\ge1,
\]
where `M` has signature `(2,1)` or `(1,2)`. There is a heavy physical coordinate

\[
r_0=\sqrt c\,e,\qquad c>63/64,
\]
and residual rows

\[
r_j=s_j e+w_j,\qquad w_j\perp e,
\]
with

\[
\sum_j w_jw_j^T=I_{e^\perp}.
\]
After the r40 partner-area exit, the genuinely hard branch may assume

\[
\boxed{\max_j\|w_j\|^2<1/36.}\tag{2.1}
\]

The determinant-pair coloring from r37 gives a literal partition of the residual original coordinates `S\sqcup T` for which

\[
\lambda_{\min}(G_S),\lambda_{\min}(G_T)>g_0,\qquad g_0:=17/288,
\]
where `G_B=\sum_{j\in B}w_jw_j^T`. Put `H={0}\cup S`, `\Gamma_H=R_H^TR_H`, and `B=A[H,T]=R_HMR_T^T`. The r38/r40 Gram factorization gives

\[
\boxed{\lambda_{\min}(\Gamma_H)>\beta_0},\qquad
\beta_0:=\frac{34}{111}\frac{17}{288}=\frac{289}{15984}
=0.01808058058058\ldots .\tag{2.2}
\]

The r40 top-two crossing lemma gives, if `\sigma_1\ge\sigma_2\ge\sigma_3\ge0` are the singular values of `B`,

\[
\boxed{\sigma_1\sigma_2>\kappa_*s^2},\qquad
\kappa_*:=\frac{34}{111}\left(\frac{17}{288}\right)^2
=0.00106725649260\ldots .\tag{2.3}
\]

Only `\sigma_3` is allowed to collapse in the punctured collar.

## 3. New lemma: the third INTERNAL curvature cannot collapse with the third crossing direction

### Lemma `QFORM-PUNCTURED-COLLAR-INTERNAL-CURVATURE-v1`

Let `U=[u_1,u_2,u_3]` be an orthonormal basis of `range(R_H)` chosen so that `u_1,u_2,u_3` are left singular vectors of `B` when `rank(B)=3`; when `rank(B)=2`, take `u_1,u_2` as its left singular vectors and `u_3` as the unit completion inside `range(R_H)`. Write

\[
C:=U^TA[H,H]U=
\begin{pmatrix}
C_0&d\\
d^T&\alpha
\end{pmatrix},\qquad d\in\mathbb R^2.
\]
Then throughout the whole punctured collar, including the exact-graph boundary,

\[
\boxed{\sigma_{\min}(C)>\beta_0s}\tag{3.1}
\]
and hence

\[
\boxed{\sqrt{\|d\|^2+\alpha^2}>\beta_0s.}\tag{3.2}
\]
Consequently at least one of

\[
\boxed{\|d\|>\frac{\beta_0}{\sqrt2}s
=0.0127849011363\ldots s}\tag{3.3}
\]
or

\[
\boxed{|\alpha|>\frac{\beta_0}{\sqrt2}s}\tag{3.4}
\]
holds.

#### Proof

Because `U` spans `range(R_H)`, put

\[
K:=U^TR_H\in\mathbb R^{3\times3}.
\]
Then

\[
K^TK=R_H^TUU^TR_H=R_H^TR_H=\Gamma_H.
\]
Furthermore

\[
C=U^TR_HMR_H^TU=KMK^T.
\]
Therefore

\[
\sigma_{\min}(C)
\ge\sigma_{\min}(K)^2\sigma_{\min}(M)
=\lambda_{\min}(\Gamma_H)s
>\beta_0s,
\]
which proves (3.1). Since the third column of `C` is `(d,\alpha)^T`,

\[
\sqrt{\|d\|^2+\alpha^2}=\|Ce_3\|\ge\sigma_{\min}(C)>\beta_0s.
\]
The dichotomy (3.3)--(3.4) follows from `a^2+b^2>r^2`. QED.

### Meaning of the lemma

In the corresponding SVD coordinates `\xi=(u,z)` on the `H` bank and `\eta=(v,W)` on the `T` bank, the exact-rank-three form has the geometric normal form

\[
Q=F(u)+2z\,d^Tu+\alpha z^2
  +2u^T\operatorname{diag}(\sigma_1,\sigma_2)v
  +2\sigma_3 zW+G(v,W),\tag{3.5}
\]
with the two banks still arising from disjoint sets of original independent coordinates. Equations (2.3) and (3.2) show that the limiting difficulty is extremely specific:

* the rank-two crossing responsible for the logarithmic endpoint stays uniformly quantitative;
* the internal third curvature vector `(d,\alpha)` also stays uniformly quantitative;
* only the *placement* of that third curvature changes as the cross shear `\sigma_3 zW` tends to zero.

Thus the third direction is not disappearing. The unpaid analytic step is an overlap-safe interpolation between the internal square/bilinear receivers (r38/r39) and the nonzero third cross shear. A proof that simply pays `1/\sigma_3` is necessarily the wrong scale near the graph boundary.

This statement is symmetric under `M\mapsto-M`; it covers both signatures `(2,1)` and `(1,2)`.

## 4. New designated-partner application: every hub-leaf extension star is quantitatively diffuse

Use the completed fleet04/B11 exact extension-mass theorem from

`yspennstate/math-open-problems@30555c1ca97752e10f5089ccd95f8514c704be5a:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T131400Z-fleet04-B11-extension-mass-r6/REPORT.md`.

For a physical pair `P={i,j}`, that theorem writes

\[
d_{P,k}=|\det M|\,(n_P\cdot r_k)^2,\qquad
T_P:=\sum_kd_{P,k}=|\det M|g_P,
\]
where `n_P=r_i\times r_j`, `g_P=\|n_P\|^2`, and proves the exact identity

\[
W_2(P)=T_P^2-\sum_kd_{P,k}^2.\tag{4.1}
\]

Apply it to the actual hub-leaf pair `P_j={0,j}`. Since `r_0=\sqrt c\,e` and `w_j\perp e`,

\[
g_{0j}=c\|w_j\|^2,
\]
and for every residual `k`,

\[
(n_{0j}\cdot r_k)^2
=(n_{0j}\cdot w_k)^2
\le \|n_{0j}\|^2\|w_k\|^2
\le \delta\,g_{0j},\qquad
\delta:=\max_k\|w_k\|^2.\tag{4.2}
\]
Thus

\[
\boxed{\max_k d_{0j,k}\le\delta T_{0j}.}\tag{4.3}
\]
Using (4.1),

\[
\sum_kd_{0j,k}^2
\le(\max_kd_{0j,k})\sum_kd_{0j,k}
\le\delta T_{0j}^2,
\]
so

\[
\boxed{
W_2(\{0,j\})\ge(1-\delta)|\det M|^2g_{0j}^2.
}\tag{4.4}
\]

In the hard r40 branch (2.1), `\delta<1/36`, hence every nonzero hub-leaf pair satisfies the explicit actual inequality

\[
\boxed{
W_2(\{0,j\})>
\frac{35}{36}|\det M|^2g_{0j}^2.
}\tag{4.5}
\]

Equivalently, choosing `\varepsilon=35/36` in fleet04/B11's heavy-extension/diffuse-star dichotomy, the heavy-extension alternative is impossible: no single physical third coordinate carries more than `1/36` of a hub-leaf pair's total extension mass. The third determinant direction is forced to be collective across many original coordinates.

This does **not** by itself close the density bound. The partner's diffuse-star density compiler still pays local pair-conditioning factors (and any single `g_{0j}` can be small in a highly spread frame). Formula (4.5) therefore removes extension-mass concentration as the obstruction while preserving the genuine remaining aggregate-before-inversion problem.

## 5. Why the two lemmas fit together

The rank-two saddle `2u^TSv` in (3.5) supplies only the borderline logarithmic regularity. The new curvature lemma proves that a third quadratic resource of size `>\beta_0s` always survives on the `H` side, even when the third cross singular value goes to zero. The partner identity proves, independently in original-coordinate determinant language, that in the small-leaf hard branch the same third direction cannot be localized in one extension coordinate: at least `35/36` of the squared extension mass is genuinely off the diagonal of the extension distribution.

So the punctured near-coloop survivor is now localized to a single analytic issue rather than a geometric loss of curvature:

> combine a uniformly paid rank-two crossing with a uniformly paid *collective* internal third curvature, while allowing the small same-bank/cross-bank shear to couple rough fragmented product laws.

The r40 counterexample forbids resolving this by a universal `L^1_W(L^2_v)` slice norm. The current interactive projected-crossing theorem pays every fixed nonzero third cross volume but deteriorates with the vanishing shear. The endpoint r38/r39 theorems pay `\sigma_3=0`. The missing theorem must interpolate these without a moment assumption and without dividing by `\sigma_3`.

## 6. Exact next implication

`QFORM-PUNCTURED-CURVATURE-INTERPOLATION-v1`:

For the product-bank normal form (3.5), assume

\[
\sigma_1\sigma_2\ge\kappa_*s^2,
\qquad \sqrt{\|d\|^2+\alpha^2}\ge\beta_0s,
\]
with the projection-density bounds supplied by cap-one product inputs. Prove a universal density bound uniform in `\sigma_3\ge0`, or give a valid counterexample. The proof must keep original-coordinate product provenance and may not use the false mixed-slice norm from r40. A promising frequency split is to combine an endpoint internal-curvature estimate below the inverse-shear scale with the rank-three crossing estimate above it, but the low-frequency passage must be established without treating `\sigma_3zW` as a small random perturbation.

Arbitrary additional nonseparable spectrum remains a separate bridge to the full owner target.

## 7. Source pins and scope

Fresh control before publication: `yspennstate/math-research-brain@f5b1fb16df62f83d216afcdd918156d44ea30d37`; owner control remains revision `2026-09-22.15` and full QFORM remains open.

Fresh math source before publication: `yspennstate/math-open-problems@c6096975fb4c91c3aa529230462fecf5d539a2e2`.

Dependencies actually used:

- fleet03/B11 r40: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T191401Z-fleet03-B11-QFORM-r40/REPORT.md` (top-two crossing and small-leaf hard chamber), canonical report commit `2db0a7f81437b6e67efe800f129abebae0e10b4c`;
- designated partner fleet04/B11 r6: commit/path pinned in Section 4;
- current interactive projected-crossing scope: `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`, read at fresh master before this report;
- current continuation: `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md`, read at fresh master before this report.

No scheduler/task-state change, email, notification, public release, paid API/model, Codex call, installation, permission expansion, remote workflow, unrelated-data access, or cross-account authentication was performed.
