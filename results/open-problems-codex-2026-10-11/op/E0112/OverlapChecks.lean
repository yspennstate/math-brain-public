import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

-- Algebraic cancellation in the Poisson two-replica Laplace functional.
theorem poisson_overlap_cancellation (lam a b : ℝ) :
    (1 + lam * a) * (1 + lam * b) - 1 - lam * (a + b)
      = lam ^ 2 * (a * b) := by
  ring

-- The square-root estimate used to pass from an L1 local limit theorem
-- to convergence of half-moments. No probabilistic theorem is formalized here.
theorem square_root_error (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    (Real.sqrt a - Real.sqrt b) ^ 2 ≤ |a - b| := by
  have hsa := Real.sq_sqrt ha
  have hsb := Real.sq_sqrt hb
  have hna := Real.sqrt_nonneg a
  have hnb := Real.sqrt_nonneg b
  rcases le_total a b with h | h
  · have hs := Real.sqrt_le_sqrt h
    rw [abs_of_nonpos (sub_nonpos.mpr h)]
    have hp := mul_nonneg hna (sub_nonneg.mpr hs)
    nlinarith
  · have hs := Real.sqrt_le_sqrt h
    rw [abs_of_nonneg (sub_nonneg.mpr h)]
    have hp := mul_nonneg hnb (sub_nonneg.mpr hs)
    nlinarith
