import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

-- The exact coordinate identity used in the convex-perspective proof.
theorem perspective_coordinate (a b t u v : ℝ)
    (ha : 0 < a) (hb : 0 < b) (ht : 0 ≤ t) (ht1 : t ≤ 1) :
    (t * u + (1-t) * v) / (t*a + (1-t)*b) =
      (t*a / (t*a+(1-t)*b)) * (u/a) +
      ((1-t)*b / (t*a+(1-t)*b)) * (v/b) := by
  have hrest : 0 ≤ (1-t)*b := mul_nonneg (sub_nonneg.mpr ht1) (le_of_lt hb)
  have hd : 0 < t*a + (1-t)*b := by
    by_cases hz : t = 0
    · simpa [hz] using hb
    · have htp : 0 < t := lt_of_le_of_ne ht (Ne.symm hz)
      have hprod : 0 < t*a := mul_pos htp ha
      linarith
  field_simp
  <;> ring

theorem perspective_weight (a b t : ℝ)
    (ha : 0 < a) (hb : 0 < b) (ht : 0 ≤ t) (ht1 : t ≤ 1) :
    0 ≤ t*a / (t*a+(1-t)*b) ∧ t*a / (t*a+(1-t)*b) ≤ 1 := by
  have hrest : 0 ≤ (1-t)*b := mul_nonneg (sub_nonneg.mpr ht1) (le_of_lt hb)
  have hd : 0 < t*a + (1-t)*b := by
    by_cases hz : t = 0
    · simpa [hz] using hb
    · have htp : 0 < t := lt_of_le_of_ne ht (Ne.symm hz)
      have hprod : 0 < t*a := mul_pos htp ha
      linarith
  constructor
  · exact div_nonneg (mul_nonneg ht (le_of_lt ha)) (le_of_lt hd)
  · apply (div_le_one hd).2
    nlinarith
