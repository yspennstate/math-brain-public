# E0093 work log

Task received 2026-11-13, Asia/Tbilisi: “Open problem E0093.”

## Start

- Literature first; no general resolution presumed. Read Diaconis Question 2 before fixing the model.
- All task writes confined to this directory. This specific instruction precludes global brain, checklist, and mesh writes; startup memory and compute state were read only. Local log serves as the task record.
- No agents, publication, pushes, or background services. Computation will use nice 10 and a single BLAS thread, with arrays far below 4 GB.
- Sources will be downloaded into memory and converted directly to plain text; no PDF file or page image will be saved.

## Literature pass (07:26–07:31 +04)

- Diaconis arXiv:1309.7754 PDF p. 9 read in full. Question 2 does not specify k, symmetry, laziness, a metric, or cutoff. It separately conjectures an n^3 log n mixing bound for every generating pair of A_n. Reference [4] is about symmetric groups, not arbitrary finite groups.
- Saved Hildebrand (arXiv and published text), Hermon–Olesker-Taylor (cutoff, geometry, upper triangular groups), Hough, Hermon–Huang, Eberhard–Jezernik, Breuillard–Green–Guralnick–Tao, Helfgott–Seress–Zuk, Helfgott–Seress, Breuillard–Varju, and Landau–Russell.
- Important current-date finding: Haoran Zhu, arXiv:2610.41347v2 (2 November 2026), Theorem 1.2, PDF p. 4, states cutoff for every finite group when k >= 2^14 log n and log k/log n -> 0. Applies to both symmetric and directed walks, in discrete and continuous time. This is a recent preprint, not a verified journal publication. v1 only assumed k/log n -> infinity; current v2 is stronger. Must not report the general high-degree cutoff problem as still open.
- This resolves a substantial precise growing-degree version; it does not settle all sizes in the source's unspecified question, constants near the generation threshold, or the every-pair A_n conjecture. Final classification will distinguish these scopes.
- Project Euclid returned HTML challenges for Roichman and Dou–Hildebrand. These are failed retrievals, not paper texts. Survey and recent papers give reliable theorem pointers; originals still being sought. Hildebrand's correction page redirects to login; cannot certify those corrections.
- Search for the requested Dubail/Heisenberg reference did not identify such a paper. Bastien Dubail's own CV lists different work; Heisenberg results located are Hermon–Olesker-Taylor. This attribution will be flagged instead of invented.
- Launcher already sets nice 10. Attempting os.nice(10) tried to add ten more and failed under the sandbox; scripts now inspect priority and only set it if below 10.

## Proof and computation pass (07:31–07:47 +04)

- Wrote explicit finite-size spectral concentration and TV bounds; constants checked independently: J(1/2)=0.130812035941137, 2/J(1/2)=15.2891130056256. Uniform-union measure requires a Dirichlet-form comparison, because involutions change the tuple weights.
- Proved a deterministic lower bound through any abelian quotient by a lifted second-moment argument; checked the gap obstruction separately by character pigeonholing. Fixed k=2 and k=3 therefore cannot have a uniform polylog bound even conditioned on generation.
- Analyzed every generating pair of prime dihedral groups: cycle or prism spectra, quadratic upper/lower mixing bounds, no cutoff, and a two-point limiting law for the scaled gap. These are explicit special-case derivations, not claimed as a new general discovery.
- Ran 144 accepted random generating sets across 24 groups, evaluating both measures (288 records). All four TV threshold times per record were verified by arbitrary-precision integer recurrences on all states. Included S_8 (40320 states), PSL(2,5/7/11), and Heisenberg mod 3/5/7.
- Independent audit passed: alternative forward-scatter exact recurrence, abelian character eigenvalues, complete dihedral spectra, group-law samples, changed ARPACK starts, and all spectral/quotient comparison bounds. Peak RSS 264.97 MiB, nice 10, one numerical thread; per-set computation totaled approximately 17 seconds.
- 25 of 144 generating sets have different t_mix(1/4) under the two weighting conventions. The largest certified t_mix(1/10) was 1913.
- Added Huang–Rao arXiv:2510.19942, Theorems 1.3–1.4. Their growing-degree theorem leaves an intermediate technical gap and uses the multiset convention (Remark 1.2); it must not be described as a theorem for every uniform-union model.
- Citation audit corrected Diaconis's first journal page to 1294, the geometry preprint version to v2, and the triangular paper's precise theorem page to PDF p. 13. Published and arXiv Hough theorem numberings differ, and both are distinguished in the report.
- Fixed math delimiters in the initial report write before completing the artifact.

## Completed (07:50 +04)

- REPORT.md starts with PARTIAL. It distinguishes the recent high-degree preprint resolution from the source's unspecified scope and the still-unresolved every-pair alternating-group assertion.
- Added a full diameter-to-mixing proof with explicit constants, matching the source's suggested route and showing where it loses a logarithm on cycles.
- Final proof audit corrected the coset convention: right multiplication preserves xH. Continuous-time half-laziness is transferred by an exact generator identity, avoiding an unsupported discrete de-Poissonization argument.
- Final artifact audit passed: 25 source/notes text files, 288 numerical records from 144 generating sets, four exact TV thresholds per record, syntactically valid code, consistent source hashes for all paper texts, and no PDF, image, scan, PS, or DVI files.
- All work products are local. No publication, pushes, external messages, subagents, or global memory/checklist/mesh mutations.
- Result: known uniform logarithmic-degree mixing bounds made explicit; fixed-degree universal polylog bound disproved with full deterministic proofs; exact dihedral pair analysis and small-group computational evidence saved. No full E0093 resolution claimed.
