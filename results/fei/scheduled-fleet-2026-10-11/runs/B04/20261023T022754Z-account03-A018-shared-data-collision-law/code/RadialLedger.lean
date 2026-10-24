import Mathlib.Tactic
-- Uncompiled source: memory admission refused. Only ordered-field ledger algebra.
theorem radial_upper (L G E R K m : ℝ)
    (h : L = G - ((1-m)*E+R+K)/2)
    (he : 0 ≤ E) (hr : 0 ≤ R) (hk : 0 ≤ K) (hm : m ≤ 1) : L ≤ G := by
  have hp : 0 ≤ (1-m)*E := mul_nonneg (sub_nonneg.mpr hm) he
  linarith
theorem owned_remaining (B U T : ℝ) (hb : 1 < B)
    (hu : U ≤ 1/8) (ht : T < 1/4) : (5/8 : ℝ) < B-U-max T 0 := by
  rcases le_total T 0 with hT | hT
  · rw [max_eq_right hT]
    linarith
  · rw [max_eq_left hT]
    linarith
#print axioms radial_upper
#print axioms owned_remaining
