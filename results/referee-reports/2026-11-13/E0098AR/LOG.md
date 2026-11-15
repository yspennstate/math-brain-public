# Independent referee log

Task received: 13 November 2026, 11:43 Asia/Tbilisi: “You are an independent referee … Break it if it is wrong.” E0098.

## 11:43–11:45 — orientation and scope

Read the supplied claim report and consulted the local startup memory and compute state (status ok, owner away). No subagents. All substantive outputs and computations stay in this directory; no publication, git mutation, or push. The current explicit directory restriction precludes writing the global mesh, checklist, or brain stores; this log is the local task record. Original claim artifacts are read-only for this review. Their pre-existing PNG is not a source page image or scan.

Initial checks: the Gaussian scaling and exponential rate appear correct. The report explicitly limits the theorem to GOE and distinguishes its planted-vector example from a Wigner counterexample. Independent literature search has begun, including the 2026 papers cited by the claim; arXiv landing pages confirm their identities. Downloaded papers will be converted entirely in memory to plain text, without retaining PDFs.

## 11:45–11:51 — proof and source audit

- Retrieved arXiv:1601.03678v3 independently into `sources/survey.txt`; verified PDF page 13 and the exact Corollary 4.8 quantifiers. Saved the relevant 2013–2026 primary sources by downloading bytes into memory and piping them to pdftotext. The source program records URL, retrieval time and the original byte hash. All retained sources are text.
- The launcher contains `nohup nice -n 10 codex …`; subprocesses inherit that priority. A redundant nested nice request was denied by the sandbox, so subsequent runs inherit the launcher's nice setting. Numeric programs set all BLAS limits to one and run sequentially; no subagents or pools. They check RSS and the compute governor.
- Checked the GOE survival expansion and both the Laplace-functional and random-normalization arguments. Gaussian direction and radius are independent; the raw Gaussian minimum and radius are not. The claimant correctly avoids assuming the latter.
- Checked the planted zero and planted nonzero constructions, spherical density, entropy derivative, Pinsker step and the uniform-in-coordinate-subset mixture bound. The construction is valid. It is not a Wigner model, and total variation Gaussian approximation cannot hold for finitely supported atom models even in dimension one. The comparison with known results must specify topology and error rate.
- Independent code written before inspecting claimant code. Matrix simulations use fresh seed 918273645 and sample plan 128:1200, 512:600, 1024:250, 2000:120 for GOE and Rademacher, each at lower edge, bulk and upper edge. No pooling of correlated indices. Through n=1024 completed; n=2000 running.
- Exact arithmetic reproduced all seven small-n simple-spectrum/zero counts. Also counted existential zeros on repeated-spectrum matrices, which are automatic from an eigenspace of dimension at least two. These cases must not be read as canonical selected eigenvectors.
- Found an omitted older reference: Igor Rivin, `math/0305252v1`, “A Note on Spheres and Minima” (2003), especially pp. 2–4. It treats the same spherical minimum and its expected asymptotic. It does not explicitly state the normalized spherical exponential/point-process limit. The latter is an immediate consequence of classical iid extreme-value/Poisson theory plus radius concentration.
- Independently recalculated all 36 primary groups from claimant raw data, without executing their code: 14,490 rows; exact scaling agreement; five unadjusted KS p-values below 0.05 and the stated single Bonferroni rejection reproduced.
- The supplied claim package omits its referenced `sources/` archive. I reconstructed the sources rather than treating their report links as evidence. Found one wording error in the sign-switching description: it fixes the first sign of the conjugating diagonal matrix, not the first diagonal entry of the Wigner matrix.

## 11:54–12:00 — independent experiments and verdict draft

- Main experiment completed: 4,340 fresh matrices, 13,020 selected eigenvectors, 24 separate groups through n=2000. Time 490.04 seconds, peak RSS 340,787,200 bytes; one sequential worker. All residuals below 3.67e-15 and norm errors below 7.78e-16. No selected floating minimum zero or below 1e-12.
- All empirical CDFs lie inside their pointwise 95% DKW band around the proposed limiting CDF. Minimum KS p-value 0.09159. These results show compatibility only. Saved complete CSV, summaries, metadata, and an independent SVG CDF figure.
- SciPy's exact KS routine emitted Accelerate arithmetic-status warnings, but every result was finite. Independently recomputed all D statistics directly (agreement <1e-14); the usual asymptotic p-value series differs by at most 0.01031. DKW comparisons do not depend on this routine.
- Fresh-matrix solver comparison, n=128,512,2000: full EVD versus narrow MRRR; maximum scaled-minimum difference 3.33e-10.
- Additional 3,000-matrix searches at each n=8,12,16,24,32,64 found respectively 1675,721,132,1,0,0 exact-certified simple-spectrum matrices with a zero coordinate. Repeated spectra counted separately: 339,57,6,0,0,0. All positives exact-certified by characteristic polynomial/minor gcds. Negative screens are numerical, not exact exhaustive certificates. Repeated-eigenspace zeros are basis-dependent for selected numerical eigenvectors. Saved code, seed, counts, and witness matrices.
- Drafted REPORT.md with first line MINOR. No load-bearing mathematical error found. Required clarifications: classical GOE prior art; requested Luh–O'Rourke/Nguyen–Tao–Vu coverage; precise scope of the hypothetical total-variation obstruction; joint small-ball condition is sufficient, not necessary; sign-switching wording; omitted qualifications in the irrelevant Lévy-matrix row; missing supplied source archive. The result remains a correct partial explanatory audit, not a solution or new universality theorem.

## 12:03 Asia/Tbilisi — final audit and completion

- Final artifact audit passed: REPORT.md begins exactly MINOR; all report links resolve; inline/display mathematical markup and table pipes checked; 13,020 independent rows and all 24 group sizes, index choices, scaling identities, residuals, and finite values verified.
- Rechecked all four saved small-size witnesses by exact squarefreeness and characteristic-polynomial/minor gcds. The n=24 witness has common factor x-2. Small-zero rerun with the same seed reproduced every count while saving witnesses.
- All 32 supplied claim artifact hashes are unchanged. sources/ contains 23 primary paper texts plus SEARCH_LOG.txt, all plain text. No PDFs, source images, scans, publication, or pushes. Only our own simulation plot was added as SVG.
- A direct attempt to retrieve the Resnick chapter returned HTML rather than PDF; no file retained. The report identifies it as a printed general iid principle, not an explicitly printed GOE theorem, and distinguishes Rivin's expected-value theorem from a distributional theorem.
- DONE: independent E0098 referee report delivered as MINOR. Core partial proofs valid; GOE result classical; construction useful but outside Wigner; no general fixed-subgaussian-atom minimum law or counterexample located through the specified cutoff. Numerical compatibility through n=2000 and exact-certified finite-size Bernoulli zeros documented.
