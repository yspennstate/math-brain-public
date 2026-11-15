# T068 working log

Task: “take the NEXT checkable step on this problem, building on that work.” Received 15 November 2026, approximately 01:08 Asia/Tbilisi; first shell clock 01:09:09.

## 01:09 — orientation and earlier files

Read the earlier REPORT.md, LOG.md and SOLVED_ELSEWHERE.md in `~/codex_op_1114/briefs/T068`. Its directory has no PROOF.md and no Python, Sage or shell scripts. The file-list and existence checks establish this; there is no earlier computation to rerun. Read startup memory and the compute state: status `warn`, mode `owner_away_open`, CPU saturated and paging. No heavy computation is planned.

Commands: `pwd`; `rg --files` on both task directories; `cat` of the three earlier artifacts and compute state; `cat ~/.claude/brain_startup.md`; `sed -n '1,90p' ~/.claude/projects/-Users-user/memory/MEMORY.md`; `test -e <earlier>/PROOF.md`; `rg --files <earlier> -g '*.py' -g '*.sage' -g '*.sh'`; `date '+%H:%M:%S %Z'`. The proof/script checks returned no paths. An initial directory listing was unnecessarily broad; no files were changed by it.

The current folder-only rule excludes the global mesh, checklist, brain writes, and recall commands that auto-refresh their indexes. These were not run. No git and no subagents.

## 01:09 — bounded literature check

Web search queries: `"Karp" "clique" "2026" algorithm random graph`; `"Optimal Hardness of Online Algorithms for Large Independent Sets"`; `Karp clique random graph polynomial algorithm breakthrough November 2026`; `"2504.11450" "recourse" OR "revision" OR "deletion"`.

Opened the arXiv abstract and full HTML of David Gamarnik, Eren C. Kızıldağ, Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, https://arxiv.org/abs/2504.11450 and https://arxiv.org/html/2504.11450v2 . The latest version there is still v2, 30 January 2026. Read Definition 2.1, condition (1), and Theorem 2.2, including the explicit constants. Search has not identified a solution of the unrestricted problem. One hit concerns a faster worst-case k-clique algorithm; its bound must be checked before treating it as relevant. The search will stop within five minutes, rather than attempt an exhaustive absence claim.

## 01:10 — independent re-derivation of earlier result: holds

In G(n,1/2), complementing each independent fair bit again gives independent fair bits, and reversing every query answer simulates clique search by independent-set search with the identical adaptive vertex order, seed, and exceptional pair sets. With L=log₂(n/2), Theorem 2.2 gives (n/2)^(-ξL)=2^(-ξL²), where c=min{ε²,1}/8 and ξ=min{ε²,1}/64. The requested target (1+ε)log₂ n exceeds (1+ε)L, so its event is contained in the bounded event. The density interval contains 1/2 once n≥max(2d,2^d). An independent natural-log calculation gives log(probability bound)=−ξ[ln(n/2)]²/ln 2. Thus the earlier algebra and model restriction hold. This checks its deduction, not the entire cited OGP proof.

## Chosen extension — bounded deletions of accepted vertices

Extend the online model by allowing an algorithm to delete previously accepted vertices, with at most r distinct vertices ever deleted, while still admitting a vertex only at its own inspection round. Keep the same bound on exceptional queried pairs inside the final output. Plan: guess the inspection rounds of the ultimately deleted vertices, simulate the deletion algorithm while omitting those vertices, and enforce clique and query-budget guards on every execution. A union bound should cost only Σ_{j≤r} binom(n,j), extending the barrier to r=O(log n) with a sufficiently small coefficient, and in particular to r=o(log n). This is the single chosen extension. The central point to audit is whether the guards preserve the successful, correctly guessed trajectory while making all other trajectories satisfy the cited theorem.

## 01:11 — literature check closed; proof structure checked

Opened https://arxiv.org/abs/2611.09764 : Virginia Vassilevska Williams, Or Zamir, *The k-Clique hypothesis is dead, for good*, submitted 6 November 2026. Its abstract gives a worst-case running-time bound n^((ω/3−c)k), not a polynomial-time algorithm for logarithmic k. The displayed guarantee does not solve this random-graph problem. No general solution was found in the bounded search. Literature check ended at about 01:11, less than three minutes after the first shell clock and within the five-minute cap. No SOLVED_ELSEWHERE.md is appropriate for this session.

Read the cited paper's Sections 4–5, especially the use of irrevocability in Lemma 4.8: final outputs intersect the inspected prefix in exactly the stopping-time output. Deletions destroy that identity, so simply reusing that proof would be invalid. The simulation reduction avoids modifying its OGP argument. Web opens were at HTML lines 310, 338, 370, 420–475, 500, 540, 565, 610; the later opens were proof reading, not a continued search. The compute-state reread at 01:10:48 still reported CPU saturation; keep verification tiny and sequential.

## Proof saved — PROOF.md

Wrote the full reduction using a fixed family of guesses T for inspection rounds of accepted vertices absent from the final output. Each simulation maintains its own irrevocable clique K independently of B's state, checks the budget before executing a new exceptional query set, and checks clique/budget before accepting a vertex. On the event that the guess is correct and B's final budget is at most q, K is always a subset of B's final clique. Thus neither budget guard can fail and the outputs agree. Wrong guesses still produce valid q-restricted irrevocable algorithms. This proves an event-level inequality, even if B's deletion/query caps hold only on the event being bounded.

Bound obtained: P(success, |D|≤r, Q≤cL²) ≤ min(1, M(n,r) 2^(−ξL²)), with M(n,r)=Σ_{j=0}^r binom(n,j), L=log₂n−1, c=min(ε²,1)/8, ξ=min(ε²,1)/64. From M≤(r+1)n^r, any fixed r≤a log₂n with a<ξ retains a 2^(−(ξ−a−o(1))(log₂n)²) bound. The concrete a=ξ/2 gives r≤floor(min(ε²,1) log₂n/128).

