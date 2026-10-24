import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

theorem corridor_quadratic (a c : ℝ) : c * (a - c) ≤ a ^ 2 / 4 := by
  nlinarith [sq_nonneg (a - 2 * c)]

theorem bootstrap_increment (a k c : ℝ) (ha : 0 < a) (hc : 0 ≤ c)
    (hca : c < a) (hk : a ^ 2 / 4 < k) :
    (k - a ^ 2 / 4) / a ≤ k / (a - c) - c := by
  have hden : 0 < a - c := sub_pos.mpr hca
  have hquad := corridor_quadratic a c
  have hnum : 0 < k - a ^ 2 / 4 := sub_pos.mpr hk
  have hfirst : k - a ^ 2 / 4 ≤ k - c * (a - c) := by linarith
  have hstep : k / (a - c) - c = (k - c * (a - c)) / (a - c) := by
    field_simp
  rw [hstep]
  apply (div_le_div_iff₀ ha hden).2
  have hm := mul_nonneg (le_of_lt ha) (sub_nonneg.mpr hfirst)
  have hm2 := mul_nonneg (le_of_lt hnum) hc
  nlinarith only [hm, hm2]

theorem clipped_step_cost (a k c : ℝ) (hca : c < a) :
    min a (k / (a - c)) * (a - c) ≤ k := by
  have hden : 0 < a - c := sub_pos.mpr hca
  have hmin : min a (k / (a - c)) ≤ k / (a - c) := min_le_right _ _
  have hm := mul_le_mul_of_nonneg_right hmin (le_of_lt hden)
  simpa only [div_mul_cancel₀ _ (ne_of_gt hden)] using hm

theorem finite_growth_obstruction (a delta j c : ℝ) (hj : a ≤ j * delta)
    (hlower : j * delta ≤ c) (hupper : c < a) : False := by
  linarith

#print axioms corridor_quadratic
#print axioms bootstrap_increment
#print axioms clipped_step_cost
#print axioms finite_growth_obstruction
