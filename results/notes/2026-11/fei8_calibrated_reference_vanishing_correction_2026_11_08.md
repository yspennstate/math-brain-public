---
name: fei8_calibrated_reference_vanishing_correction_2026_11_08
description: "Yes on the families tried (8 Nov, FEI8): a variance-calibrated activation-cover reference makes A_c/I <= (16ln2/3)2^-3w on tribes of majorities and keeps it < 15.722 on growing-query cycle/prism DNFs; my small-law recompute matches to 11 digits"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T12:42:16+04:00
  status: verified
  evidence: "frontier T021 20d313404c; claim_19e05e74; fei8_check.py"
---

Does a better reference law fix FEI7's divergent correction? Yes on the families tried (8 Nov, FEI8, frontier T021, pushed 20d313404c, card claim_19e05e74bef3442ab76629651f898733).

Q_c is FEI5's activation-cover law (activate each term with its true probability, take the union of activated variables, draw a uniform subset) with its nonempty part rescaled to the true variance and Q_c(empty) = fhat(empty)^2. On FEI7's tribes of majorities, A_c/I <= (16 ln2/3) 2^(-3w), so it goes to 0 where FEI7's unfolded reference grew past 10^6 at w=128. Limits along s=2^w: H/I -> 4 ln 2, D/I -> (4/3) ln 2, H(Q_c)/I -> (16/3) ln 2. On connected cycle and prism vertex-clause DNFs, with optimal expected queries >= (81/512)m (the growing-depth regime FEI6 avoided), A_c/I stays under 15.722 (FEI5's constant) and I(Q_c) is within a constant of I.

My check, fei8_check.py (own Walsh transform, own Q_c from the one-sentence definition): variance and H/I on four small.csv rows to every printed digit; I(Q_c)/I to 11 digits on three; for prism_m8_k1 and cycle_m8_k2 the full Q_c law has mass 1 and covers supp P, and A_c/I, D/I agree to 11-12 digits. Not re-derived: the 2^(-3w) proof, the query floor, the large tables.

Not new as FEI: FEI for read-k DNFs is already known (claim_6be3bfaf), so the DNF families add no FEI class; the result is about which reference to compare against. General FEI and arbitrary-depth read-twice formulas are open. Next brief: an activation-cover law at an overlapping internal cut of a read-twice formula, keeping the two-read budget without DNF expansion.


Related: [[fei7_unfolding_collision_entropy_cancels_kl_tribes_of_majorities_2026_11_08]] - the obstruction this reference removes; [[fei5_summed_han_r_bounded_by_entropy_read_twice_15p72_2026_11_08]] - source of the activation-cover law and the 15.722 constant.

Later (8 Nov, FEI9): the recursive version needs each child conditioned nonempty; then the correction stays bounded with depth - [[fei9_child_conditioned_reference_bounded_raw_diverges_2026_11_08]]
