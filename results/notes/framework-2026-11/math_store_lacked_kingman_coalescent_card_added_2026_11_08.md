---
name: math_store_lacked_kingman_coalescent_card_added_2026_11_08
description: "Yes until 8 Nov 06:23: the math store had no Kingman's coalescent card (only the general coalescent card and his subadditive theorem); added with Exp(k choose 2), E T_MRCA 2(1-1/n), 2H_{n-1}, Watterson, sim-checked 7/7, ranks 1st for 3 of 5 wordings; a store write flips WAL and the sqlite3 CLI ro open gives error 14 until -shm exists"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T06:24:52+04:00
  status: verified
  evidence: "math_recall 5 W09 probes; sqlite title/body search; kingman_check.py 7/7; add_classical claim_af437f86f4; recall ranks 1,1,1,2,2"
  modified: 2026-11-08T02:25:19.338Z
---

Question: does the math store carry Kingman's coalescent, the basic genealogy model of population genetics?

It did not until 8 Nov 06:23. W09 asked math_recall five classical probability questions: Azuma-Hoeffding, optional stopping, coupling from the past, Kingman's coalescent, the Lovasz local lemma. Four had their own card at rank 1. Kingman's coalescent did not. A read-only search of node titles and bodies found the general card "Coalescent and fragmentation processes" (claim_20714692, which gives only the pair rate), two cards on Kingman's subadditive ergodic theorem, and 11 bodies that name him. None stated the holding times or the time to the most recent common ancestor.

Added under a mesh write claim on the store, with add_classical.py (tag w09-classical-c410f4d2-2026-11-08): claim_af437f86f4eb4225a8c7f4899e41ec54. It states holding times Exp(k choose 2), uniform pair choice, E T_MRCA = 2(1 - 1/n) with variance limit 4 pi^2/3 - 12, E L_n = 2 H_{n-1}, consistency and coming down from infinity, Watterson's E S_n = theta H_{n-1}, and the Wright-Fisher scaling (N generations haploid, 2N diploid). It links to claim_20714692 (0.9) and the Poisson process card claim_0df3e85951 (0.4). The spec is in the c410f4d2 as w09_kingman.json.

Check, before writing: kingman_check.py compares the exact sums with the closed forms, then runs 40,000 n = 10 trees built from one rate-1 clock per pair, so the simulation does not assume the result it tests. All seven lines agree (sim E T_MRCA 1.7935 vs 1.8, Var 1.155 vs 1.158, E L 5.645 vs 5.658, E S 4.229 vs 4.243 at theta 1.5). After writing, the new card ranks 1st for "time to most recent common ancestor coalescent", "Watterson estimator number of segregating sites" and "Kingman's n-coalescent pairwise merging rate". It ranks 2nd for "Kingman coalescent" and "coalescent comes down from infinity", behind the general card. Three of these wordings were asked before the card existed: "Kingman coalescent" (now 2nd), "time to most recent common ancestor coalescent" (1st) and "Kingman's n-coalescent pairwise merging rate" (1st). The Watterson and "comes down from infinity" wordings came after it and borrow its terms. They show the card can be found, not that a cold question finds it.

A side effect worth knowing: a writable open of the store (ResearchStore, store.py:309) switches it to WAL. Header bytes 18-19 went from 01 01, as in the 01:29 transport backup, to 02 02. Until some reader creates brain.sqlite3-shm, the sqlite3 command line with -readonly and mode=ro fails with "unable to open database file (14)". Python's sqlite3 mode=ro, math_recall and the hooks kept working: the hook harness was 89/89 right after. So a direct title search right after a card add may fail. Run math_recall once, or wait a minute, and retry; do not take error 14 as a missing or broken store.

Also seen, not measured: "coupling from the past" puts the Propp-Wilson card 1st by its own title, yet math_recall prints WEAK MATCH (score 18.04 under the usual 24). A title hit at rank 1 can still carry the weak flag.

How to apply: the store's gaps are specialist objects, as in [[math_store_lacked_6_of_10_t228_probability_tools_added_2026_11_08]], and this is one more outside tail theory. Before adding a card, search titles and bodies directly, check its formulas against a simulation that does not assume them, then check that the wordings that missed now find it.

