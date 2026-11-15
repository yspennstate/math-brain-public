# T090 work log

Task: “push this problem forward by one checkable piece.” First recorded local clock: 2026-11-14 21:57:51 +04 (Asia/Tbilisi). The prompt receipt time is unavailable.

## Orientation and constraints

Read the local PROMPT.md, the available memory index, one relevant priority-setting memory, and the compute governor state. The governor reported `status: warn`, `mode: owner_away_open`, CPU 98.1%. No simulation or heavy computation is planned. All shell calls use `OMP_NUM_THREADS=1 nice -n 15`; the sandbox prints `nice: setpriority: Operation not permitted`. No effective priority change is claimed. Shell work has consisted of short reads. No git or subagents used.

The task-specific rule forbidding all writes outside this folder takes precedence over the global checklist, mesh, recall logging, and brain-writing instructions. Those state-writing utilities were not run. Read-only orientation used existing memory files instead.

## Step 1: bounded literature search

Search started approximately 21:57 +04. Web search tool queries included:

- `"KPZ" "2+1" rigorous exponents 2026 2025`
- `"2609.15832"`
- `"2412.10311"`
- `site.arxiv.org KPZ "strong" "2026" "two"`
- `site.arxiv.org "KPZ" "2025" "variance" "two-dimensional"`
- `site.arxiv.org "KPZ" "2026" "exponents" "two-dimensional"`
- `"Critical 2D KPZ Process"`
- `"two dimensional" "KPZ" "strong coupling" "2026" mathematical`

Opened primary sources:

- https://arxiv.org/abs/2609.15832
- https://arxiv.org/abs/2412.10311
- https://epubs.siam.org/doi/full/10.1137/25M1805643
- https://arxiv.org/abs/2610.31614

Output that matters: arXiv:2610.31614, submitted 22 October 2026, is titled *The Critical 2D KPZ Process*. Its abstract claims convergence of centered Gaussian-polymer log partition functions at criticality, a renormalized Cole–Hopf construction from the critical SHF, and non-Gaussianity. This is a substantial advance beyond the supplied list of critical-SHF results, although it is earlier than the supplied summary's broad “Nov 2026” label. It does not by its abstract settle fixed-coupling exponents.

Choice: follow the user's step-1 stopping branch if the paper's theorem statements confirm these claims. Read the primary paper, write SOLVED_ELSEWHERE.md and REPORT.md, and stop without a separate proof or computation. This avoids treating the existence of a critical random distribution as a theorem about fixed-coupling long-time height fluctuations.

## Step 2: theorem-level scope audit

Opened https://arxiv.org/html/2610.31614v1 and read equations (1.5)–(1.6), Theorem 1.2, Remark 1.3, Theorems 1.4 and 1.6, Proposition 1.5, and the beginning of Section 9. The abstract's non-Gaussianity claim is explicitly a theorem for flat initial data and nonzero nonnegative smooth compactly supported test functions. The convergence topology is local negative Sobolev space, for every positive Sobolev-loss parameter, jointly for finitely many positive times and bounded continuous initial conditions. This is not path-space convergence or a point-height theorem.

Important failed extension: Remark 1.3 only expects the corresponding noise-mollified KPZ approximation to converge and omits the technical adaptations. It must not be reported as covered by Theorem 1.2.

Independent scale check, by hand: equation (1.6) gives `exp(beta_N^2)-1 = (1 + theta/log N)/R_N`, while (1.5) gives `R_N ~ log N/pi`. Thus `beta_N^2 ~ pi/log N`, so the disorder tends to zero. Conversely, if `beta_N=b>0` is fixed, `(exp(b^2)-1) R_N` diverges, whereas the theorem requires it to tend to 1. This independently rules out applying the result at fixed polymer coupling. The approximate numerical growth exponents in the prompt were not re-estimated.

Chronology check: the identified paper is dated 22 October, not after November 2026. It is missing from the summary and later than the latest specifically identified September preprint. The report will call it an omitted substantial advance, not a post-November discovery or a solution of T090.

## Step 3: independent presentation check and stopping branch

Opened the 84-page primary PDF at https://arxiv.org/pdf/2610.31614. Its printed p. 6 confirms Theorem 1.2, p. 8 confirms Theorem 1.6, and p. 7 confirms the omitted noise-mollification adaptations. These agree with the HTML theorem statements. The PDF title page says 23 October while the arXiv submission record and HTML say 22 October; the bibliographic date reported is explicitly the submission date. Reading two formats checks transcription and scope, not the correctness of the entire proof.

Created SOLVED_ELSEWHERE.md and REPORT.md using `apply_patch`. The verdict is PARTIAL because the original fixed-coupling problem is not solved. No PROOF.md or data/script is appropriate for this literature-only stopping branch. All writes remained in T090. No external messages were sent.

## Final file check

Command: `OMP_NUM_THREADS=1 nice -n 15 sh -c 'head -1 REPORT.md; wc -c LOG.md SOLVED_ELSEWHERE.md REPORT.md; rg -n "VERDICT|Theorem|fixed|Next worker|Task:" REPORT.md SOLVED_ELSEWHERE.md'`.

Output confirmed the required first line `VERDICT: PARTIAL omitted critical-regime advance identified; fixed-coupling T090 remains open`, three nonempty artifacts, theorem references, fixed-coupling caveats, and the next-worker instruction. The shell again reported the sandbox's priority-setting restriction. Clock tool at completion preparation: 2026-11-14 17:59:55 UTC = 21:59:55 +04. Literature search and primary-source audit completed in under ten minutes.
