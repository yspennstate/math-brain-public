---
name: fei7_unfolding_collision_entropy_cancels_kl_tribes_of_majorities_2026_11_08
description: "Can FEI's unfolding collision term J be bounded alone on read-twice formulas with growing decision depth? No (8 Nov, FEI7): A/I and KL/I diverge like (37/32)^w/w and cancel, H/I -> 4 ln2; 5 small cases match to 12 digits"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T12:06:31+04:00
  status: verified
  evidence: "the private brain repository: 5fdedfedc7; fei7_check.py"
---

No (8 Nov): on read-twice formulas whose decision depth grows, the occurrence-unfolding collision term cannot be bounded on its own. FEI7 (Codex) used tribes of majorities F_{s,w} = OR_j AND_k MAJ on disjoint blocks, s = 2^w, decision depth Theta(2^w). There A/I and D(P||Q)/I both grow like (8/3)(1-1/e)(37/32)^w/w and cancel in H(P) = H(Q) + A - D, while H/I -> 4 ln2. The local seed is the mismatch between a majority (probability 1/2) and its unfolding (37/64).

Checked by an agent: the identity and local numbers by hand. fei7_check.py, my own brute force from the definitions, matches small.csv to 12 digits on five (s,w) cases up to 24 occurrence inputs. The large-w asymptotics were not re-derived. Row T021, pushed 5fdedfedc7; math card for the obstruction.

How to apply: a FEI proof through the unfolding must keep A - D together, or swap Q for a reference law calibrated to the true gate probabilities. This does not bear on FEI itself: the family is a disjoint composition, so its H/I being bounded is expected. It follows [[fei6_read_twice_chains_fei_bounded_but_easy_regime_unfolding_fails_2026_11_08]] (bounded-query regime). Same morning: [[fei_per_coordinate_kkl_form_han_r_at_most_i_ln_e_over_i_2026_11_08]].

