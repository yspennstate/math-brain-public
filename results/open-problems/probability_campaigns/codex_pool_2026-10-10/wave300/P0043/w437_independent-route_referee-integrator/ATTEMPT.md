# P0043 independent route (written before reading w435/w436 proofs)

2026-10-10. Work with independent Bernoulli **bond** percolation on an infinite, connected, locally finite, quasi-transitive graph, and assume p_c<1. Put a_n(p)=P_p(o connected to the boundary of B(o,n)). Then a_n(p) decreases to theta_o(p). I would try to control the loss of connectivity across scales by a finite-volume differential inequality and a revealment algorithm for a_n. If one could prove a scale-uniform estimate that forces a_n(p_c) to zero as n grows, this would settle the conjecture; any inequality whose constants depend unboundedly on n is insufficient.

The independent obstacle is precisely the missing scale-uniform estimate in polynomial/subexponential growth, including Z^3. Exponential-growth quasi-transitive graphs are covered by Hutchcroft (2016). A positive-density infinite cluster, if assumed, cannot simply be thinned and declared supercritical: no theorem establishing that implication has been supplied. This is an approach and a gap, not a proof.

Current source-status alert: a public OpenAI math repository has a September 2026 preprint claiming this exact general statement. Verify its actual theorem and proof before making any novelty or open-status claim. Its Lean comparator challenge currently ends in `sorry`, so that file alone is no formal proof.
