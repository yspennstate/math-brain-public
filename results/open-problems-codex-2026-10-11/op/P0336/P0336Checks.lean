import Mathlib.Data.Real.Sqrt
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

-- Algebraic core of the excess-cost rationalization; no analytic assumptions hidden.
theorem excess_identity (d h r : ℝ) (hr : r ^ 2 = d ^ 2 + h ^ 2) :
    (r - d) * (r + d) = h ^ 2 := by
  nlinarith

-- Squared-height uncrossing, used for the surrogate only.
theorem height_uncrossing (a a' b b' : ℝ) (ha : a < a') (hb : b < b') :
    (a - b) ^ 2 + (a' - b') ^ 2 < (a - b') ^ 2 + (a' - b) ^ 2 := by
  have hp : 0 < (a' - a) * (b' - b) := mul_pos (sub_pos.mpr ha) (sub_pos.mpr hb)
  nlinarith

-- Rigorous separation of costs for the two-point counterexample.
theorem rank_counterexample :
    Real.sqrt (416 / 100 : ℝ) + Real.sqrt (404 / 100 : ℝ) <
    Real.sqrt (109 / 100 : ℝ) + Real.sqrt (909 / 100 : ℝ) := by
  have h1 := Real.sq_sqrt (show (0 : ℝ) ≤ 416 / 100 by norm_num)
  have h2 := Real.sq_sqrt (show (0 : ℝ) ≤ 404 / 100 by norm_num)
  have h3 := Real.sq_sqrt (show (0 : ℝ) ≤ 109 / 100 by norm_num)
  have h4 := Real.sq_sqrt (show (0 : ℝ) ≤ 909 / 100 by norm_num)
  have n1 := Real.sqrt_nonneg (416 / 100 : ℝ)
  have n2 := Real.sqrt_nonneg (404 / 100 : ℝ)
  have n3 := Real.sqrt_nonneg (109 / 100 : ℝ)
  have n4 := Real.sqrt_nonneg (909 / 100 : ℝ)
  have u1 : Real.sqrt (416 / 100 : ℝ) < 2040 / 1000 := by nlinarith
  have u2 : Real.sqrt (404 / 100 : ℝ) < 2010 / 1000 := by nlinarith
  have l1 : 1044 / 1000 < Real.sqrt (109 / 100 : ℝ) := by nlinarith
  have l2 : 3014 / 1000 < Real.sqrt (909 / 100 : ℝ) := by nlinarith
  linarith
