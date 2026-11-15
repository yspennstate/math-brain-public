---
name: c0012_liouville_rw_subdiffusive_upper_bound_open_2026_11_13
description: "[PROVISIONAL] C0012 (Biskup notes arXiv 1712.09972, Problem 16.12): Liouville RW on Z^2, |X_T| <= T^{1/psi(beta)} e^{(log T)^{1/2+delta}} whp; open. BDG 2016 (CMP 2019) give E exit time N^{psi+o(1)}, lower bound only; the missing step is exit-time concentration"
metadata:
  type: project
status: provisional
---
C0012, rank 8 on the 200 list. Biskup, Extrema of the 2D DGFF (arXiv 1712.09972), Problem 16.12, subdiffusive upper bound: for the random walk on Z^2 with conductances e^{beta(h_x+h_y)} driven by the DGFF h (notes, eq. 13.9), show that for each beta, delta > 0, P^0_h(|X_T| <= T^{1/psi(beta)} e^{(log T)^{1/2+delta}}) -> 1 in P-probability.

What the notes say right after (text read 13 Nov 2026): the key issue is to show the exit time from B(N) is reasonably concentrated around its expectation, perhaps through better control of how the effective resistance concentrates. The notes prove the expected-exit-time theorem (13.2) and a subdiffusive LOWER-bound corollary.

Literature, checked 13 Nov 2026 (two web searches):
- Biskup-Ding-Goswami, Return probability and recurrence for the random walk driven by 2D GFF, arXiv 1611.03901, CMP 2019: recurrence, return probability T^{-1+o(1)}, E exit time from a ball of radius N equal to N^{psi(gamma)+o(1)} with psi > 2. The abstract says a full proof of subdiffusive behavior remains elusive. Effective resistance is N^{o(1)}.
- No 2020-2026 paper found that closes the upper bound. The planar-map analogues (Gwynne-Miller-Sheffield, mated-CRT maps) use different tools and do not transfer directly.

Status: open. Route: tail bounds on the exit time from the effective-resistance concentration plus the commute-time identity. The notes' sketch says this is the gap. How to apply: start there, and cite BDG and the notes.
