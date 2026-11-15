---
name: t021_abs_change_bound_fails_n8192_1p0017_16384_1p0040_signed_0p28_flat_2026_11_09
description: "[VERIFIED] No (T021, 9 Nov): A/room passes 1 at n=8192 (1.0017) and 16384 (1.0040, referee agrees); signed S/room flat at 0.28, so only the signed route survives"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T01:59:09+04:00
  status: provisional
  evidence: "fei_sym_agent_2026_11_08/MACMINI_NOTES.md c798bbfb39"
  originSessionId: 472b1d4f-77c3-4c94-8b40-709cb36c538f
---

---
status: verified
---
Does T021's absolute-change bound A <= room hold at large n? No. On the levelwise A/room check (bulk {h}, far {h-d}, every integer d from 0.6 sqrt n to 0.95 sqrt n, exact integers), the max is 0.9809 at n=1024 (d 24), 0.9924 at 2048 (d 34), 0.9986 at 4096 (d 49), 1.0017 at 8192 (d 70, over 1 for d 68-70), and 1.0040 at 16384 (d 100, over 1 for d 95-104). The excess grows with n. An mpmath referee at 50 digits, computed straight from the definitions with no homogeneity step, gives 1.00173 and 1.00402 at the two crossings.

The signed change S (the same sum without the absolute value), which is all the bound needs, gives S/room of 0.278 to 0.286 at every one of those peaks, flat in n (0.373 at n=1024, c=0.5). r_u is 2.83 to 2.87 bits against H0 = 4.532. So the absolute route is dead past 8192, while the signed route keeps about a factor of 3.5. an agent's own n = 512 and 1024 values (S/room 0.24-0.37) agree.

How: D is homogeneous of degree 2, so D(P,Q) = P^2 D(1, Q/P) with P = a+b and Q = a-b as exact ints. This keeps float overflow away past n = 1024. The big-int version matches the float script exactly at n = 128 and 1024.

Files: brain-repo 06_math_research/frontier/T021/fei_sym_agent_2026_11_08/ (MACMINI_NOTES.md, sym_abs_change_big.py, sym_signed_big.py, referee_mp.py, the every-d outputs), commit c798bbfb39. Related: [[fei19_reserve_floor_pi2_over_2_2026_11_09]], [[fei_t021_parity_remainder_turns_positive_c1p5_by_32768_c1p25_by_2048_2026_11_09]].

