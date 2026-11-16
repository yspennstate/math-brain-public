---
name: fei_symmetric_min_entropy_3p3975_fsym15_2026_11_09
description: "Yes, computer-assisted (FSYM15): symmetric f has H_inf <= 3.3975 I; exact max for n<=30 is 2 or 2(n-1)/n; full rerun PASS; novelty unchecked (FSYM33)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T07:47:07+04:00
  status: verified
  evidence: "fsym15_check/reproduce.log PASS; frontier/T021/fsym_workers_2026_11_09/FSYM15"
---

Yes, computer-assisted (FSYM15, Codex gpt-6.1-sol high, 9 Nov; rerun in full on this worker machine at 07:4x, PASS): H_inf(fhat^2) <= 3.3975 I(f) for every symmetric Boolean f. Whether this is new in the literature is unchecked; FSYM33 is checking.

Exact maxima of H_inf/I for n <= 30: 2 for even n, 2(n-1)/n for odd n >= 3, attained by four functions in each dimension. My independent enumeration for n <= 14 gives the same values.

How the proof goes:
- Suppose h > C I. Then W_0 < 2^{-CI}.
- Stability (Theorem B) gives Var/I = int_0^1 s(rho) d rho <= int_0^1 exp(-N u^2/2) du < sqrt(pi/(2N)). The identity int F(N(1-rho^2)/4) = int exp(-N u^2/2) checked to 15 digits at N = 1, 5, 40, 300.
- So I >= sqrt(2N/pi) Var, which bootstraps to a large lower bound on I.
- A geometric-law Gibbs bound then gives L/I small, and Robbins plus Jensen give B/I < 3.
- The interval certificate covers n = 31..300 (smallest margin 7.2e-5) and a tail for n >= 301 (margin 0.0228).

Side results:
- B/I < 3 for symmetric f, so H < (log2(4+e) + 3) I; weaker than [[fei_symmetric_paper_v2_6p1347_level_bound_2p692_2026_11_09]].
- FSYM05: certified exhaustive max Delta_1/I_1 for n = 33..64 is at most 4.2858, by branch and bound in 2,070 s. With w05 (n <= 32) and the OR_3 value 4.8677, an explicit cutoff n0 would give H <= 4.87 I for all symmetric f. FSYM31 (extend past 64) and FSYM32 (lower n0 from FSYM04's 10^4) were briefed at 07:4x.

Rerun: fsym15_check/reproduce.log; worker folder pushed under the private brain repository: frontier/T021/fsym_workers_2026_11_09/FSYM15.

