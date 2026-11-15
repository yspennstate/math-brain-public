# T176 continuation log

Task: “Verify: has open problem T176 been settled by the OpenAI math release?” — 15 November 2026, approximately 10:00 Asia/Tbilisi at session start (exact receipt time unavailable).

## 1. Orientation and bounded follow-up search

Read the round 3, 4 and 5 REPORT.md, LOG.md and PROOF.md records, and round 5's only script, audit_sources.py. Some batched output was truncated; the mathematical notes are being reread separately before relying on them. All earlier folders remain read-only. Read the startup memory index and compute_state.json: warn / owner_away_open, CPU saturated, 41% memory free. No heavy computation or Lean build is planned. The current task's folder-only rule excludes global mesh, checklist and brain mutations; no such commands, git, subagents or external writes are used.

Initial commands were short read-only pwd, rg, cat and sed reads. Subsequent shell programs will use OMP_NUM_THREADS=1 and nice -n 15. Previous rounds reported that nice fails to change priority; this will be checked before any computation.

Web search queries: `"Thorp" "shuffle" "2026" "optimal"`, `"Optimal-order mixing of the Thorp shuffle"`, `"Thorp" "shuffle" "all even" mixing 2026`, `"Thorp shuffle" "November" "2026" mixing even`, `"Thorp" "OpenAI" "error" "2026"`, and `"Thorp shuffle" arxiv 2026 optimal`. Opened the repository history, lean/docs/238.md and arXiv:2611.03959. No later all-even solution or specific refutation appeared. Search snippets and derivative expositions are not treated as opened papers or proof validation. The five-minute follow-up window is still open for final primary-page reads.

## 2. Earlier-result recheck (in progress)

Round 5 established a source-level distinction between Main's inverse-square Fourier route and FirstMain's first-power route, interpreted the physical full-permutation model, and checked deterministic-free-set half balancing. Recheck these load-bearing scalar claims independently before extending the audit. No complete proof certification was claimed earlier.

## 3. Bounded search concluded; priority and earlier scalar check

The bounded search ended within five minutes of the first search. Primary pages opened: repository history.md (last listed update October 29, no Thorp entry), lean/docs/238.md, Yunjiang Jiang's arXiv:2610.18884 (dyadic d^(5/3) bound, v1 October 3), Yunjiang Jiang's arXiv:2611.02092 (adhesive riffles, v1 November 1), and Ilya Mironov's arXiv:2611.03959 (random-pair Monte model, v1 November 2). These last two precede the earlier rounds and concern different models. No SOLVED_ELSEWHERE.md is warranted. No later all-even solution or specific correction was found; this bounded search is not proof of absence.

Ran `OMP_NUM_THREADS=1 nice -n 15 python3 -B -c 'import os; print("priority", os.getpriority(os.PRIO_PROCESS, 0))'`. Output: `nice: setpriority: Operation not permitted`, then `priority 20`. The actual inherited priority is already lower than nice 15. Tiny single-thread standard-library checks can therefore proceed; no Lean build or substantial numerical run is planned.

Independently re-derived the balancing estimate by writing X=a+Bin(b,1/2), m=2a+b. The bad threshold is a downward deviation of m/4 from m/2, so Hoeffding gives exp(-m²/(8b))≤exp(-m/8)<(9/10)^m for b>0; b=0 is deterministic. Recomputed the rational factors 881/1000 and 16/25 and the Fourier exponent 2-16/4=-2. Thus the main local result of round 5 survives. The import count and constants will also be checked by a separately written script rather than by rerunning its script unchanged.

## 4. ONE extension chosen, before the proof and computation

Audit the tagged-flow identity in ConditionalLaw.lean and MaskedResampling.lean, the first next step named by round 5. The issue is whether replacing unexposed switch coins by fresh coins preserves their joint law with the exposed endpoints, and whether iterating this identity really gives the tagged-card deviation used for fixed input lists. Prove this finite identity independently, check its precise hypotheses, and test all endpoint indicator functions in small physical shuffles by exact enumeration. This is one conditional-law link; the rotating-half reindexing in HalfHistories remains for a future worker.

Read the saved ConditionalLaw, MaskedResampling, ConditionalFlow, PairAveraging, TaggedDeviation, TaggedCompletion and PrefixTests sources. One attempted LOG context patch failed without changing files; this corrected append records it. The proof and computation follow.

## 5. Fresh source acquisition and the identity's hypotheses

Opened current ConditionalLaw.lean and MaskedResampling.lean with the read-only GitHub fetch tool, plus the short paper's build/main.tex and the two companions' build/sections/00-introduction.tex. Saved the exact bodies under sources/. Tool records give the two Lean files' modification date as October 6. Only the endpoint identity is under audit: its test depends on the exposed endpoints and tagged endpoint, and does not assert equality after conditioning on the entire original coin array.

The one-step argument resamples only pairs with two free endpoints. It fixes all exposed positions because each exposed point lies outside B. For a fixed past, B and its mask are fixed before the next fresh coin; this is needed for uniformity. Raw weights may be signed and need not be supported on B for the one-step identity. Centered tagged weights are supported on B. These distinctions will be tested with exact indicator-basis comparisons and two deliberately invalid variants.

