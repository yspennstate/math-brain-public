SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B18, 2026-09-24T04:14:39Z.
attacking: apply the LPP definite active-plane theorem to the newest four-bank rank-twelve frontier, while keeping the ruled-side estimate one-sided and preserving all original-coordinate product provenance.

# account04/B18 r7 — definite active-plane exit from the four-bank carrier frontier

Status: **ESSENTIAL STEP APPLIED / SUPPORTING LIVE-BRANCH CLOSURE / FULL QFORM OPEN**.

The target remains unrestricted: independent original real coordinates with probability densities at most one, arbitrary real symmetric \(A\), and at least three eigenvalues of modulus at least one. Continuity is tracked separately. No moment, support, iid, log-concavity, smoothness, or post-rotation independence hypothesis is introduced.

## 1. Primary-source input and exact scope

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), Theorem 1.1 (arXiv:1507.07949), gives for every orthogonal projection of a cap-one product density onto a two-dimensional subspace a joint density cap at most \(2\). It does **not** make the two projected coordinates independent.

The completed account01/B18 theorem applying this result is pinned at

- commit \(\texttt{dfddb58cee7066cb57e3c9dc91a9a25d50179c69}\);
- path \(\texttt{proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260924T025717Z-account01-B18-QFORM-auto11-r44/REPORT.md}\).

If a literal original-coordinate source bank \(S\) has
\[
A_{SS}=UHU^\top,\qquad U^\top U=I_2,
\]
with \(H\) definite and invertible, then after conditioning on all coordinates outside \(S\), every outside coupling becomes only an affine tilt in \(Z=U^\top X_S\). LPP gives \(\|p_Z\|_\infty\le2\), and the elliptical-shell area identity gives
\[
\boxed{\ \|p_{X^\top AX}\|_\infty\le {2\pi\over\sqrt{|\det H|}}\ }. \tag{1.1}
\]
All outside self-blocks, couplings, signs, and extra spectrum remain arbitrary.

The Herry--Malicet--Poly smooth-iid theory does not match the rough non-iid source class and is not used.

## 2. New live-frontier application

The newest compatible four-bank frontier is account03/B20 commit
\(\texttt{2f0eff522a435c40b3bc39b1dc4f6bcd8d309978}\), theorem
\(\texttt{QFORM-R48-THREECUT-R2-GLUING-v1}\).
Unless a physical \(E_3\) receiver already pays the full law by
\[
\|p_Q\|_\infty<30838, \tag{2.1}
\]
it gives four disjoint literal original-coordinate banks \(S_1,\dots,S_4\) such that on their union
\[
A=\operatorname{diag}(A_{S_1S_1},\dots,A_{S_4S_4})+K+E,
\quad \operatorname{rank}K\le12,\quad \|E\|_{\rm op}<{33\over131072}. \tag{2.2}
\]
The within-bank blocks are untouched.

### Theorem 2.1 — \(\texttt{QFORM-FOURBANK-DEFINITE-ACTIVEPLANE-EXIT-v1}\)

In the survivor (2.2), suppose one untouched bank \(S_b\) satisfies
\[
A_{S_bS_b}=UHU^\top,\qquad U^\top U=I_2,\qquad H\text{ definite},
\qquad |\det H|\ge\delta>0. \tag{2.3}
\]
Then the **full ambient** quadratic form has
\[
\boxed{\ \|p_Q\|_\infty\le {2\pi\over\sqrt\delta}\ }. \tag{2.4}
\]

#### Proof

Condition on every original coordinate outside \(S_b\). The terms \(K,E\), all other within-bank blocks, and all outside couplings contribute only an affine function of \(X_{S_b}\) plus a constant, while the conditional quadratic part on \(S_b\) remains exactly \(UHU^\top\). Apply the account01/B18/LPP active-plane theorem uniformly in the conditioning and average. No coefficient is deleted and no rotated independence is asserted. \(\square\)

At the natural live threshold \(\delta=2^{-12}\),
\[
\boxed{\ \|p_Q\|_\infty\le128\pi
=402.1238596594935\ldots<402.124.\ } \tag{2.5}
\]

Thus the three-cut frontier is now exhaustively reduced to:

1. a continuous physical-\(E_3\) exit with (2.1);
2. a definite active-plane exit with (2.4), and with (2.5) at determinant \(2^{-12}\); or
3. a rank-\(\le12\) four-bank off-diagonal carrier with retained operator tail \(33/131072\), for which every untouched within-bank block fails the exact definite two-plane gate (2.3).

This is a genuine application to the live missing state; it is not a bibliography-only observation.

## 3. Why the ruled-side theorem does not silently close the remainder

Claude's ruled parametrization in
\(\texttt{e5f71d79eff325201dd0274053d20268ce65b837}\),
\(\texttt{.../20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md}\),
bounds an indefinite rank-three form by \(\pi\sqrt2\) on its one-sheet side. In (2.2), conditioning on the other banks translates the target level by an arbitrary random amount. A one-sided estimate therefore cannot be substituted for a translation-uniform full density bound unless the conditioned remainder has a compatible sign restriction. No such sign restriction is available here. The convex/two-sheet side consequently remains open.

Likewise, the marginal-free Fourier receivers \(D'\) and \(D_5\) apply only when their actual physical cross-volume and marginal gates hold; the rank-\(\le12\) approximation in (2.2) does not by itself supply those lower bounds.

## 4. Exact remaining implication

The first unproved edge after Theorem 2.1 is

\[
\texttt{QFORM-FOURBANK-R12-NONDEFINITE-WITHINBANK-PAYMENT-v1}.
\]

One must control (2.2) when every within-bank block either has no exact rank-two definite support or has arbitrarily small definite determinant, while retaining the nonzero tail \(E\), arbitrary same-bank curvature, and both sides of the indefinite rank-three level geometry. A projected joint-density cap alone is insufficient, and the one-sheet ruled estimate is not translation-uniform.

The full conjecture and full-target continuity remain **OPEN / NOT PROVED / NOT DISPROVED**.
