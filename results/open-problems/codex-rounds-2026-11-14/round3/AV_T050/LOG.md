# T050 continuation log

Task: “Verify: has open problem T050 been settled by the OpenAI math release?” Continuation started 15 November 2026, 00:51 +04.

## 1. Earlier work and resource limits

Read the earlier REPORT.md, LOG.md and VERIFY.md in `~/codex_op_1114/briefs/AV_T050`. PROOF.md is absent and there are no Python scripts there. The earlier result is a scope finding (planar exponential strict convexity claimed), followed by a limited algebra check of the scale contraction. The explicitly unchecked part is the upstream construction and uniformity assumptions (G)/(L).

Command: `OMP_NUM_THREADS=1 nice -n 15 python3` reading those files and `os.getpriority`. Output: inherited nice = 20; the attempted nice 15 reports permission denied because the process is already at lower priority. Only small file reads were run. Global mesh/checklist/brain writes are excluded by the task's instruction to write only here; no subagents or git.

Web search begun immediately: exact convexity title; `openai/math first-passage error`; `strict convexity first-passage percolation 2026 arxiv`. Results include the same manuscript and the already-known Armstrong–Bou-Rabee citation; no new resolution established. Search results alone are not treated as source evidence.

## 2. Brief update search; choice of extension

Opened current primary introduction, manuscript README, repository history, and `lean/docs/212.md`. Also opened the arXiv abstract and HTML of Scott Armstrong and Ahmed Bou-Rabee, *Fluctuation bounds for rotationally invariant first-passage percolation*, arXiv:2610.42124v1. These reproduce the earlier picture: the exponential planar theorem is still claimed; strict convexity remains outside the selected Lean statements; repository history has no listed repair or withdrawal for it. Read-only GitHub issue search `repo:openai/math "first-passage"` returns an empty list. Exact-title searches with error/correction/refutation/November, and arXiv/general November searches, located no new solution or substantive proof review. This bounded search ended within five minutes of starting; absence in a search is not evidence of universal absence.

Independent scope check: opened the current introduction rather than relying on the prior report. It specifies unoriented nearest-neighbor edges on Z² and exponential weights of a fixed rate. The displayed strict-convexity assertion is exactly for the time-constant unit ball. All positive rates reduce to rate one by multiplying every edge by 1/lambda, which rescales the ball by lambda. For d=2, the minimum of four rate-lambda exponentials is rate 4lambda, so its second moment is 2/(4lambda)^2 < infinity. This is genuinely a special case of our row, with no quantifier over other continuous laws or d>=3. The earlier main scope finding holds.

Choice, before the extension: inspect the finite-cell/local-gauge step underlying input (G), especially its claimed bounds independent of s and the road rule. The previous worker explicitly left this unchecked, while the final contraction needs its constants before choosing s. Read the current primary `strict/foundations.tex` through the GitHub connector and the earlier saved copy. No heavy computation, Lean build, or numerical simulation is planned.

## 3. Primary-source comparison and selected lemma

Reopened the exact introduction TeX files for all three candidates via the read-only GitHub connector; all are readable. Saved the current foundations source as `strict-foundations-current.tex`. Small Python comparison reports byte-identical foundations source to the earlier worker's file: SHA256 `2b4099ac2502613172cba97cd1cd8c842f7ffab33678fa9fee7fa1e013792ba4`. Copied the earlier verification and its 15 supporting evidence files here so that its local links remain reviewable; the earlier folder is untouched.

Read foundations lines 528–875 and 952–1100, including the comparison network, finite-cell lemma, interpolation, envelopes, and common-world gauges. Narrowed this session's extension to the finite-cell lemma alone (`found:lem-finite-cell`). Its proof appears to work under its stated independent-cell hypotheses. The next deliverable will supply full details and an explicit uniform error constant, with a separate check of the boundary detour and finite-product projection identities. This does not validate the comparison-network application or all of input (G).

## 4. Quantitative proof written

Wrote PROOF.md with a complete derivation of the abstract finite-cell lemma, using the manuscript's gauge formula. An explicit admissible bound is `C_H = 2 + 2 N_H B_H 2^m`, with `R=8H+20`, `m=(2H+1)^2`, `N_H=(2R+1)^2 2^((4H+1)^2)`, and `B_H=4R+4H+11`. The boundary detour uses the shorter arc on a square of perimeter 8R and a straight eastward tail, giving B_H rather than the manuscript's looser path bound. The union, not the sum with the intersection counted twice, bounds the number of component errors by 2N_H. For H=2, two substitutions give `C_2=2+1737254*2^106`.

