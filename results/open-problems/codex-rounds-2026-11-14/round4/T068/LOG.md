# T068 working log

Task: “take the NEXT checkable step on this problem, building on that work.” Received 15 November 2026, first recorded clock 04:33:47 Asia/Tbilisi (00:33:47 UTC).

## Orientation and literature check

Read the startup memory and compute governor state, and both earlier REPORT.md and LOG.md files. The first folder has SOLVED_ELSEWHERE.md in place of PROOF.md and has no scripts. Read that file too. The current folder-only instruction overrides the earlier requests to mutate the global mesh, checklist, and brain. No such commands will be run; the earlier log records that even brain recall attempts an external background write. No git or subagents.

Governor: status warn, mode owner_away_open, 63 percent free memory. Only short single-threaded standard-library computations are planned. All subsequent shell commands use OMP_NUM_THREADS=1 and nice -n 15. The launcher warns that setpriority is not permitted; computation will verify actual inherited priority before running.

Literature search began at 00:33 UTC. Queries: “Karp random graph clique online algorithms log n Gamarnik Kızıldağ Warnke 2026”; “2504.11450 clique online”; “random graph clique finding Karp problem solved 2026”. Opened https://arxiv.org/abs/2504.11450 and https://arxiv.org/html/2504.11450v2 . The abstract still lists v2, 30 January 2026. Search surfaced a related October 2026 induced-matching paper, not a solution to the clique problem. Source checking continues within the five-minute limit.

## 04:34 — literature check closed; earlier work read

Opened the arXiv pages for Abhishek Dhawan, Eren C. Kızıldağ, Neeladri Maitra, Cheng Mao, Timothy L. H. Wee, *Half-Optimal Induced Matchings in Random Graphs: Online and Low-Degree Algorithms*, https://arxiv.org/abs/2610.40369 (29 October 2026), and Virginia Vassilevska Williams, Or Zamir, *The k-Clique hypothesis is dead, for good*, https://arxiv.org/abs/2611.09764 (6 November 2026). The former concerns induced matchings; the latter's stated worst-case running time has exponent proportional to k. Neither stated guarantee solves this problem. No unrestricted solution found in the bounded search, which closed within one minute of the first clock. This is not an exhaustive absence certificate. No SOLVED_ELSEWHERE.md is warranted.

Read the full round-3 PROOF.md, LOG.md, and verify_reduction.py. The first folder has no PROOF.md or computation scripts, as its own report and round-3 file checks also record. The round-3 reduction preserves a private simulation of B, so acceptance in the separate output need not affect B's later inspection/query choices. Its three guards make each wrong guess satisfy the external theorem. On the correct guess D, every retained output vertex lies in J; therefore no guard fires, and the output equals J. This independently re-derives the main reduction, including its event-level rather than unconditional budget requirement. Complementation gives L=log₂n−1, c=min(ε²,1)/8, ξ=c/8, and (n/2)^(-ξL)=2^(-ξL²). The asymptotic loss follows from log₂ M≤r log₂n+log₂(r+1). No error found.

Started the earlier verification read-only with `OMP_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/T068/verify_reduction.py`. The -B flag prevents bytecode writes in the earlier folder.

## Chosen extension — bounded final late admissions, with arbitrary intervening revisions

Allow arbitrary clique updates among inspected vertices, including rejection followed by admission and deletion followed by readmission. For each v_t, record only its membership in C_t immediately after its inspection round. Let P={v_t:v_t∈C_t}, J=C_n, D={t:v_t∈P\\J}, and R=J\\P. Guess D and retain the irrevocable core J∩P. The expected reduction loses |R| vertices from the target but incurs no guessing factor for R. The private simulation can carry all late admissions, even arbitrarily many temporary ones. The correct-guess invariant becomes K_t=(J∩P)∩V_t. This directly addresses the prior report's next step, with a stronger count based on final disagreement rather than all revision operations.

Plan: prove P(|J|−|R|≥(1+η)L, |D|≤r, |E∩pairs(J)|≤c_η L²)≤M(n,r)2^(−ξ_η L²), for any fixed η>0. Then translate to target (1+ε)log₂n with at most βlog₂n final late admissions, η=ε−β>0. Audit using independent bit-mask enumeration on small graphs, including readmissions, multiple old admissions in one round, adaptive order, and wrong-guess guard failures. This is the one chosen extension.

