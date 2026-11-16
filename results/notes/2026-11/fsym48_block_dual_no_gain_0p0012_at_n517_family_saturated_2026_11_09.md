---
name: fsym48_block_dual_no_gain_0p0012_at_n517_family_saturated_2026_11_09
description: "[PROVISIONAL] No (FSYM48): k=2,3 block dual past n=24 lowers the symmetric FEI ledger only 4.650431 -> 4.649239 (gain 0.0012 < 0.002 bar), block edge ~1/n^2; the 4.650431 paper bound stands"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T13:20:14+04:00
  status: provisional
  evidence: "the private brain repository: 06_math_research/frontier/T021/fsym48_block_dual_2026_11_09 commit 64701ba02e"
---

Does a k-coordinate block dual (k = 2, 3) past n = 24 lower the symmetric FEI constant 4.650431? No (FSYM48, 9 Nov 2026, gpt-6.1-sol high).

Projected ledger maximum 4.650430788786 -> 4.649239445948, still binding at n = 517: a gain of 0.001191 bits per unit influence, under the 0.002 bar the brief set, so nothing was certified and paper v4.1's 4650431/1000000 stands. With the paper's 1/1000 safety pad the gain is 0.001136.

How: the restriction of a symmetric f to k revealed coordinates has an influence-weighted spectral law that is a hypergeometric thinning of the original, T_(s,i) = binom(n-r-1,s) binom(r,i-s)/binom(n-1,i). That lets the paper's scalar tangent bounds be pooled into a block dual with n level inequalities, no truth-table enumeration. The identity was checked exactly on 240 tables (31,320 coefficients); 5,340 scalar inequalities were re-evaluated in a separate 80-digit implementation (worst objective gap 2.7e-10).

Measured block advantage over the one-coordinate bound U_n: 0.027 at n = 25, 0.0042 at n = 64, falling roughly like 1/n^2. My extrapolation (not run): carrying blocks to n = 517 adds about 64^2 * 0.0042 * (1/64 - 1/517) / 517 ~ 0.0005, so the total stays near 0.0017, still under 0.002 before padding. Re-optimizing the k = 1 duals alone gives 0.0000068. The scalar-tangent dual family is close to saturated at n ~ 500; a lower constant needs a new idea (a joint multivariate majorant for D_k), not more of this.

Outputs: the private brain repository: 06_math_research/frontier/T021/fsym48_block_dual_2026_11_09 (commit 64701ba02e, 34 files read back).

