# T116 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Start: November 15, 2026, 04:54 Asia/Tbilisi.

## Startup and earlier-result recheck

Read REPORT.md, LOG.md, SOLVED_ELSEWHERE.md in both earlier folders, and the round 3 AUDIT.md, in full. Neither earlier folder has PROOF.md or research scripts. Their result is a literature finding and statement audit, not a construction or computation.

Read startup memory index and compute state directly. State: warn, owner_away_open, CPU saturated. The task-specific restriction forbids writes outside this folder, so no shared-brain, mesh, or checklist mutations or logging recall commands are used. No subagents, git, external messages, or heavy computation.

Commands: tiny pathlib reads under `OMP_NUM_THREADS=1 nice -n 15 python3 -B`. The wrapper warns `setpriority: Operation not permitted`; an initial call to os.nice(0) failed before reading the files. Repeated the reads without os.nice. This failure does not concern any mathematical result. Use os.getpriority for the final priority check.

Independent algebraic recheck, conditional on the stated theorem: take any fixed deletion probability 0<q<1, fixed success 2/3, and c=1/(8 log 2). For any fixed A>0, the ratio of the claimed lower bound to n^A is exp((c log(q^3 log n)-A) log n). Its exponent tends to infinity because log(q^3 log n)=log log n+3 log q. Thus the earlier fixed-q consequence holds. A second check writes L=log n: log(lower bound)=c L log L+3c L log q, whose ratio to L diverges. This rules out polynomial sample complexity if the preprint theorem is valid; it does not certify that theorem.

Next: bounded web search for later changes and opening the primary introduction and formalization note. If the reported resolution is confirmed, obey the literature-stop instruction. A narrow dependency-assumption audit, if immediately accessible, would extend the previous statement audit without claiming formal verification.

## Literature check and stop decision (04:55–04:56)

Web searches: `"Quantitative lower bounds for trace reconstruction"`; `"trace reconstruction" "November" "2026" lower bound polynomial`. No later result changing the remaining order gap found in this bounded search.

Opened primary sources with the web tool:
- https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/main.tex
- https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/introduction.tex
- https://raw.githubusercontent.com/openai/math/main/lean/docs/122.md
- https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/TraceReconstruction.lean

The header identifies author OpenAI, date September 24, 2026. The complete-trace model, unrestricted estimator, quantitative exponent and fixed-success quantifiers match the earlier report. The three comparator theorem bodies still contain sorry. The earlier result holds as a report of the preprint and its algebraic consequence; the proof remains uncertified here.

Choice of additional check: inspect the release's own description and directory for implementation availability. This directly addresses the earlier report's proposed next step: a checker run cannot certify unavailable proofs. This is a narrow source-availability check within the literature branch, not a separate research extension. Stop after documenting it.

Effective nice independently queried with os.getpriority(os.PRIO_PROCESS,0): 20. No numerical computation or Lean build run.

## Additional source-availability audit and final checks

Opened the release README, lean/README.md, the manuscript README, lean/ComparatorChallenges/README.md, lean/formalization.yaml, lean/ComparatorChallenges/TraceReconstruction.json, and lean/OAI/Probability/TraceReconstruction.lean using the web tool, all under https://raw.githubusercontent.com/openai/math/main/.

The connected GitHub tool's read-only directory request https://api.github.com/repos/openai/math/contents/lean returned only an action-completed response to the text extractor; it supplied no useful directory evidence. Switched to explicit raw files. Web finds in formalization.yaml for TraceReconstruction and Quantitative lower found no matches; this is not evidence that a solution is absent. The actual JSON names the separate solution module, and opening that module succeeds.

New evidence: the comparison configuration allows only propext, Quot.sound, Classical.choice, disables nanoda, and lists the three target theorems. The solution imports Induction and Testing and supplies proof bodies. These are static observations only. No inference of checker success is made. AUDIT.md records the entry point and limits. The main-branch sources were not pinned to a commit.

Self-checks: fixed q is the deletion rate, q^3 log n diverges, and positive success 2/3 is covered. The coefficient c=1/(8 log 2) lies strictly inside the stated interval. A high-probability estimator would satisfy fixed success 2/3 eventually. Neither endpoint q=0 or q=1 is included, and rapidly vanishing deletion rates are not covered by the fixed-channel inference. The asymptotic lower-bound exponent is not a matching order. The original two reports are unchanged.

Files written: LOG.md, AUDIT.md, SOLVED_ELSEWHERE.md, REPORT.md. No PROOF.md is supplied because no new proof was attempted under the stop branch.

Final audit command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B - <<'PY'` with pathlib nonempty-file assertions, required-verdict assertion, audit-limit assertion, and os.getpriority. Output: LOG.md 5519 bytes; AUDIT.md 1897 bytes; SOLVED_ELSEWHERE.md 1687 bytes; REPORT.md 2248 bytes; File audit: PASS; Effective nice: 20; clock 2026-11-15T04:56:26.648687+04:00. Byte count for LOG.md precedes this appended entry. Stop decision and output preparation finished within five minutes of start.
