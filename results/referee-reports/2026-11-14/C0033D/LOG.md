# C0033D log

All times use Asia/Tbilisi (UTC+4). Numerical claims below distinguish ordinary
floating point, high precision, and outward-rounded interval certificates.

- 2026-11-14 01:59: Task received: “Open problem C0033, fourth attempt: inequality
  (21) on connected strict three-point kernels.” Read C0033A, B and C reports in
  full, including C Sections 4 and 6. No subagents or model workers started.
- 2026-11-14 02:02: Brain recall and the relevant identity and C0033 memory cards
  read. Mesh hello, digest, claim and assert fail with “attempt to write a
  readonly database”; checklist fails with PermissionError. Read-only inspection
  of mesh claims finds no C0033 or workspace claim. The supplied local
  claim_files/README.txt identifies this run. Shared memory is not modified.
- Copied dpp.py and dpp.cpp verbatim from C0033C (the inherited C0033B/A code),
  and built libdpp.dylib. NumPy, SciPy, SymPy and mpmath available. All numerical
  processes use nice >=10 and one numerical thread; no worker pools.
- Computation state at startup: warn/cpu_saturated, owner_away_open. Use a single
  low-priority numerical process; read compute state again before larger runs.
- 02:05–02:07: Implemented the seven-parameter chart and polynomial gradients.
  Independent determinant/gradient and gauge checks passed. The inherited process
  priority is nice 20 (an attempted additional nice increment is disallowed by
  the sandbox); all computations retain nice 20.
- Expanded search: 132,000 random attempts in eleven families, three differential
  evolution runs, and 36 seven-variable Nelder–Mead runs; 392,301 total proposed
  evaluations. Saved all family and restart extrema. Search runtime 38.47 s,
  peak RSS 78 MiB. Best binary theta=0.9690821913 is ill conditioned.
- 02:13: At 180 decimal interval digits all 51 rational roundings of saved extrema
  certify positive margins and positive definite negative full Hessians. The
  best binary candidate actually has margin 0.0314852127373 after exact rational
  rounding, not 0.0309178087450. The original and seven-atom interval formulas
  overlap. mpmath.iv's complex conjugate method raises a library exception;
  explicit real/imaginary conjugation fixes it.
- Derived an exact 7x7 probability-coordinate criterion by Woodbury, retaining
  all nine ambient directions. Proved the full ambient Hessian sign on the
  equal-modulus imaginary cyclic family. Its boundary margin is asymptotic to
  4/log(k), so a uniform positive global gap is impossible.
- 02:16–02:20: Proved leading scalar expansions at generic diagonal kernels and
  along uniform approaches to zero and identity. Obtained a separate sufficient
  inequality using the cardinality score and Cauchy–Schwarz.
- The interval branch-and-bound completely covers a specified 7D box in seven
  nodes/four leaves. A wider box and the domain with spectral and edge margins
  1/10 have unresolved checkpoint cells. The initial wide run used expanded atom
  polynomials; keeping the diagonal shifts factored improves coverage. Historical
  data/bnb_local.json is retained; current runs use bnb_local_improved.json.
- 02:22: Exact rational boundary probes with phase pi, and their complementary
  phase-zero kernels, certify all nine Hessian directions through eigenvalue
  scales 10^-24. Closed-form cyclic certificates extend to k=10^1000, with margin
  about 0.001734165374. No violation found. The generic mixed spectral/graph
  boundary is still not controlled uniformly.
- 02:26: The full-Hessian fallback covering run stops at its stated 20,000-node
  cap: 1,408 certified leaves, 8,578 discarded leaves and 29 pending cells.
  Accepted root volume is about 3.375078e-13; this is not a near-complete cover.
  The fallback did not certify additional cells beyond the cardinality bound.
- 02:31: Removed a search-only upper-score guard of 1.1, replacing it by the
  rigorous scalar range upper bound 3 (with a numerical allowance of 0.001).
  A full deterministic search rerun gives exactly the same witnesses and
  evaluation counts; no candidate was lost to that guard in the recorded run.
- 02:33: Sequential reproduction passed. Recomputed all 51 rational search-point
  certificates, eight structured boundary certificates, eight cyclic closed-form
  interval certificates, symbolic determinant identity, 2,000 independent
  numerical checks, and the complete four-leaf local cover.
- Independent exact partition audit reconstructs the prescribed bisection tree
  from every saved leaf, verifies prefix-free complete partitions and exact
  rational volumes, and re-evaluates every accepted and discarded leaf in all
  four current covering runs. All checks pass. Largest measured peak RSS among
  final runs: 87.91 MiB. One numerical thread, no pool, nice 20 throughout.
- Final result: PARTIAL. REPORT.md contains the seven-parameter/7x7 reduction,
  a strict full-Hessian theorem on the imaginary cyclic family, the two leading
  boundary expansions, the simple spectral-face expansion, the cardinality
  sufficient bound, rigorous point/box certificates, all search tables, and the
  unresolved boundary and covering requirements. All code and data remain here.
  Durable mathematical results are in the report; shared brain/checklist writes
  remain unavailable in this sandbox.
