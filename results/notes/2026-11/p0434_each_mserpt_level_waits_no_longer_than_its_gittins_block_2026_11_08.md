---
name: p0434_each_mserpt_level_waits_no_longer_than_its_gittins_block_2026_11_08
description: "P0434 8 Nov 23:3x: proof sketch that each M-SERPT rank level waits no longer than its Gittins block, at every level and load (needs a referee)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T23:32:58-05:00
  status: provisional
  evidence: "own_p0434 a2_blocks/a2_mass/a2_work/a2_work_lemma .out"
---

P0434 (M-SERPT vs Gittins, discrete laws), 8 Nov 23:3x, an agent. Proof sketch, needs an independent referee.

Claim (a''): for every M-SERPT rank level L and every load, M-SERPT's waiting of L is at most the Gittins waiting of L's
Gittins block B (the classes of L and the levels below sharing a Gittins final rank with a class of L), hence at most
the Gittins waiting of L and every level below. Waiting factorises as (mass_L/gapn_L) * B_L with B_L = lam sq/(2 gap0).

Proof in three pieces (own_p0434/NOTE.md 22:4x, 23:2x, 23:3x):
1. M-SERPT's rank is a running max, so its level-L work set is min(S, c0_MS) with no tails (0 tails on 1233 levels).
2. Mediant lemma: G(a) <= G(c_L) for left ends a in [c_L, c0_MS), c_L the level's jump point (V(c_L) = r_L); split the
   Gittins ratio at the optimal horizon b*. Hence Gittins' cut for every block class is >= c0_MS, so sq and gap0 dominate
   termwise: B_L <= B_G,k for each k in B.
3. Mass bound: mass_L/U(c_L) <= mass_B/U(c_G), from V(c_L) = r_L, V(c_G) < r_L and the classes between c_G and L lying in
   the block. Then W_MS(L) <= (sum_B p_k/gapn_G,k) B_L <= W_G(B).
Checks: a2_blocks.py 300 laws x 4 loads (merged levels max 0.686, worker-machine 0.9927), control with L's own classes fails at
9.40; a2_mass.py last inequality 0.99994 on the worker machine (nearly sharp); a2_work.py 0 failures; a2_work_lemma.py max
-1.88e-2. Pushed to research-repo codex-fleet runs/own_p0434.

Limits: assumes the SOAP waiting formula (split_T) and that the classes of an M-SERPT level share their factors. It does
not bound the full M-SERPT/Gittins ratio: blocks of different levels overlap, and residence is separate. Route history:
the 22:5x 'no factor-wise route' reading was a weighting artifact (compare against blocks, not all lower classes).
Related: [[p0434_lemma_b_by_mserpt_rank_level_survives_splitting_tight_near_two_2026_11_08]],
[[a_family_max_was_set_by_a_level_both_policies_share_2026_11_08]].


Addendum 23:4x (a2_overlap.py, a2_share.py, NOTE.md 23:4x): summing (a'') counts a block once per M-SERPT level using
it (worker-machine: three levels on one block, ratio 1.96 under the overlap bound 2.92). Per-block conjecture (c): the levels
sharing a Gittins block wait at most 2 x the block's Gittins waiting. worker machine 1.9939, random laws <= 1.449 (2300 laws,
up to 4 levels per block). (c) would give M-SERPT waiting <= 2 x Gittins waiting. Next: hunt near-tied triples.

Addendum 23:5x (a2_share_hunt*.py, NOTE.md 23:5x): no counterexample to (c). Hill-climbs from the worker machine (a local max,
1.99387) and from 3000 random three-twin laws (best climb 1.9689) never pass 2; the near-2 laws always have two heavy twin
levels on one block, never three.

Addendum 9 Nov 00:0x (a2_share_prefix.py, a2_share_mass.py, NOTE.md 9 Nov 00:0x): (c) for two levels on a block is
immediate from (a''). For three or more, charging each level to its own classes fails: the telescoping bound
W_MS(L_i) <= W_G(B_i) - W_G(B_{i-2}) reaches 111.9 on the worker machine, whose lowest level holds 0.991 of the block's Gittins
waiting and waits 0.004 of it while the two above wait 0.993 and 0.997. Per block, the work factor (largest B_L against
the mean B_G) stays <= 1, but the summed mass factor is 2.98 there, so a proof must keep each level's mass with its own B_L.

Addendum 9 Nov 00:1x (a2_share_below.py, a2_share_rest.py): a prefix form, levels below a block's top waiting at most
their classes' Gittins waiting, fails at 1.187 on a block of three medium levels (0.505, 0.593, 0.438). What holds:
(r) every level of a block except its heaviest waits at most W_G(g) together: max 0.99666 (worker-machine), 0.943 on 2000
random laws. (a'') plus (r) gives (c), so (r) is the open step.

Addendum 9 Nov 00:2x (a2_rest_hunt.py, a2_rest_break.py): (r) is FALSE. A climbed seven-atom law has a block of three
levels at 0.571, 0.544, 0.572 of W_G(g): rest 1.115, while (c) holds at 1.687 (stable 1-rho 1e-5..1e-7). The open
question for (c) is whether four or more medium levels can share one block; nothing so far shows it.

Addendum 9 Nov 00:3x (a2_four_hunt.py, a2_four_held.py): blocks of 4-8 levels exist (798 of 1500 laws of four near-tied
pairs) but never pass 2: best sampled 1.614, climbs held to 4+ levels reach 1.884. Unheld climbs fall back to 2-3
levels (best 1.894). (c) stands numerically, max 1.99387 (worker-machine); no proof mechanism yet.

Addendum 9 Nov 00:4x: the levels charged to one Gittins block are an exact priority chain (each level's new gap is the
old gap of the level below; top g0 = g0_G, bottom gn = gn_G), on all 771 random shared blocks (a2_gap_chain.py). So
S_g/W_G = sum_i (Q_i/Q_G)(m_i/m_g) g0_G gn_G/(g0_i gn_i) exactly, Q_i/Q_G <= 0.9969 sampled, and (c) reduces to the scalar
bound T_g = sum_i (m_i/m_g) g0_G gn_G/(g0_i gn_i) <= 2 (worker machine 1.99398, random max 1.589). Not yet proved.

Addendum 9 Nov 01:0x: conjecture (c) now has a heavy-traffic proof from the chain and the M-SERPT record condition, T_g <= 1 - x_n + x_n/x_{n-1} < 2; see [[p0434_levels_on_a_gittins_block_wait_under_twice_by_record_telescoping_2026_11_09]].