Audit so far: a separate randomized-guess argument recovers exactly M(n,r), without conditioning the graph law on the correct guess. Natural-log conversion independently matches the exponent. The case of late admission is explicitly excluded; allowing it freely permits selecting a maximum clique after inspecting the full graph. Next, test the guards and adaptive order exhaustively on small graphs. One attempted append patch failed to match its context and made no change; the proof write succeeded.

## Finite verification — passed

Created `verify_reduction.py`, using only the Python standard library. It enumerates every graph on n=2,3,4,5, three deletion/query policies, two order rules (one depends on revealed graph information), every guessed deletion-round set of size at most two, and query budgets 0,1,3. It checks that every simulated output is a clique satisfying its query budget, and that the correct-guess simulation has the same transcript, final output, and exceptional union as B whenever B's final budget condition holds. It also checks the prefix invariant K=J∩V_t. All three protective guards are exercised by wrong guesses. These are finite implementation checks, not a proof of the cited asymptotic theorem.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_reduction.py`

Output (exit 0):

```text
nice: setpriority: Operation not permitted
nice=20; OMP_NUM_THREADS=1; no numerical-library imports
Exact combinatorial-count checks: 230; epsilon=1/2, c=1/32, xi=1/256
x=1024, r=2: log2 M=2047.000000, log2 probability upper bound=-2041.003906, crude exponent=-2038.418944
x=4096, r=8: log2 M=32752.700792, log2 probability upper bound=-32751.303114, crude exponent=-32732.833981
x=16384, r=32: log2 M=524170.336736, log2 probability upper bound=-524277.667170, crude exponent=-524154.959512
Exhaustive reduction checks: {'correct_guess_events': 3815, 'graphs': 1098, 'guarded_runs': 308736, 'nontrivial_correct_guess_events': 3485, 'original_runs': 6588}
Adversarial guard coverage: {'addition_budget_rejections': 51031, 'clique_guard_rejections': 374264, 'query_guard_stops': 7794}
PASS; elapsed=6.181s; peak_RSS=15302656 bytes
```

The `nice` launcher warned, but the script independently read the actual scheduling priority using `os.getpriority` before computation and found nice 20, lower priority than the required 15. Thus the computation complied. The script asserts OMP_NUM_THREADS=1, imports no threaded numerical library, has a 120-second CPU limit and 180-second enumeration deadline, and used about 15.3 MB RAM. No external writes, GPU, torch, MLX, git, or subprocess workers.

The combinatorial count is checked by two independent constructions: exact binomial coefficients and Pascal's recurrence. At large n, exact integer M agrees to 1e−8 in log₂ units with r log₂n−log₂(r!), and natural-log evaluation agrees with the base-two probability exponent. Additional hand checks: 1098=2+8+64+1024 graphs; 6588=1098·3·2 original runs; 308736=18·(2·4+8·7+64·11+1024·16) guarded runs. At x=1024, (x−1)²/256=4088.00390625 and log₂M≈2047, yielding −2041.00390625 as printed. This verifies sign, magnitude, shift, and the deletion coefficient independently.

## Self-audit: failure modes and scope

The original restriction on queried pairs inside the final output does not automatically hold for a wrongly guessed simulation: it may retain a vertex B later deletes. This is why a naive simulation without both budget checks is invalid. The finite check exercises 7794 query stops and 51031 admission-budget rejections, in addition to clique failures. The proof checks the budget before the query is made, so it never has to undo a forbidden query. The simulation uses its own B-state for adaptive choices, so rejecting a vertex in K does not change the simulated trajectory.

At r=0 the factor M is exactly one. At q=0 the pre-query guard still works, including exceptional sets containing pairs whose status is already known. At r=n the event bound is valid but may be vacuous after capping at 1. Immediate rejection of the current vertex does not require guessing it; counting it as an immediate deletion only enlarges D and leaves the proof valid. Randomized B is covered by sharing its independent seed with each A_T; no graph distribution is conditioned on the realized deletion set.

Free late admission falls outside the theorem, as does free readmission of previously deleted vertices. With arbitrary late admission, full inspection followed by exact maximum-clique selection is an obstruction even at zero exceptional budget; the reduction cannot cover it. The general polynomial-time conjecture remains unresolved. Priority of this elementary reduction in the literature has not been established; the result is new relative to the earlier task report.

## 01:17 — report and final audit

Created REPORT.md with first line `VERDICT: PROVED online clique barrier with bounded deletions`. Read back the complete proof and report, checked the explicit r coefficient ξ/2=min(ε²,1)/128, and checked the exact exponent expansion −ξ(x−1)²+ax²=−(ξ−a)x²+2ξx−ξ. Corrected an imprecise description of the unrelated worst-case k-clique running time to its actual displayed expression n^((ω/3−c)k). Used the first recorded clock (01:09) on the final task line because the exact receipt timestamp is unavailable. No further computation was needed after the verification passed.

Readback command: `wc -l REPORT.md PROOF.md LOG.md verify_reduction.py; sed -n '1,200p' REPORT.md; tail -n 15 LOG.md; date '+%Y-%m-%d %H:%M:%S %Z'`. Exit 0. At readback the four authored files were present (31, 185, 71, 208 lines respectively before the final prose corrections and this log entry). The clock read 2026-11-15 01:16:36 Asia/Tbilisi. All authored files are inside the current task folder; earlier work was read only. The new result is the bounded-deletion reduction, not a resolution of unrestricted T068.
