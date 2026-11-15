# D0073 work log

Started 2026-11-13 09:00 +04 (Asia/Tbilisi).
Task: “Open problem D0073”: literature, reduction, rigorous partial results, and finite SAW enumeration.

Constraints: all artifacts and writes stay in this directory; no subagents; no publication or git pushes; one computation worker, nice 10, below 4 GB. Source PDFs will be fetched into memory and converted directly to plain text, never stored. The later task-specific directory restriction takes precedence over global instructions to write mesh, checklist, or brain state outside it. Startup orientation and compute state were read without modifying them. Compute state: warn/cpu_saturated, owner_away_open; use modest serial work.

## Literature phase

- Located the strict inequality paper: arXiv:1301.3091 (not 1310), SIAM J. Discrete Math. 28(3), 1306–1333 (2014), DOI 10.1137/130906052.
- Located Martineau–Severo: arXiv:1803.09686, Ann. Probab. 47(6), 4116–4136 (2019).

- Read all of survey Section 4 (PDF pp. 14–18). Exact conventions: directed orbit multigraph with loops in Theorem 4.2; undirected simple orbit quotient in Questions 4.5–4.6, with loops discarded and multiplicities merged. G belongs to the locally finite class defined in the survey. Transitivity of the simple quotient means transitivity of its own automorphism group, not necessarily a group induced from Gamma.
- Read arXiv:1301.3091 Sections 3.4–3.6 and proof Section 5, including the non-normal outline of Theorem 3.12. Normality makes orbit equality Gamma-invariant and transports a fixed nonclosing lift to every vertex. Arbitrary quotient automorphisms need not lift.
- Read Martineau–Severo definitions/results; Theorem 2.1 uses weak covering, disjoint tree lifting, tame fibres; Corollary 2.2 handles free group quotients without normality. Their introduction cites GL14 Theorem 3.8 as analogous, not as a solution of the full SAW question.
- Niceness audit: inherited process niceness is already 10. An explicit `nice -n 10` wrapper attempted to increase this to 20 and printed an OS warning; subsequent commands inherit the required nice 10 directly.

## Reduction and proof phase

- Broad searches by exact question, non-normal subgroup, covering maps, connective constants, quotients, and date windows 2017–2026 did not locate a full solution. Checked the requested locality, height-function, Lindorfer, Panagiotis, cubic, and Martineau–Severo sources, plus 2024 symbolic dynamics and many-ended work. Checking the author's current publication page also located the October 2026 preprint “SAWs, trails, kites, patterns”; this will be inspected before closing the search.
- Saved provisional REPORT.md with status PARTIAL. Proposed elementary result: if every orbit has an internal edge, quotient walks admit optional one-step insertions at every visited orbit, giving mu(G) ≥ (mu(H)+sqrt(mu(H)^2+4mu(H)))/2 > mu(H). This needs no normality. The proof will use generating functions so differing output lengths are handled correctly.
- Proposed complete tree proof: degree loss gives strictness immediately; with no degree loss the quotient is a classical covering and must contain a cycle; one forbidden nonbacktracking continuation per fixed-size block gives a strict growth bound.

- Completed inspection of the October 2026 pattern preprint 2611.00816. Its Theorem 4.5 gives a conditional reduction when the height-function group normalizes A and a bridgeable, admissible collision pattern exists; no claim is made that all quotients meet these hypotheses.
- Added direct proofs for internal-fibre insertion (including a polynomial version), finite clique factors, Cartesian doubling, trees, and the normal-core reduction. These do not establish the remaining core-free, degree-preserving case without compatible patterns.

## Enumeration and audit phase

- Exact serial enumeration completed for square cylinders (widths 2, 3, 4), brick-wall hexagonal cylinders (widths 2, 4, 6), 3- and 4-regular trees, S3 x Z and D8 x Z with complete finite-factor generators, and a sparse S3 x Z example. Finite group controls were also counted.
- Every graph agrees through n=6 with a second method that merges (endpoint, visited-set) states with integer multiplicities. Tree counts agree with d(d-1)^(n-1). Finite complete-graph counts agree with falling factorials. K3 x Z and the circumference-3 square cylinder agree through n=14.
- Group enumeration verifies freeness, non-normality and trivial core for the order-two subgroups of S3 and D8; quotient finite factors are K3 and K4. Both infinite products are transitive.
- Checked the exact coefficient inequalities from the optional-edge injection on all saved lengths for three group examples.
- Peak enumeration RSS was 94.5 MiB. Inherited nice=10, threads=1. macOS rejected attempts to lower RLIMIT_AS/RLIMIT_DATA; used conservative finite vertex/state budgets and checked peak RSS instead. No large jobs were launched.
- Source extraction occasionally emitted NUL characters. Replaced those control bytes by the literal text [NULL], indexed all sources and their theorem/page locations, and retained only plain-text source files.
- Citation audit found that the later 2025/2026 percolation reproof cites the published Martineau–Severo Theorem 1.1, whereas the downloaded 2018 arXiv version has Theorem 2.1. Report citations explicitly identify the arXiv numbering rather than claiming it is the journal numbering.

## Final result — 2026-11-13 09:23 +04

- REPORT.md first line is exactly PARTIAL. The general inequality remains unresolved in this work; no published resolution was located in the documented search.
- Final report includes the precise simple/directed quotient distinction; exact hypotheses and page references for the normal theorem; the non-normal proof obstruction; the percolation comparison and its missing counting step; complete elementary proofs of the uniform fibre-path criterion, clique-factor and Cartesian cases, tree case, and normal-core reduction; and a separately identified conditional deduction from the October 2026 preprint.
- Final mathematical audit corrected “increasing bridge” to the precise (+)/(−) bridge definition: bridge heights need not be monotone. Also recorded that finite-width strips have p_c=1, so the Martineau–Severo hypothesis does not cover them despite their strict SAW gaps.
- `code/audit_artifacts.py` passed: all 12 report comparison rows agree with saved data; 19 graphs were independently checked through length 6; all 16 extracted source text hashes agree; UTF-8 sources contain no NUL bytes; no PDF or paper-image files are present. Counting used nice 10, one worker, and peak RSS 94.5 MiB.
- Authored artifacts are confined to this directory. No publication, push, external message, subagent, or unrelated brain work was performed.

Task: “Open problem D0073” — 13 November 2026, 09:00 +04.
