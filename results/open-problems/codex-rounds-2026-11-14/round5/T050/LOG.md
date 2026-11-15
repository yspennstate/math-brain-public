# T050 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded clock: 2026-11-15 03:41:24 UTC, 07:41:24 Asia/Tbilisi.

## Orientation and literature update

Read the startup memory, compute governor state, mesh protocol, and all three
prior REPORT.md and LOG.md files. File enumeration finds no research scripts
in the prior folders, and no PROOF.md in the original folder. Round 3 and
round 4 have PROOF.md files; their mathematical read and recheck follow.
The current task's folder-only rule precludes shared mesh, checklist, recall
logging and memory mutations. None are made. No git or subagents.

Shell reads use `env OMP_NUM_THREADS=1 nice -n 15 <command>`.
The sandbox prints `nice: setpriority: Operation not permitted` and completes
the reads. A successful priority change is not claimed. Governor status is
warn, mode owner_away_open, CPU saturated; no heavy computation is planned.

Web search queries:
- `"strict convexity" "first passage" 2026 2025 exponential`
- `"Strict convexity and differentiability" "exponential" September 2026`

Opened the manuscript landing page and the primary scope note:
https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/
https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/212.md

These still identify OpenAI as author and September 24, 2026 as manuscript
date. The scope note excludes strict convexity from its selected Lean
statements. The landing page says nobody has checked that the Lean statements
match the paper. No verified solution of the full continuous-law problem was
located. Close the bounded update search here, within five minutes. Further
source access is for the mathematical audit. Direct PDF open failed with an
internal access error; try the landing page's linked PDF.

Commands so far: `pwd`; `cat` of the startup/compute files and mesh protocol;
`rg --files` on all four T050 folders; `cat` of the prior reports and logs
and original SOLVED_ELSEWHERE.md. Every shell command used the env/nice
wrapper above. Prior folders are read only.

Next: independently rederive round 4's finite-cell lemma, then record one
extension before attempting it. The intended candidate is the passage from
individual anchor errors to simultaneous envelopes in Lemma 10.4.

## Prior result independently rechecked: holds

Read round 3's complete PROOF.md and round 4's complete PROOF.md with
`env OMP_NUM_THREADS=1 nice -n 15 cat <absolute path>`.
No missing scripts exist. The round-4 finite-cell statement holds under its
stated assumptions. Independent derivation: expand each conditional
expectation into coordinate averaging and centering operators. For a local
comparison on A, only components S contained in A survive; summing them
recovers its centered part. In the difference of the two gauges, the shared
components apply to W-E, and components present at only one endpoint lie
on the cutoff boundary. A boundary path first keeps an extreme coordinate
fixed, changes a second coordinate, then goes to the eastern reference.
Its worst length is `(d+3)R+1`, and one label change gives J. Its distance
from S is at least `R-2H=H+1`, so each local support misses S. Thus the
boundary error is `J 2^m epsilon`; the centered remainder is at most
`2 epsilon`. At most 2N components gives exactly `2+2NJ2^m`. The union
of component supports is within `R+2H=5H+1`. This derivation uses finite
operators, without an infinite expansion or a supremum over labels.
The d=1 sign example also checks: correlation with a middle independent
sign is 0 for local endpoint gauges and 1 for the required telescoped sum.

The literature-update search is closed. Clicking link 8 on the landing
page opened the 95-page PDF. Mathematical source reads: Lemmas 10.2 and
10.4, Section 10.3, and Sections 15.6–15.7 for scope. Author: OpenAI;
title and date as above; no arXiv identifier verified.

## One chosen extension, before its proof

Prove an explicit simultaneous-envelope theorem from finite anchor increment
errors, covering all occurrences, switches and physical competitors in fixed
windows. This is the next step round 4 names (Lemma 10.4). Retain the number
of periods and the length of the anchor comparison tree in the constant.
The aim is to prove that no factor for microscopic occurrence count is
needed, while making clear which factors can grow if new road labels are
added. Also test whether a label-independent estimate is possible from
these assumptions. This is one extension of the finite-cell result; the
later contraction and its parameter ordering are outside the claimed proof.

## Simultaneous-envelope theorem saved

Wrote PROOF.md with a finite-window theorem and full measurability argument.
Let p be the total number of periods, q the number of edges of a deterministic
tree comparing the starting anchors, and let c beta bound each anchor
increment error. The explicit comparison variable is

    B = sum_periods (D_i+|C_i|) + sum_tree |e_uv|,
    E B <= [2p+c(p+q)] beta.

