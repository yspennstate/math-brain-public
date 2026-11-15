# T116 work log

Task: push worst-case trace reconstruction forward by one checkable piece.
Start: 2026-11-14 22:00 Asia/Tbilisi (18:00 UTC).

## Scope and startup
All writes stay inside this folder. No git, external messages, subagents, or shared-brain/mesh/checklist writes: the task-specific folder restriction overrides those earlier routines. Read startup memory index, brain index, and compute state. Compute state: status warn, mode owner_away_open, CPU saturated; no heavy computation planned. Invocations use OMP_NUM_THREADS=1 and nice -n 15. The inherited priority may already be at its limit: nice prints setpriority: Operation not permitted; verify actual priority before computation.

## Literature search, step 1
Web search queries: `trace reconstruction polynomial quasipolynomial Burudgunte Valiant Wang 2026 2607.04073`; `worst case trace reconstruction polynomial November 2026 improved lower bound`.
Search returned a primary-source lead: OpenAI, Quantitative lower bounds for trace reconstruction, dated 24 September 2026, claiming n^{Omega(log log n)} samples for fixed deletion probability, and an October companion algorithm. This would answer the polynomial-sample question negatively. Search snippets are not evidence enough: next open the primary paper and verify theorem, authors, conditions and publication status. If confirmed, follow the requested SOLVED_ELSEWHERE branch and stop.

## Literature verification, step 2
Opened the primary introduction.tex in openai/math: theorem thm:main defines complete deletion traces of deterministic binary words and unrestricted randomized estimators. It states T_{q,s}(n) >= n^{c log(q^3 log n)} eventually for fixed s>0, 0<c<1/(4 log 2), and q^3 log n -> infinity. It explicitly states the fixed-q superpolynomial consequence. Opened arXiv:2607.04073 and confirmed its authors and July baseline. Directory pages failed with cache misses; source files are accessible. A search for exact titles found the corporate author OpenAI and two October companion results. No arXiv identifier for the lower bound has been verified.
Commands: `ps -o pid,ppid,ni,comm -p $$ -p $PPID` was rejected by the sandbox (operation not permitted); do not claim priority independently verified. No numerical computation has run. Only tiny file reads/writes under the requested nice wrapper.
Next: read PDF title/theorem independently of TeX, then write the two requested reports and stop.

## Literature verification, step 3

PDF extraction failed: raw.githubusercontent.com returned application/octet-stream, which the web reader does not parse; a GitHub raw URL returned cache miss. Instead opened the primary manuscript header and abstract at:

https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/main.tex

Output: title Quantitative lower bounds for trace reconstruction; author OpenAI; date September 24, 2026. Opened the release README, which agrees. No arXiv id appears in its citation.

Opened the final proof section:

https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/transfer.tex

Output that matters: restoration/padding lemma supplies distinct words of exact length n; the final theorem proof handles any fixed positive success s using a fixed number of independent hard blocks and factorized posteriors. This is not merely a lower bound for mean statistics, random inputs, a subsequence of lengths, or success above 1/2. These observations check scope, not the full construction.

Opened https://github.com/openai/math/blob/main/lean/docs/122.md. It reports the same lower-bound scope. No formal checker was run and no certification is inferred from this document alone.

Opened the October algorithmic manuscript:

https://raw.githubusercontent.com/openai/math/main/preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/build/manuscript/main.tex

Output: OpenAI; October 5, 2026; uniform algorithm for rational p, known length n, success 2/3, sample bound ceil(exp(C B(n,p))), time polynomial in n + encoding length + sample budget. For fixed p, B=O_p((log n)^3(1+log log n)^6). A spectral-mask companion was found, but only its README was opened, so its theorem is not used in the report.

## Audit and stop decision

Independent algebraic checks of the lower-bound consequence:

1. At fixed q>0, log(q^3 log n)=log log n+3 log q. Its unbounded positive term eventually dominates the fixed additive constant; choose any allowed c>0 to obtain a positive multiple of log log n in the power of n.
2. For any fixed A, the ratio of the displayed lower bound to n^A has logarithm (c log(q^3 log n)-A) log n, tending to positive infinity. This directly rules out O(n^A) samples.

Checked boundaries: no claim for q=0 or q=1; no application to arbitrary sequences q tending to zero without the stated condition; no claim of a matching order. A bound at fixed success s=2/3 already rules out polynomial samples for high-probability recovery.

Decision: the literature contains a substantial later advance and a reported negative resolution of the polynomial-sample question. Follow step 1, write SOLVED_ELSEWHERE.md and REPORT.md, and stop. This is a literature result, not a new theorem proved in this folder. The verdict is PARTIAL to preserve the distinction between locating the preprint and independently certifying its proof.

Files written using apply_patch: SOLVED_ELSEWHERE.md, REPORT.md, and this appended log. No writes outside the task folder, no git, no external messages, no subagents, no simulation.

Final file audit command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B -c <read the three report files; assert verdict prefix and baseline identifier>`; output: all three files readable and nonempty; REPORT first line has the required VERDICT: PARTIAL prefix; baseline arXiv identifier present. No mathematical computation was required. Session literature check and report preparation completed within ten minutes.
