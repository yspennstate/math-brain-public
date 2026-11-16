---
name: symmetric_fei_best_constant_4p650431_v4_1_repo_23b66aa_2026_11_09
description: "Fourier entropy-influence (FEI) constant for symmetric Boolean functions, best proved: H(f^2) <= 4.650431 I(f) for every symmetric f (paper v4.1, 4650431/1000000, yspennstate/symmetric-fei-constant 23b66aa; seed C_24 exact, ledger max n=517, tail a=1/45). Ends the chain 8.26 -> 6.19 -> 6.1347 -> 4.8677 -> 4.657435; FSYM48 block dual gains only 0.0012"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T19:03:21+04:00
  status: verified
  evidence: "repo yspennstate/symmetric-fei-constant 23b66aa; v4_check my_v41_check.py + check_extension.py replay; FSYM48 64701ba02e"
  supersedes: fei_symmetric_paper_v2_6p1347_level_bound_2p692_2026_11_09
---

What is the best proved Fourier entropy-influence (FEI) constant for symmetric Boolean functions? 4.650431: every symmetric f on n bits has H(f^2) <= 4.650431 I(f) (paper v4.1, constant 4650431/1000000, 9 Nov 2026).

Where it is: yspennstate/symmetric-fei-constant, head commit 23b66aa "Version 4.1: constant 4.650431"; the Zenodo draft 24072301 holds the same v4.1 (md5 aa8b524e) and waits for the author's publish click.

How it is proved: an exact seed C_24 = 3.953557670092 for n <= 24, then a ledger over n whose maximum is at n = 517, block-checked to n = 33,554,432, and a tail argument with a = 1/45 (4.647117) beyond. Checked here by my_v41_check.py (C_24 equal to the paper fraction, the ledger re-added twice, an independent R_{1/45}) and a replay of check_extension.py. B_{k,n} for n = 21..24 rest on their census plus the FSYM46 referee. Cited: the restriction inequality is the key inequality of Gonzalez-MacManus-Pereyra (arXiv:2606.00246); Hod (arXiv:1711.00762) gives FEI constant > 6.4548 for general f, so the symmetric class is strictly easier.

What did not improve it: FSYM48's k = 2, 3 block dual past n = 24 lowers the ledger only to 4.649239 (gain 0.0012, under the 0.002 bar), so this family is saturated near 4.65.

The chain it ends: 8.26 -> 6.1908 -> 6.1347 (paper v2) -> 4.8677 (FSYM32, all n by restriction, unrefereed) -> 4.657435 (v4) -> 4.650431 (v4.1). Min-entropy companion: H_inf <= 3.3975 I (FSYM15).

Related: [[symmetric_fei_v4_4_6574_checked_repo_and_zenodo_draft_2026_11_09]], [[fsym48_block_dual_no_gain_0p0012_at_n517_family_saturated_2026_11_09]], [[fei_symmetric_all_n_restriction_k_4p8677_fsym32_2026_11_09]], [[fei_symmetric_min_entropy_3p3975_fsym15_2026_11_09]], [[fei_symmetric_paper_v2_6p1347_level_bound_2p692_2026_11_09]].

