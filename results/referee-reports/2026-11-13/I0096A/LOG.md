# I0096 work log

Task received: 2026-11-13, approximately 18:56 Asia/Tbilisi (14:56 UTC).
User task: "Open problem I0096"; literature first, then a deterministic attack and numerics.

## 2026-11-13 14:57 UTC — setup and literature triage

- Working only in this directory, as requested; no subagents, publication, pushes, or changes to shared brain/mesh/checklist state. The directory-only instruction overrides the general shared-state bookkeeping instructions. Read relevant brain recall as background, treating it as unverified prior work.
- Compute governor reports owner away, CPU saturated, memory available. Computations will use nice 10 and one BLAS thread; no worker pool. Memory budget below 4 GB.
- Verified arXiv abstract pages for 2603.29571, 1308.4718, 2607.06249, 2609.28198, 2608.07410. All correspond to the requested works.
- Search found the original ACHA article, its author-hosted published version, the 2025 Phasebook survey, and 2025 optimal planar frames work. No resolution established yet.
- The published Balan–Wang section 5 already proves the elementary inverse-square-root bound and mentions a stronger unpublished polynomial bound. Do not count rediscovery as progress.
- Source retrieval will convert PDF responses directly in memory to plain text; no PDF or image file will be written.

## 2026-11-13 — citation chase

- Saved complete API responses: OpenAlex 75 citing works; Semantic Scholar 90 citing records. Index coverage differs. Semantic Scholar metadata endpoint returned HTTP 429; citations endpoint succeeded. No claim that either index covers every paper.
- Important additional primary works: Liu–Wang (2016), DOI 10.1142/S1793557116500753; Liu (2024), OaM 18, 273–293; Xu (2025), arXiv:2508.10452; Freeman–Haider (2025), arXiv:2502.09898; Xu–Xu–Zhang (2025/2026), arXiv:2510.04099; Wen–Häggblom–Yang (2026-11-04), arXiv:2611.06736.
- The 2016 Liu–Wang article proves the inverse-three-halves estimate for (n+2)-by-n matrices (Lemma 2.4 in the author manuscript). Thus even improving the elementary inverse-square-root bound to this power is old.
- Original arXiv Balan–Wang has a sign typo in Conjecture 5.1 (beta^{-n}); the published article p. 484 and Randomstrasse state beta^n. Its reference to k=1 in the stronger estimate conflicts with the simplex example; use the actual Liu–Wang lemma for the corrected n+2 case.
- Process priority was already nice 20. An attempted `nice -n 10` emitted a sandbox priority error; subsequent commands inherit nice 20, which yields more than the requested nice 10. Numerical code will verify priority and enforce one BLAS thread.

## Literature stage complete; start deterministic attack

- Saved `LITERATURE.md` before mathematical experiments. No universal resolution found in the citation indexes, exact-conjecture searches, or targeted 2025–2026 searches. Some source pagination still needs final audit.
- Retrieved the five requested preprints and the published Balan–Wang text, plus relevant deterministic and Lipschitz papers, as text only.
- Will now check the proposed volume weighting, projection induction, and Plücker routes, and enumerate numerical candidates through M=12. Old polynomial estimates will be explicitly credited.

## Deterministic and numerical findings

- Derived the exact proposed weighted mean: `E dist^2=1/tr((A^T A)^-1)` at N=2M-1. It stays polynomial even on unit-norm tight frames.
- Projection induction preserves full spark but gives no uniform norm contraction. Local real Plücker relations force a constant separation; no valid exponential iteration found.
- Identified an equivalent exponential circuit-imbalance extremal question, with rigorous two-sided inequalities after whitening. Checked 2025 excluded-line-minor and 2026 exponential-imbalance papers; neither settles this question.
- Complete candidate enumeration reached M=12 (1,352,078 square subsets for each M=12 candidate). Initial families: harmonic, equispaced Vandermonde, three row-normalized Gaussian and three scaled-Haar samples, two orthonormal bases, and simplex plus rows. SLSQP optimization through M=8; further refinement uses stronger Paley candidates.
- Truncated Paley conference frames strongly improve the initial best results at M=7 and M=9. The q=9 conference candidate is numerically singular and is excluded as a full-spark candidate. Added projected Paley trials, with complete subset enumeration for every trial.
- Some NumPy/Accelerate matrix multiplies emitted overflow/division warnings on bounded inputs, despite finite results. Changed construction checks to exact integer matrix multiplication and will independently audit witnesses. Do not interpret warnings as a proof of either failure or accuracy.
- Enumeration timing in the initial run was captured before the expensive call. These timing fields will be marked unusable; numerical values and subset counts are unaffected. Fixed instrumentation for later runs.

## Final audit and deliverables

- `REPORT.md` starts with `NO_PROGRESS`. No new universal or conditional exponential bound, new polynomial bound, or proved counterexample family was obtained. Known results are credited instead of being classified as progress.
- Saved 57 source text/access-note files, about 3.35 MB; expanded the citation audit to 94 distinct normalized titles from the two indexes. Retrieved available arXiv copies of indexed phase-retrieval papers and screened the relevant sections. Non-arXiv access gaps and the inaccessible Liu–Wang publisher copy are explicit limitations.
- Numerical records: 160 candidates/refinements, 23,777,666 final-candidate subset evaluations. This excludes optimizer-internal evaluations and projection trials that did not improve the incumbent. Optimization reached M=9; complete candidate enumeration reached M=12.
- Reenumerated every best candidate for M=2–12 by QR followed by SVD. Maximum disagreement with direct SVD: 1.1275702593849246e-16. Identity checks through M=7 passed; maximum relative Cauchy–Binet error 1.5543122344752192e-15.
- Full independent numerical audit peak RSS: 158,810,112 bytes. Process priority nice 20, one configured BLAS thread, batches of 2048, no worker pools. At most two numerical processes overlapped.
- Repaired an incorrectly labeled source filename for arXiv:2212.13681: the actual authors are Alharbi, Freeman, Ghoreishi, Lois, and Sebastian. The source itself always contained the correct authors. Rename provenance is in the source manifest.
- Initial timing records were retained in `data/numerics_original_timing.jsonl`; their corresponding canonical timing fields are null with an explanatory note. The independent audit timings are valid.
- Removed extraction control characters from source text; retained page separators and source URLs, and saved source checksums. No PDFs or paper images were written.
- Task: “Open problem I0096” — 13 November 2026, work begun 18:56 Asia/Tbilisi.