Wrote check_local_potential.py for an independent graph-distance calculation and exact rational finite-product identities. It uses one standard-library Python process, enforces a 768 MiB data limit and 60 CPU-second limit, and requires inherited nice>=15 and OMP_NUM_THREADS=1. Started command: `OMP_NUM_THREADS=1 nice -n 15 python3 check_local_potential.py`.

First script launch exited before the checks: `setrlimit(RLIMIT_DATA, ...)` raised `ValueError: current limit exceeds maximum limit`. Inspecting inherited limits before adjusting the resource guard; no mathematical output or result was produced by that launch.

## 5. Independent checks passed; report saved

Inherited limits print as infinity, but macOS rejects lowering RLIMIT_DATA even when both limits are supplied. RLIMIT_CPU can be lowered. Updated the script to handle that platform failure, retain a 60 CPU-second cap, use fixed small state spaces, and report peak resident memory.

Reran `OMP_NUM_THREADS=1 nice -n 15 python3 check_local_potential.py`; exit 0. Breadth-first search for H=2,3,5,10,20 gave maximum boundary detours 162,198,270,450,810, respectively, matching `4R+4H+10`; the enlarged local supports miss every possible S in Q_(2H). Exact rational arithmetic checked all 16 atom-basis functions of a biased four-cell product for the decomposition, zero means, and L1 projection bounds. All 2,800 support-cancellation checks passed. Two computations agree on `C_2 = 140942788854329116202736232342545760258 = 2+1737254*2^106`. Runtime 4.279 seconds; peak RSS 15.09 MiB. The finite tests supplement the general argument in PROOF.md.

Saved REPORT.md using the continuation's required PROVED verdict for the abstract lemma, while explicitly preserving PARTIAL-CLAIMED for the literature question. The FPP hypothesis verification is not included in the proved result. Recommended next check is the common-world gauge lemma and its admissibility/independence assumptions.

## 6. Source refresh and attempted falsification

Saved current-source-audit.json with fresh connector responses and URLs for the three introductions, scope note and history. Every quoted theorem still exactly occurs in the current primary source. Raw file equality initially printed False for those five files; a second comparison with unified diffs showed that the sole difference in each is one terminal blank line. All match after rstrip. The foundations source is exactly byte-identical, not just whitespace-equivalent.

Rechecked the proof against nonlocal individual potentials, random common offsets, nonzero means, same-index changes, arbitrary label sets, boundary corners, and the distinction between increment and absolute errors. No counterexample was found under the abstract lemma's hypotheses. The identity for the centered error was derived directly as `-(delta-E delta)` to check its sign; the component count is the union of the two active sets and is at most 2N_H. Wrote these limits into PROOF.md and the continuation spot check in VERIFY.md. No FPP proof-correctness conclusion is drawn.

Updated VERIFY.md with the independent exponential-rate/moment calculation, the current lemma result, the brief follow-up search, and explicit provenance of inherited follow-up records. Recommended replacement remains three sentences and states only partial coverage by the named September 24 preprint.

## 7. Final audit — 00:58 +04

Ran a small read-only Python audit under OMP_NUM_THREADS=1 and nice 15 (inherited nice 20). PASS: required files exist; REPORT has the continuation's PROVED first line; all four theorem quotations exactly match refreshed primary sources; all five refreshed evidence files match apart from terminal blank lines; foundations files match byte for byte; replacement status has three sentences; all 14 local Markdown links outside code resolve; PROOF explicitly excludes verification of the FPP application. Audit peak RSS 16.59 MiB. No further tests were needed.

Completed REPORT.md, VERIFY.md, PROOF.md, check_local_potential.py and source evidence. Literature result remains PARTIAL-CLAIMED; the new proved item is only the abstract finite-cell lemma under its hypotheses. No git, push, posts, accounts, external messages, Lean builds, subagents or intentional writes outside this folder.

Task: “Verify: has open problem T050 been settled by the OpenAI math release?” — continuation received 15 November 2026, 00:51 +04.
