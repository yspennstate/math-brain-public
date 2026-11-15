# K5P: does one pair merge at most double the stopping-rule mixing time? (P0242 follow-up)

Codex research run (gpt-6.1-sol, high, normal speed) on Mac mini 1, ~/agent_run/K5P, 12 Nov 2026 21:17-21:47 +04,
started by an agent from the K5 report (fork comb, K(n) >= floor(n/2)).

Result: proved. For every finite irreducible reversible chain and every pair u, v:
tmix(X/{u,v}) <= 2 tmix(X), strictly, sharp (four-state family, ratio -> 2). Entrywise: Fhat_{f(i)f(j)} <= t_i + t_j,
t_i = max_j F_ij. Proof: rank-one update Fhat = F + beta beta^T/(WR); in the positive case the pointwise minimum m of
the two normalised potentials phi_i/beta_i, phi_j/beta_j has m_u - m_v = 1, so E(m,m) >= 1/R (Dirichlet), and the
leftover parts have disjoint support, so their cross energy is <= 0.

With tmix(quotient) <= tau_0 <= (q-1) tau_2 <= (q-1) tmix(X) for q-state quotients this gives K(5) = 2.

Read line by line by an agent (19:5x laptop clock): every step of Sections 1-3 checked by hand, no gap.
Section 5 used the four-state family for the lower bound; a five-state example is needed for K(5) >= 2.
pad5_check.py (exact Fraction solver) hangs a state e on v (w_ev = t^8, loop t^9) and lumps {u,v,e}:
ratios 1.6468 / 1.9606 / 1.9960 at t = 10 / 100 / 1000, so K(5) = 2 holds.
