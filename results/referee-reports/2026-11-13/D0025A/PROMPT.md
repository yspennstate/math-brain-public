Open problem D0025. Source: T. Seppalainen, "Recent results and open problems on the hydrodynamics of disordered asymmetric
exclusion and zero-range processes" (1999; arXiv:math/9906194), Problem 4, Section 4, PDF p. 9: for the disordered totally
asymmetric exclusion process (jump rates attached to particles or to sites, with at most K particles per site), is there a phase
transition similar to the one for the disordered zero-range process? Does the flux function f_K(rho) have a flat segment on an
interval around rho = K/2? Read the source for the exact wording (which disorder, which K, what is meant by phase transition).

Prior internal work (internal only, never cite publicly): our run D0023 on Problem 2 of the same paper (stationary condensation on
finite rings for the constant-rate disordered zero-range process); its folder is not available here.

Do this, in order, saving as you go:
1. Literature first. Get arXiv:math/9906194 into sources/ (plain text only) and state Problem 4 exactly. Search: Krug-Ferrari
   1996 and Evans 1996 (particle disorder TASEP = zero-range mapping, phase transition proved), Seppalainen-Krug ("Hydrodynamics
   and platoon formation for a totally asymmetric exclusion model with particlewise disorder", J. Stat. Phys. 1999), Bahadoran
   ("Blockage hydrodynamics of one-dimensional driven conservative systems"), Bahadoran-Bodineau ("Quantitative estimates for the
   flux of TASEP with dilute site disorder", EJP 2018), Basu-Sidoravicius-Sly (slow bond problem, 2014: flat segment for a single
   slow bond), Janowsky-Lebowitz, Tripathy-Barma (site disorder, flat segment conjecture, PRL 1997), Krug ("Phase separation in
   disordered exclusion models", Braz. J. Phys. 2000), Harris-Stinchcombe, Calder-Mannion, Seppalainen ("Existence of
   hydrodynamics for the totally asymmetric simple K-exclusion process", Ann. Probab. 1999), Bahadoran-Mountford-Ravishankar-Saada,
   Emrah-Janjigian-Seppalainen, and 2014-2026 work on "site disorder TASEP flat flux". Decide separately for particle disorder
   (K = 1 and general K) and site disorder: is a phase transition / flat segment proved, for which disorder laws (dilute, i.i.d.
   bounded away from zero, with a gap at the lowest rate), and for which K. If printed theorems answer Problem 4 in all its
   cases, give them with pages and stop with RESOLVED_IN_LITERATURE; if only some cases, say which remain.
2. Understand: the particle-disorder case maps to the zero-range process with site disorder (condensation behind slow
   particles, platoons); the site-disorder case is the hard one (each slow site acts like a slow bond; flat segment means the
   current is pinned at the maximal current of the slowest stretch). Explain the heuristics (Tripathy-Barma, Krug) and what
   Bahadoran-Bodineau actually prove (dilute disorder? quantitative bounds?).
3. Prove what you can, with complete proofs: for example a flat segment for site disorder when the rate law has an atom or a
   positive-probability interval of minimal rates, by comparison with long slow stretches (existence of arbitrarily long runs of
   slow sites in an i.i.d. environment) and the K-exclusion hydrodynamics; or the particle-disorder K-exclusion case via a
   zero-range mapping.
4. Compute (evidence only): simulate site-disordered TASEP on rings (K = 1, 2), n up to 10^5, and measure the current as a function
   of density, looking for a flat segment around K/2.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
