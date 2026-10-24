# Post-readback addendum — fresh account03/B03 clique-theta stress test

This addendum preserves the immutable `report.md` and records a relevant peer artifact that landed after the report was committed.

Fresh peer consumed: account03/B03 run `20260922T043338Z-b03-forest-r12`, report blob `a1e4fb931fd7f024376ba263d38309b63f690450`, candidate `FOREST-STARK-THETA-EXACT-v1`.

B03 independently rederived the complete-graph Hermite theorem and constructed simple clique-theta graphs from `r` copies of `K_m-uv` glued at `u,v`. Its exact two-cut formula shows that same-bridge marked pairs induce a virtual boundary weight

`lambda=(r-1)(Z_m/P_m-2)`

and its Stark asymptotics give

`lambda=(r-1)(m/2-7/4+13/(8m)+O(m^-2)) -> infinity`.

This peer result is fully compatible with the present correction and strengthens its interpretation: any separator globalization must control genuinely unbounded positive virtual weights. However, B03's final globalization paragraph again invokes the same disputed fixed-graph Cocks implication. Therefore the clique-theta calculation is retained as an exact stress theorem, while its final `unit K_n => weighted K_n` closure is not accepted independently.

Combined with the equivalence proved in the canonical report, the unbounded `lambda` phenomenon explains why a bounded-weight or unit-only perturbative bridge cannot close the all-graphs problem: weighted complete-graph control across the full positive orthant is equivalent to the parent target.
