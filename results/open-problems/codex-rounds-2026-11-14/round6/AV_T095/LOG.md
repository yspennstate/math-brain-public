# T095 continuation, round 6

Task: “take the NEXT checkable step on this problem, building on that work.” Started 15 November 2026, approximately 09:52 Asia/Tbilisi.

## 1. Orientation and scope

Read startup memory index, compute state (ok / owner_away_open), mesh protocol, and the round 3–5 inventories. Read their REPORT.md, LOG.md, PROOF.md and audit.py; combined output was truncated, so targeted reads recover the omitted pieces. The current task forbids mutations outside this folder, overriding the earlier general mesh/checklist/brain-write instructions. No such mutations, git, subagents or external messages are used. All shell programs are wrapped in `OMP_NUM_THREADS=1 nice -n 15`; the inherited nice value will be checked because the wrapper reports `setpriority: Operation not permitted`.

## 2. Bounded literature update

Web searches: exact shape title, first-passage differentiability with OpenAI/2026/November/error, and the exact folder name with error. Opened the actual repository history page and arXiv:2610.42124 (Scott Armstrong and Ahmed Bou-Rabee, *Fluctuation bounds for rotationally invariant first-passage percolation*). Search finds the same Gamma-specific claim and selected Lean statements, not a full continuous-law T095 resolution. The continuum fluctuation paper is not that resolution. No later specific correction located in this brief search. Further source reads below concern the selected proof step, not an extended search for updates.

## 3. Selected extension (recorded before work)

Check the next probabilistic reduction in `source-witnesses.tex`: `df:wi:continuous-bk` and its use in `df:wi:long-paths`. These form one link from the already audited disjoint witnesses to the uniform long-path bound. The vulnerable points are upper quantile rounding at dyadic endpoints, repeated event labels, certificates for overlapping boxes, the weak-composition count, and the path-dependent union bound. First independently rerun the preceding finite audit and re-derive its main deterministic inequality; if that fails, report the failure instead.

## 4. Earlier result rechecked

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/AV_T095/audit.py`. Exit 0. All 723 paths, 3,222 chunks, 559,764 intervals and 3,222 greedy/DP packing comparisons pass; all four theorem blocks and document checks pass. Runtime 6.335 s, peak RSS 17,743,872 bytes, actual nice 20. The wrapper warning does not indicate a high-priority process.

Independent derivation: put a=ηs. Each threshold-stopped prefix has defect in [−2a,−a), because its final step loses at most a; the residual suffix has defect ≥−a. Thus H(Q)≥−a−2aM_Q. If a full chunk has no witness its defect is ≥a, while for M_Q≥1 the preceding bound is ≥a−4aM_Q. Summing full chunks and the remainder gives H(P)≥(N−1)a−4aM_tot. Distinct chunks have disjoint edges because the path is simple, even if their coarse labels repeat. This independently confirms the earlier main claim under its recorded scale and endpoint inputs.

Reopened the actual current `build/sections/differentiability/witnesses.tex` using the read-only GitHub connector, and saved it as `source-witnesses.tex`. The target lemmas and constants agree with the inherited source. No mathematical failure in the preceding result was found.

## 5. Primary inputs opened

Read the original J. van den Berg and H. Kesten paper, *Inequalities with applications to percolation and reliability* (1985), PDF pages 7–10 in the web viewer, especially Theorem (3.3), equation (3.4), the positive-witness definition and Corollary (3.10). Opened Richard Arratia, Skip Garibaldi and Alfred W. Hales, *The van den Berg–Kesten–Reimer operator and inequality for infinite spaces*, arXiv:1508.05337, abstract and full HTML, especially Section 5. The monotone Bernoulli BK input needed by this step has the advertised scope. The general nonmonotone BKR operator is not assumed associative; the proof below supplies the needed monotone recursion explicitly.

Reopened official `lean/docs/212.md`: still Gamma differentiability only, with exponential strict convexity outside the selected statements. Latest-commit API still returns `4eaee87548250b2682affda7d05d947c05554bae`, 30 October 2026. Reopened the shape introduction. Two other introduction requests initially returned 404 because their files are `01-introduction.tex`; corrected using the paths in the earlier record, then reopened and saved all three introductions. These are read-only retrievals, not git operations.

The analytical check finds no issue so far: upper dyadic rounding decreases to the original uniforms, strict inequalities pass to finite precision for each finite witness list, and complementing the bits converts edge-disjoint certificates into disjoint positive witnesses. Repeated labels require separate certificates, not separate spatial boxes. Plan for an independent exact audit: compare direct edge-support packing against a separate bit-certificate oracle, enumerate repeated lists under finite product measures, and count weak compositions by dynamic programming rather than the binomial formula.

## 6. All-case reduction saved

Wrote PROOF.md with the complete upper-rounding argument, explicit q-fold iteration of finite monotone BK, countable-path measurability, the deterministic list cover, and summability. Re-derived every constant: low total defect gives M_tot>N/8−1/4; the retained count is floor(N/16); N transitions cost at most 49^N; position allocations cost at most 4^N; hence P(B_N)≤196^N p^floor(N/16). The scale condition gives the geometric ratio 196p^(1/16)<49/200<1. As a second geometry check, actual consecutive index differences are at most 2 in each coordinate, so the manuscript's bound 3 is safely loose. No sharper constant is claimed as the main result.

Saved audit.py. Its two disjointness oracles share the truth of individual events but not their certificates: one packs actual path-edge supports, the other derives minimal positive certificates from all subconfigurations of the finite-bit truth table. The tests use exact exponential-quantile cost comparisons by rational products, including repeated traversal and labeled threshold copies. Composition counts use separate dynamic programming. A 60-second alarm bounds the run, with small finite state spaces and actual RSS checked against 1 GB. Next write the verification record and a provisional report, then execute the audit.

## 7. Verification record and adversarial fixtures

Saved VERIFY.md with all four main theorem environments copied verbatim from the newly reopened actual sources; the clause-by-clause comparison; the sources opened this round, distinguished from inherited external kernel reports; the new spot check; and the three-sentence status recommendation. Reopened all three `build/main.tex` entry files and confirmed author OpenAI, dates September 24 / September 24 / September 25, 2026. Wrote a provisional REPORT.md before running the finite audit.

An adversarial fixture explicitly uses a one-edge cost bound log(8): at two-bit precision, bit-disjoint certificates for two copies of that event can exist on the same edge even though two edge-disjoint path witnesses cannot. The audit demands at least one strict containment example. This tests the proof's use of containment rather than an incorrect equality between bit-disjoint occurrence and path-disjoint occurrence.

Started `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py`; output follows when complete.

## 8. Exact audit result and attempts to break the reduction

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py`. Exit 0:

