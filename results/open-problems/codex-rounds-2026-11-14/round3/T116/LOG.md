# T116 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Start: 2026-11-15 01:30 Asia/Tbilisi.

## 1. Startup and earlier files (01:30)

Read the earlier folder's REPORT.md, LOG.md, and SOLVED_ELSEWHERE.md in full. PROOF.md is absent; there are no Python or shell scripts. The earlier result is a literature finding, not a new construction or numerical calculation.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B - <<'PY'` with pathlib reads of the four named files, a script-file listing, startup MEMORY.md and compute_state.json. Output: earlier files readable, PROOF.md absent, script list empty. Compute state: warn, owner_away_open, CPU saturated. The nice wrapper emitted `setpriority: Operation not permitted`; effective priority is not independently verified. No heavy computation will run.

The current task permits writes only in this folder. Consequently no shared brain, mesh, checklist, git, or external-system mutations are made. Startup memory was read directly; recall commands that log outside this folder were not run.

## 2. Literature check (01:30)

Web search queries: `"Quantitative lower bounds for trace reconstruction" OpenAI` and `trace reconstruction superpolynomial lower bound 2026 OpenAI September`.

The same September 24, 2026 repository preprint was returned, with the complete-trace theorem in a primary-source search result. Search results also identify its Lean comparator. These are leads; the manuscript and comparator must be opened before using them. No new mathematical conclusion has yet been accepted.

Next check: compare the manuscript theorem and the Lean comparator's channel and estimator definitions. This is the earlier report's named next step. If the primary statement confirms the negative polynomial-sample answer, follow the user's literature-stop branch; do not start a separate research extension.

## 3. Primary sources and independent recheck (01:31–01:32)

Opened with the web tool:

- https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/main.tex
- https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/sections/introduction.tex
- https://raw.githubusercontent.com/openai/math/main/lean/docs/122.md
- https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/TraceReconstruction.lean

The manuscript header confirms author OpenAI and date September 24, 2026. Its model and theorem agree with the earlier report. No later change resolving the remaining order gap was found in the bounded search. The comparator scope audit is recorded separately in AUDIT.md.

Independent derivation of the earlier consequence: fix q in (0,1), s=2/3, and c=1/(8 log 2). This c is positive and strictly below the theorem's endpoint. For any A>0, once log n >= q^(-3) exp((A+1)/c), the displayed lower-bound expression is at least n^(A+1). Combining this with the theorem's eventual validity gives T_{q,s}(n)/n^A >= n, hence divergence. The displayed threshold is only for this algebraic comparison, not an effective threshold for the theorem itself.

Second derivation: log(n^{c log(q^3 log n)})/log n = c log log n + 3c log q, which diverges. Thus its exponent eventually exceeds every fixed A. High-probability reconstruction would in particular succeed with probability 2/3, so this consequence addresses the question asked. The earlier result holds as a correctly reported implication of the preprint; its underlying construction has not been independently proved here.

Boundary audit: q is deletion probability; q=0, q=1, and rapidly vanishing q are not covered by this fixed-channel reasoning. The theorem concerns every sufficiently large length, not only a subsequence. Small fixed positive success probabilities are explicitly in its statement, but the elementary two-point testing argument alone would not establish that stronger scope. No matching asymptotic order follows.

Decision within the five-minute literature allowance: retain the reported negative answer and follow the required stop branch. The added check is a statement-level comparator audit, not a Lean execution. No simulation or proof build is necessary for this branch.

## 4. Final file and priority audit (01:32)

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B - <<'PY'` reading LOG.md, AUDIT.md, SOLVED_ELSEWHERE.md and REPORT.md; checking nonempty content, verdict prefix, comparator caveat and the algebraic comparison; querying `os.getpriority(os.PRIO_PROCESS, 0)`.

Output: `File audit: PASS`; `Effective nice: 20`; clock `2026-11-15T01:32:18.854408+04:00`. Thus this process's effective priority was independently verified as nice 20 despite the wrapper warning. The earlier log's initial uncertainty about priority is resolved for this final process. All local invocations were tiny one-thread Python reads; no proof build or numerical run occurred. The initial literature check and stop decision took less than five minutes.
