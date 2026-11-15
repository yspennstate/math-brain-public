# F0127A status (an agent, 12 Nov 2026 22:42 laptop time)
Aldous (Bernoulli 2013) Open Problem 2: assuming (5.2), under what further conditions is E T_coal ~ 2 tau_meet?
Codex run (gpt-6.1-sol high, normal speed, Mac mini 1) returned COUNTEREXAMPLE to the candidate condition
"uniform stationary law + worst-start t_mix = o(tau_meet)": symmetric-rate chain on n = k^4 + k states (complete core
of k^4 sites at rate 1/N, k slow sites joined to every core site at rate sqrt(log k)/N^2). tau_meet ~ n/2, all
distinct-pair meeting times uniformly ~ tau_meet, t_mix ~ 2 log 4 n / sqrt(log n) = o(tau_meet), yet
E T_coal ~ (n/2) sqrt(log n). Lower bound is elementary (second-largest of k Exp(r) exit clocks).
Checked by hand by an agent (pair-type equations, spectral TV formulas, the order-statistic lower bound);
numerics exact to 1e-15 against full pair and subset generators.
Verdict for the ledger: PARTIAL (negative example narrowing OP2; OP2 itself is open-ended). Close precedent:
Kanade-Mallmann-Trenn-Sauerwald arXiv 1611.02460 Thm 1.2 (t_mix = o(M) with EC/M -> infinity, almost-regular graphs,
discrete time). Not paper-worthy alone; candidate remark inside a broader coalescence note.
