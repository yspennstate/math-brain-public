# Verification record

Manuscript: *Cover-time fluctuations beyond the maximal hitting-time scale*,
Yitzchak Shmalo, September 2026 version (20 pages, 12 sections, one appendix).

This file records a line-by-line verification of the manuscript: each proof
was re-derived independently of the text, every closed form was recomputed by
exact arithmetic from the graphs themselves, and the finite content of the
argument was checked in Lean 4 against Mathlib. The sections below give the
verdict, the checks that support it, and the changes made to the text.

## Verdict

The mathematics is correct as stated. No proof needed repair. Every exact
formula in the paper (the hitting table, `t_hit(G_k)`, the excursion
transform and its moments, the coupon-clock mean and variance, the initial
variances, the exact hitting identity for decorated cores, `t_hit(D_k)`, the
star variance) reproduces from the graphs by rational arithmetic, and every
asymptotic statement was re-derived from those formulas and from the estimates
in the text.

## The argument, step by step

Section 2, Theorem 2.1 and Corollary 2.2. The constants of (2.4)-(2.7) follow
from (2.2)-(2.3) and (2.1); the interpolation exponent
`sqrt 2 * 2^{-beta} (log k)^{beta-1/2} = (log k / 2)^{beta - 1/2}` is checked
symbolically and in Lean. The contradiction with a universal `A e^{-au}` bound
uses `u_k = c sqrt(log k)` and `h_k / sqrt(h_k t_cov) -> sqrt(2/log k)`, giving
the limit `1 - Phi(c sqrt 2)`.

Section 3, Proposition 3.1. The three first-step systems (targets `a`, `s`,
`g`, `q`) were solved by hand and their solutions forced in Lean by explicit
`linear_combination` certificates; the full `(2k+1)`-vertex systems were also
solved exactly for `3 <= k <= 14` and match the table entry by entry, and the
maximum over all ordered pairs is `2k^2 + k + 1`. The comparison polynomial
`2t^3 + 16t^2 + 38t + 20` is verified.

Lemma 3.2. The transform (3.2) is recovered by composing the generating
functions of `D_i` and `F`; the mean, variance and third moment follow by
symbolic differentiation (`E Y^3 = 6k^6 - 6k^5 - ... + 2`, degree six, as
(3.5) requires). The moment-generating bound (3.6): the closed form of
`E exp(cY/k^2)` is bounded uniformly at `c = 1/4` (maximum 1.332 over
`3 <= k <= 199`), and the algebra `(1-1/k)(1 + Cc/k) <= 1 - 1/(2k)` for
`Cc <= 1/2` and the resulting geometric series bound are in Lean.

Section 4, Proposition 4.1 and Lemma 4.2. The stage transform (4.1) and its
moments (4.2)-(4.3), the third moment `E N_j^3 = 1/j + 6/j^2 + 6/j^3 <= 13/j`,
and the closed forms (4.5)-(4.10) were obtained by differentiating the
transforms with `k` symbolic (`r <= 6`) and, independently, by solving a
lumped absorbing chain for the leaf-completion clock from all four start types
(`3 <= k <= 12`). The identities `mu_k + 2k = d_k` and
`sigma_k^2 + mu_k^2 - 4 mu_k - 4k = c_k` are verified. The Berry-Esseen input
`E|U - EU|^3 <= 8 E U^3` rests on `(a+b)^3 <= 4(a^3 + b^3)`, in Lean.

Section 5, Lemma 5.1 and the second-order expansions. The union bound
`k(1 - 1/(k-1))^{t_0} <= k^{-3}` for `t_0 >= 4(k-1) log k` is in Lean. The
residual argument (the trap symbol is last among `r+1` symbols with
probability `1/(r+1)`; a first excursion covers the clique except with
probability `O(log k / k)`) was re-derived. The exact cover-time mean from the
lumped chain satisfies `0 <= E_x tau - m_{k,x}` for every start and
`3 <= k <= 12`, as (5.3) asserts, and the exact variance ratio to the
right-hand side of (2.3) rises from 0.84 to 0.96 over that range. The
expansion (2.2) is derived in Lean from `H_k` bounds with an explicit error
`3k log k + 5k` for the leading start; `|c_k - 2k^4| <= 4k^3` and
`|d_k^2 - k^4| <= 5k^3` are also in Lean.

Section 6, Theorem 6.1. The cumulant expansion (6.1) with `z = theta a_k
k^2 / b_{k,r}` gives `theta^2/2 + O(a_k / sqrt(log k))`; the scaling identity is
in Lean, and the three exponential-equivalence estimates (for `T_s`, for
`L_{k,r}` by Chebyshev, and for the residual) were re-derived; each is
superexponentially small at speed `a_k^2` because `a_k^2 = o(log k)`.

