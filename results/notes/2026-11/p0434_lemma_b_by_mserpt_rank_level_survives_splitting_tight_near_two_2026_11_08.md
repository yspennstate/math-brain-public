---
name: p0434_lemma_b_by_mserpt_rank_level_survives_splitting_tight_near_two_2026_11_08
description: "P0434 8 Nov 21:0x: lemma (b) restated by M-SERPT rank level (R-1 <= largest level share) is split-invariant and held on the ray, split ray and Mac mini laws; hunt reached 0.99982, nothing above 1"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T21:07:05-05:00
  status: provisional
  evidence: "codex_fleet/runs/own_p0434/rank_level.out rank_level_hunt.out"
---

P0434 (M-SERPT vs Gittins, Conj. 8.1 T_MS <= 2 T_G), 8 Nov 21:0x, an agent. Lemma (b) R - max_k m_k <= 1 died under atom splitting ([[p0434_lemma_b_false_per_class_charges_die_under_atom_splitting_2026_11_08]]). Restated by M-SERPT rank level it survives every test so far.

Statement (b'): group classes into M-SERPT rank levels (maximal runs of k with the same final-piece rank, the running max of the SERPT left-end values; exact ties). With m_k = p_k T_MS,k / T_G and M_L the sum of m_k over a level, R - 1 <= max_L M_L; equivalently the M-SERPT shares of all levels but the largest sum to at most one T_G. CANDIDATE, not proved.

Measured (codex_fleet/runs/own_p0434/rank_level.py, rank_level_hunt.py, .out files; NOTE.md 21:0x):
- Split-invariant where (b) was not: near copies of an atom fall in one level. (R-1)/max share 0.784/0.770/0.745 at K 26 split x1/x2/x4, 0.897/0.893/0.884 at K 101 (b's rest went 0.82 -> 1.41 and 0.91 -> 1.56).
- Mac mini law: 0.789/0.977/0.997 at 1-rho 1e-5/1e-6/1e-7.
- Nelder-Mead push (400 evals a start): polished 1.985 law 0.999820 (R 1.984249, max share 0.98443, 1-rho 1.13e-7), Mac mini + mid atom 0.998564. Nothing above 1.
- Tight near 2: one level carries m ~ 0.98 with g ~ 0, every other level nets m ~ g.

Scar: the statement needs EXACT rank ties. At tol 1e-6 the Mac mini twins merge with the small classes and the ratio drops to 0.49, which proves nothing. The levels must be M-SERPT's own priority classes, not size clusters.

How to apply: next, a denser breaker hunt (random m 4-6 and the three-twin optimum), then the t -> 0 first-order check on the ray with rest_pi_limit.py's mpmath shares. Do not call it a lemma until one of those passes and someone proves it.


Addendum 8 Nov 21:1x: rank_level_hunt2.py (15 starts, perturbed and random, m 4-6) found nothing above 1; best 0.998440 at R 1.502 with max share 0.503, so the near-tightness is a family (one level with g ~ 0, the rest summing to just under one T_G), not only the near-2 laws.

Addendum 8 Nov 21:2x (level_cap_hunt.py): (b') is never stronger than (b) (largest level share >= max m_k), so on the ray it inherits (b)'s sup 1 - 1/K. Scar: I expected the ray's three ranks to be strictly increasing; near f -> 1 the second SERPT value drops below E[S] and atoms 1, 1+d share a level, so print the ranks before saying levels = atoms. Two levels reduce (b') to the per-level cap (a') M_L <= 1; a hunt on (a') only found the one-level corner at exactly 1.

Addendum 8 Nov 21:3x (one_level_r.py): one M-SERPT level is exactly an NBUE law (mean residual <= E[S] at every age), M-SERPT is then FCFS, and 600 random one-level laws gave R = 1.000000000000 (Gittins = FCFS), so (a') holds with equality at one level. Recalled as Aalto-Ayesta-Righter 2009 (Gittins reduces to FCFS for NBUE); not in the math store, check the paper before citing. Inside every level the residual law from the level's start is NBUE on that stretch: the structure a proof of M_L <= 1 can use.

Addendum 21:4x (two_level_terms.py, NOTE.md 21:4x): on the Mac mini and polished laws every level share is waiting to
four digits (residence <= 2e-4 T_G). Gittins puts ~0.96-0.99 T_G of waiting on the two small atoms; M-SERPT gives them
~0.004 and gives about one T_G to EACH twin (0.959, 0.963 at 1e-7 Mac mini; 0.987, 0.985 polished). The twins' rank
gaps above the bottom level are 1.2e-8 / 2.9e-7 (Mac mini) and 4e-6 / 1.1e-4 (polished), so the separate levels exist
only under exact ties. New candidate (a''), untested beyond these laws: a level's M-SERPT waiting <= the Gittins
waiting of that level and all below it (0.95868 <= 0.96568, 0.96303 <= 0.96572); it implies (a').

Addendum 21:5x (a2_cum_wait.py, a2_multi.py, NOTE.md 21:5x): (a'') level M-SERPT waiting <= Gittins waiting of that
level and all below held everywhere tried: Mac mini 0.9923/0.9972, polished 0.9947, hunt2 best 0.99924, split ray up
to 0.99999, 300 random laws max exactly 1 (one-level, FCFS = Gittins) and up to 0.9999999999 with >= 2 levels. Tight,
never above. It gives (a') and two-level (b'); three or more levels still need (b').

Addendum 22:0x (a2_factors.py, a2_halves.py, NOTE.md 22:0x): CORRECTION to 21:5x - the random laws' near-1 (a'') maxima
were the top level, whose waiting is identical under both policies, so they were not evidence; the informative maxima
are 0.992-0.9992 at the twins (Mac mini, polished, hunt2) and 0.99998 at the ray's bottom level. Factoring a level's
M-SERPT waiting as (mass_L / gap_new_L) * lam sq/(2 gap0): half (i) mass_L <= gap_new_L holds with a short proof (rank >=
E[S]); half (ii) lam sq/(2 gap0) <= cumulative Gittins waiting is FALSE (4.47 on a random law, 8427 at a top level). A
proof must keep the two factors together. Scar: a max over a family can be set by a level where the two policies
coincide; report the maximiser's level before calling a bound tight.

Addendum 22:1x (a2_tail.py, NOTE.md 22:1x): relaxing mass_L to P(S > c_L) also breaks (a'') (1.197 random, 1.002 ray),
always at the bottom level, where P(S > 0) = 1 > mass_0. Above the bottom the two agree to 3-4 digits. The bottom level
needs its own same-classes argument: mass_0 lam sq_0/(2 gap0_0) <= Gittins waiting of those classes.

Addendum 22:2x (a2_bottom.py, NOTE.md 22:2x): at the bottom M-SERPT level, (a'') holds class by class: M-SERPT's
lam sq <= each class's Gittins lam sq and M-SERPT's gap0 >= each class's Gittins gap0, max ratio exactly 1 over 300
random laws x 4 loads plus the Mac mini law and split ray. So the bottom case is two monotonicity facts (Gittins puts at
least as much work ahead of each bottom class), still to be proved.

Addendum 22:4x (a2_grank.py, a2_workset.py, a2_workset_ctrl.py, NOTE.md 22:3x-22:4x): the bottom-level case is NOT a
rank comparison (Gittins' final rank of bottom classes < E[S] in 109/300 laws) but IS a work-set inclusion: M-SERPT's
work set at E[S] sits inside Gittins' work set for each bottom class on all 300 laws + Mac mini + ray, while the reverse
inclusion fails on 109 (control trips). Proof of the inclusion still open.

Addendum 22:4x (a2_lemma.py, NOTE.md 22:4x): PROOF SKETCH of (a'') at the bottom M-SERPT level. M-SERPT's bottom work
set is min(S, c) (running max, no tails; 0/2000 laws). Lemma: Gittins rank G(s_{i-1}) <= G(0) at every left end before
c, by a mediant split of the Gittins ratio at the optimal horizon b* (b* > a: G(0) mediates A >= G(0) and X >= G(a);
b* <= a: E[S] mediates G(0) and V <= E[S], so G(0) >= E[S] >= G(a)). Hence Gittins' c0 >= c for every bottom class and
its waiting factors dominate. Strict on 2000 random laws (max -2.06e-4). Provisional: needs an independent read; upper
levels still open.

Addendum 22:5x (a2_upper.py, a2_upper2.py, NOTE.md 22:5x): above the bottom level, W_MS(L) = (mass_L/gapn_L) B_L vs
W_G(<=L) = sum w_k B_G,k (w_k = p_k/gapn_G,k). The mass factor (2) mass_L/gapn_L <= sum w_k holds everywhere below the
top (Mac mini 0.996/0.997, random <= 0.924), but B_L <= mean_w B_G fails (4.49 on the 4.47 law, level 1, where (2) =
0.22). The factors trade off, so a proof of the upper levels must couple them; no factor-wise route.

Addendum 23:0x (a2_blocks.py, a2_blocks_where.py, NOTE.md 23:0x): correction to 22:5x: the factor-wise route survives
when each M-SERPT level is compared only with the Gittins blocks it meets (classes of L and below sharing a Gittins
final rank with a class of L). Then (1'') B_L <= w-mean B_G over the block and (2'') mass_L/gapn_L <= sum w over the
block hold on 300 laws x 4 loads (merged levels: W 0.686, (1'') 0.963, (2'') 0.887; Mac mini 0.9927), giving
W_MS(L) <= W_G(blocks(L)). The 4.49 came from weighting in the bottom class. Control (L's own classes only) fails at 9.40.

Addendum 23:2x (a2_mass.py, NOTE.md 23:2x): PROOF SKETCH of (2'') mass_L/gapn_L <= sum_B p_k/gapn_G,k. Keys: V(c_L) = r_L
at M-SERPT's jump point, so U(c_L) >= lam r_L P(S>c_L); V(c_G) < r_L at any earlier left end gives dW < r_L P(c_G<S<=c_L);
the classes between c_G and L all sit in the Gittins block (running max of final ranks). Uses only that Gittins ranks
are a running max. Steps hold on all 153 levels; last inequality 0.488 random, 0.99994 on the Mac mini level 2.
Left: (1'') B_L <= w-mean of B_G over the block.

Addendum 23:3x (NOTE.md 23:3x): (1'') proved too, so (a'') holds at every M-SERPT level (sketch, needs a referee). See
memory p0434_each_mserpt_level_waits_no_longer_than_its_gittins_block_2026_11_08.
