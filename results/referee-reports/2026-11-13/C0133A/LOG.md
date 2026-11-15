# C0133 work log

Started 2026-11-13 04:36 (Asia/Tbilisi; host clock). Task: “Open problem C0133.”

- Scope: this directory only; no publication, pushes, or subagents. Numerical work, if needed, will use one process at nice 10 and bounded memory.
- Read the startup memory, recalled the shared brain, and checked the compute state. The shared mesh is outside the writable scope, so a directory-local coordination/checklist store is used. The attempted shared digest was denied as read-only.
- First step: download arXiv:1204.1895, check the journal version, read the precise hypotheses and Section 4, then search the later literature before attempting a proof.

Findings and proofs below will be dated as work proceeds. An unsuccessful search is not evidence that a problem is still open.

## 04:40 — exact source and first literature findings

- Downloaded the arXiv v2 PDF (37 pages) and the journal PDF (53 pages). Both use Problem 4.7. It occurs on arXiv PDF page 19 and journal PDF page 28, printed page 132. SHA-256 hashes will be retained in the source manifest.
- The model explicitly permits infinitely many non-placebo cookies per site. IID applies to whole site stacks, not to entries within a stack. EL means every nearest-neighbor probability at every finite visit index is strictly positive a.s.; it does not give a uniform lower bound or divergent sums over a stack.
- Downloaded and read Amir–Berger–Orenshtein, arXiv:1304.7287v2: Theorems 1.2 and 1.3 establish a directional zero-one law and a deterministic speed in d=1 for stationary ergodic elliptic stacks, including infinite stacks. Thus the requested claim holds in d=1, by taking the subsequence of visits to a fixed site. This is not a resolution in general d.
- Downloaded Zerner (2002). Theorem 1 concerns iid RWRE and oscillation in a coordinate. Its proof uses the quenched strong Markov property at repeated visits to the same site; ordinary ERW changes the residual stack there, so this step cannot simply be copied.
- Downloaded Kosygina–Peterson, arXiv:1504.06280, and Amir–Orenshtein, arXiv:1307.6052. These give further d=1 results; neither supplies the general multidimensional conclusion.
- Searches used exact problem numbering, non-transient/nontransient/non-transience, recurrent-event speed, infinite-stack speed, and LLN with years through 2026. A reproducible OpenAlex forward-citation search over both indexed survey records is being saved, rather than treating keyword search as exhaustive.
- Caution under investigation: finite cookies imply exhaustion in each fixed recurrent box, not immediate global exhaustion. Long excursions beyond that box require a separate argument.

## 04:44 — forward citations and a proposed general argument

- OpenAlex returned 37 citations of its journal record and 23 of its arXiv record, 45 distinct OpenAlex work IDs after merging (some are duplicate versions of the same paper). Raw JSON and a TSV are saved. The latest returned items are two 2026 centrally/radially excited-walk papers, whose spatial dependence is outside IID. No general resolution was identified in this citation set.
- The Santos counterexample found in that search concerns zero speed despite infinitely large mean cookie count in a stationary ergodic d=1 environment. It is not a counterexample to Problem 4.7.
- Downloaded the specified Holmes, Holmes–Salisbury, Menshikov–Popov–Ramírez–Vachkovskaia, Zerner directional-transience, and van der Hofstad–Holmes papers. Two guessed PDF URLs returned 404, retained as errors in the manifest rather than presented as read sources.
- A general proof is now being audited. For a coordinate e, suppose P(A_e)=0. The survey's slab lemma implies that a path bounded below in that coordinate cannot also be unbounded above. After any fixed finite path ending back on the initial hyperplane, the quenched chance of staying strictly to its right and reaching all levels must therefore be zero, by ellipticity and concatenation. This gives a vanishing upper bound for fast final crossings from fresh hyperplanes, uniformly over the finite set of histories of length at most c. Bounded martingale differences along every L-th hyperplane turn the bound into a frequency bound. Zerner's deterministic Lemma 3 contradicts positive limsup speed.
- The key improvement over blindly restarting a cookie walk is to retain each finite consumption history separately. No equivalence between original and shifted infinite-stack laws is assumed. This is a candidate argument, not yet the final status.

## 04:52 — proof and numerical audit

- Wrote the full argument to REPORT.md, with provisional PARTIAL status pending audit. It uses only IID/EL and the survey's Theorem 2.5, Lemma 3.18, and Theorem 3.16. The deterministic lemma from Zerner (2002) is reproved with different counting constants.
- Independently checked the fresh-half-space estimate by conditioning on the full environment, retaining the exact finite consumption prefix, dropping only its probability factor (which is at most one), and integrating the still-pristine right half-space. Ellipticity is used to concatenate each finite prefix under the original law; it does not give a uniform likelihood bound, and none is needed.
- The martingale indicators are measurable at the next hyperplane hitting time along each residue class modulo L. Infinite hitting times cause all subsequent indicators to vanish; no conditional-on-recurrence martingale law is used.
- Numerical run completed: 64 walks each of four two-dimensional laws, 65,536 steps per walk, plus 20,000 trials of the specified two-site trapping event. One worker, inherited nice 15 (more yielding than nice 10). No BLAS threads. Initial /usr/bin/time -l resource collection hit a sandbox sysctl denial after the Python process finished; the script is being updated to record its own peak RSS.
- 400 finite-path checks of both counting sums and the strict-growth implication passed. A separate exhaustive finite-horizon prefix-factorization check is now being run with both pristine and already-used left half-spaces.
- The 2022 Alves–Iacobelli–Valle Bernoulli preprint is withdrawn (arXiv v3, 2023-03-24); this explains the missing PDF and it is not used as evidence. The 2026 radial paper is superseded by the joint centrally excited paper; both have position-dependent origin-directed drift, outside IID.

## 04:54 — result

- The proof audit found no remaining gap: REPORT.md now begins PROVED. The finite-history conditional bound, martingale frequency law, and deterministic path lemma establish zero vector speed on the non-transient event under precisely IID and EL, with arbitrary infinite stacks. No uniform ellipticity, finite drift, or finite stack assumption was introduced.
- Exhaustive finite-horizon audit: all 18 prefix-factorization cases passed, maximum absolute discrepancy 1.1102230246251565e-16. The 400 counting checks also passed.
- The rerun recorded peak RSS 47,841,280 bytes and one worker at nice 15. Full simulation output and data were saved. The specified two-site trapping event had frequency 845/20,000 = 0.04225, consistent with the independently computed probability 0.04242660227895439. The positive-speed-looking finite excursions in other runs are not evidence about their infinite non-transience event.
- Saved source PDFs, text extracts, checksums, raw forward-citation records, code, data, and the report. No publication, push, subagent, or mutation outside this directory was part of the research work.
