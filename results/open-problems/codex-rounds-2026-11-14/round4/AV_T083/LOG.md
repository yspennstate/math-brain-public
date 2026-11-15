# T083 round 4 log

Task: “Verify: has open problem T083 been settled by the OpenAI math release?”
First clock reading: 15 November 2026, 04:16:23 +04; exact receipt time unavailable.

## 1. Orientation and prior work

Read the earlier REPORT.md, LOG.md and VERIFY.md, and round 3 PROOF.md and check_transference.py. The first session has no PROOF.md or scripts in its file listing. Round 3 proves only a conditional transference bridge; the local depth-variation estimate is its unresolved premise.

Commands used `OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c ...` for read-only listings and document reads. The inherited process priority prevents an additional nice increment (`setpriority: Operation not permitted`); the prior worker measured inherited nice=20. We will verify this ourselves. Compute state says warn/cpu_saturated, owner_away_open; only tiny single-thread programs will run. No git, subagents, or external mutations. The current explicit folder-only order supersedes shared-brain, mesh and checklist writes; existing memory is consulted read-only where available.

## 2. Literature refresh started

Web search queries: `"pointwise" "triple" "ergodic" "2026" convergence`; `"openai/math" "ergodic" error`; exact consecutive-triple title. Results include the already known expositions, the repository sources and a new lead on Christoph Thiele's papers page concerning two commuting transformations. These snippets do not establish a settlement. GitHub read-only connector successfully opened the consecutive-triple build/paper directory. Next open the lead and source sections, within the five-minute refresh limit.

Refresh concluded after opening Thiele's papers page, Bogdan Grechuk's 10 November exposition, and release history. The first concerns two commuting transformations and a norm-variation blueprint, as already noted in round 3; it does not settle arbitrary k. No new settlement was found in this bounded check. No SOLVED_ELSEWHERE.md is justified.

## 3. Re-check of round 3

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/AV_T083/check_transference.py` (read-only execution; no bytecode writes). All polygon moments, 11 quadratic Taylor tests, 140 prefix tests, six source comparisons and three quotation checks passed. Area=1/7500, mean eta^2=1/135000, per-scale normalized Taylor factor=1/270000, summed factor=1/202500. Peak RSS=14,581,760 bytes, elapsed=0.004 s, inherited nice=20. Independently, writing u=xi and v=xi+3eta gives eta=(v-u)/3 with independent uniform u,v in [-e,e]; hence mean eta^2=(2e^2/3)/9=2e^2/27 and Taylor factor=e^2/27. The reported conditional result holds; this does not prove its local analytic premise.

## 4. ONE extension selected

Verify the depth-varying catalog-row lemma (rows.tex, Lemma `row-depth`), including its maximal-row premise `row-maximal`. This is the central new operator estimate in the consecutive-triple paper's adaptation from fixed inputs to depth schedules. The completed local theorem invokes it repeatedly. This is a narrower, checkable next step than certifying the entire long analytic argument. We will prove precisely the stated row lemma under all its catalog, whole-support, refinement and Bessel hypotheses, and identify which remaining dependencies are outside that check.

Opened and saved current original transfer.tex, rows.tex, base.tex, localization.tex and completion.tex using read-only GitHub fetches. These sources show that the final local estimate still imports the trilinear-Hilbert-transform manuscript H; verifying `row-depth` alone cannot establish that final estimate.

## 5. Main-claim and follow-up refresh

Retrieved the three current original introduction files and candidate 1 inputs.tex; saved these along with the consecutive-triple bibliography. The main theorem hypotheses remain mixing, invertibility and probability preservation; candidate 1 still states its wider general-triple lemma internally.

Opened arXiv:2608.27321: Floris van Doorn, Polona Durcik, Joris Roos, Lenka Slavíková, Christoph Thiele; its abstract concerns norm-variation, not the full pointwise assertion. Opened OSVerify's actual trilinear-Hilbert-transform case page: the same three issues with proposed repairs are listed, without a claim that they refute the main theorem. No new expert certification was found in the bounded search.

Retrieved current lean/formalization.yaml and lean/docs/145.md. Searched the catalogue for ergodic/pointwise/slopes/mixing: only unrelated mixing hits. Web opening lean/docs failed with a cache miss; the read-only GitHub directory listing succeeded and has no 154.md. The saved 145.md concerns multiple mixing, not pointwise averages. Opened Lean README and release history; history's latest entry remains 29 October. Sources and the parsed docs listing are saved locally. No compilation or Lean proof audit is claimed.

## 6. Row-lemma findings before writing the proof

The catalog gives pointwise coefficient comparison D^(-1)||a|| <= ||sum a_v Phi_v|| <= D^(3/2)||a||. The squared condition-number cost is D^5. Choosing T=2^ceil(5 log2 D) buckets and threshold tau=lambda/(4 D^(3/2)) makes the many-hit loss at most 16 B^2 E/lambda^2. A dyadic-prefix bound costs L_D=1+ceil(5 log2 D); together they yield exactly (16/9)(9+L_D^2) B^2 E/lambda^2. Integrating the weak tail yields (8/3)sqrt(9+L_D^2), the manuscript's constant. Abel summation within each deterministic block followed by Cauchy–Schwarz cancels W^(-1/2) against sqrt(W). No failure found in this finite row lemma so far. Whole-row assignment, persistent coefficients and nondecreasing reads are essential to this argument.

## 7. Proof, independent finite checks and saved deliverables

Wrote PROOF.md, giving all hypotheses, coefficient comparison, whole-row bucket induction, many-hit bound, dyadic-prefix estimate, weak-tail integration, Abel identity and block Cauchy–Schwarz. Independently simplified the final constant inequality: 25(x+1)^2-[9+(5x+2)^2]=30x+12, positive for x=log2 D>=1. No H estimate is needed for this finite lemma itself.

Wrote check_rows.py using exact rational arithmetic and no external packages. Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B check_rows.py`. A finite Haar-row model has one persistent column (m(y),1), varying physical sign m, one private coordinate, D=2 and independently computed Bessel norm squared <=2. All 4,240 stopping/bucket/prefix configurations passed. These exercise branch-dependent hits, whole-support assignment, zero tests, empty rounds, oversized hits and omitted rows after the cap. All 8,480 direct Abel-versus-summation-by-parts and block-domination checks passed, including repeated/skipped reads and absent blocks. Constant identities passed. Four current sources match round 3 unchanged. Peak RSS=16,662,528 bytes; elapsed=2.024 seconds; inherited nice=20. These finite models supplement, not replace, the all-row proof.

