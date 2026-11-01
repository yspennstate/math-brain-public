# B04 / A018 — shared-data curvature pays a failing selector-only charge

**Status:** PROVED on a growing vanishing-gap family, pending independent review. **Universal GU and full FEI remain OPEN.**

## Frozen candidate

- Primary packet: **A018**.
- Attempt: `A018-CURVATURE-REFUND-2`.
- Stable gap: `G-LOW-GAP-SHARED-DATA-COLLISION`.
- Claim version: `B04-A018-CURVATURE-REFUND-v1`.
- Frozen local pair: `(a,b)=(1,0)`.

For a selector coordinate `s`, test the complete signed increment

\[
Q_s:=G(f)-\frac{G(f_{s,+})+G(f_{s,-})}{2}
=\Delta_sU+\sum_{i\ne s}\Delta_s\Delta_iU
\]

against `Inf_s(f)`. The prior first-order theorem gave only `Q_s/Inf_s->1` and did not determine the sign of the surviving reserve.

## New theorem

Take the OR of `k=2^r` disjoint `r`-bit point defects and expose one bit of one block. The children share every remaining data coordinate and disagree with probability

\[
\delta=\operatorname{Inf}_s=2^{1-r}(1-2^{-r})^{2^r-1}\to0.
\]

The exact heterogeneous-child formulas and a second-order expansion give

\[
\boxed{\frac{\Delta_sU}{\delta}=1+2r2^{-r}+O(2^{-r}),}
\]

but

\[
\boxed{\frac{Q_s}{\delta}=1-2r^2 2^{-r}+O(r2^{-r}).}
\]

Thus, for all sufficiently large `r`,

\[
\Delta_sU>\operatorname{Inf}_s,
\qquad
\Delta_sU+\sum_i\Delta_s\Delta_iU<\operatorname{Inf}_s.
\]

The mixed shared-data curvature has the explicit negative scale

\[
\frac1\delta\sum_i\Delta_s\Delta_iU
=-2r^2 2^{-r}+O(r2^{-r}).
\]

This is the first proved vanishing, nonuniform branch-gap example here where the selector-only charge fails but the complete signed GU increment is paid by the same physical selector influence.

## Exact GU and terminal implication

For the frozen pair `(1,0)`, the local residual increment `Q_s-Inf_s` is negative. Nevertheless the companion B16 theorem proves that the root residual `G(f_r)-I(f_r)` is positive. Hence favorable local drift does not close GU unless the child/terminal residual is retained and paid. This is an explicit demonstration that a stopping proof cannot discard its terminal `U`/residual boundary.

The theorem is restricted to the growing OR-defect family. It neither proves `G<=I` nor supplies a universal pair. Its structural contribution is sharper: the full signed shared-data term can reverse the sign of a selector-only overrun without any gap lower bound.

## Verification

The 120-digit reconstruction checks all exact heterogeneous `U` and `G` formulas for `4<=r<=50`. In all 47 cases, `Delta_s U>delta` while `Q_s<delta`; the three normalized second-order ratios move toward one. The finite table is diagnostic only; the theorem follows from the analytic expansion in `CURVATURE_REFUND.tex`.

## Next unpaid step

Find a Boolean-specific sign or reserve theorem for the mixed curvature beyond this family, with the terminal child residual included. A useful next test is the same calculation for addressing/near-identical branches where the shared data are not block-symmetric.

Review targets: A090, A091, A094.

