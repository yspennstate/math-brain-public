# B16 handoff — central Bernoulli/Walsh compiler

Status: **PROVED exact bridge / full FEI OPEN / WITHOUT_VERIFIED_BRAIN**.

The main new identity is that the exact odd q-flip parity-frustration
polynomial is complementary-Bernoulli antisymmetry of the Walsh transform
of the live signed R32 coefficient field:

\[
P_s^{odd}(t)
=
\frac12\left(
E_{\operatorname{Ber}((1-t)/2)}\Phi_s
-
E_{\operatorname{Ber}((1+t)/2)}\Phi_s
\right).
\]

For each active q-flip `v` its first-hit derivative is exactly

\[
m'_{v,s}(t)
=
\frac18\sum_{u\ne v}
\left(
E_{(1-t)/2}\Delta_u\Delta_v\Phi_s
-
E_{(1+t)/2}\Delta_u\Delta_v\Phi_s
\right).
\]

The live potential is not synthetic:

\[
\Phi_s(S)=\Phi_{C_0,s}(g_S)-\Phi_{D_d,s}(g_S),
\]

so the existing exact MacWilliams formula retains the genuine
`RM(1,n)` multiplicity and terminal code.

For a single odd syndrome degree `q>=3`, the central radial multiplier is

\[
(q-1)t^{q-2}\le2t\quad(0\le t\le1/2),
\]

and its exact Hardy/Ward scalar square weight is

\[
\omega_q=\frac{q-1}{(2q-1)2^{2q}}\le\frac1{160}.
\]

Thus radial syndrome degree itself is dimension-free after the exact odd
projection/refund. The remaining possible growth is cross-relation and
physical-coordinate geometry.

A second exact theorem computes the unweighted two-point Borel coefficient
correlation at fixed symmetric difference `Delta`. If `m=|Delta|` and `k`
is the affine-span dimension of nonzero `Delta in C_0`, then

\[
\sum_{A\in C_0}c_A(s)c_{A\triangle\Delta}(s)
=
2N(-1)^{m/2}\sin(2s/N)^m
\left[
\cos(2s/N)^{N-m}
+
(2^{n-k}-1)\cos(2s/N)^{N/2-m}
\right],
\]

with the second term absent when its multiplicity is zero. The phase-twisted
version is a constrained `RM(1,n)` weight enumerator. In particular, the
pair correlation of two simultaneously frustrated relations vanishes
unless `f_Delta=+1`.

**Exact remaining obstruction:** the Hardy/R16 kernel still contains
`(q_A-1)/q_A`, `(q_B-1)/q_B` and `|R_A cap R_B|`, which depend on the two
relations separately. The next move is to convert those first-hit weights
to auxiliary integral/noise parameters and try to extend the two-point
MacWilliams collapse before taking any absolute value.

Do not revive:
- basiswise local `L_v=O(n)`;
- absolute Shapley turnover;
- unsigned pairwise-square divergence;
- generic endpoint `L2` control.