Section 7 and 8, the operational construction and Theorem 7.1. The
construction is exact: with `k` rate-one leaf processes in local time at each
core vertex and rate-one core jumps, the next edge is uniform among the
`d_v + k` choices, and the pathwise identity `tau_cov = 2P_k(sigma_k) +
J(sigma_k) - 1` holds because the last threshold is crossed at a first
arrival. Lemma 8.1: the occupation covariance `(2/q) L^+` was checked by
simulation, and the perturbation identities `lambda'(0) = 0`,
`lambda''(0) = (2/q) f^T L^+ f` were checked numerically to 1e-16 on nine cores
and exactly for the single edge, where the top eigenvalue of
`-L + z diag(a, -a)` is `-1 + sqrt(1 + a^2 z^2)`; the coefficient-matching
argument is in Lean. Lemma 8.2: both threshold tails are in Lean. The
inversion argument of Lemma 8.3 and the martingale transfer (8.11)-(8.13) were
re-derived. The scaling `sqrt q * N(0, (2/q) L^+) = N(0, 2L^+)` connecting (8.1)
to (7.1) was checked.

Section 9, Proposition 9.1, Corollary 9.2, Theorem 9.3. The elimination of leaf
states, the pendant-target value `2qk + 2e - 1` from `1^T L = 0`, and the
linearity of the Dirichlet problem are in Lean; (9.1)-(9.3) and (9.11) were
checked exactly on the edge, the paths on three and four vertices, the
triangle, the three-leaf star, the four- and five-cycles, `K_4` and the paw,
with equal decorations `k <= 4` and all leaf vectors in `{1,2,3}^q`. The
two-vertex formula `G = sqrt 2 (a Z_+ + b(-Z)_+)` and its mean and variance are
verified symbolically and in Lean.

Section 10, Theorem 10.1, Proposition 10.2. `t_hit(D_k) = 6k + 3` is verified
exactly for `k <= 25` and in Lean from the first-step equations; the constants
of (10.2)-(10.5) follow from `E|Z| = sqrt(2/pi)` and `Var|Z| = 1 - 2/pi`
(integrals checked symbolically). The exact cover-time moments of `D_k` were
computed for `k <= 16` and the star variance formula `4(k^2 H_k^(2) - k H_k)`
for `k <= 30`; the bound `SD/t_hit <= pi/sqrt 6` is in Lean with
`H^(2) <= pi^2/6` taken from Mathlib.

Section 11, Proposition 11.1. The law-of-total-variance identity is in Lean;
the orders of the clock error against the fluctuation scale were re-derived.

## Diagnostics beyond the exact checks

An exact-in-law sampler of `tau_cov(D_k)` built from the operational
construction (thresholds are maxima of `k` exponentials, marks are Poisson in
local time) agrees with the exact lumped chain at `k = 1000` (mean coefficient
of `k sqrt(log k)`: 3.874 +/- 0.012 sampled against 3.861 exact). The
standardized cover time approaches the half-normal limit slowly: at
`k = 3000` the exact `(E tau - 4k log k)/(k sqrt(log k))` is 3.72 against the
limit `4/sqrt(pi) = 2.26`, and `Var/(k^2 log k)` is 8.20 against
`8(1 - 2/pi) = 2.91`, both decreasing as `1/sqrt(log k)` corrections allow.
This is consistent with (10.3)-(10.4), which are limit statements, and says
nothing against them; it does mean that the leading terms are poor
approximations at any `k` one can compute with.

## Literature

Question 5.2 of Ding, Lee and Peres was read at the source (arXiv:1004.4371,
Section 5): "Is the standard deviation of tau_cov bounded by the maximal
hitting time t_hit? Furthermore, does (tau_cov - t_cov)/t_hit exhibit an
exponential decay with constant rate?", stated after the assumption
`t_cov(G_n)/t_hit(G_n) -> infinity` and Aldous's theorem, exactly as the
introduction describes. Ding's abstract (Ann. Probab. 42, 2014) states the
geometric-mean concentration for trees, and Zhai's bound has the form quoted
in (1.1) with `sqrt(lambda R) M`, which is the dimensionally consistent form
(with `sqrt(lambda) R M` the bound would fail already on the complete graph).

## Changes made to the text

1. Cross-references to lemmas, propositions and corollaries printed as
   "theorem" in eleven places (Lemma 3.2, Lemma 4.2, Lemma 5.1, Lemmas
   8.2 and 8.3, Proposition 9.1, Corollary 2.2). They now carry the right
   names.
2. Appendix A now describes the checks and the Lean development that
   accompany the paper.
3. The acknowledgements, the competing-interest statement and the declaration
   on the use of generative AI were rewritten in the author's standard form,
   and a code-availability statement citing this repository was added.
4. A repository reference was added to the bibliography.

No mathematical statement was changed.

## Scope of the formal development

The Lean files formalise finite identities and inequalities: first-step
systems, generating-function algebra, sums over stages, tail bounds of the
threshold variables, the linear algebra of the Dirichlet problems, the
coefficient identities of the spectral perturbation, and the constants. They
do not formalise the probability spaces, the strong Markov property, the
martingale arguments, weak convergence, the Berry-Esseen theorem or the
Gartner-Ellis theorem; those parts of the proofs were verified by hand only.
Every theorem in the development depends only on `propext`,
`Classical.choice` and `Quot.sound`; the listing is in `formal/output/`.
