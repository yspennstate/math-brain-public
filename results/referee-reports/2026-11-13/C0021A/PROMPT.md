Open problem C0021. Source: C. Garban and J. Steif, "Noise Sensitivity of Boolean Functions and Percolation" (Cambridge,
2014; draft on the authors' pages / arXiv lecture notes), Chapter VIII, Exercise VIII.5 and the note after it, p. 97: the
revealment of the iterated 3-majority function on n = 3^k bits decays like n^{-sigma}; determine sigma. Revealment
delta(f) = min over randomized decision-tree algorithms A computing f of max over bits i of P(A queries bit i), with uniform
random input. Read the source for the exact definition and what is already proved (the known upper and lower bounds on
the revealment of iterated majority, and how the Schramm-Steif theorem uses it).

Do this, in order, saving as you go:
1. Literature first. Get the Garban-Steif text into sources/ and read Chapter VIII around Exercise VIII.5. Search for later
   work on revealment / randomized query complexity of recursive (iterated) 3-majority: Jayram-Kumar-Sivakumar 2003,
   Leonardos 2013, Magniez-Nayak-Santha-Sherman-Tardos-Xiao 2016 (their bounds are on expected queries, (1.5..2.65)^k -
   relate them to revealment), Peres-Schramm-Sheffield-Wilson "random-turn hex", O'Donnell-Saks-Schramm-Servedio (OSSS:
   revealment times total influence >= Var), and any 2014-2026 paper determining or bounding sigma. If sigma is determined in
   print, give the exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Bounds. Derive the best rigorous lower bound on sigma-type decay you can (OSSS gives delta >= Var/I; compute the total
   influence of iterated 3-majority exactly: I_k = (3/2)^k) and the best upper bound from explicit recursive randomized
   algorithms (e.g. the "evaluate two random children, the third only if they disagree" recursion and its improved
   variants); write each as n^{-sigma} with sigma explicit (log base 3).
3. Compute. For small k (k = 1,2,3, and 4 if feasible) compute the exact optimal revealment, using the recursive structure
   and symmetry: formulate it as a linear program over randomized algorithms or as a minimax over directional
   (depth-first) algorithms, and prove (or test) whether directional algorithms are optimal for revealment. Fit the
   exponent and compare with the bounds from step 2.
4. If you can, prove the exact value of sigma (matching upper and lower bounds), or state precisely what remains.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE
(PROVED means sigma determined with proof). Then the statement, the proof or bounds, what was checked and how, and the
literature result. Keep LOG.md as you go. Code in code/, data in data/. Do not save page images of papers anywhere in this
directory (text extracts in sources/ only). Work only in this directory. At most 4 threads, under 4 GB, nice 10. No
publication anywhere, no pushes.
