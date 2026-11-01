import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

/- The determinant of a symmetric 2 by 2 matrix after a rank-one update
   is affine in the update parameter. This is a finite algebraic check,
   not a formal verification of the full probabilistic proof. -/
theorem symmetric_rank_one_det (a b c u v r : ℝ) :
    (a + r * u ^ 2) * (c + r * v ^ 2) - (b + r * u * v) ^ 2 =
      a * c - b ^ 2 + r * (a * v ^ 2 + c * u ^ 2 - 2 * b * u * v) := by
  ring

theorem internal_edge_cancels (x y : ℝ) : (x - y) + (y - x) = 0 := by
  ring
