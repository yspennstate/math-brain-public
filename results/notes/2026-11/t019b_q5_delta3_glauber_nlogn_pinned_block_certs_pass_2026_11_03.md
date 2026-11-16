---
name: t019b_q5_delta3_glauber_nlogn_pinned_block_certs_pass_2026_11_03
description: [PROVISIONAL] T019b: computer-assisted O(n log n) Glauber for 5-colourings at max degree 3 via pinned block coupling (11/21, 1-6/(7n)) + BCCPSV Thm 1.11; 910/910 certificates and Def 1.9 step checked; b=1/40 and novelty unchecked
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T18:01:56+04:00
  status: provisional
  evidence: "06_math_research/frontier/rows/T019/m5f_T019b_pinned_block/REVIEW.md"
---

Codex worker m5f-T019b (report 3 Nov 13:38; lead an agent stopped before reading it; reviewed by an agent 3 Nov) gives a computer-assisted route to O(n log n) single-site heat-bath Glauber mixing for proper 5-colourings on every graph of maximum degree 3.

The route: a pinned star-block path coupling with per-neighbour local cost at most 11/21. Drift -(d+1) + (11/21)2d, which is -6/7 at d=3, gives contraction 1 - 6/(7n) under every pinning. That feeds BCCPSV arXiv:2103.07459 Definition 1.9 and Theorem 1.11 (eta = 2 gamma^2 D M/(1-kappa) = 112/3, D/(1-kappa) = 14/3), then marginal boundedness b = 1/40, and so O(n log n).

What I checked:
- audit_transport.py reruns on a copy: 910 of 910 exact integer transport certificates pass, digest ba134e63... equal to the report's.
- geometry_check, raw_rim_coverage and witness_check outputs are byte-identical on rerun.
- 11/21 by hand: coordinate TV 3/7 + 2/21.
- The drift and the sum mu <= 2d bound.
- The Definition 1.9 step against the BCCPSV PDF text. The extended kernel keeps proper states proper, and W1 <= kappa H on all proper pairs is what the definition asks.

Not checked: b = 1/40, total connectedness under pinnings, the O(n^2) comparison route, and Target 3's entropy numbers (numerical only).

Novelty: not found in a BCCPSV abstract read or a web search on 3 Nov. BDG(J) 1998/1999 full text is not yet searched for an existing O(n log n) statement.

Status provisional until an expert reads PINNED_PROOF.md. Files: the private repository, 06_math_research/frontier/rows/T019/m5f_T019b_pinned_block/ (20 files, REMOTE_IDENTICAL).

Related: [[t019_delta3_q5_glauber_open_bdg_is_block_chain_hamming_fails_2026_11_03]] (the row state before this: BDGJ O(n^8 log n), O(n log n) open; the 'Hamming coupling fails' there is the single-site one, and this uses blocks), [[t019_glauber_q5_cubic_exact_gap_n_gap_0p30_min_2026_11_02]] (the exact small-graph gaps this run reused), [[fleet_report_lead_reviews_line_stale_reviews_live_online_2026_11_03]] (how this report nearly went unread).


Update 3 Nov 18:03: b = 1/40 (each unpinned neighbour avoids a with prob >= 1/2 since it has >= 2 allowed colours; (1/2)^3 times 1/5) and total connectedness (a blocker always has a second colour) rechecked by hand and hold. Left: Theorem 1.6's other hypotheses, read only through the worker, and novelty against BDG(J) full text.

Novelty framing, 3 Nov 18:05 (abstracts and citing works only; BDG full text not read): BDG SODA 1998 proved rapid mixing of their block heat-bath chain for q=5, Delta=3 by computer-assisted path coupling (hundreds of LPs, per DGGJM SICOMP 2001). That is the unpinned version of this coupling. BCCPSV 2021's remark after Theorem 1.11 turns a block coupling into O(n log n) Glauber mixing, provided the coupling holds under every pinning. So the content T019b adds is the pinned extension of BDG's computation (910 certificates, 11/21) plus the observation that BCCPSV applies. Someone may already have made that observation; check citers of BCCPSV and BDG before claiming anything.