Wrote VERIFY.md with exact current theorem environments, comparison, internal wider triple claim, sources opened and three-sentence replacement status. Wrote REPORT.md using the later continuation instruction's PROVED prefix, explicitly restricted to the finite row lemma; it does not call T083 proved. An initial JavaScript document-assembly call had an unescaped Markdown code fence and failed to parse before any tool ran or file was written; corrected assembly succeeded.

Opened the actual H main TeX: author OpenAI, title “An L^3 bound for the trilinear Hilbert transform”, date October 5, 2026. Its full analytic proof is not audited. Opened current main sources of all three candidates to verify their author and date as well. Saved these source headers/files locally.

## 8. Final audit and handoff

After VERIFY.md was written, reran check_rows.py so its three exact theorem-quotation checks were exercised. All previous finite checks passed again: 4,240 stopping configurations, 8,480 Abel checks, constants, and four unchanged-source comparisons. Final run: peak RSS 16,744,448 bytes, elapsed 1.993 seconds, nice=20. Read back REPORT.md and VERIFY.md and checked current source author/date declarations. No mathematical check failed.

The maximal estimate's constants were derived both from the coefficient condition-number calculation and from the explicit stopping-tail algebra; the final logarithmic comparison was independently reduced to 30x+12. The proof treats zero energy/B=0, repeated reads, empty blocks of reads, whole-row assignment before observation and common null sets explicitly. Finite tests include overshoots and paths whose rows are omitted after the cap. These checks found no defect in the selected lemma, and do not justify dropping any of its structural hypotheses.

Added an explicit PARTIAL-CLAIMED literature verdict to VERIFY.md to distinguish the original scope question from REPORT.md's later-instructed PROVED verdict for one lemma. Next worker: candidate3-base.tex, “A separated scale sum on depth inputs” (lem:hbase-scale, source line 467), particularly the transfer of the row hypotheses and complexity budgets into its analytic construction. The whole local estimate remains unverified.

All artifacts are inside this task folder. No git, subagents, external writes or publication were used. No heavy programs ran. Last recorded clock before this final audit: 15 November 2026, 04:26:24 +04. Task: “Verify: has open problem T083 been settled by the OpenAI math release?”; exact receipt time unavailable, first clock 04:16:23 +04.

Final read-only document audit passed: report scope and format, three exact theorem quotations, three-sentence recommendation, no duplicate paragraph, and proof artifact presence.
