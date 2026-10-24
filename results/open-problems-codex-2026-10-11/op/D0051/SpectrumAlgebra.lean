import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

-- Algebra only; the annulus theorem and covering proof are in ATTEMPT.md.
theorem brownian_parameters (g : ℝ) (hgpos : 0 < g) (hg : g ^ 2 = 8 / 3) :
    (g / 4) * (2 / g + g / 2) = 5 / 6 ∧ (g / 4) ^ 2 = 1 / 6 := by
  have hgne : g ≠ 0 := ne_of_gt hgpos
  constructor
  · calc
      (g / 4) * (2 / g + g / 2) = 1 / 2 + g ^ 2 / 8 := by
        field_simp
        <;> nlinarith
      _ = 5 / 6 := by rw [hg]; norm_num
  · nlinarith [hg]

theorem independent_kpz_wrong_value (x Q : ℝ)
    (hprod : x * Q = 5 / 6) (hsq : x ^ 2 = 1 / 6) :
    x * Q - x ^ 2 / 2 = 3 / 4 := by
  rw [hprod, hsq]
  norm_num

theorem negative_threshold_bound (x Q a : ℝ) (hx : 0 < x)
    (hprod : x * Q = 5 / 6) (hsq : x ^ 2 = 1 / 6)
    (ha : -x < a) : x * (Q - a) < 1 := by
  have hm : x * (-x) < x * a := mul_lt_mul_of_pos_left ha hx
  nlinarith

theorem threshold_is_negative (x Q : ℝ) (hx : 0 < x)
    (hprod : x * Q = 5 / 6) (hsq : x ^ 2 = 1 / 6) :
    Q - 1 / x = -x := by
  have hxne : x ≠ 0 := ne_of_gt hx
  apply (mul_left_cancel₀ hxne)
  field_simp
  nlinarith

#print axioms brownian_parameters
#print axioms independent_kpz_wrong_value
#print axioms negative_threshold_bound
#print axioms threshold_is_negative
