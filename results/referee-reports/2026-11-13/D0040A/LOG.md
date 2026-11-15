# D0040 work log

Task received: 2026-11-13 09:52 +04 (Asia/Tbilisi): “Open problem D0040.”
Scope: literature first, then precise gaps, rigorous results, and small simulations if needed. No publication or pushes. One agent; numerical programs nice 10, one BLAS thread, small memory footprint.

## 2026-11-13 — orientation and source

Read the startup memory index and mesh protocol; checked compute state (ok, owner_away_open). The task-specific instruction to work only in this directory takes priority over writing to the global mesh, checklist, or brain. Progress and durable findings are recorded locally instead. No subagents used.

Located Virág, arXiv:1804.06953 (2014 article uploaded 2018). Section 4, Theorem 4.1, PDF p.5, and Question 2, PDF p.6. The source explicitly reverses the usual finite-model indexing. Need distinguish infinite Jacobi leading-minor nesting from the full Dixon–Anderson Gibbs corners process; their joint laws need not coincide.

Checklist: literature search IN PROGRESS; source texts IN PROGRESS; precise interpretation IN PROGRESS; proofs PENDING; simulations PENDING; final audit PENDING.

## 2026-11-13 — literature findings

Saved plain-text, page-marked copies of Virág; Dumitriu–Edelman; Killip–Nenciu; Edelman–Sutton; Forrester–Rains; Neretin; Borodin–Gorin; Gorin–Shkolnikov; Gorin–Marcus; Assiotis; Sun; Budway–Shkolnikov. Conversion uses pdftotext with PDF bytes only in memory. Initial pypdf extraction of Dumitriu–Edelman had pathological whitespace; replaced it by the clean arXiv text via pdftotext. No PDF file was saved.

Virág Q2 asks about one random orthogonality measure, hence nested Jacobi matrices, not a prescribed full corners law. Borodin–Gorin §1.5, PDF p.9, explicitly gives the dimension obstruction to obtaining the full corners process from a tridiagonal model. Killip–Nenciu Theorems 1 and 2 are finite-size matrix models, not by themselves consistency statements. Sun's matrix statements have beta=1,2 restrictions, not arbitrary beta.

Dumitriu–Edelman Theorem 3.4, PDF p.14, yields the Laguerre candidate after reversal and transpose. Need retain fixed hard-edge exponent: at size n the original theorem parameter is A_n=beta(n+a)/2, not a constant A. Jacobi reversed models contain a changing terminal boundary term; merely reversing independent beta variables does not establish nesting. Circular unitary principal minors have an elementary obstruction.

Recent search includes Budway–Shkolnikov (2024), Sun's 2025 publication (using the 2016 preprint for exact theorem/page citations), Kawamoto–Shibukawa (2026), Nakano–Trinh–Trinh (2026), and Petrov–Xu (2026). ALEA PDF request failed (HTTP 400/timeout); will use an author/arXiv alternative if available. No theorem/page claim will rely on an abstract alone.

## 2026-11-13 — interpretation fixed; proceeding to proofs

Literature does not justify RESOLVED_IN_LITERATURE for the whole requested structured-matrix classification. Stop condition has not been met. Proceeding with PARTIAL, distinguishing established literature from elementary deductions here.

Correction to the earlier page note: Borodin–Gorin §1.5's singularity discussion is PDF p.8 in the downloaded 59-page version, not p.9. Page markers now checked directly.

Planned rigorous results: (i) nested fixed-hard-edge Laguerre via reversed/transposed bidiagonal B; (ii) generalized Dixon–Anderson law derived from Dirichlet residues, explaining why ordinary Laguerre/Jacobi corners shift parameters; (iii) no full absolutely continuous corners law from a single real tridiagonal matrix; (iv) only quadratic full-line potentials have independent canonical Jacobi entries, with the spectral-weight assumption explicit; (v) beta=2 fixed-weight DA coherence forces Gaussian; (vi) obstruction to unitary CBE principal-minor nesting; (vii) explicit failure of reversed Killip–Nenciu Jacobi candidate. These do not classify arbitrary dependent Jacobi models.

The process already has niceness 10. An attempted extra `nice -n 10` reported a sandbox setpriority denial; subsequent getpriority confirmed niceness 10. Numerical programs inherit that priority and set one thread for BLAS/OpenMP/vecLib. One numerical process, no workers.

## 2026-11-13 — Monte Carlo completed (data saved 09:59 +04)

Ran code/check_models.py, seed 400020261113, 30,000 independent matrices per parameter case; beta=0.5,1,2,4, hard-edge parameter a=-0.25,1.5, sizes 1 through 4. Target checks: exact gamma trace law at every n, exact beta law for the n=2 squared relative gap, joint n=2 probability-integral-transform bins, and ordered eigenvalue marginals at n=3,4 against independent standard decreasing-index DE draws. Included direct n=1 Jacobi controls and reversed n=4 KN negative controls.

108 positive tests; no Holm-adjusted rejection at 0.05. Smallest raw p=0.0073086871. Maximum absolute log-determinant mean z-score=1.84851. Max matrix nesting discrepancy 7.11e-15, max interlacing roundoff violation 3.99e-15. Reversed Jacobi scalar marginals rejected for all four betas, agreeing with an independently derived wrong-mean formula. Data and raw samples saved in data/. Runtime 1.63 seconds; peak RSS 203,128,832 bytes; process niceness 10; one numerical thread.

Additional literature: Dumitriu–Forrester Theorem 1.1, PDF pp.2–3, gives another nested model after reversal: the antisymmetric Gaussian beta ensemble (multiply by i for Hermitian interlacing). Forrester–Rains §4.2's Jacobi recurrence has an x(x−1) coefficient and parameters depending on terminal size; it is not automatically a single ordinary Jacobi matrix. Assiotis–Najnudel §8 provides coherent Hua–Pickrell and inverse-Wishart arrays at all beta, with size-dependent weights; these are distinct from fixed-bandwidth nesting. 2026 high-temperature spectral-measure results vary beta with N and do not establish the fixed-beta finite-prefix property.

## 2026-11-13 10:10:07 +0400 — final audit and delivery

Completed REPORT.md with first line PARTIAL, 18 converted primary-source texts plus source inventory and search record, reproducible simulation and audit programs, raw samples and numerical summaries. All requested stages were attempted in order. The report proves the Laguerre construction and explicit limited obstructions while keeping the unresolved general questions visible.

Independent audit passed: 100 reversal/transpose and arrow-spectrum checks, residue normalization, four exact rational Jacobi means, all 108 Holm calculations, code/data hash agreement, 36 raw sample arrays, all source page-marker sequences, Python parsing, local links, and absence of PDFs or paper images. Corrected an initially overbroad circular no-go statement before delivery: unitarity forces diagonalization, which excludes irreducible CMV/Hessenberg models but is not by itself a theorem against every diagonal phase coupling.

Checklist: literature DONE with bounded negative-search conclusion; source conversion DONE; interpretation DONE; proofs DONE for stated partial results; Monte Carlo DONE; final audit DONE. No publication or pushes. No subagents, external state updates, or work outside the directory.

Task: “Open problem D0040.” — 2026-11-13 09:52 +04.
