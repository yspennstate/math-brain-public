# T132 verification log

Started 2026-11-14, Asia/Tbilisi (session directory timestamp about 21:07).

1. Read directory listing, startup memory index, brain index, and compute state. No files outside this directory were changed. The task-specific instruction to write only here overrides global mesh/checklist/brain writes; those services were not invoked. Compute state: warn, owner_away_open; no heavy computation planned. Commands use `OMP_NUM_THREADS=1 nice -n 15`; macOS reports `setpriority: Operation not permitted`, so priority enforcement needs checking before further local work.
2. Web tool opened all three supplied GitHub folder URLs. Each returned a cache-miss fetch failure; no preprint text obtained. Next: raw TeX paths and web search.

3. Raw paper.tex URLs also failed via the web tool. Web search found indexed abstracts and an AI Proof Watch assessment; these are leads, not substitutes for the theorem text. Tested direct raw-file download via urllib; result printed in tool output.

4. Direct urllib raw download failed: DNS resolution unavailable. Process priority checked with os.getpriority: 20 (lower scheduling priority than requested 15); nice attempts warn because inherited priority is already at the floor. All local commands remain light, single-threaded, and bounded. Blob paper.tex paths also failed through web. Opened lean/docs/211.md successfully: its scope is fixed q>4, n^(-1/2), Brownian CRT, normalized degree measure, all integer sizes; not the requested subcritical LQG limit. Trying PDF and build/paper.tex routes.

5. Read-only GitHub connector fetch also returned API 404 for candidate 1 paper.tex. Web searches (exact titles, plus theorem) located actual PDF filenames: candidates 1 and 2 main.pdf; candidate 3 linear-clock-random-walk-tree-weighted-planar-maps.pdf. Search leads include Plectis Atlas family 211 (theorem transcription), oai-math-revised pages, and a claimed follow-up arXiv:2610.10501 attributed to Nina Holden. These leads require primary-source checks.

6. Opened the three actual PDF GitHub wrappers (1.58 MB, 1.46 MB, 613 KB); wrappers expose no PDF body. Opened Plectis Atlas family 211, which distinguishes q>4 Lean verification from the unformalized LQG claims. Next: actual raw PDF content and primary follow-up arXiv page.

7. Raw PDFs exist but the web reader rejects application/octet-stream. Opened arxiv.org/abs/2610.10501: Nina Holden, The Tutte embedding of tree-weighted planar maps converges to Liouville quantum gravity, submitted 7 October 2026; abstract concerns a Boltzmann disk with growing boundary and Brownian motion modulo time, not a fixed-size spherical graph-metric theorem. Trying build/main.tex and raw=true PDF.

8. Located and opened actual TeX entry points for candidates 1 and 2: build/main.tex. Both say author OpenAI and date September 24, 2026. Their theorem-bearing introduction files are sections/01-introduction.tex and sections/00-introduction.tex respectively. Candidate 3 root TeX guess was 404. Raw=true PDF blocked by robots.

9. Successfully opened candidate 1 build/sections/01-introduction.tex and candidate 2 build/sections/00-introduction.tex directly. Candidate 1 main theorem claims GHP convergence for fixed q in (0,4) plus tree-weighted maps with arbitrary deterministic a_n -> 0 and degree measure; immediately afterward it explicitly disclaims a normalization power law and says uniform-vertex measure needs a separate argument. This prevents an unqualified literal full-statement verdict. Opened repository LICENSE (Apache 2.0).

10. Search for exact candidate-1 title with error/gap/correction/arxiv returned catalog/assessment pages, no primary error report. A second follow-up lead is arXiv:2610.10505, attributed to Nina Holden and Pu Yu; will verify authors and scope on the primary page. Candidate 2 introduction confirms it proves only q=4 and does not use another-q convergence theorem.

11. Located candidate 3 actual TeX entry point build/paper.tex. Opened candidate 2 main theorem (Joint critical universality, Theorem 1.2) and continuum Theorem 1.1 in its introduction; endpoint q=4 is outside our 0<=q<4 range and also has no asserted power law. Opened primary follow-ups: arXiv HTML 2610.10501v1; arXiv abstract 2610.10505, authors Nina Holden and Pu Yu, exact title: The circle packing and Riemann uniformization embedding of the tree-weighted planar maps converges to Liouville quantum gravity.

