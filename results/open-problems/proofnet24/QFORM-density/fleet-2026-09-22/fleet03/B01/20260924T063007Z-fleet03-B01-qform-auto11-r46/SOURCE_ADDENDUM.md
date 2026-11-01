# Source addendum for fleet03/B01 r46

This addendum supplies one omitted immutable source pin and corrects one internal section reference. It changes no theorem, proof, hypothesis, constant, or status in `REPORT.md`.

1. The sign-cut/cross-cut lemma used in Theorem 4.1, Case B, is proved in full at
   `yspennstate/math-open-problems@0993b0d6fcaadedcc7873bf89d99c5eedf630dc0`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260924T002941Z-auto11/REPORT.md`, Lemma 4.1. In the notation of the current report it states that if `s=||S||_op` and `max_i |S_ii|<=theta s`, then some original-coordinate cut has cross block `B` with `||B||_op >= (1-theta)s/2`. The current proof uses `theta=1/3`, hence `||B||_op>=s/3`.

2. Section 2.1 of `REPORT.md` says the fleet04/B01 partner theorem is applied in Section 7. The actual application is Section 8 (`Actual fleet04/B01 partner application: integrated frequency control`).

Full QFORM status remains OPEN. The new supporting results remain pending independent review.
