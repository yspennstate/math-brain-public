---
name: p0165_monotone_gap_closed_by_mossel_odonnell_2005_n7_not_new_2026_11_15
description: "[VERIFIED] P0165 majority-optimal r-player agreement: Mossel-O'Donnell 2005 Thm 1.4 proves optimal f is left-monotone and their Sec 5 already enumerates n<=8 (135 at n=7); our n<=7 check is not new; n=8,9 (2470, 319124 functions) would be"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T06:28:46+02:00
  status: provisional
  evidence: ""
---

P0165 (O'Donnell list: is majority on a subset optimal for r players each seeing an eps-noisy copy of x?) is Conjecture O of Mossel and O'Donnell, Coin flipping from a cosmic source: on error correction of truly random bits, Random Structures Algorithms 27 (2005), doi 10.1002/rsa.20062, arXiv math/0406504 (read 15 Nov 2026). Their Theorem 1.4: any optimal protocol has all players using one left-monotone function (Steiner symmetrization); so restricting a search to monotone, indeed left-monotone, antisymmetric functions loses nothing. Their Section 5 counts the antisymmetric left-monotone functions: 7 (n=5), 135 (n=7), 2470 (n=8), 319124 (n=9), and solves n=5 nearly completely (Fact 5.1: MAJ1 best for 2<=k<=9; MAJ3 and MAJ5 take intervals of eps from k=10, 12). Open Problem 1 there: MAJ1 best for 2<=k<=9 for all n. Our 14 Nov grid check (op/P0165: all odd f at n=5, 1,422,564 self-dual monotone at n=7, no counterexample) therefore repeats their method on a grid and is not a paper. **Why:** a paper was planned from it on 15 Nov and dropped after reading the source. **How to apply:** before writing up a small-n computer check of an open problem, read the paper that posed it for its own computer section; the next real step here is n=8,9 over left-monotone functions with exact comparison in eps. Related: [[p0165_majority_optimal_exhaustive_n_le_7_2026_11_14]].
