# T050 work log

Task received: 2026-11-14; first recorded clock reading 16:46:04 UTC
(20:46:04 Asia/Tbilisi). Task: “push this problem forward by one checkable piece.”

## 1. Orientation and literature search

Read the local PROMPT.md, the startup orientation, and the compute governor
state. The governor reported status `ok`, mode `owner_away_open`. The present
task's restriction to this directory overrides earlier instructions to mutate
the shared checklist, mesh, or brain; no such shared-state tools were run.

Read command:
`OMP_NUM_THREADS=1 nice -n 15 cat ~/.claude/brain_startup.md ~/.claude/compute/compute_state.json PROMPT.md`

The sandbox printed `nice: setpriority: Operation not permitted`, then completed
the read. No numerical computation has been started. Do not assume a requested
priority change succeeded.

Web search queries:
- `"first passage percolation" "strict convexity" 2025 2026`
- `"limit shape" "strictly convex" "first-passage" recent`

The first search returned a potentially decisive September 24, 2026 manuscript,
attributed to OpenAI, claiming strict convexity and C1 regularity for planar
exponential FPP and differentiability for planar Gamma weights. This contradicts
the supplied status paragraph for exponential weights. Search snippets alone
are insufficient: next open the primary manuscript and check its exact scope
and verification status. If confirmed as a substantial claimed advance, take
the requested literature-discovery branch and stop with SOLVED_ELSEWHERE.md
and REPORT.md; do not claim the full continuous-law, all-dimensions conjecture.

## 2. Primary manuscript located

Opened the manuscript landing page and its linked PDF using the web tool:
https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/

PDF: same directory, `main.pdf` (95 pages).

The landing page identifies author OpenAI and date September 24, 2026. Its
formalization section says the selected Lean statements cover differentiability
for exponential and positive Gamma laws, explicitly excluding exponential
strict convexity. It also says nobody has checked that those Lean statements
match the paper. Therefore neither formalization nor an abstract alone warrants
calling the strict-convexity conjecture independently verified.

Additional web queries:
- `"Strict convexity and differentiability of the planar exponential" arxiv`
- `"Strict convexity and differentiability" "error" percolation`

No arXiv identifier for this manuscript appeared in these search results.
Direct GitHub directory and scope-note opens failed; the linked PDF opened.
Next read the theorem statements and primary scope note through its raw URL.

## 3. Scope checked; literature-discovery stop branch chosen

By 16:46:57 UTC, the web tool had opened the manuscript's title page, located
Theorems 1.1 and 1.2 (PDF page 3), and located Section 16's concluding proof of
Theorem 1.1 (PDF page 88). The theorem statements match the abstract's distinction:
strict convexity for planar exponential weights; differentiability for planar
positive Gamma weights. No full-law or higher-dimensional theorem is stated.

The primary scope note opened successfully:
https://raw.githubusercontent.com/openai/math/main/lean/docs/212.md

It explicitly says strict convexity is outside the selected differentiability
statements. This independently checks the limitation noted on the landing page.
No claim of a fully audited proof is made. A further original raw-PDF open
failed with `Unsupported content-type: application/octet-stream`; a PDF
screenshot attempt failed with `Cache miss`. Parsed theorem text was available.

Choice: use the explicit step-1 stop branch, documenting a substantial claimed
advance rather than initiating a separate proof or computation. The preprint
predates the supplied November status check but directly contradicts its claim
about exponential weights. Its correctness is still to be independently checked.

## 4. Adversarial checks and deliverables

- Checked the general-Gamma theorem separately: differentiability does not
  supply strict convexity. Checked that both statements are planar.
- Checked the formalization scope against the author's own raw note: it excludes
  exponential strict convexity. Did not equate comparator acceptance with proof
  of the conjecture or run a Lean build.
- Read the final argument as well as the theorem statement. Its strict-convexity
  contradiction depends on a positive lower bound and an iterated improvement
  for the same admissible path class; those substantive propositions have not
  been independently verified here.
- No load-bearing numerical estimate is asserted as a new result, so there is
  no numerical recomputation or simulation data. No new mathematical proof is
  claimed.
- Wrote SOLVED_ELSEWHERE.md and REPORT.md. The report uses PARTIAL because a
  source discovery and a verified proof are different outcomes.

All file writes used the patch tool within T050. All literature queries and
opens used the web tool. No shared brain/checklist/mesh mutations, git, external
posts, or numerical programs were used.

## 5. Final readback

Command:
`OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md SOLVED_ELSEWHERE.md LOG.md`

Output: all three files read back successfully, including the required first
line `VERDICT: PARTIAL ...` in REPORT.md. The same priority warning appeared;
exit code was 0. Final clock reading after readback: 16:48:03 UTC. The literature
check and write-up therefore finished within two minutes of the first recorded
clock reading, below the ten-minute search limit.
