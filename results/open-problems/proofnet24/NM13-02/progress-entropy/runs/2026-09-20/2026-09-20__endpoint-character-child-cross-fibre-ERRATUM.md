# Erratum to endpoint-character-child-cross-fibre report

This auxiliary correction applies only to the displayed one-point specialization in Section 6 of `2026-09-20__endpoint-character-child-cross-fibre.md`. The theorem, its proof, the checker, the stopping-tree corollary, and `ledger_delta` are unchanged.

For the one-point opposite child, with `delta=2^{1-n}` and nonempty child coefficient magnitude `t=2 delta`, equation (3.7) gives

\[
U_n(2\delta)=2\psi_n(\delta)-\frac12\psi_{n-1}(2\delta).
\]

The correct normalized identity is

\[
\boxed{
\frac{U_n(2\delta)}{\delta^2}
=4\left[n2^{-1/n}-(n-1)2^{-1/(n-1)}\right]-2
=2+o(1).
}
\]

The original displayed line omitted the final `-2`. The subsequent statement `A_i/Inf_i -> 2` and all numerical checker values are correct. The omission does not enter Sections 4–5, where the all-dimensional theorem is proved.
