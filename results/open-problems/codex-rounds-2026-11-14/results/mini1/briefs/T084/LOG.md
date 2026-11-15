# T084 work log

Task received: 2026-11-14, approximately 20:52 +04 (Asia/Tbilisi).
Task: “push this problem forward by one checkable piece.”

## 1. Orientation and literature check

All writes are restricted to this folder. The task-specific restriction overrides
the global requests to update the external brain, checklist, and mesh; those
commands can write outside the folder and will not be run. No git or subagents.

Read the startup memory and compute governor. Governor at 20:52:21 +04:
status=warn, mode=owner_away_open, 37% free memory, CPU saturated.
Any computation will use one thread, OMP_NUM_THREADS=1, nice -n 15,
and a bounded run well below 1 GB and 20 minutes.

Initial web searches: “negative correlation forests 2026 2027”, and the
three recent arXiv identifiers in the brief. They returned the cited papers;
no later resolution identified yet. Opening primary sources next.

Opened https://arxiv.org/abs/2610.00549,
https://arxiv.org/abs/2609.26134, and
https://arxiv.org/abs/2609.11578. Additional web searches:
“random-cluster negative correlation November 2026”,
“forests Rayleigh series-parallel”, and
“uniform forests negative correlation proof October 2026”.
These found a possible substantial advance omitted from the brief:
Ying Cao and Houshan Fu, “Negative edge correlation in complete bipartite
graphs”, listed as published 27 October 2026 by Valency Hub. Also found
Idriss Olivier Bado, “Negative edge correlation for uniform random forests
on wheel graphs”, Statistics & Probability Letters, DOI
10.1016/j.spl.2026.110960 (issue dated February 2027; online date not yet
checked). Neither search hit is yet being treated as a verified result.
Checking the primary sources and dates before choosing any original work.

## 2. Primary-source confirmation and stopping decision

Web query: `"Negative edge correlation in complete bipartite graphs" Cao Fu arxiv`.
Output: Ying Cao, Houshan Fu; arXiv:2610.36749; submitted
27 October 2026 at 07:05:57 UTC.

Opened all three primary-source representations:

- https://arxiv.org/abs/2610.36749
- https://arxiv.org/html/2610.36749v1
- https://arxiv.org/pdf/2610.36749

Output that matters: PDF page 2, Theorem 1.1 gives
`i_e(K_mn) i_f(K_mn) - i_ef(K_mn) i(K_mn) > 0` for all m,n >= 2
and distinct edges. Theorem 1.2 gives the corresponding inequality with
connected-spanning-subgraph counts j. PDF page 1 defines forests as all
acyclic edge subsets, including the empty set. HTML and abstract agree.
If a part has size one, the PDF explicitly gives equality instead.

Independent scope check: dividing the count inequality by the positive
square of the total count gives exactly the requested probability
inequality, with strict sign. The adjacent/disjoint distinction imposes
no restriction in the theorem. This checks interpretation; it is not a
second proof of the cited theorem. No load-bearing numerical computation
was made.

Decision: this is a substantial advance missing from the supplied status,
later than the recent results cited there. Apply step 1 and stop; do not
choose an original research subtask. Wrote SOLVED_ELSEWHERE.md and REPORT.md.
The general problem is not claimed solved. The wheel-paper publisher URLs
returned HTTP 403 when opened and were not used for the stopping decision.

Clock command: `date '+%Y-%m-%d %H:%M:%S %Z'`.
Output: `2026-11-14 20:54:06 +04`. Literature check took about two minutes,
within the ten-minute limit. No git, external writes, or numerical runs.

Final file audit: `head -1 REPORT.md`,
`wc -l LOG.md REPORT.md SOLVED_ELSEWHERE.md`, and an `rg` check of the
identifier, theorem numbers, general-case limitation, and verdict.
Output confirmed the required `VERDICT: PARTIAL ...` first line and all
three deliverables. REPORT.md explicitly distinguishes the literature
finding from an original proof or computation.
