# Independent audit: input-regular moderate-bias odd-crossing FEI

Date: 2026-10-03. Auditor: `/root/heat_entropy`.

**Verdict: analytic PASS.** I read the complete new
[candidate](input_regular_moderate_bias_odd_crossing_fei_candidate.md), after
independently reconstructing the proposed averaging extension. Every step,
including the changed (B^2) in the block-size choice, is valid. This audit
is separate from the preserved
[bounded-ratio audit](regular_moderate_bias_odd_crossing_heat_audit.md).
No earlier stable proof was modified. Historical novelty and external review
are not certified.

## The actual stronger hypothesis and conclusion

The input weights need only satisfy

\[
 \sigma^2=\sum_i w_i^2>0,
 \qquad \max_i|w_i|\le B\sigma/\sqrt n,
 \qquad B\ge1.                                  \tag{A}
\]

No positive lower bound on any individual weight is used. There are (m)
distinct genuine crossings, (m\ge1) odd, all within
([ -\lambda\sigma,\lambda\sigma]). Labels alternate on complementary
open intervals; each crossing may take either neighboring label; additional
isolated point anomalies are excluded. For fixed (m,B,\lambda), the
candidate proves a dimension-independent **ordinary** FEI constant for
(g=F(\sum_i w_iX_i)), with no output character.

The allowed weights include tiny and zero weights. Sign flips orient them
nonnegatively without changing spectral entropy or physical influence. The
statement uses (A) in the stated ambient dimension. Deleting a zero-weight
coordinate only improves (A) with the same (B), since (sigma) is fixed
and the new dimension is smaller. If all weights are zero, the function is
constant and entropy zero; the proof never applies a variance denominator
to that case.

## Previously audited inputs remain valid

The halfspace noise/product/tie argument and the complete degree-tail
entropy calculation from the bounded-ratio proof use no weight lower bound.
They therefore give here

\[
 H(g)\le C_H\sqrt n,
 \qquad C_H=(1+4Am)/\ln2,
 \qquad A=41/[\sqrt2(1-e^{-1})].                  \tag{B}
\]

The opposite-tail signed translation lemma likewise depends only on the
odd crossing count. For fixed shifts (u,v), the open pivotal set has at
most (2m) bounded components and Lebesgue measure at least (|u-v|).
Removing all translated crossing points handles arbitrary legal tie choices
and coincident translated crossings. Since these points are discarded only
for a lower bound, any pivotal discrete endpoint atoms are harmless.

