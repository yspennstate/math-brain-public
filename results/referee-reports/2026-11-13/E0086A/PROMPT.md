Open problem E0086. Source: Y. Hu and Z. Shi, "Topics and problems on favorite sites of random walks", arXiv:1606.03787, Open
problem 2, PDF p. 6. For simple random walk on Z^2 run up to tau_n (read the source for the exact stopping time: exit of the disc
of radius n, or time n), and a region D_n contained in the complement of the disc D(0, a_n) with a_n -> infinity, what is the
almost sure asymptotic of M_{D_n}(n), the maximal local time over D_n (or the radius of the largest disc in D_n completely covered)?
The source is especially interested in D_n = D(0, 2a_n) minus D(0, a_n) with a_n = n^alpha, 0 < alpha < 1/2, noting that the
largest disc completely covered before tau_n has radius n^{1/2+o(1)}, and conjectures a corresponding statement for
a_n >= n^{1/2+eps}. (Read the source for the exact quantity, normalisation and conjecture: favourite-point local time, the
Dembo-Peres-Rosen-Zeitouni thick-point and cover results, and which statement is conjectured.)

Do this, in order, saving as you go:
1. Literature first. Download arXiv:1606.03787 into sources/ (plain text only) and read Section 1-2 and Open problem 2 exactly.
   Search for the tools and any resolution: Dembo-Peres-Rosen-Zeitouni "Thick points for planar Brownian motion and the
   Erdos-Taylor conjecture on random walk" (Acta Math 2001) and "Cover times for Brownian motion and random walks in two
   dimensions" (Ann. Math. 2004), "Late points for random walks in two dimensions"; Rosen "A random walk proof of the Erdos-Taylor
   conjecture"; Jego "Thick points of random walk and the Gaussian free field" and "Planar Brownian motion and Gaussian
   multiplicative chaos"; Abe "Second order term of cover time for planar simple random walk"; Belius-Kistler; Belius-Rosen-
   Zeitouni "Tightness for the cover time of the two dimensional sphere"; Okada "Frequently visited sites of the inner boundary
   of simple random walk range" and "Topics and problems on favorite sites" follow-ups; Bass-Rosen; Comets-Popov-Vachkovskaia
   two-dimensional random interlacements and conditioned walk; anything 2016-2026 citing 1606.03787. If it is answered in print,
   give the exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Make it precise. Write the precise statements in the regimes a_n = n^alpha (alpha < 1/2, alpha = 1/2, alpha > 1/2) and a
   heuristic for the answer from the Dembo-Peres-Rosen-Zeitouni multiscale (excursion-count) picture: the number of excursions
   between circles around a point at distance ~a_n, the Green's function of the walk killed at tau_n at such points, and the
   resulting first-order asymptotic of max local time and of the largest covered disc in the annulus.
3. Prove what you can, with complete proofs: the first-order almost sure (or in-probability) asymptotic of M_{D_n}(n) in the
   annulus for some range of alpha; or matching upper and lower bounds up to constants; or the in-probability version if the a.s.
   one is out of reach. Use the excursion-counting second-moment method of DPRZ and the Green's function estimates near the
   boundary/at distance a_n.
4. Compute (as evidence only). Simulate planar SRW up to the exit of D(0,n) for n up to what fits in 4 GB, record max local time
   and the largest fully covered disc inside annuli D(0,2a)\D(0,a) for a = n^alpha with a few alpha, and compare with the
   heuristic constants.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