## Earlier verification output — passed

The read-only rerun exited 0:

```text
nice=20; OMP_NUM_THREADS=1; no numerical-library imports
Exact combinatorial-count checks: 230; epsilon=1/2, c=1/32, xi=1/256
x=1024, r=2: log2 M=2047.000000, log2 probability upper bound=-2041.003906, crude exponent=-2038.418944
x=4096, r=8: log2 M=32752.700792, log2 probability upper bound=-32751.303114, crude exponent=-32732.833981
x=16384, r=32: log2 M=524170.336736, log2 probability upper bound=-524277.667170, crude exponent=-524154.959512
Exhaustive reduction checks: {'correct_guess_events': 3815, 'graphs': 1098, 'guarded_runs': 308736, 'nontrivial_correct_guess_events': 3485, 'original_runs': 6588}
Adversarial guard coverage: {'addition_budget_rejections': 51031, 'clique_guard_rejections': 374264, 'query_guard_stops': 7794}
PASS; elapsed=5.975s; peak_RSS=15351808 bytes
```

These counts agree with the earlier log. Together with the independent re-derivation above, the earlier result holds. The underlying OGP theorem is still an external theorem, not independently proved here.

## Proof saved; independent verification started

Wrote PROOF.md with the general event inequality and the explicit two-budget consequence. For fixed β<ε, use η=ε−β, at most βx final late vertices, and at most ax on-inspection acceptances absent from J, where a<ξ_η. The bound is 2^(−(ξ_η−a−o(1))x²). Choosing β=ε/2 and h=min(ε²/4,1) gives late cap floor(εx/2), deletion-disagreement cap floor(hx/128), exceptional cap hL²/8, and exponent −(h/128−o(1))x². No identities of late vertices are guessed. Arbitrarily many transient late admissions/readmissions are allowed.

Created verify_revision.py as an independent bit-mask implementation, rather than modifying the earlier script. It enumerates every legal clique trajectory on every graph of order at most four, and separately tests information-dependent inspection order and exceptional-query choices. The original process is rerun from the same seed for each guess, so transcript equality is checked rather than assumed by replay. Every fixed clique schedule is made a valid algorithm on other graphs by checking its proposals against known answers. Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_revision.py`. Initial output confirms nice 20 and OMP_NUM_THREADS=1; result pending.

## 04:38 — revision verification passed

Command `OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_revision.py` exited 0. Complete substantive output:

```text
nice=20; OMP_NUM_THREADS=1; CPU limit=120s
Exact counting cases=90; epsilon=1/2, beta=1/4, eta=1/4, c=1/128, xi=1/1024, a=1/2048
x=4096, r=2, s=1024, core_target=5120: log2M=8191.000000000, exponent=-8185.000976562, crude=-8182.416014062
x=8192, r=4, s=2048, core_target=10240: log2M=32763.415037499, exponent=-32756.585939063, crude=-32749.679048468
All-trajectory audit: {'correct_guess_events': 23112, 'exhaustive_graphs': 75, 'exhaustive_trajectories': 23112, 'guarded_runs': 367036, 'late_operations': 29281, 'mixed_correct_events': 2828, 'multiple_old_admissions': 2834, 'original_runs': 23112, 'readmissions': 8062}
Combined audit: {'adaptive_test_graphs': 106, 'correct_guess_events': 26405, 'exhaustive_graphs': 75, 'exhaustive_trajectories': 23112, 'guarded_runs': 468796, 'late_operations': 31027, 'mixed_correct_events': 3012, 'multiple_old_admissions': 3187, 'original_runs': 24808, 'readmissions': 8579}
Guards: {'budget_reject': 9593, 'clique_reject': 56599, 'query_stop': 2804}
PASS; elapsed=3.709s; peak_RSS=15073280 bytes
```

The all-trajectory part covers every graph on 1–4 vertices, every legal clique sequence at fixed inspection order, every guess T⊆[n], and zero exceptional queries. The second part covers all graphs on 2–4 vertices and 32 deterministic graphs on 5 vertices; four revision policies, two query policies, two order rules, every guess, and budgets 0,1,3. The 26,405 correct-guess/budget events preserve the entire private transcript and output exactly J∩P. There are 3,012 such events with all of core, R, and D nonempty. Counts of late operations and readmissions describe test coverage, not theorem parameters. All guards fire on wrong guesses. The output-size identity and numerical exponent are checked separately. These are finite checks of the reduction; they do not establish the external asymptotic theorem by experiment.

## Independent second counts and edge-case audit

Created audit_counts.py to sum over schedules first instead of graphs: each schedule forces a union U of clique pairs, and the number of compatible graphs is exactly 2^(binom(n,2)−|U|). This independently reproduces 23,112 legal graph/trajectory pairs and 367,036 guarded runs. Including the adaptive cases gives 24,808 original and 468,796 guarded runs, agreeing exactly with verify_revision.py. Exact rational arithmetic rechecks the exponent expansion and coefficients. A separate set-based calculation checks explicit histories with readmission but zero final disagreement, nonempty core/D/R together, and several old vertices added at the final update. During readback, two initial witness histories did not illustrate their comments; strengthened those fixtures and reran the tiny audit. No theorem or main verification change was needed.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_counts.py`. Final run exited 0:

