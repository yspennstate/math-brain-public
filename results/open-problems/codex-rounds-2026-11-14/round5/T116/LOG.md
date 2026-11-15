# T116 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Start: November 15, 2026, 08:22 Asia/Tbilisi.

## Startup and earlier result

Read REPORT.md, LOG.md, SOLVED_ELSEWHERE.md and all available AUDIT.md files in the three earlier folders. Directory listings confirm that none contains PROOF.md or research scripts. No earlier files were edited. Read startup MEMORY.md, BRAIN_INDEX.md and compute_state.json directly. State: warn, owner_away_open, CPU saturated. The current folder-only order precludes shared brain, mesh and checklist writes, including recall commands that log elsewhere. No git or subagents.

Initial shell reads used ordinary shell tools; subsequent Python invocations use `OMP_NUM_THREADS=1 nice -n 15 python3 -B`. The wrapper warns `setpriority: Operation not permitted`; `os.getpriority(os.PRIO_PROCESS,0)` independently returns 20. No heavy computation is planned. An initial file enumeration was unnecessarily broad and truncated; narrowed subsequent reads to the task files. No private file contents were opened by that enumeration.

Earlier result re-derived independently, conditional on its stated theorem: fix q in (0,1), s=2/3 and c=1/(8 log 2). For every A>0, choosing log n >= q^(-3) exp((A+1)/c) makes n^{c log(q^3 log n)}/n^A >= n. The theorem supplies an additional unspecified eventual threshold. Second check: the logarithm of the bound divided by log n equals c log log n+3c log q, which diverges. Thus the reported polynomial-sample consequence holds; this does not verify the hard-pair construction.

## Literature check, 08:22–08:24

Web searches: `"Quantitative lower bounds for trace reconstruction"`; `trace reconstruction superpolynomial lower bound September 2026 OpenAI`.

Opened primary source header and introduction under:
https://raw.githubusercontent.com/openai/math/main/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/

Header: author OpenAI, September 24, 2026. Introduction confirms ordinary complete traces, unrestricted computation, every fixed positive success, and the previously reported bound. No subsequent change resolving the remaining order gap was found. A search-result commit identifier adc7f1241b42e322a6451854ab7e4b4c146bf78a did not yield an accessible pinned introduction (cache miss); no immutable snapshot established.

Opened `build/sections/transfer.tex` and the actual imports `lean/OAI/Probability/TraceReconstruction/Testing.lean` and `Induction.lean`. Initial guesses without the OAI/Probability prefix failed; corrected paths succeed. Testing imports Restoration; Induction imports Amplification and Propagation. Source availability is rechecked, not kernel acceptance.

Choice written before further work: make one narrow audit of the restoration/testing transfer, especially whether complete traces and success below 1/2 are handled. This is the last report's fallback next step and belongs to verifying the already reported resolution. Under the literature-stop branch, do not attempt a separate construction or computational research extension. Write the result and stop.

## Transfer audit result

Opened the rest of transfer.tex, all of Testing.lean, and Restoration.lean using the web tool. New beyond round 4: the Lean implementation uses a common-reference family bound, rather than the manuscript's factorized-posterior proof. In Testing.lean, `ConcreteLevelPair.restored_family` (lines 76–121) constructs injective length-n words and bounds each m-trace law's distance to the all-zero-choice member by sqrt(m*g*N^(-d))+2*m*g*U.error. `family_testing_bound` (lines 164–201) deduces s <= 2^(-g)+epsilon. This route handles every fixed positive s if the displayed distance tends to zero for fixed g.

Restoration.lean independently exposes the needed common-kernel transfer: `approximate_hellinger_transfer` (lines 24–35) gives sqrt(mV)+2mE; `degraded_sample_tv` (lines 121–137) applies one hypothesis-independent deletion kernel per sample. Its extra deletion probability is (q-r)/(1-r), so the total deletion probability is r+(1-r)*(q-r)/(1-r)=q. Suffix padding in Testing.lean uses an independent tail law shared by both hypotheses. These are static source observations; no Lean build or dependency closure check was run.

Decision: the negative polynomial-sample answer remains a reported preprint resolution, confirmed within the five-minute literature allowance. Complete the instructed stop branch. Record an explicit independent proof of the narrow common-reference testing inequality in PROOF.md as an audit of existing work, not a new trace lower bound or certification. No new research program or computation is started.

## Self-check and completion, 08:24

PROOF.md derives s<=2^(-g)+epsilon first by summing conditional output probabilities, then independently by comparing the uniform-prior joint laws. Checks: identical hypotheses' observation laws allow only the prior guessing rate; disjoint laws make the bound vacuous rather than contradictory; noninjective word maps invalidate a necessary premise. A concrete symbolic margin verifies sqrt(mgN^(-d))<=eta/2 when m<=eta^2*N^d/(4g), with the other term controlled separately. This is not a numerical experiment or a new lower-bound construction.

Final command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B - <<'PY'` with pathlib nonempty-file checks, verdict and limitation assertions, earlier-script listings, os.getpriority, and datetime. Output: LOG.md 4713 bytes, PROOF.md 3308, AUDIT.md 1272, SOLVED_ELSEWHERE.md 1339, REPORT.md 2063; File audit: PASS; Effective nice: 20; clock 2026-11-15T08:24:35.444421+04:00. LOG.md byte count precedes this appended entry. All three earlier folders lack PROOF.md and research scripts. No build, simulation or writes outside this folder. Stop branch completed in less than five minutes.
