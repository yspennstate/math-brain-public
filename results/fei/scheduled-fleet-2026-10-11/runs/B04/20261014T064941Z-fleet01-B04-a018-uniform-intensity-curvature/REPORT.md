# B04 / A018 — uniform vanishing-gap curvature with an exact paid boundary

**Status:** PROVED for a growing shared-data family uniformly on fixed-intensity compacta away from the balanced spectral atom; pending independent review. **Universal GU and full FEI remain OPEN.**

## Frozen candidate

Primary packet: **A018**. Attempt: `A018-UNIFORM-INTENSITY-CURVATURE-3`. Stable gap: `G-LOW-GAP-SHARED-DATA-COLLISION`. Claim version: `B04-A018-UNIFORM-INTENSITY-CURVATURE-v2`.

For one physical coordinate `s`, test the complete signed increment

\[
Q_s=G(f)-\frac{G(f_{s,+})+G(f_{s,-})}{2}
=\Delta_sU+\sum_{i\ne s}\Delta_s\Delta_iU
\]

against `Inf_s(f)`, while retaining the exact child residual rather than declaring a favorable local step to be closure.

## New theorem

Let `f_{k,r}` be the OR of `k=floor(lambda 2^r)` disjoint `r`-bit point defects and expose one bit of one block. The children share all remaining physical data and have disagreement gap

\[
\delta=\operatorname{Inf}_s(f_{k,r})\asymp_\lambda2^{-r}.
\]

For every compact `K` contained in `(0,infinity)\{ln 2}`, uniformly for `lambda in K`,

\[
\frac{\Delta_sU}{\delta}=1+2r2^{-r}+O_K(2^{-r}),
\]

but

\[
\boxed{\frac{Q_s}{\delta}=1-2r^2 2^{-r}+O_K(r2^{-r}).}
\]

Thus for all sufficiently large `r`, uniformly on `K`, the selector-only coefficient-one payment fails while the complete shared-data increment satisfies `Q_s<Inf_s`. This extends the preceding `lambda=1` result to an all-parameter fixed-intensity family without any positive lower bound on the branch gap.

## Exact child transport

With `E=G-I`, restriction gives exactly

\[
Q_s-\delta=E(f)-\frac{E(f_{s,+})+E(f_{s,-})}{2}.
\]

The root residual is nevertheless positive:

\[
E(f_{k,r})=4\lambda e^{-\lambda}r^2 2^{-r}+O_K(r2^{-r}).
\]

Therefore

\[
\frac{E(f_{s,+})+E(f_{s,-})}{2}=E(f)+(\delta-Q_s).
\]

The curvature refund is a genuine nonreused reserve, but it is transported into a larger average child debt. This is the requested paid boundary: no leaf inequality is assumed, and favorable local drift is shown explicitly not to close `G<=I`.

## Exceptional balance and verification

`lambda=ln 2` is excluded because the constant Fourier mass tends to zero and the `x log(1/x)` cusp invalidates the bounded-derivative expansion. Exact formulas remain valid there, but it is a separate asymptotic regime.

The 120-digit reconstruction tested eight intensities from `0.1` through `4`, six ranks at each intensity, and 96 strict sign assertions. It retained both unequal children and all physical restrictions. The numerical table is diagnostic; the theorem is analytic.

## GU implication and next unpaid step

This proves a coefficient-one complete-increment payment for one broad vanishing-gap shared-data family, but not a universal pair `(a,b)`. The remaining task is to find a Boolean posterior/terminal potential `P` such that

\[
Q_s-a\operatorname{Inf}_s-b\Delta_sU\le P(f)-\mathbb E_sP(f_s)
\]

and `P` has a dimension-independent terminal bound, with each influence spent once. The next concrete test is the exceptional balanced intensity and then a non-block-symmetric addressing family.

Review targets: A090, A091, A094.
