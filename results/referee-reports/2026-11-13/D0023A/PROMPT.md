Open problem D0023. Source: a 1999 open-problems paper on disordered asymmetric exclusion / zero-range processes (source id
disordered_asep_open_1999; find it by searching "disordered" "zero-range" "open problems" 1999, likely by E. Saada, C. Bahadoran,
J. Krug, P. Ferrari or K. Ravishankar), Problem 2, Section 4, PDF p. 9: for the zero-range process with sitewise disorder, in the
phase-transition case the hydrodynamic theorem gives only trivial behaviour at high density rho > rho* (the profile does not
move). On a finer space scale one expects inhomogeneities to develop, specifically that the excess particles concentrate on
exceptionally slow sites. Give a rigorous description of this concentration. Read the source for the exact wording.

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only). Search: Bahadoran-Mountford-Ravishankar-Saada
   ("Supercritical behavior of asymmetric zero-range process with sitewise disorder", arXiv:1411.4305; "Supercriticality
   conditions for asymmetric zero-range process with sitewise disorder"; "Hydrodynamics in a condensation regime: the disordered
   asymmetric zero-range process", Ann. Probab. 2020; later papers), Andjel-Ferrari-Guiol-Landim (convergence to the maximal
   invariant measure), Krug-Ferrari (phase transitions in driven diffusive systems with random rates), Evans, Godreche-Luck
   (condensation in random-rate ZRP), Grosskinsky, Jatuviriyapornchai, Mountford, and 2015-2026 work. Decide exactly what is
   proved about where the excess mass goes (slowest sites in growing windows, time scales, extremal statistics of the rates).
   If a printed theorem gives the rigorous description asked, give it and the page and stop with RESOLVED_IN_LITERATURE.
2. Understand the gap: the mesoscopic picture (for i.i.d. rates near the infimum c with P(rate near c) ~ eps^kappa, which
   sites hold the excess at time t, how many particles, on what space scale) and what BMRS leave open.
3. Prove what you can, with complete proofs: a concentration statement in a tractable setting (totally asymmetric, constant
   jump rate g(n)=1 i.e. a tandem of M/M/1 queues with random service rates; or a finite ring / interval with i.i.d. rates),
   e.g. that the mass outside the k slowest sites in a window is O(window) while the excess sits on sites whose rate is within a
   vanishing distance of the infimum, with explicit scaling.
4. Compute (evidence only): simulate the disordered TAZRP (queue tandem) from supercritical initial data for several rate laws,
   tracking where the excess mass sits versus the order statistics of the rates.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
