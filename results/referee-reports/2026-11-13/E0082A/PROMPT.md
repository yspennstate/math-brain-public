Open problem E0082. Source: J. Pitman and W. Tang, a 2014-2017 paper on waiting times for patterns in random walks /
Brownian motion, with a "matching matrix" method (source id pitman_tang_patterns_2014; find it on arXiv by authors and words
"patterns", "random walks", "Brownian bridge", "first passage"), Open problem 2.3, PDF p. 13: using the matching matrix method as
in Theorem 2.1, (1) determine the exact asymptotics of E T(BR_{alpha,n}) for alpha in R as n tends to infinity, and (2) determine
the exact asymptotics of E T(FP_{alpha,n}) for alpha < 0. The source proves c n <= E T <= C n in both cases and obtains
E T(BR_{alpha,n}) of order n by a scaling limit argument. Read the source for the exact definitions (the pattern families BR =
discrete bridges and FP = first-passage paths of length n with drift/level parameter alpha, the waiting time T in an i.i.d.
+-1 sequence, the matching matrix of Theorem 2.1).

Prior internal work to reuse and cite as internal only: our run E0081 proved an n log n asymptotic for a related first-passage
pattern problem from the same source (memory e0081_pitman_tang_first_passage_pattern_n_log_n_proved_2026_11_12; its folder is
not available here, so re-derive what you need).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only). State Theorem 2.1 and Open problem 2.3 exactly. Search:
   Pitman-Tang published version, citers 2014-2026, Guibas-Odlyzko (string overlaps, correlation polynomials), Li 1980,
   Gerber-Li, Nielsen, Chen-Zame, Banjevic, waiting-time results for families of patterns. If the exact asymptotics are printed,
   give the theorem and page and stop with RESOLVED_IN_LITERATURE.
2. Set up: for a family of patterns, E T = 1 / (sum of entries of the inverse matching matrix) or the Conway/Li leading-number
   formula; identify what must be computed (sums of overlap probabilities between paths in the family), and the continuum limit
   of those sums (Brownian bridge / first-passage overlaps under scaling).
3. Prove what you can, with complete proofs: lim E T(BR_{alpha,n})/n = c_BR(alpha) with an explicit c_BR, and the same for
   FP_{alpha,n}, alpha < 0, by passing the matching-matrix sums to the limit (dominated convergence for overlap sums, a local
   limit theorem for the counts), with the constant as an explicit integral or series.
4. Compute (evidence only): exact E T for n up to the feasible size via the matching matrix (or a Markov chain on prefixes) and
   Monte Carlo for larger n, against the claimed constants.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
