VERDICT: PROVED T115's O(d sqrt(n)) bound, elsewhere (OpenAI, 2026)

OpenAI, *Average sensitivity of polynomial threshold functions*,
25 September 2026, Theorem 1, proves total influence at most 8d sqrt(n).
The theorem is uniform in n and d and includes polynomial zeros.
[Primary paper](https://github.com/openai/math/blob/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf).
No arXiv identifier for this preprint was identified.

The complete statement is settled, so the session stops under the explicit
step 1 exception. This session claims no new proof or computation.

SOLVED_ELSEWHERE.md gives the references and checks of multilinearization,
edge normalization, constants, degree range and zero conventions. The
October revision of arXiv:2604.08095 independently cites the solution and
prints the same bound.

Commands and tool calls: read-only `ls`, `rg`, `sed`, `cat`; `web.run`
search/open; connected GitHub fetch of the primary TeX and Lean files.
Queries, paths, significant output and retrieval failures are in LOG.md.
There were no numerical runs or package installations.
The final file check passed; its `nice -n 15` wrapper reported that the
environment rejected the priority adjustment. No heavier program was run.

What failed: the web tool could not decode the raw PDF; an initial TeX path
was wrong. Reading the actual primary TeX source resolved both issues.
The proof's Sections 1–5 were read and its final constants checked. Lean
was not rebuilt; no claim about a local formal verification is made.

Next worker: update the problem list to record the complete asymptotic
solution. Further research on the optimal constant would be a separate task.

Task: “Push this problem forward by one checkable piece.” Received
14 November 2026, approximately 21:17 Asia/Tbilisi.