## 6. Exact computation started

Wrote check_conditional.py independently of round 5's script. It checks round 5's import graph by queue traversal and Kahn elimination, recomputes its rational constants, and compares the two freshly fetched identity files with the earlier snapshots. For the new identity, it compares direct cut-and-drop permutations with the binary physical map, then checks every initial basis weight and every joint endpoint-indicator test. It uses integer flow matrices with common denominator 2^t. A second calculation groups direct histories by complete exposed paths and compares conditional tagged probabilities, both uncentered and centered.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B check_conditional.py > check-output.json`. The script requires actual nice≥15, enforces a 180-second CPU ceiling and 900 MiB address-space ceiling, and uses only the standard library. Planned scope: all free sets on 2 and 4 cards at times 0 through 4, all free sets on 8 cards at time 2, and eight specified free sets on 8 cards at time 3. No random sampling, full mixing computation, or compiler invocation is involved.

The first run stopped before any enumeration: Darwin rejected setrlimit(RLIMIT_AS, 900 MiB) with `ValueError: current limit exceeds maximum limit`. A diagnostic reported unlimited inherited AS/CPU limits and startup RSS 11,730,944 bytes. Corrected the script to keep the 180-second CPU limit and use bounded inputs plus an observed-RSS stop at 256 MiB. At most 4096 histories per free set are accumulated, with eight rows and columns; the tables are discarded between free sets. Re-ran the same command. The initial address-space-enforcement statement above describes the failed first version, not the successful run.

## 7. Computation completed and proof saved

The corrected command exited 0. check-output.json records actual nice 20, 1.960 seconds elapsed and peak RSS 45,662,208 bytes. It checked 103,884 history/free-set cases and 2,536,256 basis/indicator equalities, all with exact error zero. The independent full-path groups numbered 128, 1248, 256, 1 and 4096 in the five documented cases, with exact conditional point and centered probabilities. Direct cut-and-drop permutations matched the bit map. The earlier import closure, source comparisons and rational constants also passed.

Re-derived the history/free-set total independently: 4(1+2+4+8+16)+16(1+4+16+64+256)+256·256+8·4096=103884. The two deliberately invalid variants give actual/flow expectations 1 and 1/2 when an exposed point is free, and P(masked coin=1)=1/4 for a mask chosen from the current coin. Both failures match the analytic examples and show where the valid proof uses its hypotheses.

Saved PROOF.md with the full resampling, joint-test induction, centering, bounded-test estimate, second path-cylinder derivation, and boundary checks. During audit clarified that the balancing lemma uses last-bit prepared halves; it does not assert balancing of the physical first-bit deck halves. The new identity proof requires no rotating-half factorization, so that separate next step remains open.

Reopened both companion build/main.tex headers, lean/docs/238.md and Main.lean through read-only GitHub fetch and saved them under sources/. All three paper headers name OpenAI and September 26, 2026. The scope document and Main still concern dyadic decks. These later reads document the claims already located in the bounded search; they are not an extension of the literature search.

## 8. Verification and report saved

Wrote VERIFY.md with five exact theorem/corollary environments extracted from the freshly fetched TeX, the clause-by-clause comparison, primary follow-up pages actually opened in this round, the Lean scope limits, a three-sentence replacement status and the tagged-flow spot check. Wrote REPORT.md with the required continuation prefix PARTIAL, the new local proof, computation, failed first resource-limit request, limits and next step. The all-even row remains outside the opened claims.

Final audit will verify source quotations and document consistency, and independently recount the finite-test totals from reachable physical deck orders without using the flow implementation. No further literature search or full-proof claim is planned.

## 9. Final audit completed

Ran `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_deliverables.py > audit-output.json`, exit 0. This independently constructs reachable deck orders by actual cuts and pair drops, without importing or using the flow implementation. It recounts 103884 history/set cases and 2536256 basis/indicator equalities, matching check-output.json. The five full-path checks have 5729 cylinders in total. It also verifies all five exact theorem quotations, all three author/date headers, the REPORT prefix and absence of control-character corruption. Its peak RSS was 20,168,704 bytes.

Read REPORT.md, all of PROOF.md, Main.lean, and the relevant scope-note passages back from disk. Reread round 3's complete PROOF.md separately to eliminate the initial batched-output truncation. The path-cylinder reasoning agrees with that earlier check; the new raw signed-weight resampling identity and fixed-list test link are the added result. Expanded the centered vector's energy calculation explicitly and corrected the adjoint notation in VERIFY.md. Added the independent audit command to REPORT.md.

No valid-hypothesis failure was found. The two invalid-variant failures are hypothesis checks, not refutations of the preprint. No Lean/Comparator build or complete proof certificate is claimed. Next remains the rotating-half reindexing/factorization link; no additional task is started in this round. All authored files and source snapshots are inside this folder; earlier folders and external systems were never modified.

Task: “Verify: has open problem T176 been settled by the OpenAI math release?” — 15 November 2026, approximately 10:00 Asia/Tbilisi at session start (exact receipt time unavailable).
