Open problem I0006B, a borderline case left open in print. Model (verify everything from the sources): the synchronous divisible
sandpile odometer on Z^d, u_0 = 0, u_{n+1}(x) = (eta(x) + P u_n(x))_+, with P the simple-random-walk averaging operator and eta
i.i.d., mean zero, positive finite variance, E exp(theta|eta(0)|) < infinity for some theta > 0 (A. Bou-Rabee, C. Panagiotis,
"Sharpness and critical scaling of parking", arXiv:2609.02820v1, Theorem 3.4 p.14, and the companion "Quantitative explosion and
percolation of the divisible sandpile", arXiv:2609.02829v1). For d >= 5 the companion's Theorem 1.3(iii)(b) (p.6; proof Proposition
6.3 p.53, Lemmas 6.4-6.5, Theorem 6.6 pp.55-56) gives E u_n(0) of order (log n)^{1/min(gamma, d/2)} when
-log P(eta(0) < -t) is between c t^gamma and C t^gamma, 1 <= gamma, gamma != d/2, and excludes gamma = d/2 explicitly (p.10).
At gamma = d/2 the printed results give c (log n)^{2/d} <= E u_n(0) <= C_eps (log n)^{2/d + eps}; the upper-bound argument hits
the logarithmic divergence of sum_y G(0,y)^{q*} with q* = gamma/(gamma-1) = d/(d-2).

The question: at gamma = d/2 (d >= 5), find the exact order of E u_n(0), e.g. (log n)^{2/d} with or without a power of log log n.
Secondary, if time remains: stretched-exponential lower tails 0 < gamma < 1 with the upper tail still exponential (the exponential
moment of |eta| fails); does (log n)^{1/gamma} still hold, or does it change?

Do this, in order, saving as you go:
1. Get both arXiv papers into sources/ as plain text. Read the companion's Section 6 (Theorem 6.1, Corollary 6.2, Proposition 6.3,
   Lemmas 6.4-6.5, Theorem 6.6, equations (86)-(94)) line by line and write down exactly where gamma != d/2 is used and what the
   log divergence costs. Search for any later work (2026) settling the borderline; if it is in print, report RESOLVED_IN_LITERATURE.
2. Attack it. Heuristic first: at level m the cost of a single deep hole is m^gamma and of a collective Green-weighted deficit is
   m^{d/2}; at gamma = d/2 both mechanisms cost the same order, and mixed configurations (a moderately deep hole plus a collective
   deficit at scale L) may gain a log factor. Compute the optimal mixed cost (a variational problem over hole depth profiles, the
   Green function sum restricted to radius L) and decide whether the rare-event exponent at level m is m^{d/2} or
   m^{d/2}/(log m)^k for some k. Then prove matching upper and lower bounds on E u_n(0) with every constant and step checked.
   A sharp order with proof is PROVED; bounds narrower than the printed ones but not matching are PARTIAL.
3. Compute only to check (the one-site and radially symmetric variational problems; small low-dimensional analogues). No simulation
   stands in for a proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
