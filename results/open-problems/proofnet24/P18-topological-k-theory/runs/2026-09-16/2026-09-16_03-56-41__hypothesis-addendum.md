# P18-P44 hypothesis addendum — exact cyclic free-source range

**Applies to:** `proofnet24/P18-topological-k-theory/runs/2026-09-16/2026-09-16_03-56-41__run-report.md`  
**Status:** clarifying qualification; the abstract theorem `P18-FREE-ORIGIN-ISOTROPY-SEPARATION-44` is unchanged.

The triangular specialization in the main report uses

\[
P=P_1C_L
\]

as a **free** `C_L`-CW complex and uses the retained nonzero classifying-space image of the scale-one cyclic class. This requires the scale-one cyclic Rips action to lie in the free range. For the standard cycle metric used throughout the retained P18/P25 source construction, it is enough (and in this program is the relevant asymptotic hypothesis) to impose

\[
\boxed{L\ge4.}
\]

Indeed, the retained free-range criterion is `1<L/3`, which is automatic for `L>=4`. For `L=2,3`, `P_1C_L` can have simplex stabilizers (for example the barycenter of the unique edge when `L=2`), so the main report's free-source application must not be read as asserting the same `P_1C_L` argument without modification at those exceptional small values.

Accordingly, the exact triangular statement of `P18-TRIANGULAR-TATE-KILLER-CERTIFICATE-44` is:

> Fix `m>=2` and `L>=4`. With the retained triangular groups, overlap `X_D^0`, quotient `Y_{m,L,D}`, and cyclic scale-one class `x_{L,1}`, define the free-origin class
> \[
> \widehat\delta_{m,L,D}\in K_1^{C_L}(EC_L\times Y_{m,L,D})
> \]
> from `P_1C_L -> Y_{m,L,D}`. Then its projection to `K_1(BC_L)` is the fixed nonzero cyclic class `±xi_L`, and
> \[
> \delta_D=0
> \iff
> \widehat\delta_{m,L,D}\in
> \operatorname{im}\bigl(
> K_0^{C_L}(\widetilde EC_L\wedge Y_{m,L,D,+})
> \xrightarrow{\partial_{\rm iso}}
> K_1^{C_L}(EC_L\times Y_{m,L,D})
> \bigr).
> \]

All asymptotic conclusions and the proposed P45 attack concern `L -> infinity`, so this qualification does not alter the research direction or any large-`L` bound. It is recorded to keep the hypotheses exact and to prevent the small-`L` simplex-stabilizer issue from being silently ignored.
