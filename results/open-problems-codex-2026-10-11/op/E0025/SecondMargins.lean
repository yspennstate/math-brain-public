import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

-- The open interval of admissible band exponents exists precisely on the
-- strict side of the threshold used in Theorem B.
theorem band_exponents (a b K : ℝ) (ha : 0 < a) (ha1 : a < 1)
    (hb1 : b < 1) (hK : b * (1-a) / (a * (1-b)) < K) :
    ∃ p q : ℝ, b / a < p ∧ p < q ∧ q < K * (1-b) / (1-a) := by
  have hc : b * (1-a) < K * (a * (1-b)) :=
    (div_lt_iff₀ (mul_pos ha (sub_pos.mpr hb1))).mp hK
  have hi : b / a < K * (1-b) / (1-a) := by
    apply (div_lt_div_iff₀ ha (sub_pos.mpr ha1)).mpr
    nlinarith [hc]
  refine ⟨(2 * (b/a) + K*(1-b)/(1-a))/3,
    ((b/a) + 2 * (K*(1-b)/(1-a)))/3, ?_, ?_, ?_⟩ <;> linarith

example : (3 : ℚ)/4 * (1-1/4) / ((1/4)*(1-3/4)) = 9 := by norm_num
example : (3 : ℚ) < 25/8 := by norm_num
example : (25 : ℚ)/8 < 13/4 := by norm_num
example : (13 : ℚ)/4 < 10 * (1-3/4) / (1-1/4) := by norm_num
example : (25 : ℚ)/8 * (51/50) < 13/4 := by norm_num
