Open problem I0005. Source: A. Bou-Rabee, C. Panagiotis, "Sharpness and critical scaling of parking", arXiv:2609.02820v1 (verify
title, authors, date, version from the listing; the companion is arXiv:2609.02829v1). Its Theorem 1.5 answers the critical-parking
analogue of Damron-Gravner-Junge-Lyu-Sivakoff [Parking on transitive unimodular graphs, AAP 2019, Open Question 3]: "P(the origin
is closer to a free spot than to a driving car at time t) -> 0?", affirmatively for d <= 3 and by counterexamples for d >= 5. The
case d = 4 is left open; it sits at the boundary where the odometer growth n^{(4-d)/4} and log n coincide (their Theorem 1.2).
State the exact model (cars and spots on Z^d, initial law, criticality, synchronous or continuous time, what "closer" means, which
distance), and the exact statements and proofs for d <= 3 and d >= 5, with page numbers.

The question: decide d = 4.
Do this, in order, saving as you go:
1. Literature first. Get both papers into sources/ as plain text; read Theorem 1.5's two proofs line by line and say exactly where
   d <= 3 and d >= 5 are used (the odometer scale versus the distance to the nearest spot; a log-correction at d = 4). Read DGJLS
   Open Question 3 and its context. Search 2026 work; if d = 4 is settled in print, report RESOLVED_IN_LITERATURE.
2. Attack it. Work out the heuristic at d = 4: the companion's odometer at d = 4 grows like log n (check exactly, with constants
   if possible), while the distance from the origin to the nearest free spot and to the nearest driving car scale how? Decide which
   wins, possibly by a power of log log, and then prove the answer, or prove it for a natural variant (e.g. the divisible-sandpile
   comparison model) and say exactly what transfers. A complete proof for the source's model is PROVED (or COUNTEREXAMPLE if the
   probability does not tend to 0); a proof for a variant or one direction is PARTIAL.
3. Compute only to check (small runs on Z^4 boxes, or low-dimensional analogues). No simulation stands in for a proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