The key pathwise estimate is total variation of h=g-P on period i at most
`D_i+|C_i|`: both its cumulative defect and its nominal parameter are
nondecreasing. Any two occurrences can be joined through their road starts
and the anchor tree using each relevant period and tree edge at most once.
Consequently every h difference is bounded by B. This supplies simultaneous
switch estimates, without summing over attachment occurrences.

The observable envelope for at most K switches has expectation at most
`(2K+1) E B`. The lower envelope for physical competitors, with two signed
center adjustments, has expectation at most `3 E B`. These observables use
only window records/gauges and, for competitors, the prescribed finite graph.
The nonlocal potential and anchor comparisons enter only their estimates.

Also proved a finite-window example showing linear growth in label count can
be necessary from the increment assumptions alone: one uniform categorical
input J gives gauges `g_a=beta(m 1_{J=a}-1)`. Each pairwise error has mean
at most 2 beta, whereas the maximum switch difference among m labels is
exactly m beta. This does not attack the canonical FPP gauge construction;
it excludes silently removing label count from the estimate just proved.

No executable computation or numerical experiment was needed. All constants
are exact symbolic counts. The single extension remains the envelope step;
no new result on later contraction parameters is claimed.

## Adversarial checks

Re-derived interpolation independently as
`h(t)=(1-theta)h_i+theta h_(i+1)+F(t)-theta D_i`,
where F is cumulative defect and `0<=F<=D_i`. This confirms the signs and
the separation of anchor error from within-period oscillation. Directly
`D_i+|D_i-e_i| <= 2D_i+|e_i|` confirms the coefficient 2 and the p+q error
count in the expectation. Independently counted K+1 legs and K switches,
giving 2K+1; one competitor and two arms gives 3.

Tested repeated visits and nominal pauses: order is the occurrence order,
not order of physical vertices or strict nominal parameters. Tested K=0,
empty intersection/path families, disconnected comparison subgraphs,
interior endpoints, shared physical vertices, arbitrary selected centers,
and the zero-error case. No supremum of a common additive calibration
offset is used. A common offset can have arbitrarily large first moment
while all relevant differences vanish.

For measurability of switch suprema, independently used a distance penalty
on the compact product of traversal intervals, followed by countable rational
suprema. For physical competitors, replaced all paths by the graph distance
and minimized a continuous objective over finitely many compact edge-piece
pairs. Thus arbitrarily many candidate paths require no union bound.

Checked the categorical example a second way by listing the exceptional
label and the m-1 others: root errors have expectation
`2(m-1) beta/m`, pairwise errors are `2 beta`, and the actual label-to-label
maximum is `m beta` on every outcome. The reference-gauge maximum is
`(m-1) beta`. Distinguished these two maxima explicitly in PROOF.md.

Strengthened this stress test to avoid zero-length windows: all labels follow
the same out-and-back traversal of one edge of weight beta/2, so period
Q and D are beta. Nominal time proportional to cost makes the interpolated
gauge constant. The same pairwise errors and simultaneous maximum hold.
This example satisfies the stated positive-edge finite-window hypotheses;
it is not claimed to satisfy the global admissible-road geometry of FPP.

## Final inspection and handoff

Re-read round 4's REPORT.md and LOG.md in a separate bounded read to ensure
that the earlier aggregate tool output had hidden no content. Re-read the
current full PROOF.md and LOG.md, then REPORT.md and the revised example.
Commands:

```sh
env OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md LOG.md
env OMP_NUM_THREADS=1 nice -n 15 cat ~/codex_op_1114r4/briefs/T050/REPORT.md ~/codex_op_1114r4/briefs/T050/LOG.md
env OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md
env OMP_NUM_THREADS=1 nice -n 15 rg --files .
env OMP_NUM_THREADS=1 nice -n 15 sed -n '285,380p' PROOF.md
```

All exited 0 with the previously recorded priority diagnostic. REPORT.md has
the required PARTIAL verdict on its first line. The file list contains the
three deliverables LOG.md, PROOF.md and REPORT.md plus the pre-existing
runtime/prompt files. No script or numerical output is claimed. Final
inspection clock: 03:47:34 UTC. Clarified that a switch counts an occurrence
transfer even when two records have the same road label. Added the exact
scope-note link to REPORT.md and made a line-wrap-only proof edit afterward.

No error was found in the prior finite-cell result or the fixed-window
envelope step. The unresolved next check is uniformity of p, q, c, K and
the actual input supports in the phase-dependent construction. No
SOLVED_ELSEWHERE.md is appropriate for the full problem on this evidence.
