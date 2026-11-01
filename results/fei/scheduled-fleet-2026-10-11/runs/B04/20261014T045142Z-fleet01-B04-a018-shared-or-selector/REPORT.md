# B04 / A018 — complete shared-selector GU increment at vanishing gap

**Status:** PROVED on a growing shared-data family, pending independent review. **Full FEI remains OPEN.**

## Frozen candidate

For a selector `F(s,x)` with branches `g,h`, analyze the exact local residual for a proposed universal pair `(a,b)`:

\[
\mathcal R_{a,b}(F)-\frac{\mathcal R_{a,b}(g)+\mathcal R_{a,b}(h)}2,
\qquad \mathcal R_{a,b}=G-aI-bU.
\]

Primary packet: **A018**. Attempt: `A018-SHARED-OR-SELECTOR-1`. Stable gap: `G-LOW-GAP-SHARED-DATA-COLLISION`. Claim version: `B04-A018-SHARED-OR-SELECTOR-v1`.

## Exact identity

Commuting physical restriction operators gives

\[
G(F)-\frac{G(g)+G(h)}2
=\Delta_sU(F)+\sum_{i\in x}\Delta_s\Delta_iU(F).
\]

Therefore the complete residual is

\[
(1-b)\Delta_sU+\sum_i\Delta_s\Delta_iU-a\operatorname{Inf}_s(F).
\]

The mixed-curvature sum is the full shared-data term. A selector-only entropy estimate does not control the GU increment unless this term is retained.

## Vanishing-gap shared-data theorem

For the OR of `k` disjoint `r`-bit point defects, expose one physical selector bit. The children share all remaining data, are nonuniform, and disagree with probability

\[
\delta_{k,r}=2^{1-r}(1-2^{-r})^{k-1}\to0.
\]

Taking `k_r 2^{-r}->lambda` for fixed `lambda>0`, the exact heterogeneous upper-set formulas prove

\[
\frac{\Delta_sU}{\delta_{k_r,r}}\to1,
\]

\[
\frac{G(F)-\tfrac12G(g)-\tfrac12G(h)}{\delta_{k_r,r}}\to1,
\qquad
\frac{\sum_i\Delta_s\Delta_iU}{\delta_{k_r,r}}\to0.
\]

The convergence is uniform for `lambda` in a compact subset of `(0,infinity)`. All selector, physical-data, normalization, and unequal-child terms are included.

## GU consequence

After division by the actual selector influence, the exact local residual tends to

\[
1-a-b.
\]

Hence every universal GU pair—and every local stopping rule that truly telescopes the GU residual—must satisfy

\[
\boxed{a+b\ge1.}
\]

This identifies the sharp single-use reserve on a nearly identical-branch family. It also falsifies the hoped-for global half-tax region: an argument concluding `G<=I/2` must have omitted or reused a term, even though its two-bit local kernel may be correct.

The result does not prove `G<=I` universally. It narrows the viable search to pairs on or above `a+b=1`, `b<1`, and supplies the exact local expression any nonreused posterior reserve must dominate.

## Verification and next step

An 80-digit reconstruction evaluates the exact heterogeneous `U` and `G` formulas for four activation intensities and `r=8,12,16,20`. It confirms the complete increment identity and the three asymptotic ratios. The table is diagnostic; the proof is the operator identity plus analytic expansion in `SHARED_OR_SELECTOR.tex`.

Next: seek a Boolean-specific inequality bounding

\[
\Delta_sU+\sum_i\Delta_s\Delta_iU\le \operatorname{Inf}_s+b\,\Delta_sU
\]

with one `b<1`, or construct an overlapping family where the normalized mixed curvature has a positive nonzero limit. Review targets: A090, A091, A094.

