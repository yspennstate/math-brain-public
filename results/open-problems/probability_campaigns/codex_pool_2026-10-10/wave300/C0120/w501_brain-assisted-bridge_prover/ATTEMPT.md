# C0120 proof checkpoint

Exact target and model assumptions are in STATEMENT_ONLY.md. Current openness is UNKNOWN; no novelty or parent-problem solution is claimed.

Prior digest: C0120-A001 (2026-09-07) proposed converting quantitative disorder chaos to variance improvement, but supplied no quantitative bound. It also imported a conditional FPP scaling relation into polymers and used xi<1 as the threshold. If Var(F_n)=n^(2 chi+o(1)) and chi=2 xi-1 are assumed, a power improvement Var(F_n)<=C n^(1-epsilon) requires xi<=3/4-epsilon/4. For xi=4/5 the assumed relation gives chi=3/5 and variance exponent 6/5, so xi<1 alone does not imply sublinear variance. This is a refutation of the numerical implication, not a theorem establishing the relation for polymers.

First failure measurement: required brain.py recall exceeded its 60-second subprocess budget (63.2059464 seconds including cleanup), produced no stdout, and returned no cards. The raw receipt is recall_receipt.json. Fallback reads used the memory index and a_read_that_takes_the_write_lock_starved_the_guarded_solvers_2026_10_10; the separate required scar perceptron_proof_open_gaps_fleet_2026_07_12 reinforced that a completed local sublemma cannot close an unchecked parent gap.

Lane: quantify the exact OU-coupled overlap bridge on the source's Gaussian maximum, and test whether existing hypercontractive marginal bounds could close it. Positive-temperature results will be labeled a separate Gaussian specialization.

Hardest remaining gap: a bound E|P_n(g) intersect P_n(g^t)|<=C n^(1-delta) at t=n^(-alpha), with fixed alpha,delta>0. The source's logarithmic-scale chaos estimate does not supply these exponents.

Completed proof attempt: LEMMAS.md contains the exact rate bridge (L1), the applicable Gaussian hypercontractivity bound (L2), the layerwise obstruction to its certificate (L3), and the conditional exponent correction (L4). BRAIN_HYPOTHESIS_CHECK.md compares four full cards, rejects the discrete-cube shortcut and records the source mismatch. The most useful new deduction is L3: the direct per-site certificate stays of order n at polynomially small noise time, and its integral is at least (n-1)/log n. This is not an actual variance lower bound.

Validation: python -X utf8 validate_math.py completed in 0.1110152 s; 24 envelope checks passed. The actual n=2 source model gives Var(M_2)=2-1/pi=1.6816901138162093, whereas numerical integration of its exact coupled-overlap expression gave 1.6816901138162585 (absolute error 4.92939e-14). These checks validate normalization and finite examples; the prose proof and independent review remain distinct.

Recovery: targeted rg over the one named math export returned 20 matches in 5.7347419 s; four full indexed read-only node/payload lookups completed in 0.0041898 s. These are different channels from brain.py's memory recall, so they do not establish a global speedup or retrieval-quality gain. The bounded proposed repair is to fail over from a deadline-expired recall to one scoped export lookup and then exact indexed card reads, keeping provenance and hypotheses visible.

Harness correction: the first recall_probe.py used a bare trailing 3, which the live CLI incorporates into the query instead of treating as a count. The actual timed-out call therefore queried the intended text plus ' 3'. The harness now uses '-n 3'. The timeout receipt is retained unchanged and is not used as ranking-quality evidence.

NEXT: Independently review the saved certificate obstruction, then attempt a bound on joint geometry of two OU-coupled maximizers at t=n^(-alpha); do not rerun open-status searches as a substitute for that proof step.