The source and normalization checks in the separate bounded-ratio audit
apply unchanged: KOS Theorems 18 and 21 in the
[primary author manuscript](https://www.cs.columbia.edu/~rocco/Public/focs02.pdf)
supply independent **bit-flip** noise estimates. The author-hosted
[O'Donnell book](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf),
Section 11.5, printed page 350, explicitly accepts .56 for the independent
nonidentical-summand Berry–Esseen bound. Open intervals are compared through
CDF left limits, justified by continuity of the Gaussian CDF. Weak logarithmic
FEI, including the empty spectral atom, is separately audited and supplies
the bounded-dimensional case.

## Every mask has a usable remainder

Set

\[
 d=e^{-(\lambda+1)^2}/\sqrt{2\pi},\quad
 c_D=\sqrt{2/3},\quad E=2.24\sqrt2,
\]

\[
 K=\max\{1,\lceil(2EmB^2/(dc_D))^2\rceil\},
 \qquad N_0=\lceil\max\{2KB^2,K^2B^2\}\rceil.     \tag{C}
\]

For (n\ge N_0), take a uniform (K)-subset (J), independently of
old and fresh signs. Write its selected energy and remainder variance as

\[
 a_J=\sum_{i\in J}w_i^2,
 \qquad s_J^2=\sigma^2-a_J.
\]

The regularity bound gives, for **every** mask,

\[
 a_J\le Kw_{\max}^2\le KB^2\sigma^2/n\le\sigma^2/2,
 \qquad s_J\ge\sigma/\sqrt2>0.
\]

The selected old and fresh scores satisfy

\[
 |U|,|V|\le Kw_{\max}\le KB\sigma/\sqrt n\le\sigma.
\]

Thus all pivotal intervals lie in
([-(\lambda+1)\sigma,(\lambda+1)\sigma]), and the conditional Gaussian
remainder density is at least (d/\sigma) there. Berry–Esseen yields

\[
 \delta_J\le0.56\frac{w_{\max}}{s_J}
           \le0.56\sqrt2 B/\sqrt n.
\]

The first inequality follows from
(\sum_{i\notin J}w_i^3\le w_{\max}s_J^2), not from a lower bound
on any weight. At most (2m) open intervals incur at most (4m\delta_J)
CDF error. Conditional on (J,U=u,V=v), the resulting inequality is

\[
 \Pr[F(R+u)\ne F(R+v)]
 \ge d|u-v|/\sigma-EmB/\sqrt n.                  \tag{D}
\]

The error is uniform in (J,u,v). As in the preceding proof, a negative
right side for some shifts does not obstruct averaging.

## The new energy averaging is a lower bound, not Jensen

Conditional on (J), independence gives

\[
 \mathbb E(U-V)^2=2a_J,\quad
 \mathbb E(U-V)^4=12a_J^2-4\sum_{i\in J}w_i^4\le12a_J^2.
\]

Hölder interpolation therefore gives

\[
 \mathbb E[|U-V|\mid J]\ge c_D\sqrt{a_J}.        \tag{E}
\]

For (a_J=0), this reads (0\ge0); no division by a zero fourth moment
is used. This detail matters because some masks can consist entirely of
zero-weight coordinates.

Uniform-subset averaging has the exact identity

\[
 \mathbb E_J a_J=K\sigma^2/n.
\]

For (L=KB^2\sigma^2/n>0), the pointwise bound (0\le a_J\le L)
implies (\sqrt{a_J}\ge a_J/\sqrt L). Consequently

\[
 \mathbb E_J\sqrt{a_J}
 \ge\frac{K\sigma^2/n}{\sqrt{KB^2\sigma^2/n}}
 =\frac{\sqrt K\,\sigma}{B\sqrt n}.             \tag{F}
\]

This is the correct inequality direction. Concavity/Jensen would give an
upper bound and would not establish (F). The upper bound on every mask
energy, together with the exact mean, supplies the needed lower bound.

Average (D), then use (E) and (F):

\[
 \Pr[g(X)\ne g(X^{\mathrm{resample}\,J})]
 \ge[dc_D\sqrt K/B-EmB]/\sqrt n
 \ge dc_D\sqrt K/(2B\sqrt n).                   \tag{G}
\]

The last inequality follows precisely from the (B^2), rather than (B),
in (C). Using the smaller bounded-ratio choice of (K) without adjustment
would not justify this step.

## Physical influence and final constant

Resampling one coordinate changes the output with probability exactly
(I_i(g)/2), and every intermediate input in a successive resampling
hybrid is uniform. The union bound and uniform-subset averaging therefore
give

\[
 \Pr[g(X)\ne g(X^{\mathrm{resample}\,J})]
       \le K I(g)/(2n).
\]

Combining this with (G) cancels both factors of two and gives

\[
 I(g)\ge dc_D\sqrt n/(B\sqrt K),\qquad n\ge N_0. \tag{H}
\]

Together (B) and (H) yield the candidate's large-dimension FEI constant.
For (1\le n<N_0), the audited weak logarithmic bound gives the other
constant. Thus

\[
 H(g)\le\max\left\{\log_2N_0+3,
   \frac{(1+4Am)B\sqrt K}{(\ln2)dc_D}\right\}I(g).
\]

The bounded-ratio premise implies (A), so this theorem includes that family
while allowing arbitrarily small individual weights. The older proof's
smaller (K) remains useful there. This statement still requires bounded
normalized locations of every crossing and fixed input regularity; it does
not resolve irregular-weight or unbounded-bias three-crossing FEI.

## Independent finite checks

The separate implementation
[verify_input_regular_odd_crossing_heat.py](verify_input_regular_odd_crossing_heat.py)
imports no author helper. Its
[report](input_regular_odd_crossing_heat_checks.json) is **PASS**: 63 rational
weight vectors with zero/tiny coordinates; 3,339 exact mask and displacement
moment checks, including 459 zero-energy masks; 189 exact mean-energy
identities and pointwise energy bounds; 189 numerical square-root averages;
and 126 exact physical-resampling comparisons. The numerical square-root
checks supplement the algebraic proof (F), which is the justification in
arbitrary dimension. The very large cutoff is not truth-table enumerated.

I also read the separately written
[author mask checker](verify_input_regular_odd_crossing_mask.py) and its
[passing report](input_regular_odd_crossing_mask_checks.json). Its 11,868
exact mask/moment checks and 362 first-moment identities deliberately include
279 zero-energy masks and rational positive-weight ratios up to 1,048,576
while the normalized maximum stays bounded. These author checks are separate
from my implementation and are not represented as my rerun.

No historical priority claim is made. The full Boolean FEI conjecture, and
ordinary arbitrary-weight arbitrary-bias three-crossing FEI, remain open.