Literature, 3 Nov 18:06: Dyer-Greenhill-Molloy, 'Very rapid mixing of the Glauber dynamics for proper colourings on bounded-degree graphs' (preprint 23 Aug 2000, web.maths.unsw.edu.au/~csg/papers/dgm-journal.pdf), proves optimal (O(n log n)) Glauber mixing for max degree D with k a small constant fraction below 2D. That does not reach k=5 at D=3. Its p.2 says BDG's chain for D=3, k=5 'is not Glauber dynamics' (paraphrase: a different chain, computer-assisted). So as of 2000 the q=5, Delta=3 Glauber O(n log n) bound was not known. Post-2021 citers of BCCPSV still unchecked.

Literature after 2021, 3 Nov 18:12: Jain-Mizgerd-Vigoda arXiv:2604.11938 (v2 27 Aug 2026) call polynomial Glauber mixing on all graphs at k >= Delta+2 a long-standing open problem. Their O(n log n) result needs girth >= 7 and Delta >= Delta0(delta), with Delta0 unstated in the abstract. Chen-Liu-Mani-Moitra give k >= Delta+3, which is 6 at Delta 3, on large girth. The triangle-free result k > 1.764 Delta is 5.29 at Delta 3. None covers q=5 at Delta=3 on all graphs. BDGJ's polynomial bound stays the best known Glauber result there, as far as I read. So, taking the novelty only from abstracts: T019b's claim is not in this literature. Still not shown new: no full-text read of CLMM or JMV, and no expert check of PINNED_PROOF.md.

Theorem 1.6 hypotheses, checked 03 Nov 18:52 against the BCCPSV text (p.5). The theorem (from CLV21) asks only for max degree Delta, eta-spectral independence under all pinnings (Def 1.4) and b-marginal boundedness (Def 1.5: mu^tau(sigma_x = a) >= b for all pinnings tau, all x and all a in Omega^tau_x, the colours still allowed at x). Delta = 3. eta = 112/3 comes from Thm 1.11 with contraction under every pinning (Def 1.9), checked before. b = 1/40 fits Def 1.5 as worded. Pinned neighbours never hold an allowed colour a. Each unpinned neighbour has at least 2 colours given everything else, so in turn they avoid a with probability >= 1/8. Then x = a with probability >= 1/5. With q = 5 >= Delta + 2 every proper partial colouring extends, so no allowed colour is cut off at longer range. So every stated hypothesis of Thm 1.6 holds, and what is left for T019b is the correctness of PINNED_PROOF.md's own steps beyond those I rechecked, and novelty. One caveat for any write-up: C = (Delta/b)^{O(1+eta/b)} with eta/b = (112/3)*40, about 1,493, so it is O(n log n) with an astronomically large constant.

Full read of PINNED_PROOF.md, 03 Nov 18:56, every section against the definitions. (1) The extended update on X_tau is always defined, since a free vertex has at most 3 forbidden colours out of 5, and on proper states it is the heat bath, so stationarity holds. (2) Gluing through improper states is valid: W1's triangle inequality needs only a kernel on all of X_tau, and the rim enumeration keeps improper rims and pin/exterior conflicts. (3) The d+1 blocks containing v cancel exactly, pinned centres included. Other centres count only through u in N(v) cap N(w) with w outside N[v], so sum mu <= 2d. (4) The extremiser was recomputed by hand: supports of 6 and 7, transport 22/42 = 11/21, marginal TVs 3/7 and 2/21. (5) Total connectedness: a neighbour holding the target colour has at least 2 available colours, one of them its own. (6) The b = 1/40 product is a chain rule with a tower step, not an independence assumption: each earlier event lies in the sigma-field of the other sites. (7) Thm 1.11 uses select-update dynamics with a pinning-independent centre choice, and N[w] minus U is the heat bath of N[w] under mu^tau. Nothing failed. What is left before calling it a theorem: novelty, which I found absent from the literature through 2026 but did not prove new, and an outside expert read.
