---
name: p0434_levels_on_a_gittins_block_wait_under_twice_by_record_telescoping_2026_11_09
description: "P0434 9 Nov 01:0x: the M-SERPT levels on one Gittins block form a priority chain, and the record condition gives T_g <= 1 - x_n + x_n/x_{n-1} < 2, so the block waits under twice Gittins (heavy-traffic; chain and Q<=Q_G numerical)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T00:59:47-05:00
  status: provisional
  evidence: "a2_gap_chain.out, a2_gap_bound.out: T/K<=0.99889 on 345 blocks"
---

P0434, 9 Nov 01:0x (an agent). Conjecture (c), that the M-SERPT levels charged to one Gittins block wait at most
twice that block's Gittins waiting, now has a short proof in the heavy-traffic limit, given two facts that are so far only
numerical.

The facts (a2_gap_chain.py, 771 random shared blocks, mismatch 0): the levels L_0..L_n on a block form a priority chain,
gn(L_i) = g0(L_{i-1}), gn(L_0) = gn_G, g0(L_n) = g0_G; and Q_i <= Q_G (max 0.9969). So
S_g/W_G = sum_i (Q_i/Q_G)(m_i/m_g) g0_G gn_G/(g0_i gn_i), and it is enough to bound T_g = the same sum without Q.

The proof: write x_i = R(c_i)/R(c_{-1}) (R(c) = E[(S-c)^+], c_i the level cut ages) and y_i = P(S>c_i)/P(S>c_{-1}).
M-SERPT starts a level only at a new record of R/P(S>.), so z_i = y_i/x_i decreases from 1. Each summand
(y_{i-1}-y_i)/(x_i x_{i-1}) equals z_{i-1}/x_i - z_i/x_{i-1}; regroup, use z_j <= 1 on positive coefficients, and you get
T_g <= 1 - x_n + x_n/x_{n-1} < 2. The Gittins block condition is never used. The bound is near 2 only when the top two
levels are near-tied and carry almost no tail work, which is the worker machine twin shape (K 1.99677, T 1.99398).

Check (a2_gap_bound.py): T_g/K_g <= 0.99889 over 345 random blocks at 1-rho 1e-2..1e-6, so it holds at finite load as
well. Still open: prove the chain and Q_i <= Q_G, handle the eps term, and rule out a level that straddles two blocks.
Files are in ~/codex_fleet/runs/own_p0434 (NOTE.md 00:4x and 01:0x). Builds on
[[p0434_each_mserpt_level_waits_no_longer_than_its_gittins_block_2026_11_08]] and
[[p0434_near_two_laws_are_twins_each_carrying_one_t_g_2026_11_08]].


Addendum 9 Nov 01:1x: the chain is now proved. The inner links follow from the wait_parts definitions. The ends follow because every strict Gittins record age is a strict SERPT record age (largest-violator plus mediant argument, NOTE.md 01:1x; a2_block_records.py, 0 exceptions in 6000 laws), so blocks are unions of levels. In the heavy-traffic limit (c) now rests on Q_i <= Q_G alone.

Addendum 9 Nov 01:2x: Q_i <= Q_G is proved. The M-SERPT piece is a running-max constant, so Q_i = lam E[min(S,c0_i)^2] <= Q_G since c0_i <= c0_G. The eps term is handled too, because eps E[min(S,c)]/P(S>c) increases. So at every load and on every discrete law, M-SERPT mean waiting < 2 x Gittins mean waiting, and 2 is sharp (worker machine 1.994). This covers waiting only; residence is separate. NOTE.md 01:2x; a referee was asked under key p0434-c-proof-1109.

Addendum 9 Nov 01:4x (an agent, audit): the whole-law statement this proves, E[Q_MS] < 2 E[Q_G] at every load, is the
published Lemma 5.6 of Scully et al. (arXiv 1907.10792), which has the sharper per-valley factor 2/(1 + sqrt(1 - rho)); a Gittins
block is one Gittins valley. So this is a second proof of a known lemma, not progress on Conj. 8.1 by itself. The open part is
residence: res_excess.py finds (R_MS - R_G)/Q_G up to 0.877 at light load and still climbing (NOTE 9 Nov 01:4x). Scar for the
next reader: before calling a P0434 bound new, check it against NOTE's 8 Nov 23:56 section (Lemmas 5.6, 5.7, Props 4.9, 4.10).
