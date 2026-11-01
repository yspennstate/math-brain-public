# ProofNet24 P04 — proof qualification for 2026-09-16 07:46:09 report

**Parent report:** `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_07-46-09__run-report.md`  
**Parent creation commit:** `55c3c8e4e245aec6d6f0420ca27dff48e71a95ea`  
**Parent blob:** `53141d29bc03899d6c7d6fb832d92c69bf0e3c46`

One measure-zero qualification should be attached to Section 7 / equation (7.4).

The displayed quotient identity for `phi(Pq)-kappa_d` is asserted only on the set where `Pq != 0` (equivalently `nu_d-s>0`). The global stability inequality remains valid also when `Pq=0`, by the separate large-`s` argument and the convention `phi(0)=0`.

For every proper deterministic coefficient subspace `ran R` used in the fixed-top theorem, the set of sphere points satisfying `q(U) in ran R` has spherical measure zero. Indeed the coherent quadratic orbit spans all of `Sym_d^0`; hence at least one nonzero linear functional annihilating `ran R` restricts to a nonzero real-analytic quadratic function on the sphere, whose zero set has measure zero. Conditional on every selected base with `k<m`, the same statement applies. Therefore equations (8.1)--(10.1), which use the quotient only inside fresh-row expectations, hold almost surely and all stated expectation identities and `O_K(d^-3)` conclusions are unchanged.

**Status:** rendering/readback corrections remain those in `2026-09-16_07-46-09__readback-correction.md`; this addendum is a rigor qualification only and does not alter any theorem status or numerical coefficient.
