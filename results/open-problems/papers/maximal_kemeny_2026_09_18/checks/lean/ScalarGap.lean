/-!
The scalar input of the upper-bound proof, checked by Lean 4 (core, no Mathlib).

Equation (3.13) of the paper is the identity
    1/54 - s^2 (1 - s)/8 = (3s - 2)^2 (3s + 1) / 216,
from which the leading constant 1/54 and the equality case s = 2/3 are read off. It is the only
step of the argument that is pure arithmetic with no graph in sight, and it is where a sign or a
coefficient could slip unnoticed. Both forms below are closed by `grind`, Lean's built-in decision
procedure with ring normalisation, so the certificate needs no external library.

Nothing here touches effective resistance, the decomposition theorem, or any graph argument.
The inequality s^2(1-s)/8 <= 1/54 on [0,1] follows from the identity because the right-hand side
is a square times the nonnegative factor 3s + 1; that one-line consequence is not re-proved here.

Checked with:  lean ScalarGap.lean      (Lean 4.34.0; exit code 0 means every theorem is accepted)
-/

/-- Equation (3.13) with denominators cleared, over the integers:
`216 · (1/54 − s²(1−s)/8) = 27 s³ − 27 s² + 4 = (3s − 2)² (3s + 1)`. -/
theorem scalar_gap_int (s : Int) :
    27 * s ^ 3 - 27 * s ^ 2 + 4 = (3 * s - 2) ^ 2 * (3 * s + 1) := by
  grind

/-- Equation (3.13) exactly as written in the paper, over the rationals. -/
theorem scalar_gap_rat (s : Rat) :
    1 / 54 - s ^ 2 * (1 - s) / 8 = (3 * s - 2) ^ 2 * (3 * s + 1) / 216 := by
  grind
