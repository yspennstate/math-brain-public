---
name: monotone_fei_per_coordinate_constant_is_also_1_2026_11_08
description: "[VERIFIED] FEI T021 8 Nov 04:1x: proved the monotone per-coordinate constant is 1: F=(z AND [|c|>=k/2]) OR (x AND cube), Krawtchouk middle values give R/(I ln 1/I) = 1-(ln k-0.049)/((k+1)ln2); 0.983 at k=512"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T04:19:34-05:00
  status: verified
  evidence: "T021/fei4_agent_2026_11_08/RESULT.md 'Proof that the monotone constant is 1', check_mono_closed.out (closed form = brute force k=4..14), commit 12b278ad"
---

Proved 8 Nov 04:1x EST: the per-coordinate constant in R_i <= I ln((1-I)/I) is 1 inside the monotone class too.

The family: k even, F = (z AND [|c| >= k/2]) OR (x AND c1...ck), with c in {0,1}^k.
- The pivot set of x is {c=1, z=0}. So I_x = 2^-(k+1), and every fhat(S+x) has size 2^-(k+1).
- Off the pivot, fhat(U+W) = -+T^(U) + O(2^-k), with T^(U) = -2^-k K_{k/2-1}(|U|-1; k-1).
- Krawtchouk symmetry and (1-z^2)^M (1+z) give |K| >= C(M, floor(r/2)), where M = k/2-1. So a^2/b^2 >= c 2^k/k in the middle levels.
- Hence R >= p_L I (k ln 2 - ln k - O(1)), and the ratio tends to 1.

The exact closed form (check_mono_closed.py) matches brute-force Walsh sums at k=4..14 to 2e-16.
- Ratio: 0.770, 0.851, 0.909, 0.946, 0.969, 0.983 at k = 16, 32, 64, 128, 256, 512.
- (1-ratio) ln(1/I) - ln k settles at -0.049.

Odd k does worse: N = k-1 is even there, and the middle Krawtchouk value vanishes at odd r. The earlier two-branch family and the DNF climbs near 0.7 (search-limited) were detours.

Repo: the private brain repository: 06_math_research/frontier/T021/fei4_agent_2026_11_08/RESULT.md, section "Proof that the monotone constant is 1", commit 12b278ad.

This supersedes [[monotone_fei_per_coordinate_ratio_stays_near_0_7_at_small_influence_2026_11_08]]. Related: [[per_coordinate_fei_bound_is_sharp_2026_11_08]] (all Boolean f; bent-cube family).

**Why:** the monotone lim sup was the open half of T021's per-coordinate constant. It is now closed at 1.
**How to apply:** for an extremal spectrum, think in Krawtchouk values and their parity zeros before running a DNF search. A threshold whose Krawtchouk row has no zeros spreads its weight over the middle levels.

