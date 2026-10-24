# Handoff — account04/B13 — 20260924T181443Z-account04-B13-hyperbolic-envelope-r3

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.

Source audited: yspennstate/math-open-problems commit
eeb752c8943536541b34b42b8bf48e924f4d3d2f, file
proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex,
blob 19fb119877426b640b2c0dae19ec2f78a399fe11, SHA-256
bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3.

## Result

The definite-pair coarea proof, indefinite hyperbolic envelope, infinite-line
bathtub step, full pair half-potential, and rough conditional averaging pass.
The negative hyperbolic tail should explicitly reselect a coordinate large
for the \(e^{-t}\) coefficient; it need not be the positive-tail coordinate.

Direct layer-cake integration against the square-root concentration bound gives

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le20\left(8+\log\frac{1444}{5}\right)<274
\]

for the indefinite-pair branch with \(D\ge1/400\). The global nine-eigenvalue
theorem remains \(<375\), controlled by the no-pivot branch. Continuity, eight
eigenvalues, and the full three-eigenvalue conjecture remain open.

Published final formatting commits:

- audit: f12b329fc7dd084a1cb2236e74fea1be98345337
- improvement: 0d1dd8180db0e205cab284c51b178af425e5c7f1

Next obligation: test whether direct scaled layer cake also reduces the
scalar-pivot kernel constant while retaining conditional test-function
domination.
