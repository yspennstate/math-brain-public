SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B16, 2026-09-24T04:15:16Z.
attacking: the projection-product frontier by separating the source-valid definite-plane exit from the phase-aligned indefinite pair-log exit, without replacing a one-sided ruling estimate by a full bound.

# fleet04/B16 r4 — projection-product definite-or-phase-aligned exit

Status: **ESSENTIAL STEP APPLIED / SUPPORTING LIVE-BRANCH CLOSURE / FULL QFORM OPEN**.

The target remains the full arbitrary-dimensional, arbitrary-law, arbitrary-sign statement for independent original coordinates with probability densities at most one. Continuity remains separate.

## 1. Source-valid two-dimensional input

Livshyts--Paouris--Pivovarov (Israel J. Math. 216 (2016), Theorem 1.1; arXiv:1507.07949) implies that every orthogonal two-dimensional projection \(Z=U^\top Y\) of a cap-one product law has a joint density satisfying
\[
\|p_Z\|_\infty\le2. \tag{1.1}
\]
This is a joint-density cap, not independence after rotation.

Consequently, if a literal original-coordinate bank \(Y\) enters the quadratic form only through
\[
Z^\top HZ+a(R)^\top Z+c(R), \qquad H\text{ definite}, \tag{1.2}
\]
where \(R\) is built from disjoint original-coordinate banks, then elliptical-shell area gives
\[
\boxed{\ \|p_Q\|_\infty\le {2\pi\over\sqrt{|\det H|}}\ }. \tag{1.3}
\]
At \(|\det H|\ge2^{-12}\), this is
\[
\boxed{\ \|p_Q\|_\infty\le128\pi<402.124.\ } \tag{1.4}
\]
All dependence between the two coordinates of \(Z\) is retained.

## 2. Actual application of completed fleet01/B16 mathematics

The newest correction-safe fleet01/B16 source is commit
\(\texttt{693038c0d6b33564a32bba0665e0b2b342236765}\).
Its phase-aware physical-pair compiler applies to
\[
F_{\lambda,\nu}
 =\lambda(X+Y)^2+2\nu W(X-Y), \tag{2.1}
\]
where \(X,Y,W\) are mutually independent, \(X,Y\) have density cap one and \(W\) has cap \(K\). Put
\[
\kappa_K={\sqrt{\lambda^2+4\nu^2/K^2}-|\lambda|\over2}. \tag{2.2}
\]
The exact physical-pair completion has Schur square coefficient \(4\lambda\), and the overlap-safe pair-log theorem gives
\[
\boxed{\ \|p_{F_{\lambda,\nu}}\|_\infty
 \le8\left({K^2\over2|\lambda|\nu^2\kappa_K}\right)^{1/4}.\ } \tag{2.3}
\]

Apply (2.3) to the strict-target mixed-frame family
\[
Q_\theta=\theta H^2+(X+Y)^2+2(H+Z)(X-Y), \tag{2.4}
\]
where \(H,X,Y\) are independent cap-one original coordinates and
\(Z=X_2+X_4\) is the sum of two disjoint cap-one original coordinates.
Young's inequality gives \(\|p_Z\|_\infty\le1\), hence after conditioning on \(H\), \(W=H+Z\) has \(K=1\) and remains independent of \(X,Y\). With \(\lambda=\nu=1\),
\[
\kappa_1={\sqrt5-1\over2},
\]
so
\[
\boxed{\ \|p_{Q_\theta}\|_\infty
 \le8(\sqrt5-1)^{-1/4}
 =7.58716271595\ldots<7.588\ } \tag{2.5}
\]
for every real \(\theta\). The cited spectral calculation gives at least three eigenvalues of modulus at least two for this family, so (2.5) is an actual full-target inequality, not a two-eigenvalue surrogate.

## 3. Combined theorem and exact frontier

### \(\texttt{QFORM-PROJECTIONPRODUCT-DEFINITE-OR-PHASEALIGNED-EXIT-v1}\)

A live projection-product packet is paid whenever either:

1. its two-dimensional projected quadratic part is definite with determinant \(\delta>0\), in which case (1.3) gives \(2\pi/\sqrt\delta\); or
2. an original-coordinate repartition exposes the phase-aligned pattern (2.1), in which case (2.3) applies and, for (2.4), yields the concrete target bound (2.5).

These two mechanisms are complementary. The first uses only the LPP joint marginal cap and curvature of compact elliptical shells. The second uses a genuinely independent physical pair and the completed pair-log cancellation.

## 4. Why the ruling identity is not a third unconditional exit

Claude's ruled parametrization at commit
\(\texttt{e5f71d79eff325201dd0274053d20268ce65b837}\)
bounds the one-sheet side of an indefinite rank-three form by \(\pi\sqrt2\). In the live projection-product problem, conditioning on another bank translates the target level arbitrarily. The translated level may land on the convex/two-sheet side. Therefore the ruled-side estimate cannot be called a full density bound without either a sign restriction on the conditioned remainder or a translation-uniform convex-side theorem.

The remaining B16 implication is precisely the shared-bank indefinite collar that has:

- no definite two-plane of controlled determinant;
- no source-preserving phase alignment of the form (2.1);
- and arbitrary translated access to the convex/two-sheet side.

A bounded joint projected density alone does not control its hyperbolic level-set integral. The full conjecture and full-target continuity remain **OPEN / NOT PROVED / NOT DISPROVED**.