12. Opened candidate 3 build/paper.tex completely: author OpenAI, date October 5, 2026, introduction sections/01-introduction.tex. Opened follow-up 2610.10505v1 full HTML (title there uses “tree-weighted planar maps converge”, unlike abstract-page grammar), and the release challenge lean/ComparatorChallenges/FKCRT.lean. Candidate-3 theorem will be read from its own TeX, not the Atlas transcription.

13. Primary Holden HTML statement explicitly names all three related OpenAI papers and says they solve several listed future directions; this is a relevant expert acknowledgement, not a referee report or proof audit. Read the q>4 quantifier and Brownian-CRT expectation limit in FKCRT.lean; its sorry is in the challenge statement file and is not itself evidence that the separate solution has a gap. Read candidate-2 Corollary 1.3 and its proof: degree-measure GHP limit at q=4 only.

14. Searched exact titles with arxiv/error/gap/refutation/correction. No same-title arXiv version, mathematical refutation, or referee report located; the negative finding is search-limited. Candidate-3 Theorem 1.1 is “Linear clock and conditional laws”; it augments a companion spatial normalization with path-law convergence and time acceleration n. Holden–Yu primary HTML explicitly says neither their results nor the OpenAI results imply the other. Follow-up sites are not treated as proof verification.

15. Candidate-3 theorem now read in full: Theorem 1.1, fixed finite T, conditional laws Q_n^T of X^n_(nt), joint convergence in delta_T, exact clock multiplier c=1. Its spatial scale is a deterministic arctan-centered diameter normalization, and its GHP convergence is explicitly a premise taken from MetricMaps. Neither a spatial exponent nor general-q convergence follows from its linear time clock. Preparing VERIFY.md and REPORT.md before a limited spot check.

16. Wrote VERIFY.md (exact main theorem source statements for all candidates, comparisons, primary follow-ups, Lean scope, three-sentence replacement) and REPORT.md. Verdict PARTIAL-CLAIMED: full requested q range for the geometric claim, but unspecified deterministic scale rather than asserted n^(-1/d_gamma+o(1)); degree measure specified. Next: one load-bearing lemma spot check and final audit.

17. Read the candidate-1 comparison wrapper (04-comparison-rigidity.tex) and conditional-local-kernel section (03-local-kernels.tex). The former delegates to common-rigidity.tex. Began identifying one load-bearing local-law lemma for a bounded spot check; no general proof audit is claimed.

18. Read-only GitHub connector successfully fetched the actual three introduction TeX files and local-kernel section after their real paths were located. Saved exact copies under sources/ and replaced all four quoted theorem blocks mechanically from those sources, preserving original whitespace and TeX. No git commands used.

19. Selected the ladder local-limit and conditional-path lemma (loc:ladder-llt) in the main metric paper for the single spot check: it supplies endpoint densities and conditioned bridge laws used by the local resampling argument. Read its complete statement and proof from saved exact TeX.

20. Spot check calculations: independently factored the Brownian endpoint density into first-passage-time density and a conditional Gaussian; derived its Fourier transform and modulus; checked the support lattice has index two; examined the reserved-block conditional-path argument. No concrete defect found in these steps conditional on the cited stopped-contour invariance principle. Final follow-up sweep opens the three community-note pages and primary arXiv:2611.03739 because a search snippet mentioned the clock paper.

21. Appended Spot check to VERIFY.md: explicit Brownian density factorization, characteristic transform and lower modulus bound, index-two lattice factor, and conditional reserved-block argument. All are consistent conditional on the underlying invariance principle; that premise and subsequent kernel/rigidity arguments are not certified. Opened all three community pages: no human notes there; candidate-2 page confirms q>4-only Lean scope.

22. Final audit: four quoted theorem blocks match the saved source TeX byte-for-byte; q/gamma substitutions for q=0,1,2,4 independently checked numerically against the displayed relation; REPORT has the required verdict prefix and two reason lines. No proof correctness judgment added. Community issue-search links were attempted but all failed with cache misses. Opened arXiv:2611.03739 abstract and HTML: a study of textual co-occurrence topology, not a mathematical proof audit.

23. Added final follow-up record to VERIFY.md: Kapulkin–Kershaw textual-topology paper includes the clock manuscript as corpus data, not proof verification; three community pages and inaccessible issue searches recorded. Saved repository Apache license beside exact source copies. Files ready: REPORT.md, VERIFY.md, LOG.md, sources/. Final task: Verify: has open problem T132 been settled by the OpenAI math release? Session began about 21:07 Asia/Tbilisi, 14 November 2026.
