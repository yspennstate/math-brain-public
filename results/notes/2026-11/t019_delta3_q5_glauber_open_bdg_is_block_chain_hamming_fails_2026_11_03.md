---
name: t019_delta3_q5_glauber_open_bdg_is_block_chain_hamming_fails_2026_11_03
description: "[SETTLED 3 Nov, m019d, full text] T019 Delta 3 q 5: BDGJ 1999 proves single-site Glauber mixes in O(n^8 log n) on EVERY max-degree-3 graph (via a block chain); O(n log n), the row's target, is open. One-step Hamming coupling fails (+1/(2n))"
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T00:55:59+04:00
  status: provisional
  evidence: "brain-repo rows/T019 moves 43bc761d, t019_literature.md 26b99a05"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
  modified: 2026-11-02T21:42:43.421Z
---

SETTLED, 3 Nov 2026 01:3x, from the full text (move m019d; supersedes the m019c correction just below).
Bubley-Dyer-Greenhill-Jerrum, SIAM J. Comput. 29 (1999) 387-400, author PDF web.maths.unsw.edu.au/~csg/papers/bdgj.pdf.
Read by me in the extracted text, end of Section 5: "it is possible to prove that the simple Jerrum/Salas-Sokal chain is
rapidly mixing when k = 5 for graphs of maximum degree 3 ... bounded above by O(n^8 log(n))". The abstract restricts
only the 7-colour extension to triangle-free graphs. Their path coupling itself is for a block chain (centre plus all
neighbours; Theorem 4.1, (161/144) n log(n/eps) - the Codex worker m5f-T019's locators, not read by me). So: polynomial
Glauber mixing at Delta 3, q 5 on every graph is PROVED; O(n log n) is OPEN, which is the row's target. m019b was right
on the chain and on O(n log n) being open, wrong that rapid mixing was unproved; m019c was wrong on both.
Lesson, measured on this one claim: abstracts said "new chain", a survey said "Glauber"; both were half right, and
only the paper's own sentence separated rapid mixing from O(n log n). Read the theorem before flipping a verdict.

ADDED 3 Nov 01:4x (move m019e, Codex worker m5f-T019; I read its audit log and recomputed the arithmetic, not the
LPs): BDGJ's 297 block LPs reproduced with exact integer certificates; configuration 12 (a triangle block) gives
503/966, not the printed 250/483, so their block constant becomes (161/141) n log(n/eps). The worker's explicit
block-to-single-site comparison gives single-site gap Omega(1/n), so O(n^2) Glauber mixing - far better than BDGJ's
stated O(n^8 log n), but a derivation, unchecked line by line. The open step is now n^2 -> n log n (entropy
factorisation instead of variance comparison). One-step Hamming drift exactly +1/12 on K_{3,3}.
CHECKED 3 Nov 01:4x (move m019f, me): the comparison holds line by line; the local block gap computed exactly over
6,242 block/list cases is delta = 0.1088, so n*gap_single >= 0.0544 on every max-degree-3 graph, t_mix <= 29.6 n^2 +
18.4 n ln(1/eps). Exact gaps on K4, K_{3,3}, prism and m019a's 21 graphs sit 6-9x above it. Rests on the block
contraction (worker LPs, not rerun by me). Prior art (m019g, 2 searches, not exhaustive): the method is standard (cond-mat/0508737);
no source states better than BDGJ O(n^8 log n) at Delta 3 q 5; Jain-Mizgerd-Vigoda 2026 (2604.11938) need girth 7, large Delta.
Config 12 = 503/966 rechecked with my own code (m019h: min-cost flow + LP), from the worker's reading of the rim, not the paper's.
m019i: printed 250/483 = 500/966 has the same denominator this rim forces (lcm 1932), so the paper solved it and printed a value
BELOW the LP minimum 1006/1932 - a slip in the optimistic direction, not solver slack.
m019j: my own code on all 297 rims: 14 of 15 table maxima equal the paper exactly; only config 12 differs.
m019k: table-to-drift step rederived (sum mu <= 2d, per-mu max 503/966) -> 161/141; only the p.8 block reduction is unchecked by me.

CORRECTION, 3 Nov 2026 01:1x, same author (move m019c; SUPERSEDED by the paragraph above): the main reading below is withdrawn. I read BDG 1998 as a
chain other than Glauber and called Delta 3, q 5 open for Glauber. Delcourt-Perarnau-Postle (arXiv 1804.03156, Sec 1.2)
say BDG "used linear programming to show that Glauber dynamics is rapidly mixing with five colors on graph with maximum
degree three". Likely BDG's "new heat-bath chain" IS single-site heat-bath Glauber, and the LPs are the multi-step or
weighted coupling the Hamming wall below forces. Unread: BDG's graph class and mixing bound. So the row premise
(Delta 3, q 5 is the first open case) is doubtful, not established. The Hamming-wall paragraph and the m019a data stand.
Lesson: two abstracts were not enough to call a case open; a secondary survey sentence overturned it in one search.

T019 (Glauber colourings, O(n log n) mixing for q >= Delta + 2 on every graph), first open case Delta 3, q 5.

Literature, read 3 Nov 2026 from abstracts and surveys only (full texts not yet read; no PDF tools on the Mac):
the one rapid-mixing result at q 5 on maximum-degree-3 graphs that may contain triangles is Bubley-Dyer-Greenhill,
SODA 1998, and it is for their own heat-bath chain, not single-site Glauber. Every single-site Glauber result at or
below q 5 for Delta 3 assumes triangle-free graphs (Dyer-Goldberg-Greenhill-Jerrum-Mitzenmacher 2001: triangle-free
regular, k >= (2 - eta) Delta; Goldberg-Martin-Paterson 2005: triangle-free 3-regular; spectral independence at
1.763 Delta). General-graph bounds all need q >= 6 at Delta 3. So the row case looks open for Glauber.

Why BDG needed a bigger update (the lead's own check, elementary): one-step path coupling for single-site heat-bath
Glauber in plain Hamming distance cannot contract at Delta 3, q 5, with or without triangles. Disagreement at v
(colours x vs y); a neighbour w whose other two neighbours carry colours a, b has free sets {y, c} vs {x, c}, so its
updates differ with probability >= 1/2; three such neighbours give expected change (-1 + 3/2)/n = +1/(2n). Any
computer-assisted attempt has to use a weighted metric, a k-step coupling or a block update.

Exact data (m019a): n * gap for heat-bath Glauber at q 5 on 21 cubic graphs up to n 10 lies in 0.30-0.50, so
relaxation is O(n) with a constant near 3 on every graph checked.

Where it lives: rows/T019/t019_literature.md and moves m019a, m019b in brain-repo 06_math_research/frontier;
Codex brief ~/codex_fleet/20261102/briefs/m5f-T019.md (queued, held by the disk gate on 3 Nov 00:5x).

How to apply: before claiming any coupling result for Delta 3 q 5, check it is single-site Glauber and that the
metric is not plain Hamming; before citing BDG, read its full text for the exact chain and bound.


Related: [[t019_glauber_q5_cubic_exact_gap_n_gap_0p30_min_2026_11_02]] (the m019a exact gaps this builds on).

Update 3 Nov 04:27 (an agent): all 297 BDGJ transport certificates (t019_bdg_certificates.jsonl) verified exactly. Primal = dual = value in every row, so every listed value is the exact LP optimum. Config 12 is 503/966, above the paper's printed 250/483, and its dual rules out anything lower. So the block-chain constant is (161/141) n log(n/eps), not 161/144, for every listed rim colouring. Still open: whether the rim lists are complete (m5f-T019b). Review: T019/reviews_agent/REVIEW_T019_CERTIFICATES.md.

ADDED 3 Nov 07:4x (m019m, rows/T019 commit 68bb0b31): conditional route to O(n log n). The BDGJ block chain contracts under EVERY pinning: max transport cost per unpinned block vertex adjacent to v is T = 11/21 over all 15 configurations, all Table 1 rims and all pinnings (1,145 LPs; 15 maximisers exact by integer flow; unpinned control 15 of 15 incl. 503/966). So 1 - kappa >= 6/(7n), BCCPSV EJP 2022 Thm 1.11 gives eta <= 112/3, CLV21 with b >= 1/40 gives C n log n (C huge). 11/21 proved by hand (TV 9/21 + 2/21). Open: rim-list completeness (m5f-T019b Target 4), independent read of path coupling under pinning, whole-graph sampler t019_pinned_graphs.py. Not a proof yet. See t019_pinned_route.md.

ADDED 3 Nov 09:2x (m019n, rows/T019 files ebc99320, move 4e38523d): the rim-list gap is closed without BDGJ. t019_complete.py enumerates every block (centre with 1-3 leaves, any leaf edges), every unpinned set, every nonempty set of unpinned leaves adjacent to v, and every forbidden set inside each degree budget: 15,842 problems by colour symmetry, 3,081 after free-vertex relabelling. All 2,699 whose cheap bound |F|*TV/mu reaches 11/21 were solved by LP on the difference of the laws (W1, equal to the full LP to 4e-16 on 60 controls). Max is 11/21 (20 distinct problems; the next is 503/966, config 12 unpinned), so T = 11/21 over the whole family. HiGHS floats, but laws have at most 256 points, so any other value is more than 1e-7 away. Lesson: at bar 2/3 the cheap-bound skip proves T<2/3 but not T=11/21; a second pass at bar 11/21 (177 LPs, 65 s) was needed to pin the max. Still open: an independent read of path coupling under pinning; the whole-graph sampler.

ADDED 3 Nov 09:28 (m019o, rows/T019 files c009384c, move d98bdb9a): BCCPSV abstract gives O(n log n) Glauber for q > (11/6 - eps0) Delta at constant Delta, so Delta = 3, q >= 6 is known and the whole Delta = 3 case of the row has a route (q = 5 conditional, ours). Open window per Delta: Delta+2 <= q <= floor((11/6 - eps0) Delta), i.e. Delta 4: q 6,7; Delta 5: 7..9. At Delta 4 the block chain needs T < 5/12; at q = 6 a tree neighbourhood with pinned distance-2 vertices gives drift -5 + 12*(1/2) = +1, so Hamming path coupling of this chain fails there. Delta 4, q 7 is the next case; Codex brief m5f-T019c queued for it.

ADDED 3 Nov 10:03 (m019p, rows/T019 files dec45060, move 96013da5): Delta 4, q 7, blocks with <= 3 unpinned vertices: all 103,934 local problems below the 5/12 bar (<= 2 unpinned max 19/52). Method that made it feasible: greedy feasible transport (nearest pairs first) as an upper bound settled 84,263 of 84,689 that passed the cheap bound, so no LP was needed for 3-free; 70 h of LPs became 2 min. Controls: D3q5 gives 11/21, D4q6 gives 11/21 > 5/12 (fails). Open: 4-5 unpinned (needs a reduction; brief m5f-T019c now says so).

ADDED 3 Nov 10:13 (m019q, files add9c6fb, move 8f8100a1): component lemma - block laws factor over components of the unpinned set and Hamming W1 of products is the sum over factors, so only connected unpinned sets need checking (353 logged disconnected problems: full LP = sum of component LPs to 1.4e-15). With the centre pinned all free leaves forbid its colour. Left at Delta 4 q 7: centre + 3 or 4 leaves, 4 leaf-connected leaves (brief m5f-T019c updated).

ADDED 3 Nov 10:37 (m019r, files dbae25b9, move 82ddea19): random probe (not proof) of connected 4-5-unpinned blocks at Delta 4 q 7: max greedy upper 0.376, max lower 0.368 over ~3,550 samples, bar 5/12, so q 7 at Delta 4 likely contracts. Scar: the first probe showed 0.4355 > bar from an IMPOSSIBLE shape (leaf of degree 5); the budget rule Delta - free nbrs - [adj v] never reserved slots for pinned block neighbours. Harmless in the certifying enumerations (superset), fatal in a counterexample search: check a violating case's degrees by hand before believing it.
ADDED 11:03 m019s: exact counts of the D4q7 blocks left, 854,019 problems (4 unpinned 112,217 up to 2,401-point laws; 5 unpinned 741,802 up to 16,807), from 23.8M raw; Burnside over colour group x vertex relabellings, equal to brute force at <=3 unpinned. 5-unpinned needs a cheaper coupling than pairwise greedy.
ADDED 11:41 m019t: sequential-coupling upper bound (t019_seq.py; exact 7x7 transport, product TV at edgeless base; adaptive = min over vertex per state) + certifier t019_seq_run.py. Never below LP on 426 (330 equal, gap <= 0.0625); 5-free samples adaptive max 0.338, ~greedy. Gives away up to 0.05 (3-free certified max 0.4149 vs 0.3654), so near-bar problems may need LP. Scar: shared-across-problems caches with colour-canonical keys cut 1.6 s -> 0.18 s.
ADDED 12:10 m019u: D4q7 4-unpinned blocks ALL certified < 5/12 by t019_seq_run.py (386,771 tuples = 150,034 distinct; fixed 386,025 + adaptive 746, open 0; max 0.416535, margin 1.3e-4; 504 s). Only the all-5-unpinned block remains (4.0M tuples, brief m5f-T019c).

Later the same day (18:57): a computer-assisted O(n log n) proof for this case now exists, still PROVISIONAL. It is the pinned block coupling (contraction 1-6/(7n)) fed into BCCPSV Thm 1.11 and Thm 1.6. Every step was checked by an agent, but novelty and an outside read are still open. See [[t019b_q5_delta3_glauber_nlogn_pinned_block_certs_pass_2026_11_03]]. 'Open' above stays true for the literature.
