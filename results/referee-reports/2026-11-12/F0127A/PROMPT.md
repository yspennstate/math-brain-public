You are a research probabilist. Problem (Aldous, "Interacting particle systems as stochastic social dynamics",
Bernoulli 2013, Open Problem 2, Section 5.5; text in aldous.txt lines ~740-795): continuous-time reversible chains with
symmetric rates (uniform stationary law) on n states, run at half speed; tau_meet = mean meeting time of two
independent walkers from uniform starts; T_coal = time for coalescing walkers started one per state to reach one
cluster. Assuming (5.2) [for each delta>0, the fraction of ordered pairs (i,j) with E T^meet_ij outside
(1 +- delta) tau_meet tends to 0], under what further conditions does E T_coal ~ 2 tau_meet hold?

Known (read oliveira.txt = Oliveira, Mean field conditions for coalescing random walks, AoP 2013; hlyz.txt = Hermon-Li-
Yao-Zhang, AoP 2022): transitive reversible chains: E C = (2 + o(1)) m whenever t_mix = o(m) (Oliveira Thm 1.1); general
chains: (1 + q_max t_mix) pi_max -> 0 suffices (Thm 1.2). Simple fact: (5.2) alone is NOT enough (a complete graph
plus one vertex joined by a symmetric edge of rate n^{-1.5}: (5.2) holds, E T_coal >= n^{1.5} >> tau_meet ~ n/2).

Target question: for reversible chains with UNIFORM stationary law (not necessarily transitive), does
t_mix = o(tau_meet) (worst-start total-variation mixing time) imply E T_coal ~ 2 tau_meet? Either prove it, or build an
explicit counterexample family (compute tau_meet, t_mix and E T_coal to leading order, and verify numerically for
moderate n by exact linear algebra / simulation), or prove it under a strictly weaker hypothesis than Oliveira's Thm 1.2
that still covers non-transitive examples Thm 1.2 misses. FIRST search the literature (arXiv, Google Scholar; in
particular Kanade, Mallmann-Trenn, Sauerwald, "On coalescence time in graphs: when is coalescing as fast as meeting?",
and any work citing Oliveira 2013 on coalescence time vs meeting time) and state precisely what is already known; do not
claim something already in print as new.
Write REPORT.md (first line: PROVED / COUNTEREXAMPLE / PARTIAL / KNOWN-IN-LITERATURE / NO-PROGRESS), full proofs with
every constant, a literature section with exact theorem numbers, LOG.md with timestamped progress, and your scripts.
Use at most 6 CPU threads and 8 GB RAM for numerics.
