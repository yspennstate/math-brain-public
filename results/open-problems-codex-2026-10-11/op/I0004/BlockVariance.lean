import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

-- Summing this identity over two independently chosen block/profile indices
-- is the algebraic core of variance addition for C(r) + j*s.
theorem block_pair_variance (a b x y : ℝ) :
    ((a + x) - (b + y)) ^ 2 + ((a + y) - (b + x)) ^ 2 =
      2 * (a - b) ^ 2 + 2 * (x - y) ^ 2 := by
  ring

-- The finite pair-scatter identity in its two-point specialization.
theorem two_point_scatter (a b : ℝ) :
    2 * (a ^ 2 + b ^ 2) - (a + b) ^ 2 = (a - b) ^ 2 := by
  ring

theorem reflection_shift (u e : ℝ) :
    (u + e - 1) - u = e - 1 := by
  ring
