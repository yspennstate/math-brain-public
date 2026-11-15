Open problem E0030. Source: S. Chatterjee, "A general method for lower bounds on fluctuations of random variables" (Ann. Probab.
47 (2019); arXiv:1706.04290; check the exact reference), list of open problems, item (2), PDF p. 27: for the length T_n of the
shortest travelling salesman tour through n i.i.d. uniform points in [0,1]^2 (or the d-dimensional analogue as stated there),
Var(T_n) is known to be bounded above and below by positive constants (Steele; the lower bound in that paper); does Var(T_n)
converge to a limit as n -> infinity? State the exact question and setting from the source (Poisson or binomial points, unit cube
or torus, which dimension).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ as plain text and state the problem exactly with page numbers. Search 2017-2026
   work: Cao ("Central limit theorems for the travelling salesman problem" or similar), Chatterjee-Sen, Kesten-Lee, Penrose-Yukich
   stabilisation, Steele's book, Yukich, Hessler-Wastlund, Gold, Wade, Barbosa, "variance asymptotics" "travelling salesman",
   "TSP" "central limit theorem", "Euclidean TSP variance". If a printed result proves convergence of the variance (or of the
   Poissonised variance n Var / ... in the stated normalisation), give the theorem and page, say whether it covers the binomial
   and the Poisson model and which dimensions, and stop with RESOLVED_IN_LITERATURE (or PARTIAL if it covers only part).
2. Otherwise, explain precisely why stabilisation methods (Penrose-Yukich) fail for the TSP (no known radius of stabilisation),
   and attempt a proof or a precise partial result: for example convergence of the variance of a boundary-functional or of a
   torus version, convergence along a subsequence, or a statement conditional on a stated stabilisation property. Every step
   checked.
3. Compute (evidence only): near-optimal tours (Concorde-free: use LKH-style 2-opt/Or-opt heuristics you write yourself, or an
   exact solver if one is available locally and quick to build) for n up to 10^4 in the torus, many samples, estimate Var(T_n)
   and its trend. State the heuristic error and do not overclaim.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