```text
n=1: legal graph/trajectory pairs=2, guarded=4
n=2: legal graph/trajectory pairs=14, guarded=56
n=3: legal graph/trajectory pairs=320, guarded=2560
n=4: legal graph/trajectory pairs=22776, guarded=364416
Independent totals: original=24808, guarded=468796
Witness: core=[0, 1, 3], D=[], R=[]
Witness: core=[2, 4], D=[1, 3], R=[0]
Witness: core=[3], D=[], R=[0, 1, 2]
Exact exponent components x=4096: negative_quadratic=-16769025/1024, r*x=8192, leading_coefficient=1/2048
Exact exponent components x=8192: negative_quadratic=-67092481/1024, r*x=32768, leading_coefficient=1/2048
PASS; nice=20; elapsed=0.001s; peak_RSS=14499840 bytes
```

## Self-audit and report

Checked the omitted cases: vertices rejected at inspection but finally retained are exactly R; vertices accepted at inspection and finally absent are exactly D; accepted/deleted/readmitted final vertices stay in the core; transient late additions absent at the end belong to neither count. Old-vertex updates can be simultaneous and need not preserve membership in K, since B has its own private state. Budget guards operate before irreversible queries, including repeated queries of already-known pairs. The theorem works at r=0 and q=0 and becomes possibly vacuous at r=n. The family of guesses is fixed independently of graph and seed, so the union bound does not condition the input distribution. Correctness of the core induction uses final J, not the intermediate cliques.

Checked coefficients independently: h=min{(ε/2)²,1}, c=h/8, ξ=h/64, a=ξ/2=h/128, and ξ−a=h/128. At ε=1/2 these are 1/128, 1/1024, and 1/2048 for c, ξ, and a. At x=4096, the quadratic cost is 16769025/1024=16376.0009765625 while log₂M≈8191, yielding −8185.0009765625. The sign and magnitude agree with both scripts. The query coefficient is evaluated at η=ε−β; retaining the original larger ε-budget without justification would be a mistake, and the report states this tradeoff explicitly.

Created REPORT.md with the required first-line verdict, exact event inequality, new scope, commands, uncertainty, failure example, and next step. No edits outside this folder, no git, no external writes, and no subagents. All mathematical computation stayed far below 1 GB, single-threaded, nice 20, and under six seconds per run. The shell nice warning is recorded but does not indicate a priority violation.

Final readback: `OMP_NUM_THREADS=1 nice -n 15 /bin/cat REPORT.md PROOF.md`, exit 0. Rechecked the theorem quantifiers, the induction's three membership cases, and all displayed coefficients. Clarified 0≤β<ε and 0≤a<ξ_η in the report, and described the query cap as possibly decreasing (it is constant while η≥1). The final authored artifacts are REPORT.md, PROOF.md, LOG.md, verify_revision.py, and audit_counts.py. No required work remains for this chosen extension.
