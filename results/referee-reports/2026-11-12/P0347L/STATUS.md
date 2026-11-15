# P0347L status (an agent, updated 12 Nov 2026 22:30 laptop time)
Codex attempt (gpt-6.1-sol high, normal speed, Mac mini 1) on the open part of P0347: PROVED a full limit law
(S_n - ES_n)/(n log n) -> W, all moments, same W for Colless (joint limit (W,W)), a_k by recurrence (4),
|a_k| <= 2^k k!, char.-function fixed point (5) unique among centered laws with an exponential moment.
REFEREED MINOR by P0347LR (independent Codex referee, Mac mini 1, report in ../P0347LR/REPORT.md). One required
change, the same one P0347R asked for: in Section 3 the lower-log endpoint bound must read
|F_{p,j}(x)| <= C (x^{p-1}|log x|^j + x^{j-1}) near 0 (counterexample F_{2,1} -> -1/2). Everything downstream
survives: (8), (9), transfers at p=1/2 and p=k, constants, (4), (5), uniqueness. Referee recomputed a_2..a_8 by fresh
quadrature and zeta formulas and matched the table (a_2 = 0.280574126406891865077...). Novelty limited to inspected
sources (Aldous-Janson OP10, BCM, Kolesnik 2404.16021, CMS 2608.18320); not a solution of OP9.
finite_moments.csv is gzipped here.
