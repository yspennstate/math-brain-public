---
name: t178_rotor_walk_z2_recurrent_bou_rabee_peres_2026_11_14
description: "T178 rotor walk Z^2 with iid uniform rotors: recurrent, range t^{1/3}, claimed by Bou-Rabee-Peres 2608.23545 (unrefereed); d>=3 open; T176 Thorp O(log^{5/3} n) by Jiang 2610.18884"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T12:15:14+02:00
  status: provisional
  evidence: ""
---

Is rotor walk on Z^d with i.i.d. uniform initial rotors recurrent in d = 2 (top-200 T178)? Claimed yes, unrefereed, as of 14 Nov 2026; d >= 3 transience still open.

- Bou-Rabee and Peres, "Eulerian walkers on Z^2 have range exponent 2/3", arXiv:2608.23545 (24 Aug 2026), abstract read: for independent uniform initial directions the explored radius is of order t^{1/3} (the 1996 Priezzhev-Dhar-Dhar-Krishnamurthy conjecture), the walker visits every lattice site infinitely often, and the visited region rescaled by t^{1/3} converges to a convex body.
- T178 row (rows_16.py) and DESERVE verdict (PARTLY_SOLVED_UNVERIFIED) updated, push 218.
- Same tick: T176 Thorp shuffle, Jiang arXiv:2610.18884 proves O(log^{5/3} n) for n = 2^d (Morris had log^3 n); order still open. T172 switch queues, Ameen-Wang 2610.37521, exponent 2^k/(2^k-1) for every k (push 217). T179-T181 unchanged.

Hint: Bou-Rabee-Peres also own the Manhattan-walk problems we worked on (I0003); the same group may settle neighbouring rows. Related: [[i0003_manhattan_orientation_fields_recurrence_partial_two_audits_2026_11_13]], [[t141_oriented_kesten_mckay_claimed_he_huang_2026_11_14]].

