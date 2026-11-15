# T176 continuation log

Task: “Verify: has open problem T176 been settled by the OpenAI math release?” Received 15 November 2026, Asia/Tbilisi; exact receipt clock time unavailable. Session starts around 00:59 local from the existing run log.

## Step 1 — read-only orientation

Ran `OMP_NUM_THREADS=1 nice -n 15 pwd`, `ls -la` in this folder and the earlier folder, and read the compute-state JSON. It reports warn / owner_away_open, CPU saturated. Each shell command reports `nice: setpriority: Operation not permitted`; no substantial local compute will run unless priority can be verified. Read the startup memory and memory index. The later folder-only instruction prevents mesh/checklist/brain writes elsewhere; no such writes, git commands, or subagents were used.

Read earlier REPORT.md, LOG.md and VERIFY.md. Earlier folder contains no PROOF.md and no scripts; its sources/ directory will be examined next. The earlier result is a scope verdict: all three papers claim optimal mixing only for powers of two, not every even deck size. Its Proposition 6.1 transfer check was conditional on input hypotheses.

Used web search queries `"Thorp" "OpenAI" "mixing" 2026`, `"Optimal-order mixing of the Thorp shuffle"`, and `"Thorp" "2610.18884"`. Results lead to the same family and some newer bibliographic entries; these are not yet validation or evidence of an all-even solution. Search/open follow-up is limited to five minutes.

## Step 2 — follow-up search concluded; independent scope recheck

Further web queries: `Thorp shuffle November 2026 "even"`, `"Thorp" "OpenAI" error refutation correction`, `"Thorp" "mixing" "November 14" 2026`. Opened repository history.md (latest listed entry October 29; no Thorp entry), arXiv:2611.03959 (Ilya Mironov, random-pair Monte model, v1 November 2), and arXiv:2611.02092 (Yunjiang Jiang, adhesive riffle models, v1 November 1). Neither is an arbitrary-even Thorp solution, and neither is a development after the November 14 report. No newer all-even solution or refutation was found in this brief search. No SOLVED_ELSEWHERE.md is warranted.

Read the primary saved source files, starting with optimal-main.tex; fetched its current raw build/main.tex independently through read-only GitHub fetch. It explicitly sets n=2^d, uses the same physical map (x_1,u) -> (u,x_1+xi_u), states full-permutation TV convergence at 1600d, and explicitly excludes arbitrary even sizes. This independently confirms the earlier scope claim. The other two introductions and scope note will be rechecked when saving the source record. No PROOF.md or computation scripts exist in the earlier folder.

## Step 3 — chosen extension, before doing it

Check the short paper's conditional-flow energy contraction, Sections 3–4, through Proposition 4.2 (Averaged ordered marginals). This is the input that the earlier worker's Fourier-transfer check assumed. The particular risks are conditioning on future exposed paths, independence across opposite halves, and averaging a random input list without accidentally making a fixed-list claim. Re-derive the recurrence and its numerical exponent independently; try to falsify its conditioning claim. Record a detailed local verification in PROOF.md, with explicit limits, rather than assert correctness of the whole preprint.

## Step 4 — primary-source snapshots and first mathematical checks

Read-only GitHub fetch opened the current short paper, both companions' introductions, and lean/docs/238.md. Saved the exact returned texts here as optimal-main.tex, compatibility-introduction.tex, routing-introduction.tex and lean-scope-238.md. These confirm all three full-deck conclusions are dyadic. No local compile was attempted. A process-priority inspection (`OMP_NUM_THREADS=1 nice -n 15 /bin/ps -o pid,ni,comm -p 1`) was denied by the sandbox; all mathematical checks remain analytic.

Independently re-derived the earlier Fourier transfer's exponent as (3/8-1)/2 = -5/16 and its squared constant as 4*8*C_1 = 32*C_1. The multiplicity argument remains valid because the orbit of one vector in V_pi tensor A_pi is the image of End(V_pi), of dimension at most (dim pi)^2. This confirms the earlier conditional spot check, without using the flow estimate to justify it.

For the new check: a feasible exposed-path event fixes exactly its visited time-edge coins, so later path constraints do not bias unvisited earlier coins. Opposite halves use disjoint fresh coin arrays during the d-1 lookback layers. Uniformity of the free set is used only unconditionally, and the bad event's possible correlation with energy is absorbed using the pathwise bound ||w||_2^2 <= 1. No defect identified in these steps. Detailed derivation and attempted countercases are being written next.

## Step 5 — local check and report saved

Wrote PROOF.md with every step of the conditional-flow calculation, and REPORT.md using the continuation task's required PARTIAL prefix. Re-derived the half-density 1/16, bad-event probability 2exp(-n/256), noise coefficient 2^(-j), decay base 31/32 and error constant 32. The exponent was checked independently by a logarithm integral and by the exact binomial inequality 59634/29791 > 2. Tested the reasoning against future conditioning, shared exposed edges, bad-event/energy correlation, m=n, m=1, d=1 and t=2d+1. The conclusion is a local verification of the source's averaged-list estimate, not a judgment that the full paper is correct. No computational experiment was needed.

## Step 6 — verification record saved

Wrote VERIFY.md with all five exact theorem/corollary environments from the freshly fetched primary texts, a clause-by-clause comparison, the bounded follow-up search, Lean scope limits and the three-sentence replacement status. Reopened both long papers' main.tex files to verify authors OpenAI and date September 26, 2026. Reopened ThorpShuffle/Main.lean and formalization.yaml; the former explicitly states 1600d convergence and IsTheta(log(2^d)). No formal proof check was run. Prior-session-only follow-ups are distinguished from pages actually reopened here.

## Step 7 — final audit

The first comparison command guessed `/bin/cmp`, which does not exist here; it made no changes. Re-ran all three snapshot comparisons with `/usr/bin/cmp`: current optimal-main.tex and both introduction sources match the earlier worker's saved files byte for byte (exit 0). Used the tool-orchestration JavaScript to compare all five exact quotations against a fresh `cat VERIFY.md`: all five match. Read REPORT.md back and confirmed the required continuation prefix and explicit limits. Clarified that `review: status: unchecked` in formalization.yaml is document-level, not an individual Thorp review. Saved the two long papers' author/date main files and the actual Lean main file here as additional primary-source snapshots. No git, external mutation, or writes outside this folder occurred.

The source calculation's numerical checks are analytic, not a simulation or formal certificate. The new result is the detailed conditional-flow/averaged-marginal check; the full arbitrary-even row remains unsettled by the opened claims. Next suggested check: Lemma 5.1 and the final Fourier/sign comparison. Task: “Verify: has open problem T176 been settled by the OpenAI math release?” — 15 November 2026, approximately 00:59 Asia/Tbilisi at session start (exact receipt clock unavailable).
