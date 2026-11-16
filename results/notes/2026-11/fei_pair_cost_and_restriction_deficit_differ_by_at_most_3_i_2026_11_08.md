---
name: fei_pair_cost_and_restriction_deficit_differ_by_at_most_3_i_2026_11_08
description: "[VERIFIED] FEI T021 8 Nov 04:3x: Delta_i = R_i + theta*sum min(a^2,b^2), theta in [4ln2,3), proved; so my per-coordinate R bound is the 23 Sep wave-1 restriction-drop lemma (card claim_d15d0160) up to 1-I; the sharpness was also ours (draft card claim_91569f69, 24 Sep composition memory, numerical to n=81); new is the R_i form and the proof of the monotone limit"
metadata:
  node_type: memory
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T04:29:55-05:00
  status: verified
  evidence: "check_deficit.py, check_deficit_mp.py;"
  modified: 2026-11-08T09:34:44.636Z
---

Proved 8 Nov 04:3x EST. The FEI restriction deficit and the pair cost differ pair by pair by a fixed multiple of the smaller squared coefficient:
D(a,b) - K(a^2,b^2) = theta min(a^2,b^2), with theta in [4 ln2, 3).

Here D(a,b) = phi(a^2)+phi(b^2)-(phi((a+b)^2)+phi((a-b)^2))/2 and phi(t) = t ln(1/t).

The proof scales to b = 1, a = r >= 1. The excess E(r) has E' = 2[second difference of x ln x at r] - 2/r, which is >= 0 by Jensen. So E rises from 4 ln2 at r = 1 toward 3, and 3 - E is about 1/(6r^2).
Checked at 50 digits (check_deficit_mp.py). On 800 random f with n <= 10, (Delta_i - R_i)/I_i stayed in [0, 2.88].

Consequence, and the scar: my per-coordinate bound R_i <= I ln((1-I)/I) ([[per_coordinate_fei_cost_is_at_most_i_ln_e_over_i_for_every_boolean_f_2026_11_08]]) gives Delta_i <= I ln((1-I)/I) + 3I.
That is the restriction-drop lemma already in [[fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23]] (Delta_i <= (2/ln2 + log2(e/tau)) I_i in bits), up to the factor 1-I. I had written "may already be known; I have not found it". It was in our own store, on math card claim_d15d0160.
Checked at 04:3x: the sharpness is mostly ours from before as well. For Delta over all f, draft card claim_91569f69 (w505: a bent function with one flipped point) already has Delta_y/I_y >= log2((2^m-1)^2+1) at I = 4^-m.
For monotone f, [[fei_most_influential_coordinate_fails_by_composition_2026_09_24]] used threshold bases plus one point, with the same Krawtchouk formula. It found coefficient 1 in exact arithmetic up to n = 81, but did not prove the limit.
What the fei4 folder adds:
- the R_i versions: [[per_coordinate_fei_bound_is_sharp_2026_11_08]] and [[monotone_fei_per_coordinate_constant_is_also_1_2026_11_08]]
- the identity |K_{k/2-1}(r;k-1)| = C(N,M)C(M,floor(r/2))/C(N,r), which proves the monotone limit
- the rate 1 - (ln k - 0.049)/((k+1) ln 2)

Repo: the private brain repository: 06_math_research/frontier/T021/fei4_agent_2026_11_08/PER_COORDINATE_NOTE.md, section "Relation to the restriction deficit", commit 298d275a.

**Why:** two names for one quantity (R_i in FEI3's pair-cost papers, Delta_i in the restriction-induction cards) let a known lemma pass as new.
**How to apply:** before calling an FEI per-coordinate bound new, translate it to Delta_i (add at most 3 I_i). Then run math_recall on "restriction drop" or "restriction deficit" as well as "pair cost". Also grep the memory folder for "Theorem 1.3", "Krawtchouk" and "coefficient 1". Three results this morning had already been found, two of them by our own 24 Sep work.

