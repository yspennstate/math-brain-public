import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Finite child-selection step in the nested thickness-band proof.
theorem full_dimension_child (u v d : ℝ) (hu : u ≤ d) (hv : v ≤ d)
    (hcover : d ≤ max u v) : u = d ∨ v = d := by
  rcases le_max_iff.mp hcover with h | h
  · exact Or.inl (le_antisymm hu h)
  · exact Or.inr (le_antisymm hv h)

-- Brownian-parameter feasibility of a full Euclidean band maximizer.
theorem full_band_negative (x a d : ℝ) (hx : 0 < x)
    (hsq : x ^ 2 = 1 / 6) (hd : 1 ≤ d)
    (hannulus : d ≤ 5 / 6 - x * a) : a ≤ -x := by
  by_contra h
  have ha : -x < a := lt_of_not_ge h
  have hm : x * (-x) < x * a := mul_lt_mul_of_pos_left ha hx
  nlinarith

theorem full_band_ambient_range (a d : ℝ) (hd : 1 ≤ d)
    (hamb : d ≤ 2 - a ^ 2 / 2) : a ^ 2 ≤ 2 := by
  linarith

#print axioms full_dimension_child
#print axioms full_band_negative
#print axioms full_band_ambient_range
