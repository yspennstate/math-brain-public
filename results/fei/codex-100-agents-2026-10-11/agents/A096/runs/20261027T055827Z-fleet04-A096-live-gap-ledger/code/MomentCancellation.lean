import Mathlib

-- Intended key finite three-cell cancellation check. NOT COMPILED:
-- memory admission refused and Mathlib's expected memory exceeds packet limits.
-- It covers only this affine-moment algebra, not the entropy projection theorem.
theorem three_cell_moment_cancellation (a z e : ℚ) :
    e * (a + z) - 2 * e * (a + 2 * z) + e * (a + 3 * z) = 0 := by
  ring
