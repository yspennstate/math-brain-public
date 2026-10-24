import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

-- This certifies finite arithmetic and sign implications only.
-- Dirichlet joint moments and the infinite series are proved in prose.

theorem explicit_kappa :
    2 * (27 / 32 : ℚ) - max (19 / 32 : ℚ) (1 / 4) = 35 / 32 := by
  have h : (1 / 4 : ℚ) ≤ 19 / 32 := by norm_num
  rw [max_eq_left h]
  norm_num

theorem explicit_pair_prefix :
    (1 / 32 : ℚ) / (27 / 32) +
      (((10 / 32 : ℚ) * (9 / 32)) / (27 / 32) ^ 2) *
        ((1 / 32) - 1) / ((27 / 32) + 1) = -133 / 4779 := by
  norm_num

theorem explicit_prefix_negative : (-133 / 4779 : ℚ) < 0 := by
  norm_num

theorem signed_tail_term_negative (A delta n c : ℝ)
    (hA : 0 < A) (hdelta : delta < 1) (hn : 1 ≤ n) (hc : 0 < c) :
    c * (delta - n) / (A + n) < 0 := by
  have hnum : c * (delta - n) < 0 :=
    mul_neg_of_pos_of_neg hc (by linarith)
  exact div_neg_of_neg_of_pos hnum (by linarith)

theorem negative_auxiliary_ratio (M K Sbound : ℝ)
    (hM : 0 < M) (hK : K ≤ Sbound) (hp : Sbound < 0) : K / M < 0 := by
  exact div_neg_of_neg_of_pos (lt_of_le_of_lt hK hp) hM

theorem family_bound_gap : (1593 / 32768 : ℚ) < 2511 / 32768 := by
  norm_num

theorem closed_form_left_drift :
    (((3 / 8 - 5 / 16) * (1 - 3 / 8 - 5 / 16) - (3 / 8) * (5 / 16)) /
      ((1 - 3 / 8) * (1 - 5 / 16)) : ℚ) = -5 / 22 := by
  norm_num

theorem closed_form_right_drift :
    (((3 / 8 - 5 / 16) * (1 - 3 / 8 - 5 / 16) + (3 / 8) * (5 / 16)) /
      ((1 - 3 / 8) * (1 - 5 / 16)) : ℚ) = 7 / 22 := by
  norm_num
