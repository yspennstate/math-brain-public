# T064 work log

Task received: 14 November 2026, approximately 20:49 Asia/Tbilisi
(16:49 UTC): “push this problem forward by one checkable piece.”

## 20:49–20:50 — orientation and literature search

Read the startup memory index and compute governor state. The latter reported
`status: ok`, `mode: owner_away_open`. The session-specific instruction to write
only in this folder supersedes the global instructions to mutate the shared
brain, mesh, and checklist; none of those stores was changed. No agents, git,
background workers, or numerical experiments were started.

Read commands used `env OMP_NUM_THREADS=1 nice -n 15 ...`. macOS printed
`nice: setpriority: Operation not permitted`, but executed the commands. This
is recorded rather than claiming that changing priority succeeded. No heavy
program will be run.

Web search tool queries:

- `random plane wave percolation conjecture Cardy SLE 2025 2026`
- `random plane wave Russo Seymour Welsh bounds percolation 2024 2025`
- `"random plane wave" percolation 2026`
- `"random plane wave" percolation 2025 Muirhead`
- `"random plane wave" "SLE" proof`
- `"Bogomolny" "Schmit" 2026 conformal`

Opened https://arxiv.org/abs/2010.11770 and
https://arxiv.org/html/2010.11770, and the article
https://link.springer.com/article/10.1007/s00440-025-01367-8.
Also opened Alex H. Barnett's RPW reference webpage to check for newer work.

Result: arXiv:2010.11770 (submitted October 2020, revised July 2023)
explicitly treats the random plane wave without FKG and proves critical
level zero. This materially corrects the supplied paragraph saying that the
available sharp-threshold work does not apply. It does not prove zero-level
RSW, Cardy's formula, or SLE(6). The 2025 article still describes critical
percolation of monochromatic waves as open.

Choice: use the substantial-advance branch of step 1, verify the exact
theorems, write SOLVED_ELSEWHERE.md and REPORT.md, then stop. This is an
omitted earlier advance, not a claim of a result first appearing after
November 2026. No independent new proof is claimed.

## 20:50–20:52 — theorem checks and attempt to falsify the update

Opened the original PDF https://arxiv.org/pdf/2010.11770 and read PDF
pages 4–5: Theorems 1.3 and 1.7 and Example 1.4. These explicitly name
the RPW, so application is not inferred merely from the abstract.
The publisher landing page returned only an iframe; the arXiv PDF was
available. Screenshot requests were also made for zero-based pages 3–4;
the substantive checks here use the PDF text returned by the web tool.

Checked the level convention a second way: write u = -l. Then l < 0
means u > 0 and {f >= u} is the small, bounded-component excursion.
When l > 0, u < 0 and the larger excursion has a unique unbounded
component. This agrees with monotonicity in l and the theorem statements.
All assertions here concern each fixed level, as in the paper.

Checked the numerical exponent by independently specializing (1.5),
rather than copying only its RPW corollary. The envelope
kappa_bar(r) = sup_{|x| >= r} |J0(|x|)| is O(r^(-1/2)). Thus
kappa_bar(sqrt(R)) <= C R^(-1/4), and its reciprocal is at least
C^(-1) R^(1/4). Since log R = o(R^(1/4)), the minimum of log R and
that reciprocal equals log R for sufficiently large R. The exponent
is therefore sqrt(log R), not log R or sqrt(R). Changing c1 absorbs
the bounded range of R. This independently reproduces Theorem 1.7's
displayed RPW specialization. It supplies no estimate uniform in l
as l approaches zero.

Looked for the missing case: l = 0 is excluded in both conclusions.
A critical parameter equal to zero does not establish the absence of an
unbounded component at zero, much less critical RSW or a conformal limit.
The later independent paper by Stephen Muirhead and Igor Wigman says
this explicitly after Proposition 1.7 and in Section 1.3.1. Its references
also independently confirm the 2023 publication, pages and author roles
of the earlier paper. The new article's publisher page gives online
publication in 2025 and volume/issue year 2026; both were preserved.

The arXiv HTML has a displayed date of August 24, 2026, whereas the
original PDF says July 18, 2023 and the version history says v3 was
submitted July 17, 2023. Used the submission history and PDF instead
of treating the HTML date as a new advance.

No computational data or new proof was produced. Created
SOLVED_ELSEWHERE.md and REPORT.md by apply_patch. The selected outcome
is a literature correction, not a solution of the scaling-limit problem.
The search and verification finished within the ten-minute allowance.

Exact shell read commands (no numerical computation):

```sh
pwd; rg --files -g 'AGENTS.md' -g 'MEMORY.md' -g 'LOG.md' -g 'REPORT.md' . ~/.claude 2>/dev/null | head -60
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/cat ~/.claude/projects/-Users-user/memory/MEMORY.md ~/.claude/compute/compute_state.json
env OMP_NUM_THREADS=1 nice -n 15 /bin/ls -la
```

Relevant outputs: correct working folder; startup memory index found;
governor `ok`/`owner_away_open`; initially only PROMPT.md, codex.log and
run.pid in the folder. The first discovery shell command did not have
the thread/priority prefix; subsequent explicit read commands did.
The priority-change warning is recorded above. No simulations ran.

## 20:51 — final artifact check

Ran `env OMP_NUM_THREADS=1 nice -n 15 /bin/cat REPORT.md SOLVED_ELSEWHERE.md`.
Exit code 0; the same priority warning appeared. Confirmed REPORT.md starts
with the required `VERDICT: PARTIAL` line, reference and theorem numbers
match the opened PDF, and both files distinguish noncritical results from
the unresolved scaling-limit conjecture. Stopped under step 1.