```text
OMP_NUM_THREADS=1; process nice: 20
Upper rounding and dyadic-endpoint checks: 320 PASS
Finite BK lists: 748
Finite BK configurations: 272
Finite BK packing_comparisons: 101728
Finite BK repeated_lists: 286
Finite BK proper_bit_supersets: 20
Direct edge packing <= bit-certificate occurrence <= product: PASS
Independent floor-index displacement cases: 16413 PASS
Weak compositions: independent DP/binomial checks: 512 PASS
Multiplicity thresholds: 4081 PASS; constants 196 and 49/200 PASS
Floor-exponent and exact geometric-tail identities: PASS
Four exact theorem blocks, preserved sources, links and verdict: PASS
Peak RSS bytes (macOS): 16678912
Elapsed seconds: 0.194
```

Re-derived the load-bearing constants a second way: explicit floor-coordinate cases give differences ≤2, stricter than the asserted bound 3; DP reproduces binom(N+t,t); integer minimal multiplicity reproduces the retained floor(N/16) count for N=16,…,4096; N=16q+r independently checks the exponent direction for p<1. With p=2^−160 the source's scale condition is exactly 400/1024=25/64<1/2 and the geometric ratio is 196/1024=49/256; the all-parameter bound is 49/200. Finite geometric summation plus its remaining tail agrees with the closed tail formula.

Adversarial cases pass: both binary expansions of 1/2, u=0, uniforms near 1, infinite rounded weights at finite precision, exact strict-threshold boundaries, impossible/certain events, empty paths, repeated edge traversals, repeated labels and overlapping boxes. There are 20 strict bit/path containment examples. A general nonmonotone BKR associativity claim is unnecessary: the written proof explicitly nests increasing multi-witness events and applies two-event BK. No mathematical assertion failed. The tests do not establish the other preprint inputs, general continuous-law differentiability, or the full Lean dependency chain.

## 9. Final audit and handoff

Finalized REPORT.md with the measured passing results. A separate small Python document audit checked the four-line continuation report, exactly three recommended status sentences, all local links, and Python syntax; it passed at nice 20. Recovered the complete earlier round 4 log and script tail, and explicitly read round 5's saved external kernel and MathVet excerpts as inherited records. None changes the selected reduction or its scope. The mathematical script was not rerun after documentation-only edits.

Clock cross-check: UTC tool returned 2026-11-15 06:01:38 UTC, independently agreeing with Python's Asia/Tbilisi clock, 10:01:38 +04:00. The initial approximately 09:52 task time is retained above. Deliverables are REPORT.md, VERIFY.md, PROOF.md, audit.py, this log and the freshly reopened source files. The result is a conditional verification of the BK/itinerary link beyond round 5; no full-law T095 resolution is claimed. Next worker: verify `df:wi:no-corner` and the conclusion section's norm/boundary regularity conversion while tracking the preceding conditional dependencies. No writes outside this folder, git operations, subagents, external messages, GPU or Lean builds occurred.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 09:52 Asia/Tbilisi.
