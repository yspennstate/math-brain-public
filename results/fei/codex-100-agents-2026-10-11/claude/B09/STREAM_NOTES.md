# B09 stream notes (Claude lead) - v2, 2026-10-11 23:33 UTC

Full FEI: OPEN. Bridge to C000 (A043, composition identity re-checked with unequal biases): corrected product-biased FEI+ on every prime gate at every interior law is equivalent to universal biased FEI+, and that gives FEI with max(C, log2 e). This is a localization, not a reduction.

## Established
- L_A = M_A + J_A; tax-free J<=M is false (AND p=1/8, q=1/4, margin > 0.1195, interval-repaired).
- SHARP ONE-BIT TAX (lead, B09-CLAUDE-SHARP-ONE-BIT-TAX v1, run claude/B09/runs/20261011T225000Z-...): for every Boolean f, in any dimension, J-M <= tau*(p) = h2(p) - min_{d<=theta}[k(d)+k(theta-d)], with k = h2(sin^2), sin^2 theta = p. For p <= 0.0832 an AND with q* = 1/(2(1+sqrt(1-p))) attains (1-p) tau*. tau* = (p/2)log2(1/p) - 0.27865p + O(p^2 log) <= (p/2)log2(1/p) + 0.4427p for p <= e^-3. tau*(1/2) = 0. A045 reconstructed (i) and the envelope; A091 has not reviewed it.
- A041's AND lower bound holds (re-derived). A041's singleton lemma <= 4 Delta holds. The A041 refresh inequality survived 1,836 random float checks; its rank/prior proof is NOT reviewed.
- A043: census 10/104/57,240 primes at n=2,3,4; localization theorem (composition part re-derived by the lead).
- A044: address gates with a common data mean satisfy H+ <= 4(I-Var), sharp; read-once compositions with equal induced means get max(4, C_leaf).

## Refuted / do not repeat
- tax-free J<=M; any O(p) or sub-1/2 tax; event-TC and coefficient-one pivotal payments (three weighted guards); a uniform-input prime estimate applied at induced biases.
- Do not recompute the one-bit tax or the AND coefficient. The tax is per revealed bit and pays nothing; it must itself be paid by delta.

## Next targets (one each)
- A041: E_{>=2} <= K Delta for two-weight thresholds 1[w sum_A X + sum_B X >= t]. Condition on the heavy count; each slice is a symmetric threshold. Uniform in arity and in every bias, or the exact obstruction.
- A042: certified sup over all (p,q) in (0,1)^2 of H+/Delta for every essential binary gate, both biases degenerating at independent rates (the arity-2 prime base case).
- A043: largest H+_mu/Delta_mu over primes n<=4 under product biases (discovery grid first, then an exact certificate). A divergent family kills the route; record it either way.
- A044: drop the common-mean hypothesis in two-mean address gates. Find the exact sup of H+/Delta over data means (m1, m2), or a divergent sequence.
- A045: test sum_i tau*(eta_i) <= K delta_eta(g) on address gates and symmetric thresholds of arity <= 6, revealing inputs one at a time at the induced biases (exact arithmetic). Report the worst ratio and its trend in arity.

Review cap: B09 is over the cap (A041 x2, A042, A043, A044, A045, lead). Review and repair come before new broad claims. REPORT.md for the lead run was refused by the subagent harness; the report is in the run's StructuredOutput and JSON records.
