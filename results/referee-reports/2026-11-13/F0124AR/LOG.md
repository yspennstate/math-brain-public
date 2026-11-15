# Independent F0124 referee log

Started 13 November 2026, approximately 07:45 Asia/Tbilisi (03:45 UTC).
Task: independent audit of the bilateral reduced-RWRS all-good claim for p>27/28.

- Read the submitted REPORT.md and LOG.md, without executing or reusing submitted code.
- Brain recall and navigation read. Startup node lookup failed (missing memory file). Mesh hello/digest failed with a read-only database; directory-only authorization prevents global checklist/memory updates. No live claim was bypassed.
- Shell inherited nice 10; computations will be single-process and bounded, with no subagents, publication, or pushes.
- Compute state warned of existing CPU saturation; use small exact computations, no worker pool.
- Initial source check: 2011 Blachere–den Hollander–Steif explicitly studies future-only conditioning; survey concerns bilateral conditioning. Proof audit underway.

## Source and proof audit

- Downloaded survey, 2005 preprint, 2011 sequel, 2020 Oberwolfach report, regular-g/non-Gibbs counterexample, generalized T,T^-1 mixing paper, perfect-simulation paper, and current den Hollander bibliography. PDF bytes passed in memory to text extraction; no PDF or image files retained.
- The 2005 preprint has custom font encoding. Added independent glyph-name decoding for printable characters, with explicit unknown-glyph markers; its Section 1.2 expressly reserves colours-only bilateral conditioning for a future paper. Its Theorems 1.2 and 1.3 have the scope claimed in the submission.
- Direct download of Verbitskiy's 2011 factor paper returned 403. Primary repository text is available in the web tool; read Theorem 1.1 there. It assumes a positive continuous g-function with summable variation and does not directly classify bilateral RWRS.
- Checked REPORT.md equations (1)–(11), first/last/whole block conditions, missing observation, arbitrary partial conditioning in domination, independence of truncated interval vacancies, and the swap involution. No load-bearing error found.
- Chronological reanchoring at time -m preserves i.i.d. p-right increments. It avoids incorrectly assigning p-right drift to the negative arm when traversed backward. Neither conditional independence of the two arms nor that incorrect drift convention is used.

## Independent exact computation

- Wrote code/independent_check.py from scratch; no submitted code was imported, run, or copied.
- 32,767 paths through length 14, 58,474 blocks: cuts, boundary restrictions, L<=3*left_steps, and duplicate-observation inequality passed, including every possible hole location.
- 576 exact cross-checks: all complete seven-time records at p=0.97, 0.9, 0.5 against direct path enumeration, plus every punctured seven-time record against an independent interval partition sum. Sixteen compatible marked pairs checked the central-swap involution and product-weight preservation.
- Computed 96 exact rational finite-window conditionals for p=0.97 and 0.9, n=2,4,6, m=n,n+4,n+12,n+24; monochrome, white tails, WWBB tails and asymmetric tails. Peak 33,156 states; 44,990,464 bytes peak RSS; 4.25 seconds; one process, nice 10.
- The sandbox rejects setrlimit even for memory-limit reductions. First two launches stopped before computation; final code enforces conservative state and RSS caps during transfer steps. Resource use stayed far below 4 GB.
- At p=0.97, rho=0.941682345 and log10(c)=-240.501966; the asymptotic continuity bound is numerically uninformative at our finite horizons. At p=0.9, rho=1.442249570, so the displayed theorem bound cannot be used. No numerical claim of sharpness or badness follows.

## Literature search

- Searched exact titles and combinations of reduced RWRS, bad/good configurations, bilateral/two-sided, continuity, quasilocality, g-measures, and T,T^-1/Kesten–Spitzer.
- Retrieved an OpenAlex citation list for the survey DOI: 34 indexed citing works dated 2006–2026. Screened titles and read relevant primary texts, including Gallo–Garcia (2013), Dolgopyat et al. (2022), and Pene–Saussol (online 2024, journal 2025). Citation indexing is incomplete, so this is not an exhaustive absence proof.
- Steif's 2020 Question B still asks for the phase diagram but summarizes the 2011 one-sided paper without restating its conditioning convention. It is not independent evidence for a proved bilateral threshold.

## Report and final audit

- Verdict drafted as ACCEPT for the stated partial theorem; no mathematical error or gap found. Not an acceptance of the full conjecture or a priority claim.
- Added 128 exact direct two-arm checks anchored at S_0=0 (negative-time positions use minus partial sums of p-right increments), plus colour flip and spatial reflection checks. Added 200 exact Chernoff checks through length 100 at the tested drift and the endpoint t=4/27. All passed.
- Final computation repeated only because these new checks changed the script: 4.12 seconds, peak RSS 53,706,752 bytes, 33,156 states, one process, nice 10.
- Recomputed the 2011 exact bound as 2985984/2989109=0.9989545379576322. Its printed approximation 0.997 is a source typo; the submission's correction is right.
- Read the three indexed forward citations of the 2011 paper at the relevant scope level. Steif–Tykesson (2019), Remark 7.17, refers to that theorem as Gibbsianness; it adds no bilateral theorem. The tree-transform paper cites it among non-Gibbs examples, not as an RWRS advance; the additive-functional paper studies Kesten–Spitzer limit laws.
- Source hashes verified; sources/ contains only .txt files. No PDFs or images anywhere in the directory. Claim files were not edited. No publication or pushes.
- Final report formatting, math delimiters, all 96 exact CSV gaps, and PDF magic-byte/extension checks passed. Citation screening is described accurately as title screening with targeted primary-source reading. REPORT.md begins exactly ACCEPT.

Completed 13 November 2026, approximately 08:00 Asia/Tbilisi.
Task: “You are an independent referee. … Break it if it is wrong.” — received approximately 07:45 Asia/Tbilisi.
