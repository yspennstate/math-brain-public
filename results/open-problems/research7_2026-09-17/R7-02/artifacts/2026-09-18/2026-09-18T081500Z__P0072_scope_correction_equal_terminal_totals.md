# P0072 suspension theorem — immutable initialization-scope correction

This addendum corrects one overbroad initialization phrase in the immutable artifact

`research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T074500Z__P0072_stochastic_suspension_extinction.md`

and its corresponding `2026-09-18T080500Z__report.md` summary.

The proof as written defines a **common** terminal total

\[
S_n=\sum_iW_{si}(n)=\sum_iW_{it}(n)=S_0+n.
\]

That equality is automatic under the source-standard all-ones initialization, and more generally whenever the two terminal totals are equal initially. It is **not** automatic for arbitrary positive integer initial weights with unequal initial terminal totals.

Therefore every phrase in those immutable files claiming the theorem for arbitrary `positive integer initial weights` must be read with the precise hypothesis

\[
\boxed{
\sum_i W_{si}(0)=\sum_i W_{it}(0).
}
\]

In particular the theorem is fully applicable to the standard initialization `W_e(0)=1` for every edge, which is the normalization used in the parent Kious–Mailler–Schapira model.

Under this corrected hypothesis, no line of the proof changes: the common scale `S_n=S_0+n`, harmonic compensator identity, excess-resistance summability, terminal-imbalance estimate, forest-pairing contraction, and martingale-tail upcrossing argument all remain exactly as written.

No claim is made here for unequal initial terminal totals. Extending the proof to that case would require keeping the two scales `S_n^L` and `S_n^R` separate and is outside this run's proved statement.

Corrected theorem scope: **for every finite two-terminal suspension graph under loop-erased reinforcement with equal initial terminal totals (in particular all initial weights one), every internal non-geodesic edge has `W_e(n)=o(n)` almost surely, and the two normalized terminal distributions converge to each other in `L1`.**

This is a scope correction only. Full canonical P0072 remains OPEN, the frozen metric remains zero, and publication novelty remains UNVERIFIED.