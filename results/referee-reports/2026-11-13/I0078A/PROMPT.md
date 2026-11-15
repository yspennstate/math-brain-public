Open problem I0078. Source: D. Dereudre and T. Digneaux, a 2025 paper on number-rigidity and Wasserstein distance of
one-dimensional point processes (identify title, authors, arXiv number, version, date and pages exactly from the listing),
Conjecture 2.9: "For -1 < s < 0, there exists beta_0(s) > 0, decreasing in s, such that for beta > beta_0(s) we have
Wass1(P_{s,beta}, Leb_R) < +infinity, whereas for 0 < beta < beta_0(s) we have Wass1(P_{s,beta}, Leb_R) = +infinity."
State exactly what P_{s,beta} is (the infinite-volume one-dimensional Riesz gas with interaction -|x|^{-s} or |x|^{-s}/s for
-1 < s < 0, its construction as a limit of finite or periodic gases, uniqueness or not), what Wass1(P, Leb_R) means for a
stationary point process (the transport cost per unit length between the process and Lebesgue measure, or to the lattice
P_Z), and what Theorem 2.2 and the other results of the paper prove about it (number-rigidity from Wass1(P, P_Z) < infinity,
and which (s, beta) are already covered).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ as plain text. Read the papers it relies on and the Riesz-gas literature for
   -1 < s < 0: Boursier (optimal local laws and CLT for 1D long-range Riesz gases; decay of correlations), Lewin's survey on
   Coulomb and Riesz gases, Leble--Serfaty, Dereudre--Hardy--Leble--Maida (DLR equations and rigidity for the sine-beta
   process), Erbar--Huesmann--Leble (the Sine-beta process is a Wasserstein-optimal matching / hyperuniformity), Huesmann--
   Sturm and Huesmann (optimal transport between point processes and Lebesgue, the L^1 and L^2 matching costs and their link
   to number variance), Ghosh--Peres (number rigidity), and any 2025-2026 paper citing the source on Conjecture 2.9. State
   exactly what is known about the variance of the counting function N[0,L] for the Riesz gas in this range (order L^{-s}?
   log L? bounded?), since Wass1 finiteness in one dimension is governed by the displacement field. If a printed result
   decides the conjecture (either direction, or shows that no threshold exists, e.g. Wass1 finite for every beta > 0 or
   infinite for every beta), report it and stop with RESOLVED_IN_LITERATURE.
2. Otherwise attack it. In one dimension a stationary process at intensity 1 has finite Wass1 cost to Lebesgue (or to a
   randomly shifted Z) iff the matching displacement is integrable; the natural candidate is the cumulative discrepancy
   D(x) = N[0,x] - x and its stationarity or growth. Decide what the known (or provable) variance and tail bounds of N[0,L]
   for P_{s,beta} imply: if Var N[0,L] grows (like L^{-s} or log L) the displacement cannot be stationary and Wass1 may be
   infinite; if it is bounded, check the stronger condition needed. Look for (i) an argument that Wass1 is finite for large
   beta (low temperature, crystallisation towards Z, a coupling with the lattice plus fluctuations whose sum converges), (ii)
   an argument that Wass1 is infinite for small beta (high temperature, a lower bound on the variance growth), and (iii)
   whether the dichotomy depends on beta at all or only on s (it might be that Var N[0,L] ~ c(s,beta) L^{-s} for every beta,
   which would make Wass1 infinite for all beta and refute the threshold form). A complete answer, or a proof that the
   conjecture fails as stated, is PROVED or COUNTEREXAMPLE; one direction (only large beta or only small beta) with every step
   checked and not already in print is PARTIAL with substance. Check every step and every exponent.
3. Compute only to check: small exact or Monte Carlo computations of periodic Riesz gases (N up to a few hundred) for the
   variance of N[0,L] at two values of beta, to see which growth the theory predicts. Keep runs small; no simulation stands in
   for a proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
