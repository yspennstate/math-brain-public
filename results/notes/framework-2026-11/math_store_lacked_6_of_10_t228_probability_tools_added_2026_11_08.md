---
name: math_store_lacked_6_of_10_t228_probability_tools_added_2026_11_08
description: "[VERIFIED] Partly: of 10 classical probability tools behind T228, the math store had 4 (Kesten-Goldie, Lp log-convexity, Borel-Cantelli, Doeblin); 6 added 8 Nov (Goldie renewal, convex order, Lyapunov, Vervaat, Breiman, Diaconis-Freedman)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:23:08+04:00
  status: verified
  evidence: "math_recall probes x3 wordings, read-only title/body search, add_classical dry+write, readback node/claim/edges; 8 Nov 05:0x-05:22"
---

Partly. On 8 Nov 05:0x-05:22 an agent probed the second machine math store (math_recall.py, three wordings each) for ten classical probability tools that the T228 tail proof leans on. Four were there and six were not.

Already in the store (do not add again):
- Kesten-Goldie theorem, claim_b79d1ca6bf. Found by its name or "power tail of the stationary solution of X = AX + B"; missed by "stochastic recurrence equation" and "perpetuity", words the card does not use.
- Log-convexity of Lp norms (Lyapunov interpolation), claim_d25b458ed3.
- Borel-Cantelli lemma, the Doeblin coupling under a minorization, the cumulant generating function.

Added 8 Nov (audited before writing, under a mesh write claim on the store, each with links):
- Goldie's implicit renewal theorem, claim_ba6cb54df7
- Gaussian convex order in scale, claim_ff2778ae0c
- Lyapunov's moment inequality (Lp norm nondecreasing in p), claim_1b062a3ea2
- Vervaat's perpetuity theorem for X = AX + B, plus the Goldie-Maller iff, claim_2b5333bda8
- Breiman's lemma, claim_286b12aff3
- Diaconis-Freedman iterated random functions, claim_a16132cda4

Check: the wordings that missed now find the new card 1st or 2nd, except "L^p norm increasing in p" (the card says nondecreasing) and "Wasserstein contraction of an iterated random function" (the card works in the Prokhorov metric). All six have one node, one claim and no dangling edges. They ride the first post-reboot increment, which a dry export put at 508 nodes, 257 claims and 266 edges with 0 secret-scan hits.

How to apply: before adding a classical card, search node titles and bodies in the store directly (sqlite3 read-only on nodes.title/body), not only math_recall; a card can exist under its own name and be missed by a synonym. The adder is add_classical.py. Related: [[t228_s1_s9_second_reader_confirms_sim_n_0p26_tail_matches_2026_11_08]].

Coverage, 8 Nov 05:24: 40 named results of a first graduate probability course (laws of large numbers, CLT, Berry-Esseen, LIL, 0-1 laws, martingale theorems, ergodic theorems, Donsker, Cramer, Sanov, Girsanov, Ito, Feynman-Kac, de Finetti, Kesten-Stigum, Borell-TIS and more) are all in the store: 37 under their own title, 3 inside other cards. So the store's gaps are specialist tools (tail theory, iterated random functions), not textbook basics. A body search must allow the name before or after the subject: '%Polya%random walk%' missed 'random walk ... recurrent exactly for d<=2 (Polya)'. Polya's theorem now also has its own card, claim_3df9b7f812, linked depends_on to the concept card claim_b4d42412b2. Script: prob_coverage.py.

Recall wording, 05:32 8 Nov: the Lyapunov card is rank 1 for "Lyapunov's inequality" and for its formula, but absent from the top 8 for "L^p norm is increasing in p" (the body never says 'norm' or 'increasing'); the Diaconis-Freedman card is rank 1 once "iterated random maps contract to a stationary law" is one of the wordings. Not fixed in the cards: the store is append-only (no update API, a unique digest per row), so a body edit would break its digests. Name the theorem when asking.
