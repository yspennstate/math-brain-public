# Handoff — account04/B14 — 20260924T071645Z

SIGNED IN — account=account04 slot=B14 actual_utc=20260924T071645Z canonical_run=20260924T071645Z-account04-B14-atomless-boundary-r11.

## New result

Atomless moving-boundary theorem. If \(b(\omega)\) has no atoms and \(h_\omega\in C_0([0,\infty))\) are jointly measurable with \(0\le h_\omega\le M\), then
\[
H(t)=\int {\bf1}_{\{t\ge b(\omega)\}}h_\omega(t-b(\omega))\,d\pi(\omega)
\]
belongs to \(C_0(\mathbb R)\) and \(\|H\|_\infty\le M\). No independence between \(b\) and \(h_\omega\), and no equicontinuity, support, or moment assumption is needed.

For
\[
B_*=I_3-\frac23{\bf1}{\bf1}^T,\qquad Q=U^TB_*U+2VW,
\]
the completed account01/B14 physical-fiber theorem gives
\[
\Pr(Q\in I)\le6\sqrt\pi |I|.
\]
The majority one-sheet submeasure has a global \(C_0\) density of height at most \(\pi\sqrt2\), because \(2VW\) is atomless. The full conjecture remains open; the minority/two-sheet branch and possible boundary atoms remain.

## Artifact

math-open-problems commit 10e3c2c60076516744368c00a83bb2f27c908298

Source pins:
- Claude baseline e5f71d79eff325201dd0274053d20268ce65b837
- account01/B14 be9d93b288079c9261fea04074bac234974da89c
- prior account04/B14 deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513

Corrections retained: no post-rotation independence, no arbitrary-joint coarea, no deletion of dense quadratic tails, and no promotion of a half-line estimate to a full theorem.
