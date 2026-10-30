SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-24T06:36:01Z.
attacking: majority-sheet submass regularity and its limits: test whether square-root input-mass gains can aggregate without dimension loss, independently recheck the ruled rough-input bridge, and apply a completed e5f71d79 result to a genuine inequality or obstruction.

# Early calculation — two zero-loss regularity reductions

## A. Telescoping the uniform ruled submass theorem

Use the preceding fleet02/B15 theorem `QFORM-RULED-SUBMASS-SQRT-UNIFORM-v1`: for the isotropic rank-three form

\[
q_R(x)=\langle r_1,x\rangle^2+\langle r_2,x\rangle^2-\langle r_3,x\rangle^2,
\qquad R=(r_1,r_2,r_3),\quad R^TR=I_3,
\]

if one ORIGINAL-coordinate factor is replaced by a cap-one subdensity of mass `m`, the positive-sheet output submeasure has density height at most `20 sqrt(2) sqrt(m)`, uniformly in dimension and orientation.

For two product laws `F=prod f_i`, `G=prod g_i`, put `delta_i=||f_i-g_i||_1`. Telescope

\[
F-G=\sum_{j=1}^n (f_j-g_j)\prod_{i<j}f_i\prod_{i>j}g_i.
\]

The positive and negative parts of `f_j-g_j` are cap-one subdensities of equal mass `delta_j/2`. Therefore each signed telescoping summand has positive-sheet output density of L-infinity norm at most

\[
2\cdot20\sqrt2\sqrt{\delta_j/2}=40\sqrt{\delta_j}.
\]

Hence

\[
\boxed{\|r_F^+-r_G^+\|_\infty\le40\sum_{j=1}^n\sqrt{\|f_j-g_j\|_1}.}
\]

This is dimension-finite, not a candidate dimension-free full-QFORM estimate. Its use is regularity: cap-preserving compact-smooth approximants are Cauchy at the positive-sheet density level for each fixed instance.

For compact-smooth product inputs, the projected 3D density is smooth and compactly supported. The e5f71d79 ruled identity expresses the positive-sheet density for `s>=0` as an angular average of line integrals. Each line integral is a continuous value of a 2D projection density and is uniformly dominated by the same projection cap used in Theorem C, so dominated convergence gives continuity all the way to `s=0`. The displayed stability then transports that one-sided continuity to arbitrary rough cap-one marginals.

The completed e5f71d79 Theorem C separately pays the height:

\[
\boxed{0\le r_F^+(s)\le\pi\sqrt2\quad(s\ge0).}
\]

Thus continuity is downstream from, not a source of, the essential bound.

## B. Countable analytic-Schwartz core from the newest fleet03/B15 skeleton

The newest fleet03/B15 theorem proves `C_all=C_Q`, where `C_Q` is the exact universal interval-height constant restricted to rational generic matrices and bang-bang marginals `1_E`, with `E` a finite rational-endpoint union of total length one.

For rational `sigma>0`, define

\[
f_{E,\sigma}=1_E*\gamma_\sigma.
\]

These are cap-one probability densities, strictly positive, real analytic, and Schwartz; the indexed class is countable. As rational `sigma downarrow0`, `f_{E,\sigma}->1_E` in L1. Product L1 convergence and deterministic pushforward contract total variation, so every rational-skeleton interval probability is the limit of probabilities from this analytic class with the SAME matrix and interval. Therefore the optimal constant on the countable analytic class equals `C_Q=C_all` exactly.

Consequently failure of the universal theorem, if it occurs, already has a blow-up sequence with strictly positive analytic Schwartz marginals and rational algebraically generic matrices. Rough discontinuities, support edges, and exact algebraic degeneracies cannot be essential to a counterexample sequence. Any regularity-based proof must therefore be uniform as the Gaussian smoothing scale tends to zero.

Status: proof details and ruled rough-input audit to be completed in REPORT.md; full QFORM remains OPEN.
