# T170 verification log

2026-11-14: Task: “Verify: has open problem T170 been settled by the OpenAI math release?”

Step 1. Inspected the working folder and compute-state file using a short Python command prefixed with OMP_NUM_THREADS=1 nice -n 15. Compute state reported status ok; no heavy computation is needed. The sandbox reports `nice: setpriority: Operation not permitted`; priority changes are unavailable. All writes are confined to this folder. Standing brain/mesh/checklist commands would write outside this folder, so the task-specific no-outside-writes rule takes precedence; they were not run. No git commands or subagents.

Step 2. Began opening all three supplied GitHub folders and searching the web for the exact preprint subjects. Results are recorded below as they arrive.

Step 3. The three supplied GitHub folder pages returned cache misses, and guessing paper.tex at each folder root returned HTTP 404. Opened the repository README (raw main/README.md) and lean/docs/087.md; 087 concerns Mahler and polar products, not this row, so it is excluded. Web search located the relevant family number 212 and a possible citing arXiv paper 2610.42124. Requested the three actual directory listings through the read-only GitHub connector, plus lean/docs/212.md, formalization.yaml, history.md, and the arXiv page.

Priority check: os.getpriority returned 20, already lower priority than nice 15; the failed attempt to change priority is harmless.

Step 4. Read all three manuscript READMEs: all name the author OpenAI, dated 24 September 2026 (strict convexity and no bigeodesics) and 23 September 2026 (symplectic packings). Their sources are modular under build/main.tex and build/sections/. PDF names are main.pdf, paper.pdf, main.pdf respectively.

Step 5. Opened lean/docs/212.md: formal scope is differentiability for positive Gamma laws, including exponential weights; strict convexity is explicitly excluded. Opened lean/README.md and repository history.md; no entry names a correction or withdrawal of these three papers. Opened arXiv:2610.42124 abstract and HTML: authors Scott Armstrong and Ahmed Bou-Rabee, submitted 30 October 2026. Introduction calls the OpenAI strict-convexity/differentiability result an announcement; its own rotationally invariant continuum model is different from lattice Eden growth.

Step 6. Opened all three build/main.tex and introduction files through read-only GitHub fetch; saved exact snapshots to sources/candidate-{1,2,3}-{main,introduction}.tex. Candidate 1 Theorem 1.1 asserts Frechet differentiability and strict convexity for exponential weights on Z^2, and Theorem 1.2 differentiability for Gamma weights. Candidate 2 concerns deterministic symplectic packings of 2n-balls for n>=3. Candidate 3 Theorem 1.1 excludes bigeodesics in planar iid nonatomic FPP with a minimum-of-four second moment. None of these statements asserts that the Eden limit shape is non-Euclidean.

Step 7. Web searches used exact titles with error/arxiv qualifiers and Eden/OpenAI/ball. They located a later continuum FPP paper, a symplectic follow-up, and expositions; unrelated last-passage-percolation hits were not treated as answers. Next: inspect Lean theorem statements and follow-up originals.

Step 8. Wrote REPORT.md with verdict NOT-THIS. The comparison is logical, independent of whether any manuscript proof is correct: Euclidean disks satisfy the regularity conclusion; no theorem states anisotropy. Read PlanarFirstPassage.lean and GammaPassage.lean comparator statements, PlanarFirstPassage.json, and the actual BoundaryCurve.lean solution theorem. Comparator sorry placeholders are challenge statements, not evidence that the submitted solution is incomplete. Read BallPacking.lean and lean/docs/343.md: symplectic scope only. No Lean execution attempted.

Step 9. Opened original arXiv pages 1705.08143 and 1008.5069 to check the existing dimensional record. Opened Liang Song, Explicit Hamiltonian ball packings in every dimension, aiXiv 2611.00466v1, a 45-page follow-up citing the symplectic preprint. This is aiXiv, not arXiv, and is not a claim about lattice growth. Also opened a public audit report located by the error searches, for relevance screening.

Step 10. Confirmed the original Bertrand–Pertinand abstract explicitly gives dimension greater than 22. The Couronné–Enriquez–Gerin abstract says larger than 35 (not >=35), an endpoint discrepancy in the supplied old note that is immaterial to the present d>22 frontier; the recommended update will omit that intermediate endpoint. Armstrong–Bou-Rabee introduction and reference Ope26 acknowledge an announcement, not a proof review. Song abstract and references identify the symplectic dependence and explicitly disclose AI-produced mathematics; this is not an independent specialist validation.

Step 11. Saved VERIFY.md with verbatim theorem environments, model/dimension/quantity/strength comparison, follow-up URLs actually opened, Lean scope and limitations, and a three-sentence recommended status. Recorded current main commit 4eaee87548250b2682affda7d05d947c05554bae through the GitHub branches API (no git command). REPORT.md was already saved before the optional spot check.

Step 12. Began optional spot check after REPORT.md: opened strict/improvement.tex, strict/conclusion.tex, and strict/foundations.tex of candidate 1. Saved these and the inspected Lean statement/solution files under sources/. Selected the fixed-scale contraction proposition improvement:contraction-proposition, the step that drives the flat-face contradiction. Checking its parameter order, rescaling, infimum argument and displayed error estimate; earlier geometric/probabilistic inputs are not thereby certified.

Step 13. Appended Spot check to VERIFY.md. Re-derived the contraction error budget, finite-range replacement counts and independence uses, scaling of the mesh/tracking/costs, and the infimum/iteration quantifiers. No error found in this deduction conditional on prior gauge/link/support inputs; those are explicitly left unverified. This is not a proof-correctness verdict. An initial patch used too short a context and failed without changing a file; the append was then applied successfully using the full paragraph. Added sources/SOURCES.md with retrieved-file URLs and Git blob hashes.

Step 14. Final audit: recomputed Git blob SHA-1 directly from each saved TeX snapshot (without git); all nine snapshots match the published hashes. Checked REPORT.md has its required verdict first line and three reason lines; VERIFY.md has four exact theorem environments (including the Gamma extension), the recommendation, and Spot check. Confirmed nice value remains 20. Finished the requested literature verification; no external writes, posts, pushes, accounts, heavy compute or proof-correctness certification.

Task: “Verify: has open problem T170 been settled by the OpenAI math release?” — received 14 November 2026; task start logged at 21:09 Asia/Tbilisi.
