import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/- Exact finite certificates for the second attempt; no probability theorem is formalized. -/
theorem first_auxiliary_certificate :
    (5 / 43 : ℚ) - 4500 / 57319 - 3325000 / 58637337 =
      -1110205 / 58637337 := by
  norm_num

theorem first_auxiliary_certificate_negative :
    (5 / 43 : ℚ) - 4500 / 57319 - 3325000 / 58637337 < 0 := by
  norm_num

theorem first_trap_integrable :
    (1 : ℚ) < 2 * (43 / 50) - (2 / 5 + 3 / 10) := by
  norm_num

theorem subsequent_origin_terms_negative (delta n : ℚ)
    (hd : delta < 1) (hn : 1 ≤ n) : delta - n < 0 := by
  linarith

theorem grouped_tail_negative (C B n : ℚ)
    (hB : B < 0) (hfirst : C + B < 0) (hn : 1 ≤ n) : C + n * B < 0 := by
  have hmul : (n - 1) * (-B) ≥ 0 :=
    mul_nonneg (sub_nonneg.mpr hn) (by linarith)
  nlinarith

theorem stronger_origin_certificate :
    (1 / 103 : ℚ) - (2352 / 10609) * (99 / 203) =
      -211939 / 2153627 := by
  norm_num

theorem stronger_exit_certificate :
    (151 / 10609 : ℚ) - (2352 / 10609) * (5149 / 41209) =
      -5887889 / 437186281 := by
  norm_num

theorem stronger_certificates_negative :
    (-211939 / 2153627 : ℚ) < 0 ∧ (-5887889 / 437186281 : ℚ) < 0 := by
  norm_num

theorem stronger_parameters :
    (1 : ℚ) < 103 / 100 ∧
    2 * (103 / 100 : ℚ) - (49 / 100 + 12 / 25) = 109 / 100 ∧
    (49 / 100 : ℚ) - 12 / 25 = 1 / 100 := by
  norm_num
