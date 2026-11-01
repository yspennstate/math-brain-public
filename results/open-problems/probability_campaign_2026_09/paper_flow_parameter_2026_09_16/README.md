# The flow parameter, the relaxation time and the diameter

Companion material for the paper of the same title (Y. Shmalo, September 2026), which answers part (ii) of
Open Problem 4.49 of Aldous and Fill, *Reversible Markov Chains and Random Walks on Graphs* (Sinclair's
question whether the inequality inf_f psi(f) <= K tau_2 log n holds with the diameter in place of log n).
It does not, for any constant: on the cone over a d-regular Ramanujan graph on n vertices the diameter is 2,
the relaxation time is at most (d+1)/(d+1-2 sqrt(d-1)), and the flow parameter tends to 2(d+1), so the
ratio of the flow parameter to tau_2 times the diameter exceeds d+1-2 sqrt(d-1) in the limit. A diameter
bound with a constant of order log D (D the maximum degree) does hold, and the cones show that order cannot
be lowered below log D / log log D.

Contents

- `paper/` the LaTeX source and the compiled PDF.
- `numerics/af449lib.py` the library: cones, BFS distances, the finite field GF(q) and the incidence graph of
  PG(2,q), the linear program for the flow parameter (SciPy, HiGHS), exact rational evaluation of edge-length
  certificates (Dijkstra on integer weights), the two-length certificate of the paper in closed form, the hub
  routing bound, the ball bound, and the spectra.
- `numerics/check_exact.py` the exact checks: the PG(2,49) numbers, the closed form of the certificate on ten
  projective-plane cones, the generic certificate evaluator against the closed form, the spectrum of the cone
  against the formula on three bases, and the hub routing evaluated as an explicit flow family.
- `numerics/test0.py`, `numerics/test1.py` the sanity checks of the linear program against known exact values
  (complete graphs, the wheel, cones over strongly regular graphs) and the linear program on the small
  projective-plane cones.
- `numerics/rr_lp.py`, `numerics/rr_lp_worker.py` the linear program on cones over random regular graphs
  (`rr_lp_results*.csv`).
- `numerics/rr_dual_large.py` the certificates on larger random cones (`rr_dual_large_results.csv`).
- `numerics/lps_cone.py` the Lubotzky-Phillips-Sarnak graphs X^{5,q} built from the six quaternions of norm 5
  as 2x2 matrices over F_q, and the certificates on their cones (`lps_results.csv`).
- `numerics/wheel_check.py` the wheels K_1 v C_n, on which the linear program equals the certificate.
- `numerics/results.md` the tables of the paper and the output of `check_exact.py`.

To reproduce: `python numerics/check_exact.py` (fractions, numpy, networkx; seconds), `python numerics/test0.py`
and `test1.py` (scipy; seconds), `python numerics/rr_lp.py` (minutes to an hour, the d = 3, n = 160 case is the
slow one), `python numerics/rr_dual_large.py` and `python numerics/lps_cone.py` (minutes). The linear-program
values carry the solver's tolerance, about 1e-8; every certificate is computed in exact rational arithmetic.
