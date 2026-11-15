# T119 work log

Session date: 14 November 2026 (Asia/Tbilisi).
Task: “push this problem forward by one checkable piece.”

## Step 1: orientation and literature search

Read the workspace listing and the shared compute-state file. The folder initially
contained PROMPT.md. Compute status was `warn`, mode `owner_away_open`; no heavy
computation was started. All writes will stay in this folder, as specifically
required by this task. Accordingly, shared checklist, mesh and brain commands
that would write outside the folder are not run.

Read-only orientation command:

```
nice -n 15 env OMP_NUM_THREADS=1 python3 -c '<read compute_state.json and available memory index>'
```

The environment printed `nice: setpriority: Operation not permitted`; the
read-only command nevertheless completed. No numerical program is run under
this failed priority setting.

Web search queries:

- `random cubic graphs independence number 0.45537 0.44533 2025 2026`
- `random 3 regular maximum independent set independence ratio rigorous 0.45086`

The first results identify arXiv:2204.01353, *Improved replica bounds for the
independence ratio of random regular graphs*, with purported rigorous upper
bounds below 0.45079. This would substantially advance the supplied status and
trigger the instruction to report the existing result and stop. Next step:
open the primary paper and verify the statement, authors and numerical values.

## Step 2: verification and stopping decision

Opened these primary sources with the web tool:

- https://arxiv.org/abs/2204.01353
- https://arxiv.org/html/2204.01353
- https://link.springer.com/article/10.1007/s10955-022-03062-7
- https://real.mtak.hu/175241/1/RSB_bounds_20230127.pdf

Confirmed sole author Viktor Harangi; arXiv v4 dated 19 December 2022;
publication 28 January 2023, Journal of Statistical Physics 190, article 60.
Read Theorem 2.2, Corollary 2.3 and Section 1.2. Cross-checked the degree-3
table between arXiv HTML and PDF text, and the theorem against the publisher
version. The reported 5-RSB upper bound is 0.45078521. Section 1.2 also gives
an explicit four-atom witness establishing the weaker bound 0.450789952.

Audit: checked that the quantity bounded is the limiting independence ratio
of uniform random regular graphs, that degree 3 is included, and that the
result is an upper bound rather than an equality. Table 5 gives extra digits
consistent with Table 2. This is documentary cross-checking, not independent
numerical reevaluation or a new proof. No numerical results are claimed as
computed here. The supplied lower bound was not independently audited.

The source substantially advances the supplied status, although it predates
its claimed November 2026 check. The prescribed early-stop branch therefore
applies. No new research piece is selected. Write SOLVED_ELSEWHERE.md and
REPORT.md, then stop. The first filename is prescribed and does not mean
that the exact constant has been determined.

Final source checks: the publisher theorem matches the arXiv statement.
The publisher HTML search did not expose the numeric table cells. A PDF
screenshot request failed with a fetch timeout, so no visual verification
is claimed. The PDF text and arXiv HTML do agree. An attempted log correction
initially failed its patch-context check; the corrected patch was then applied.
Created the two requested reports and stopped on the literature branch.
