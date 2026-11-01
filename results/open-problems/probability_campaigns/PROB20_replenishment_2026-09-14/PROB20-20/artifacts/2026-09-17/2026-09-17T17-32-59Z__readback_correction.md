# PROB20-20 exact-readback correction — 2026-09-17T17-32-59Z report

This is a notation-only correction to the immutable report

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-20/runs/2026-09-17/2026-09-17T17-32-59Z__report.md`

at creation commit

`d9e5480ccfd8f4f1908d23b520d071929b283232`.

The report defines `u_r` as the **actual activity profile**, `v_r` as the regular majorant activity profile, and `nu` (with no subscript) as Janson's boundary mean. Exact-commit readback found five displays where the TeX symbol `\nu_r` or `\nu_j` was accidentally typed where the already-defined actual activity `u_r` or `u_j` was intended.

The five corrections are:

1. Equation (3.3): `\nu_r = ...` should read `u_r = ...`.
2. Equation (4.5): `\nu_j \ge \kappa v_j` should read `u_j \ge \kappa v_j`.
3. Section 12's repeated display of the alternating-cliff example: `\nu_r = ...` should read `u_r = ...`.
4. Equation (13.3): `\nu_r \le v^{(R)}_r` should read `u_r \le v^{(R)}_r`.
5. The displayed contact inequality in the proof of Corollary 13.2: `\nu_r \ge \kappa v^{(R)}_r` should read `u_r \ge \kappa v^{(R)}_r`.

All surrounding prose, subsequent formulas, and proofs already use `u_r` consistently. In particular, equations (3.4)--(3.7), (4.4), (5.1)--(5.7), (8.5)--(10.2), the proof of Lemma 13.1, equation (13.7), and the `ledger_delta` use the intended actual activity variable.

No hypothesis, inequality, theorem statement, proof step, status, or frozen metric changes. The corrected mathematical claim remains Theorem 6.1: for a fixed divisibility-chain law with actual activities `0<u_r<=v_r`, a summable locally regular majorant `v`, and infinitely many roots with `u_j>=kappa v_j`, every fixed admissible `m_n/n->lambda>nu` has a deterministic subsequence on which `Y_(1)/n -> lambda-nu` in probability, so the restricted-class limsup metric equals `lambda-nu`.

The source-level status remains **PARTIAL / OPEN** and the unrestricted arbitrary-weight branch of Janson Problem 18.39 remains unchanged.